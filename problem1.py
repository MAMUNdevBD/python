while True:
    number = input("Employee's number: ")
    workHours = float(input("Worked hours: "))
    salaryPerHour = float(input("Salary per hours: "))

number = input()
workHours = float(input())
salaryPerHour = float(input())

salary = workHours*salaryPerHour
salary = "{:.2f}".format(salary)

print("NUMBER =",number)
print("SALARY = U$", salary)

    # check = input("Calculate another employee? enter Y to restart or any key to exit: ")
    # if check.upper() == "Y":
    #     continue
    # print("Exiting...")
    # break

