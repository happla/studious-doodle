import csv


def my_split(sentence, sep):
    lst = []
    tmp = ''
    for c in sentence:
        if c == sep:
            lst.append(tmp)
            tmp = ''
        else:
            tmp += c
    if tmp:
        lst.append(tmp)

    return lst


def my_join(lst, sep):
    mystr = ''
    for elem in lst[0:-1]:
        mystr += str(elem) + str(sep)
    mystr += str(lst[-1])

    return mystr


class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class SalaryEmployee(Employee):
    def __init__(self, id, name, monthly_salary):
        super().__init__(id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


while True:
    print("(1) Lisää työntekijöitä listaan\n(2) Kirjoita työntekijät tiedostoon\n(3) Lue työntekijät tiedostosta\n(4) Tulosta työntekijät\n(0) Lopeta\n")
    selection = int(input("Valitse toiminto: "))
    if selection == 1:
        salary_employees = []
        name = " "
        id = 1
        while name != '0':
            name = str(input("Anna työntekijän nimi (0 lopetus):"))
            if name != '0':
                try:
                    salary = int(input("Anna kuukausipalkka:"))
                except:
                    salary = 0
                salary_employees.append(SalaryEmployee(id, name, salary))
                id += 1

    ### put your code here ###
### put your code here ###
    elif selection == 2:
        with open("salary_employee.csv", "w") as file:
            file.write("id,name,monthly_salary\n")
            for employee in salary_employees:
                employee_data = [str(employee.id), employee.name, str(
                    employee.monthly_salary)]
                employee_data_joined = ",".join(employee_data) + "\n"
                file.write(employee_data_joined)
        print(len(salary_employees),
              " työntekijä(ä) lisätty tiedostoon salary_employee.csv")
    elif selection == 3:
        def read_employees_from_file():
            with open("salary_employee.csv", "r") as file:
                next(file)
                for line in file:
                    employee_data = my_split(line.strip(), ",")
                    id = int(employee_data[0])
                    name = employee_data[1]
                    salary = int(employee_data[2])
                    salary_employees.append(SalaryEmployee(id, name, salary))
        file.close()
        print(len(salary_employees)," työntekijä(ä) luettu tiedostosta salary_employee.csv")

    elif selection == 4:
        for employee in salary_employees:
            print("Id:", employee.id, "Nimi:", employee.name,
                  "Kuukausipalkka:", employee.monthly_salary)
    elif selection == 0:
        print("Palvelu suljetaan, kiitos")
        break
    else:
        print("Virheellinen valinta.")
