#Simple Sort in a line
listed = [1,2,3,4,5,7,8,534,5,6,755,632,234,0]
listed.sort(reverse=False)
print(listed)


#Simple Sort in a -line
listed = [1,2,3,4,5,7,8,534,5,6,755,632,234,0]
listed.sort(reverse=True)
print(listed)#


#Simple Sort of alphabet positive.
listed = ['d', 'a','j','m','c','b','e','r']
listed.sort(reverse=False)
print(listed)


#Simple Sort of alphabet Negative.
listed = ['d', 'a','j','m','c','b','e','r']
listed.sort(reverse=True)
print(listed)



############################################################################
# sorting using custom key :::: 

####Multi Dimention Array#####
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# custom functions to get employee info
def get_name_Function(employee):
    return employee.get('Name')


def get_age_Function(employee):
    return employee.get('age')


def get_salary_Function(employee):
    return employee.get('salary')


# sort by name (Ascending order)
employees.sort(key=get_name_Function)
print(employees, end='\n\n')

# sort by Age ######(Ascending order)#######
employees.sort(key=get_age_Function)
print(employees, end='\n\n')

# sort by salary ######(Descending order)######
employees.sort(key=get_salary_Function, reverse=True)
print(employees, end='\n\n')



