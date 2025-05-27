def write_csv_lines(rows, total_cols):
    lines = []
    if rows:
        max_len = max(len(row) for row in rows)
    else:
        max_len = total_cols
    lines.append(','.join([''] * (max_len - 1)))
    for row in rows:
        trimmed_row = row[:max_len]
        if trimmed_row and trimmed_row[-1] == '':
            trimmed_row = trimmed_row[:-1]
        line = ','.join(map(str, trimmed_row))
        lines.append(line)
    return lines

__all__ = ['write_csv_lines']