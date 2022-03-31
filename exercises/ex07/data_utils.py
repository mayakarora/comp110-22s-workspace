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
    """Produces a list of all values from the column of the given column name."""
    store: list[str] = []
    for row in table:
        item: str = row[column_name]
        store.append(item)
    return store


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transforms data from row-format table to column-format table."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(unmutated: dict[str, list[str]], y: int) -> dict[str, list[str]]:
    """Allows you to see some initial rows of data."""
    visual: dict[str, list[str]] = {}
    if y > len(unmutated):
        return unmutated
    for key in unmutated:
        values: list[str] = []
        i: int = 0
        while i < y:
            values.append(unmutated[key][i])
            i += 1
        visual[key] = values
    return visual



def select(unchanged: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    """Allows you to specify an area of data to focus on."""
    focus: dict[str, list[str]] = {}
    for key in copy:
        focus[key] = unchanged[key]
    return focus


def concat(one: dict[str, list[str]], two: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produces a new column-format table that combines two other column-format tables."""
    combined: dict[str, list[str]] = {}
    for key in one:
        one[key] = combined[key]
    for key in two:
        if combined[key] == two[key]:
            i: int = 0
            add: list[str] = two[key]
            while i < len(two[key]):
                combined[key].append(add[i])
                i += 1
        else:
            combined[key] = two[key]
    return combined


def count(values: list[str]) -> dict[str, int]:
    """Creates a dictionary that shows the frequency of the values from the original list."""
    frequency: dict[str, int] = {}
    for item in values:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency