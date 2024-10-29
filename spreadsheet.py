
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
            elif '+' in value:
                parts = value[1:].split('+')
                if all(part.lstrip('-').isdigit() for part in parts):
                    result = sum(int(part) for part in parts)
                else:
                    result = "#Error"
            elif '-' in value:
                parts = value[1:].split('-')
                if all(part.lstrip('-').isdigit() for part in parts):
                    result = int(parts[0]) - int(parts[1])
                else:
                    result = "#Error"
            elif '*' in value:
                parts = value[1:].split('*')
                if all(part.lstrip('-').isdigit() for part in parts):
                    result = 1
                    for part in parts:
                        result *= int(part)
                else:
                    result = "#Error"
            elif '/' in value:
                parts = value[1:].split('/')
                if all(part.lstrip('-').isdigit() for part in parts) and int(parts[1]) != 0:
                    result = int(parts[0]) // int(parts[1])
                else:
                    result = "#Error"
            elif '%' in value:
                parts = value[1:].split('%')
                if all(part.lstrip('-').isdigit() for part in parts) and int(parts[1]) != 0:
                    result = int(parts[0]) % int(parts[1])
                else:
                    result = "#Error"
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

