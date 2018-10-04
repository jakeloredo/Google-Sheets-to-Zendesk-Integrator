import sqlite3
import os
import sys


def get_db():
    db_path = os.path.join(sys.path[0],'data','db','integrator.db')
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    db = get_db()
    c = db.cursor()
    sql_path = os.path.join(sys.path[0],'data','db', 'schema.sql')
    with open(sql_path, 'r') as sql:
        c.executescript(sql.read())
    c.close()


def init_spreadsheet(spreadsheet_id, sheet_range):
    db = get_db()
    c = db.cursor()
    p = (spreadsheet_id, sheet_range)
    c.execute('INSERT INTO spreadsheet_counts VALUES(?, ?, 0)', p)
    db.commit()
    c.close()


def remove_spreadsheet(spreadsheet_id):
    db = get_db()
    c = db.cursor()
    c.execute('DELETE FROM spreadsheet_counts WHERE sheet_id=?', (spreadsheet_id,))
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


