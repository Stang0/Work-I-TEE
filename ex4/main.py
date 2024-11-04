with open('employeelist.txt', 'r') as file:
    Contents = file.read().splitlines()
    male = []
    female = []
    Manager = []
    Developer = []
    Designer = []
    other = []
    employeelist = []
    salary = []
    for i in Contents:
      Split = i.split()
      employeelist.append(Split)
    for i in employeelist:
        salary.append(int(i[4]))
        print(salary)
    for i in employeelist:
      if i[3] == 'Manager':
        Manager.append(i)
      elif i[3] == 'Developer':
        Developer.append(i)
      elif i[3] == 'Designer':
        Designer.append(i)
      else:
        other.append(i)


    print(f"{'ID':<5}{'First Name':<15}{'Last Surname':<15}{'Position':<10}{'Salary':<6}{'Age':<6}{'Gender':<6}")
    print("="*70)
    for i in employeelist:
      id = i[0]
      FN = i[1]
      LS = i[2]
      Position = i[3]
      Salary = i[4]
      age = i[5]
      G = i[6]
      print(f"{id:<5}{FN:<15}{LS:<15}{Position:<10}{Salary:<6}{age:<6}{G:<6}")
    print()
    print('Summary of Employee Data:')
    print(f'Manager:{len(Manager)}')
    print(f'Developer:{len(Developer)}')
    print(f'Designer:{len(Designer)}')
    print(f'Total Employees:{len(employeelist)}')
    print(f'Maxinum Salary:{max(salary)}')
    print(f'Maxinum Salary:{min(salary)}')
    print(f'Maxinum Salary:{sum(salary)}')


