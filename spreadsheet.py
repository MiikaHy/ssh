
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        value = self.get(cell)
        if cell in self._evaluating:
            return "#Error"
        self._evaluating.add(cell)
        try:
            if value.startswith("='") and value.endswith("'"):
                return value[2:-1]
            if value.startswith("'") and value.endswith("'"):
                return value[1:-1]
            if value.lstrip('-').isdigit():
                return int(value)
            if value.startswith("="):
                if value[1:].isdigit():
                    return int(value[1:])
                elif value[1:].lstrip('-').isdigit():
                    return int(value[1:])
                else:
                    ref_value = self.evaluate(value[1:])
                    if isinstance(ref_value, int):
                        return ref_value
            return "#Error"
        finally:
            self._evaluating.remove(cell)

