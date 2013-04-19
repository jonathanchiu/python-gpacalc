# Constants
A = 4.000
A_MINUS = 3.667
B_PLUS = 3.333
B = 3.000
B_MINUS = 2.667
C_PLUS = 2.333
C = 2.000
C_MINUS = 1.667
D_PLUS = 1.333
D = 1.000
D_MINUS = 0.667
F = 0.000

# Fall 2012 Grades
FALL_12 = [[A_MINUS, 4],   # East Asian Studies
            [A, 1],        # Overview I
            [B_MINUS, 4],  # Discrete Structures
            [B, 4],        # Fundies I
            [B, 1],        # Fundies I Lab
            [A_MINUS, 4]]  # College Writing
                           # ______________________
                           # Fall 2012 GPA: 3.278

# Make a formatted grade list that will work with the below functions
def make_grade_list():
    result = []
    numberOfCourses = int(raw_input("How many courses did you take?: "))
    for i in range(0, numberOfCourses):
        grade = raw_input("Grade for course?: ")
        credit = raw_input("Number of credits for course?: ")
        if grade == 'A':
            combo = [A, credit]
        elif grade == 'A-':
            combo = [A_MINUS, credit]
        elif grade == 'B+':
            combo = [B_PLUS, credit]
        elif grade == 'B':
            combo = [B, credit]
        elif grade == 'B-':
            combo = [B_MINUS, credit]
        elif grade == 'C+':
            combo = [C_PLUS, credit]
        elif grade == 'C':
            combo = [C, credit]
        elif grade == 'C-':
            combo = [C_MINUS, credit]
        elif grade == 'D+':
            combo = [D_PLUS, credit]
        elif grade == 'D':
            combo = [D, credit]
        elif grade == 'D-':
            combo = [D_MINUS, credit]
        else:
            combo = [F, credit]
        result.append(combo)
    return result


# Calculate the quality points of each
# course and make a list out of them
def qpt_calc(l):
    initialResult = []
    for i in l:
        # Make a list of list
        initialResult.append([i[0] * i[1]])
    # Flatten the list
    finalResult = [i for subl in initialResult for i in subl]
    return finalResult

# Calculate the total credit hours for your schedule
def total_credit_hours(l):
    result = 0
    for i in l:
        result += i[1]
    return result

# Calculate final GPA
def gpa_calc(l):
    sumQPT = sum(qpt_calc(l))
    totalHours = total_credit_hours(l)
    return sumQPT / totalHours
