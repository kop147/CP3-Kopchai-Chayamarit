import csv


def read():
    with open('Lecture86_homework.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0

        for row in csv_reader:
            if line_count == 0:
                print(f'Cloumn names are {",".join(row)}')
                line_count +=1
            else:
                print(f'\t{row[0]} favorites movies is {row[1]} and his favorite pet is{row[2]}')
                line_count += 1
        print(f'Processed {line_count} lines.')


def write():
    with open("Lecture86_homework.csv", mode="a") as employee_file:

        employee_file = csv.writer(employee_file, delimiter=',', quotechar= '"',quoting=csv.QUOTE_MINIMAL)

        employee_file.writerow(['Dilock', 'matrix', "dog"])



write()
read()