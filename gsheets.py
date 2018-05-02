from googleapiclient.discovery import build
from oauth2client import file, client, tools
from httplib2 import Http


class GoogleSheets:

    def __init__(self):
        self.service = None

    def setup_sheets_service(self):
        # Basic setup from quick start guide
        # Setup the Sheets API
        SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
            creds = tools.run_flow(flow, store)

        self.service = build('sheets', 'v4', http=creds.authorize(Http()))

    def get_service(self):
        if self.service is None:
            self.setup_sheets_service()
        return self.service


class GoogleSheet(GoogleSheets):

    def __init__(self, spreadsheet_id):
        self.spreadsheet_id = spreadsheet_id
        self.title = None
        GoogleSheets.__init__(self)

    def get_values(self, range_name):
        r = self.get_service().spreadsheets().values().get(spreadsheetId=self.spreadsheet_id,
                                                                range=range_name).execute()
        return r.get('values', [])

    def get_title(self):
        if self.title is None:
            r = self.get_service().spreadsheets().get(spreadsheetId=self.spreadsheet_id).execute()
            self.title = r.get("properties", {}).get("title", "")
        return self.title


if __name__ == '__main__':
    values = GoogleSheet('1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms').get_values('Class Data!A2:E')
    if not values:
        print('No data found.')
    else:
        print(values)
