employee_object1 = {
    "name": "Bogart Torres",
    "department": "Sales",
    "age": 30,
    "email": "bogart.torres@company.com"
}


employee_object2 = {
    "name": "Bogart Reyes",
    "department": "Human Resources",
    "age": 25,
    "email": "bogart.reyes@company.com"
}


employee_object3 = {
    "name": "Bogart Dela Cruz",
    "department": "IT",
    "age": 40,
    "email": "bogart.delacruz@company.com"
}


employee_object4 = {
    "name": "Lisa Wong",
    "department": "Marketing",
    "age": 28,
    "email": "lisa.wong@company.com"
}


employee_object5 = {
    "name": "Paul McDonald",
    "department": "Finance",
    "age": 35,
    "email": "paul.mcdonald@company.com"
}


employees = [employee_object1, employee_object2, employee_object3, employee_object4, employee_object5]


for employee in employees:
    print(f"Employee: {employee['name']}, Department: {employee['department']}, Age: {employee['age']}, Email: {employee['email']}")