import pandas as pd

def find_row_index(df, value):
    # Find the first row index where any cell matches the value (case-insensitive, strip spaces)
    match = df.map(lambda x: isinstance(x, str) and x.strip().lower() == value.lower())
    rows = match.any(axis=1)
    if not rows.any():
        raise ValueError(f"'{value}' not found in the sheet.")
    return rows.idxmax()

def get_player_data(sheet_name, xlsFile):
    df = pd.read_excel(xlsFile, sheet_name=sheet_name, header=None)
    header_idx = find_row_index(df, 'Name')
    totals_idx = find_row_index(df, 'TOTALS')
    header = df.iloc[header_idx]
    players = df.iloc[header_idx+1:totals_idx]
    players.columns = header
    data_rows = []
    for _, row in players.iterrows():
        last_valid = row.last_valid_index()
        # Skip the first column (index 0), start from player name
        data = row.iloc[1:players.columns.get_loc(last_valid)+1].tolist()
        data_rows.append(data)
    return data_rows

def process_xls(xlsFile):
    # Get batting and pitching data for visitor
    visitor_batting = get_player_data('VisitorBatting', xlsFile)
    visitor_pitching = get_player_data('VisitorPitching', xlsFile)
    # Get batting and pitching data for home
    home_batting = get_player_data('HomeBatting', xlsFile)
    home_pitching = get_player_data('HomePitching', xlsFile)

    # Calculate max columns for each group
    visitor_batting_cols = max((len(row) for row in visitor_batting), default=0)
    visitor_pitching_cols = max((len(row) for row in visitor_pitching), default=0)
    home_batting_cols = max((len(row) for row in home_batting), default=0)
    home_pitching_cols = max((len(row) for row in home_pitching), default=0)

    # Total columns for each side
    visitor_total_cols = visitor_batting_cols + visitor_pitching_cols
    home_total_cols = home_batting_cols + home_pitching_cols

    # Prepare visitor rows
    visitor_rows = []
    for row in visitor_batting:
        padded = row + [''] * (visitor_total_cols - len(row))
        visitor_rows.append(padded)
    for row in visitor_pitching:
        if row:
            padded = [row[0]] + [''] * (visitor_batting_cols - 1) + row[1:] + [''] * (visitor_total_cols - visitor_batting_cols - len(row[1:]))
            visitor_rows.append(padded)

    # Prepare home rows
    home_rows = []
    for row in home_batting:
        padded = row + [''] * (home_total_cols - len(row))
        home_rows.append(padded)
    for row in home_pitching:
        if row:
            padded = [row[0]] + [''] * (home_batting_cols - 1) + row[1:] + [''] * (home_total_cols - home_batting_cols - len(row[1:]))
            home_rows.append(padded)

    return visitor_rows, visitor_total_cols, home_rows, home_total_cols