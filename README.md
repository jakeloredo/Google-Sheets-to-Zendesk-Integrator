# Google-Sheets-to-Zendesk-Integrator

Program to check Google Sheets for new rows and make a Zendesk ticket for each new row.

## Requirements

Python 3 and the following modules:

- requests
- google-api-python-client 
- oauth2client

## Getting Started

Setup a Google Sheet as described in the below example.

Follow these steps after downloading the repo:

1. Edit the Zendesk config file with your credentials: data/config/zendesk.json

2. Setup the database (see below)

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


## Example Google Sheet

The first row of the sheet must contain the headers for your table.

Column A should contain the email address that will be used as the requester for the ticket:

![Example Sheet](https://github.com/jakeloredo/Google-Sheets-to-Zendesk-Integrator/blob/master/example_sheet.PNG)

For this sheet, you would need to setup the range in the integrator database as something like "Sheet1!A1:F".

The Zendesk ticket description for the entry in this sheet would be as follows (raw text without the markdown):

    Email: jake@example.com
    Date: 4/12/2018
    Comments: The servers are too hot
    Building: A
    Space: 17

