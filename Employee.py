employees = []
running = True


class Employees:

    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def calculate(self, e):
        return e * self.d


while running:
    print("(1) Add employee")
    print("(2) Enter hourly of employee")
    print("(3) Show employee information")
    print("(4) Exit")

    number = int(input("Enter a number: "))

    if number == 1:
        print("Enter employee name: ", end="")
        a = (input())

        print("Enter department: ", end="")
        b = input()

        print("Enter position: ", end="")
        c = input()

        print("Enter rate: ", end="")
        d = int(input())

        employees.append(Employees(a, b, c, d))

        continue

    elif number == 2:
        emp = Employees(a, b, c, d)
        print("Enter the index of the employee: ")

        user = int(input())
        print(employees[user].a, " selected")
        print("Enter the hourly of employee: ")
        hour = int(input())
        print(employees[user].d * hour)
        continue

    elif number == 3:

        for x in employees:
            print("\nName:", x.a, "\nDepartment:", x.b, "\nPosition:", x.c, "\nRate:", x.d,"\n")

        continue

    elif number == 4:
        print("Done.")
        break

    else:
        print("Please enter valid number: ")
        continue
