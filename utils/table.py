def display_table(headers, rows):
    """Display data in a formatted terminal table."""
    if not rows:
        print("No data available.")
        return
    # Convert all values to strings
    headers = [str(header) for header in headers]
    rows = [[str(value) for value in row] for row in rows]
    # Calculate the width of each column
    widths = []
    for i, header in enumerate(headers):
        column_values = [row[i] for row in rows]
        width = max(len(header), *(len(v) for v in column_values))
        widths.append(width)
    # Create table border
    border = "+" + "+".join(
        "-" * (width + 2) for width in widths
    ) + "+"
    def print_row(row):
        print("| " + " | ".join(
            value.ljust(widths[i])
            for i, value in enumerate(row)
        ) + " |")
    print(border)
    print_row(headers)
    print(border)
    for row in rows:
        print_row(row)
    print(border)
