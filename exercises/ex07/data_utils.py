"""Dictionary related utility functions."""

__author__ = "730410153"


from csv import DictReader


def read_csv_rows(x: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    file_handle = open(x, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column_name: str) -> list[str]:
    store: list[str] = []
    for row in table:
        item: str = row[column_name]
        store.append(item)
    return store


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(unmutated: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    visual: dict[str, list[str]] = {}
    values: list[str] = []
    i: int = 1
    for key in unmutated:  
        while i <= y:
            for item in unmutated[key]:
                values.append(item)
    for key in visual:
        visual[key] = values
    return visual