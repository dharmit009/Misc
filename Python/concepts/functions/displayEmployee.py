def displayEmployee(name, salary=9000): 
    print("Name:", name);
    print("Salary:", salary);
    return 



name = input("Enter the name of the employee: ");
salary = float(input("Enter the salary of the employee: "));

displayEmployee(name, salary);
displayEmployee(name);
