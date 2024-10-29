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
