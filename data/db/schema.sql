DROP TABLE IF EXISTS spreadsheet_counts;
CREATE TABLE IF NOT EXISTS spreadsheet_counts(
    sheet_id text PRIMARY KEY,
    range text,
    last_row integer
);