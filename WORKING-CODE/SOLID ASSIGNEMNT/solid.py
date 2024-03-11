class Employee(ABC):
    def __init__(self, identifier):
        self.identifier = identifier

    # Define abstract methods for subclasses to implement.
    @abstractmethod
    def compute_reward(self):
        """Determine the bonus amount for a staff member."""
        pass

    @abstractmethod
    def execute_tasks(self):
        """Carry out specific tasks based on the staff role."""
        pass

class Manager(Employee):
    # Calculate bonus for a Manager.
    def compute_reward(self):
        return 1000
