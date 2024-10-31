from unittest import TestCase
from spreadsheet import SpreadSheet


class TestSpreadSheet(TestCase):

    def test_evaluate_unsigned_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_signed_integer(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "-1")
        self.assertEqual(-1, spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_input(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "1.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_single_quotes(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_no_single_quotes(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_no_trailing_quote(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "'Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_no_heading_quote(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "Apple'")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_string_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple'")
        self.assertEqual("Apple", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_integer_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_string_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "='Apple")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_reference_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "42")
        self.assertEqual(42, spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_reference_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "42.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_circular_reference_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=B1")
        spreadsheet.set("B1", "=A1")
        self.assertEqual("#Circular", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_addition_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3")
        self.assertEqual(4, spreadsheet.evaluate("A1"))

    def test_evaluate_valid_subtraction_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1-3")
        self.assertEqual(-2, spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_addition_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1+3.5")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_invalid_division_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1/0")
        self.assertEqual("#Error", spreadsheet.evaluate("A1"))

    def test_evaluate_valid_division_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=3/3")
        self.assertEqual(1, spreadsheet.evaluate("A1"))

    def test_evaluate_valid_multiplication_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=1*5")
        self.assertEqual(5, spreadsheet.evaluate("A1"))

    def test_evaluate_valid_modulo_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=14%12")
        self.assertEqual(2, spreadsheet.evaluate("A1"))

    def test_evaluate_valid_complex_formula(self):
        spreadsheet = SpreadSheet()
        spreadsheet.set("A1", "=3-1*2")
        self.assertEqual(7, spreadsheet.evaluate("A1"))
