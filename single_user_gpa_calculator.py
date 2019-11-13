import csv


course_list = []
score_list = []
unit_list = []
TCP_list = []
grade_list = []

# defining the input function


def input_func():
    print("Input course code, score and course unit seperated by comma or q to exit")
    while True:
        data = input(": ").capitalize()
        if data == 'Q':
            break
        try:
            course, score, unit = data.split(',')
            score_list.append(int(score))
            unit_list.append(int(unit))
            course_list.append(course)
        except:
            print('Invalid Input, Please retry')
            continue


# defining the grading function


def grade_function(score_list):

    for score in score_list:
        if score >= 70:
            grade = 5
            # print("A")
        elif score >= 60:
            grade = 4
            # print("B")
        elif score >= 50:
            grade = 3
            # print("C")
        elif score >= 45:
            grade = 2
            # print("D")
        else:
            grade = 0
            # print("F")

        grade = int(grade)
        grade_list.append(grade)


# defining computation function


def compution_func(unit_list, grade_list):
    TLU = sum(unit_list)

    for i in range(0, len(grade_list)):
        TCP_list.append(grade_list[i] * unit_list[i])

    TCP = sum(TCP_list)

    gpa = TCP / TLU
    gpa = round(gpa, 2)

    print("Your gpa for this semester is ", gpa)
    return gpa

# defining the file function


def writting_to_file(course_list, unit_list, score_list, grade_list):
    data = []
    data.insert(0, course_list)
    data.insert(1, unit_list)
    data.insert(2, score_list)
    data.insert(3, grade_list)
    # data.insert(4, f'Student GPA = {GPA}')

    csv.register_dialect('myDialect', delimiter='-')
    quoting = csv.QUOTE_NONE,

    with open('textfile.csv', 'w') as csvFile:
        writer = csv.writer(csvFile, dialect='myDialect')
        writer.writerows(data)

    csvFile.close()
    print("Data = ", data)
    print(f'Writting DATA to csvFile.......')



# calling all the functions in order of preference


input_func()
grade_function(score_list)
compution_func(unit_list, grade_list)

writting_to_file(course_list, unit_list, score_list, grade_list)
