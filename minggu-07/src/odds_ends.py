class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print("Name: {}, Departement: {}, Salary: {}".format(john.name, john.dept, john.salary))