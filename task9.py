class Staff:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def display_info(self):
        print(f"Role: {self.role}, Department: {self.department}, Salary: {self.salary}")


class Teacher(Staff):
    def __init__(self, role, department, salary, subject):
        super().__init__(role, department, salary)
        self.subject = subject
    def display_info(self):
        print(f"Teacher - Role: {self.role}, Department: {self.department}, Salary: {self.salary}, Subject: {self.subject}")


teacher = Teacher("Teacher", "Arts", 48000, "Literature")
teacher.display_info()