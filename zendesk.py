import json

import requests


class Zendesk:
    def __init__(self, domain='', creds=()):
        self.url = 'https://' + domain + '.zendesk.com/api/v2/'
        self.creds = creds
        self.headers = {'content-type': 'application/json'}

    def get(self, endpoint):
        url = self.url + endpoint
        return requests.get(url=url, auth=self.creds, headers=self.headers)

    def post(self, endpoint, payload):
        url = self.url + endpoint
        return requests.post(url=url, data=json.dumps(payload), auth=self.creds, headers=self.headers)

    def put(self, endpoint, payload):
        url = self.url + endpoint
        return requests.put(url=url, data=json.dumps(payload), auth=self.creds, headers=self.headers)

    def create_ticket(self, payload):
        return self.post('tickets', payload)


def get_zendesk_client_from_config(file_path):
    with open(file_path, 'r') as infile:
        c = json.loads(infile.read())
        domain = c.get('domain')
        creds = (c.get('username'), c.get('password'))
        return Zendesk(domain=domain, creds=creds)
