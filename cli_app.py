import sys
import os
from core import process_xls
from utils import write_csv_lines

def main():
    if len(sys.argv) < 2:
        print('Usage: python cli_app.py <xls_file>')
        sys.exit(1)
    xlsFile = sys.argv[1]
    visitor_rows, visitor_total_cols, home_rows, home_total_cols = process_xls(xlsFile)
    cwd = os.getcwd()
    # Write visitor.csv
    visitor_lines = write_csv_lines(visitor_rows, visitor_total_cols)
    with open(os.path.join(cwd, 'visitor.csv'), 'w') as f:
        f.write('\n'.join(visitor_lines))
    # Write home.csv
    home_lines = write_csv_lines(home_rows, home_total_cols)
    with open(os.path.join(cwd, 'home.csv'), 'w') as f:
        f.write('\n'.join(home_lines))

if __name__ == '__main__':
    main()
