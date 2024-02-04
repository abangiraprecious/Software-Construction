from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name
    # implementing abstract methods to provide specific behavior for each role. 
    @abstractmethod
    def calculate_bonus(self):
        """Calculate and return the bonus for an employee."""
        pass

    @abstractmethod
    def perform_duties(self):
        """Perform role-specific duties."""
        pass

class Manager(Employee):
    # Example of bonus calculation for a manager
    def calculate_bonus(self):
        return 1000
    
    # Example of duty for a manager
    def perform_duties(self):
        print(f"{self.name} is managing the team.")

class Developer(Employee):
    # Example bonus calculation for a developer
    def calculate_bonus(self):
        return 500

    def perform_duties(self):
        # Example duty for a developer
        print(f"{self.name} is conducting a code review.")

class ReportGenerator:
    # Generating a report specific to the employee's role
    def generate_report(self, employee):
        print(f"{employee.__class__.__name__} Report: {employee.name}")

class BonusCalculator:
    # Calculating the bonus using the employee's calculate_bonus method
    def calculate_bonus(self, employee):
        return employee.calculate_bonus()

if __name__ == "__main__":
    employees = [Manager("Alice"), Developer("Bob")]

    report_generator = ReportGenerator()
    bonus_calculator = BonusCalculator()

    for employee in employees:
        employee.perform_duties()  
        report_generator.generate_report(employee)  
        bonus = bonus_calculator.calculate_bonus(employee) 
        print(f"{employee.__class__.__name__} Bonus: ${bonus}")

# I have not implemented logic but returned a fixed bonus amount for each role. In a real-world scenario,
# the bonus calculation might involve more complex logic, possibly considering factors like performance metrics, 
# company profitability, and employee seniority.