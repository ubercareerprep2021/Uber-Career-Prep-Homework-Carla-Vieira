import pytest
from trees.ex2 import OrganizationStructure, Employee


def test_print(capsys):
    organization = OrganizationStructure(Employee("A", "CEO", [Employee("B", "CFO", [
        Employee("I", "Director", [Employee("J", "Sales Representative", [Employee("K", "Sales Intern")])])]), Employee(
        "C", "CTO",
        [Employee("D", "Manager", [Employee("F", "Engineer"), Employee("G", "Engineer"), Employee("H", "Engineer")]),
         Employee("E", "Manager")])]))
    organization.print_by_level()
    capture = capsys.readouterr()
    assert """Name: A, Title: CEO

Name: B, Title: CFO
Name: C, Title: CTO

Name: I, Title: Director
Name: D, Title: Manager
Name: E, Title: Manager

Name: J, Title: Sales Representative
Name: F, Title: Engineer
Name: G, Title: Engineer
Name: H, Title: Engineer

Name: K, Title: Sales Intern""" in capture.out
