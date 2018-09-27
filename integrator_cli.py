import argparse

import integrator_database
import integrator


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-run", action="store_true", help="Use to run the integration")

    parser.add_argument("-init", action="store_true", help="Use to initiate an empty table in a new database")

    parser.add_argument("-add", type=str, nargs=2, help="Use to add a Google sheet to the database")

    parser.add_argument("-remove", help="Use to remove a Google sheet from the database")

    parser.add_argument("-list", action="store_true", help="Use to list the contents of the database")

    args = parser.parse_args()

    if args.run:
        integrator.main()
    else:
        if args.init:
            integrator_database.init_db()

        if args.add:
            sheet_id = args.add[0]
            sheet_range = args.add[1]
            integrator_database.init_spreadsheet(sheet_id, sheet_range)

        if args.remove:
            print("Google Sheet with ID {} has been removed".format(args.remove))

        if args.list:
            sheets = integrator_database.get_all_sheets()
            print()
            row_format = "{:45} | {:5} | {}"
            print(row_format.format("Google Sheet ID", "Range", "Row Count"))
            for s in sheets:
                print(row_format.format(s['sheet_id'], s['range'], s['last_row']))
            print()
