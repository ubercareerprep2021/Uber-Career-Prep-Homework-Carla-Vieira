from collections import deque

class Employee:

    def __init__(self, name, title, direct_reports=[]):
        self.name = name
        self.title = title
        self.direct_reports = direct_reports

class OrganizationStructure:

    def __init__(self, ceo):
        self.ceo = ceo

    def print_by_level(self):
        queue = deque()
        last_level = 1
        queue.append((self.ceo, 1))
        while queue:
            current_employee, current_level = queue.popleft()
            if current_level > last_level:
                print()
            print(f"Name: {current_employee.name}, Title: {current_employee.title}")
            for direct_report in current_employee.direct_reports:
                queue.append((direct_report, current_level+1))
            last_level = current_level