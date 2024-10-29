
class SpreadSheet:

    def __init__(self):
        self._cells = {}
        self._evaluating = set()

    def set(self, cell: str, value: str) -> None:
        self._cells[cell] = value

    def get(self, cell: str) -> str:
        return self._cells.get(cell, '')

    def evaluate(self, cell: str) -> int | str:
        if cell in self._evaluating:
            return "#Circular"
        self._evaluating.add(cell)
        
        value = self.get(cell)
        if value.startswith("='") and value.endswith("'"):
            result = value[2:-1]
        elif value.startswith("'") and value.endswith("'"):
            result = value[1:-1]
        elif value.lstrip('-').isdigit():
            result = int(value)
        elif value.startswith("="):
            if value[1:].isdigit():
                result = int(value[1:])
            elif value[1:].lstrip('-').isdigit():
                result = int(value[1:])
            else:
                reference = value[1:]
                if reference in self._cells:
                    result = self.evaluate(reference)
                else:
                    result = "#Error"
        else:
            result = "#Error"
        
        self._evaluating.remove(cell)
        return result

