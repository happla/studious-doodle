class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

employees = []
i = 1
while True:
    name = input("Anna työntekijän nimi: (0 lopetus): ")
    if name == '0':
        break
    employee = Employee(i, name)
    employees.append(employee)
    i += 1

for employee in employees:
    print(f"Id: {employee.id} nimi: {employee.name}")
