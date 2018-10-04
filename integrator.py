import sys
import os

from gsheets import GoogleSheet
from integrator_database import get_all_sheets
from integrator_database import update_last_row_by_id
from zendesk import get_zendesk_client_from_config


def make_zendesk_payload(subject, gs_row, gs_headers):
    l = [str(header) + ': ' + str(row) for header, row in zip(gs_headers, gs_row)]
    comment = '\n'.join(l)
    payload = {
        'ticket':
        {
            'requester': gs_row[0],
            'subject': subject,
            'comment':
            {
                'body': comment
            }
        }
    }
    print(comment)
    return payload


def open_zendesk_ticket(payload):
    try:
        config_path = os.path.join(sys.path[0], 'data', 'config', 'zendesk.json')
        zd = get_zendesk_client_from_config(config_path)
        r = zd.create_ticket(payload)
    except:
        return None

    if r.status_code != 201:
        return r
    return None


def main():
    sheets = get_all_sheets()
    zendesk_payloads = list()

    for sheet in sheets:
        sheet_id = sheet['sheet_id']
        sheet_range = sheet['range']
        last_row = sheet['last_row']

        gs = GoogleSheet(sheet_id)
        values = gs.get_values(sheet_range)
        sheet_title = gs.get_title()

        if values:
            labels = values.pop(0)
        else:
            # Prevents error if no values were returned
            continue

        new_last_row = len(values)

        if new_last_row < last_row:
            # Rows may have been deleted from the sheet
            # Need to handle this somehow
            pass# continue

        for row in values[last_row:]:
            zendesk_payloads.append(make_zendesk_payload(sheet_title, row, labels))

        update_last_row_by_id(sheet_id, new_last_row)

    # Open a ticket for each of the new payloads
    # Errors is a map iterable with None for tickets that succeeded
    errors = map(open_zendesk_ticket, zendesk_payloads)

    # TODO: Handle errors

if __name__ == '__main__':
    main()

