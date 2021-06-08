import pytest
from trees.ex3 import OrganizationStructure, Employee


def test_print_above(capsys):
    organization = OrganizationStructure(Employee("A", "CEO", [Employee("B", "CFO", [
        Employee("I", "Director", [Employee("J", "Sales Representative", [Employee("K", "Sales Intern")])])]), Employee(
        "C", "CTO",
        [Employee("D", "Manager", [Employee("F", "Engineer"), Employee("G", "Engineer"), Employee("H", "Engineer")]),
         Employee("E", "Manager")])]))
    organization.print_level()
    capture = capsys.readouterr()
    assert "5" in capture.out


def test_print_below(capsys):
    organization = OrganizationStructure(Employee("A", "CEO", [Employee("B", "CFO", [
        Employee("I", "Director")]), Employee("C", "CTO", [
        Employee("D", "Manager", [Employee("F", "Engineer"), Employee("G", "Engineer"), Employee("H", "Engineer")]),
        Employee("E", "Manager")])]))
    organization.print_level()
    capture = capsys.readouterr()
    assert "4" in capture.out
