
# Importing the ABC (Abstract Base Class) module for abstract class functionality
from abc import ABC, abstractmethod

# Employee Class: Represents a basic employee with 'name' and 'role' attributes.
class Employee:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# ReportWriter Abstract Class: Defines a base class for report writers with a 'write_report' method.
class ReportWriter(ABC):
    @abstractmethod
    def write_report(self, employee):
        pass

# BonusCalculator Abstract Class: Defines a base class for bonus calculators with a 'calculate_bonus' method.
class BonusCalculator(ABC):
    @abstractmethod
    def calculate_bonus(self, employee):
        pass

# ManagerReportWriter Class: Implements ReportWriter for managers, printing a manager-specific report.
class ManagerReportWriter(ReportWriter):
    def write_report(self, manager):
        print(f"Manager Report: {manager.name}")

# DeveloperReportWriter Class: Implements ReportWriter for developers, printing a developer-specific report.
class DeveloperReportWriter(ReportWriter):
    def write_report(self, developer):
        print(f"Developer Report: {developer.name}")

# ManagerBonusCalculator Class: Implements BonusCalculator for managers, returning a fixed bonus amount.
class ManagerBonusCalculator(BonusCalculator):
    def calculate_bonus(self, manager):
        return 1000

# DeveloperBonusCalculator Class: Implements BonusCalculator for developers, returning a fixed bonus amount.
class DeveloperBonusCalculator(BonusCalculator):
    def calculate_bonus(self, developer):
        return 500

# ManagerRole and DeveloperRole Abstract Classes: Abstract classes defining manager and developer roles.
class ManagerRole(ABC):
    @abstractmethod
    def manage_team(self):
        pass

class DeveloperRole(ABC):
    @abstractmethod
    def code_review(self):
        pass

# Manager Class: Inherits from Employee and ManagerRole, representing a manager with a 'manage_team' method.
class Manager(Employee, ManagerRole):
    def manage_team(self):
        print(f"{self.name} is managing the team.")

# Developer Class: Inherits from Employee and DeveloperRole, representing a developer with a 'code_review' method.
class Developer(Employee, DeveloperRole):
    def code_review(self):
        print(f"{self.name} is conducting a code review.")

# create_report Function: Generates a report using the provided report writer for a given employee.
def create_report(employee, report_writer):
    report_writer.write_report(employee)

# calculate_bonus Function: Calculates bonus using the provided bonus calculator for a given employee.
def calculate_bonus(employee, bonus_calculator):
    return bonus_calculator.calculate_bonus(employee)

# Main Block: Demonstrates the use of classes and functions.
if __name__ == "__main__":
    manager = Manager("Alice", "Manager")
    developer = Developer("Bob", "Developer")

    manager_report_writer = ManagerReportWriter()
    developer_report_writer = DeveloperReportWriter()
    manager_bonus_calculator = ManagerBonusCalculator()
    developer_bonus_calculator = DeveloperBonusCalculator()

    create_report(manager, manager_report_writer)
    create_report(developer, developer_report_writer)

    manager_bonus = calculate_bonus(manager, manager_bonus_calculator)
    developer_bonus = calculate_bonus(developer, developer_bonus_calculator)

    print(f"Manager Bonus: ${manager_bonus}")
    print(f"Developer Bonus: ${developer_bonus}")

    manager.manage_team()
    developer.code_review()
