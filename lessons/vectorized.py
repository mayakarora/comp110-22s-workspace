from __future__ import annotations


class StrArray:
    items: list[str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: str):
        """Vectorized concatenation operator."""
        # Set up a result list of strings that is empty
        empty: list[str] = []
        if isinstance(rhs, str):
            # Loop through each item in self.items
            for item in self.items:
                # For each item, append the concatenation of item and rhs to result list
                empty.append(item + rhs)
        else:
            assert len(self.items) == len(rhs.items)
            for i in range(0, len(self.items)):
                empty.append(self.items[i] + rhs.items[i])
        # Return a newly constructed StrArray whose items are result
        return StrArray(empty)


first: StrArray = StrArray(["Armando", "Brady", "Caleb"])
last: StrArray = StrArray(["Bacot", "Manek", "Love"])
result: StrArray = first + "!"
print(result)
print(first + " " + last)
