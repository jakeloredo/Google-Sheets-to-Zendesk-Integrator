import sqlite3


def get_db():
    conn = sqlite3.connect('./data/db/integrator.db')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db = get_db()
    c = db.cursor()
    with open('./data/db/schema.sql', 'r') as sql:
        c.executescript(sql.read())
    c.close()


def init_spreadsheet(spreadsheet_id, sheet_range):
    db = get_db()
    c = db.cursor()
    p = (spreadsheet_id, sheet_range)
    c.execute('INSERT INTO spreadsheet_counts VALUES(?, ?, 0)', p)
    db.commit()
    c.close()


def get_last_row_by_id(spreadsheet_id):
    db = get_db()
    c = db.cursor()
    result = c.execute('SELECT last_row FROM spreadsheet_counts WHERE sheet_id = \'?\''.replace('?', spreadsheet_id))
    if list(result):
        return list(result)[0][0]
    else:
        return -1


def update_last_row_by_id(spreadsheet_id, last_row):
    db = get_db()
    c = db.cursor()
    c.execute('UPDATE spreadsheet_counts SET last_row = ? WHERE sheet_id = ?', (last_row, spreadsheet_id))
    db.commit()
    c.close()


def get_all_sheets():
    db = get_db()
    c = db.cursor()
    r = c.execute('SELECT * FROM spreadsheet_counts')
    return [x for x in r]


if __name__ == '__main__':
    init_db()

