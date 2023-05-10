from collections import defaultdict
import operator

# read N integer
N = int(input())

# read data from file
applicants = []
with open('applicants.txt', 'r') as file:
    for line in file:
        first_name, last_name, gpa, *priorities = line.split()
        applicants.append([f'{first_name} {last_name}', float(gpa), priorities])

# sort applicants by name and gpa
applicants.sort(key=operator.itemgetter(0))  # sort by name
applicants.sort(key=operator.itemgetter(1), reverse=True)  # sort by gpa

departments = defaultdict(list)
department_names = ['Biotech', 'Chemistry', 'Engineering', 'Mathematics', 'Physics']

for i in range(3):  # for each priority
    remaining_applicants = []
    for applicant in applicants:
        name, gpa, priorities = applicant
        if len(priorities) > i and len(departments[priorities[i]]) < N:
            departments[priorities[i]].append([name, gpa])
        else:
            remaining_applicants.append(applicant)
    applicants = remaining_applicants

# print departments
for department_name in department_names:
    print(department_name)
    for name, gpa in sorted(departments[department_name], key=lambda x: (-x[1], x[0])):
        print(name, gpa)
    print()
