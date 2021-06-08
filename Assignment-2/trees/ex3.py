from collections import deque

class Employee:

    def __init__(self, name, title, direct_reports=[]):
        self.name = name
        self.title = title
        self.direct_reports = direct_reports

class OrganizationStructure:

    def __init__(self, ceo):
        self.ceo = ceo

    def print_level(self):
        queue = deque()
        last_level = 1
        queue.append((self.ceo, 1))
        while queue:
            current_employee, current_level = queue.popleft()
            for direct_report in current_employee.direct_reports:
                queue.append((direct_report, current_level+1))
            last_level = current_level
        print(last_level)