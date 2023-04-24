
### put your code here ###
class HourlyEmployee(Employee):
    def __init__(self, id, name, hour_rate, hours_worked):
        super().__init__(id, name)
        self.hour_rate = hour_rate
        self.hours_worked = hours_worked

    def ask_salary(self):
        self.hours_worked = float(input("Anna tehdyt tunnit:"))		
        self.hour_rate = float(input("Anna tuntipalkka:"))

    def calculate_salary(self):
        return int(self.hour_rate * self.hours_worked)

class CommissionEmployee(SalaryEmployee):
    def __init__(self, id, name="", monthly_salary=0, *args, **kwargs):
        super().__init__(id, name, *args, **kwargs)
        self.monthly_salary = monthly_salary
    def ask_salary(self):
        self.monthly_salary = float(input("Anna kuukausipalkka:"))
        self.commission = float(input("Anna komissio:"))

    def calculate_salary(self):
        return int(self.monthly_salary + self.commission)
	