# Google-Sheets-to-Zendesk-Integrator

Program to check Google Sheets for new rows and make a Zendesk ticket for each new row.

## Requirements

Python 3 and the following modules:

- requests
- google-api-python-client 
- oauth2client

## Usage

### Setup or reset the database:

    python integrator_cli.py -init
  
### Add a sheet to the database:

    python integrator_cli.py -add 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms "Class Data!A2:E"

In the above example, the Google Sheet ID is 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms and the range that the script will check is Class Data!A2:E

### Remove a sheet from the database:

    python integrator_cli.py -remove 1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms

### Run the integrator once:

    python integrator_cli.py -run
    
I would set this command up on a cron job or similar.
