from __future__ import print_function
from httplib2 import Http
import os
from datetime import datetime
                                                    # Механизм запроса данных
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

ALL_STAGES_CONST = ['проводник', 'своим скажет', 'доверие', 'услышал', 'нужна встреча', 'перезвонить', 'нужен e-mail',
                    'секретарь передаст', 'отправил сообщен', 'нет на месте', 'недозвон', 'недоступен', '---',
                    'нет контактов', 'не занимаюсь', 'не понимает', 'не верит', 'рыпу']

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/people.googleapis.com-python-quickstart.json
SCOPES_CON = 'https://www.googleapis.com/auth/contacts' #.readonly'       #!!!!!!!!!!!!!!!!!!!!!!!!! read-only !!!!!!!!!!!
SCOPES_CAL = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'People, Calendar API Python Quickstart'


def get_credentials_con():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'people.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES_CON)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_credentials_cal():
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar.googleapis.com-python-quickstart.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES_CAL)
        flow.user_agent = APPLICATION_NAME + 'and test'
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def main():
    """Shows basic usage of the People API.

    Creates a People API service object and outputs the name if
    available of 10 connections.
    """
    credentials_con = get_credentials_con()
    http_con = credentials_con.authorize(Http())

# Вытаскиваем названия групп
    serviceg = discovery.build('contactGroups', 'v1', http=http_con,
                               discoveryServiceUrl='https://people.googleapis.com/$discovery/rest')
    resultsg = serviceg.contactGroups().list(pageSize=200).execute()
    groups = {}
    groups_reverse = {}
    contactGroups = resultsg.get('contactGroups', [])
    for i, contactGroup in enumerate(contactGroups):
        groups[contactGroup['resourceName'].split('/')[1]] = contactGroup['name']
        groups_reverse[contactGroup['name']] = contactGroup['resourceName'].split('/')[1]

# Контакты
    service = discovery.build('people', 'v1', http=http_con,
                              discoveryServiceUrl='https://people.googleapis.com/$discovery/rest')
    results = service.people().connections().list(
            resourceName='people/me',
            pageSize=1000,
            personFields='addresses,ageRanges,biographies,birthdays,braggingRights,coverPhotos,emailAddresses,events,'
                         'genders,imClients,interests,locales,memberships,metadata,names,nicknames,occupations,'
                         'organizations,phoneNumbers,photos,relations,relationshipInterests,relationshipStatuses,'
                         'residences,skills,taglines,urls,userDefined'
    ).execute()
    connections = results.get('connections', [])
    contacts = []
    for i, connection in enumerate(connections):
        contact = {}
        name = ''
        onames = connection.get('names', [])
        if len(onames) > 0:
            name = onames[0].get('displayName')
        contact['fio'] = name
        biographie = ''
        obiographies = connection.get('biographies', [])
        if len(obiographies) > 0:
            biographie = obiographies[0].get('value')
        contact['note'] = biographie
        phones = []
        ophones = connection.get('phoneNumbers', [])
        if len(ophones) > 0:
            for ophone in ophones:
                phones.append(ophone.get('canonicalForm'))
        contact['phones'] = phones
        memberships = []
        omemberships = connection.get('memberships', [])
        if len(omemberships) > 0:
            for omembership in omemberships:
                memberships.append(groups[omembership['contactGroupMembership']['contactGroupId']])
        contact['groups'] = memberships
        stage = '---'
        ostages = connection.get('userDefined', [])
        if len(ostages) > 0:
            for ostage in ostages:
                if ostage['key'].lower() == 'stage':
                    stage = ostage['value'].lower()
        contact['stage'] = stage
        contacts.append(contact)

# Добавляем массив стадий из контактов
    all_stages = ALL_STAGES_CONST
    for i, contact in enumerate(contacts):
        has = False
        for all_stage in all_stages:
            if all_stage == contact['stage']:
                has = True
        if not has:
            all_stages.append(contact['stage'])

# Тест календаря
    credentials_cal = get_credentials_cal()
    http_cal = credentials_cal.authorize(Http())

    service_cal = discovery.build('calendar', 'v3', http=http_cal)

    # Call the Calendar API
    now = datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    now = datetime(2010,1,1,0,0).isoformat() + 'Z'
    print('Getting the upcoming 10 events')
    events_result = service_cal.events().list(
        calendarId='primary',
        timeMin=now,
        maxResults=10,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])


if __name__ == '__main__':
    main()

