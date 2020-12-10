import glob

def data_parser(input_str):
    input_list = input_str.split('\n')
    data = {}
    for line in input_list:
        if(len(line) > 0):
            attr_input_list = line.split(",")
            attr_name = attr_input_list[0]
            domains = attr_input_list[1:]
            data[attr_name] = domains
    return data

def clue_parser(line):
    line_elements = line.split(" ")
    if line_elements[0] == "if":
        equality = line_elements[1].split('=')
        x, a = equality[0], equality[1]

        if line_elements[3] == "not":
            equality = line_elements[4].split('=')
            y, b = equality[0], equality[1]

            return [2, [x, a, y, b]]

        elif line_elements[3] == "either":
            equality = line_elements[4].split('=')
            y, b = equality[0], equality[1]

            equality = line_elements[6].split('=')
            z, c = equality[0], equality[1]

            return [3, [x, a, y, b, z, c]]
        
        else:
            equality = line_elements[3].split('=')
            y, b = equality[0], equality[1]

            return [1, [x, a, y, b]]

    elif line_elements[0] == "one":

        equalities = line_elements[2][1:-1].split(',')
        
        equality = equalities[0].split('=')
        x, a = equality[0], equality[1]

        equality = equalities[1].split('=')
        y, b = equality[0], equality[1]

        equality = line_elements[5].split('=')
        z, c = equality[0], equality[1]

        equality = line_elements[7].split('=')
        t, d = equality[0], equality[1]

        return [9, [x, a, y, b, z, c, t, d]]

    elif line_elements[0][0] == "{":
        equalities = line_elements[0][1:-1].split(',')

        equality = equalities[0].split('=')
        x, a = equality[0], equality[1]

        equality = equalities[1].split('=')
        y, b = equality[0], equality[1]

        equality = equalities[2].split('=')
        z, c = equality[0], equality[1]
        
        return [10, [x, a, y, b, z, c]]

    else:
        tmp = line_elements[0].split('(')
        n = tmp[0]
        equality = tmp[1][:-1].split('=')
        x, a = equality[0], equality[1]

        if line_elements[1] == '>':
            tmp = line_elements[2].split('(')
            equality = tmp[1][:-1].split("=")
            y, b = equality[0], equality[1]

            return [7, [x, a, y, b, n]]

        elif line_elements[1] == '<':
            tmp = line_elements[2].split('(')
            equality = tmp[1][:-1]
            y, b = equality[0], equality[1]

            return [8, [x, a, y, b, n]]

        else:
            tmp = line_elements[2].split('(')
            equality = tmp[1][:-1].split('=')

            y, b = equality[0], equality[1]

            if len(line_elements) > 3:
                m = int(line_elements[4])

                if line_elements[3] == '+':
                    return [5, [x, a, y, b, n, m]]

                elif line_elements[3] == '-':
                    return [6, [x, a, y, b, n, m]]
            else:
                return [4, [x, a, y, b, n]]

def clue_1(s, x, a, y, b):
    if {x, y}.issubset(set(s.keys())):
        if s[x] == a:
            return s[y] == b
    return True

def clue_2(s, x, a, y, b):
    if {x, y}.issubset(set(s.keys())):
        if s[x] == a:
            return s[y] != b
    return True

def clue_3(s, x, a, y, b, z, c):
    if {x, y, z}.issubset(set(s.keys())):
        if s[x] == a:
            return (s[y] == b) ^ (s[z] == c)
    return True

def clue_4(s1, s2, x, a, y, b, n):
    if {x, n}.issubset(set(s1.keys())) and {y, n}.issubset(set(s2.keys())):
        if s1[x] == a and s2[y] == b:
            return int(s1[n]) == int(s2[n])
    return True

def clue_5(s1, s2, x, a, y, b, n, m):
    if {x, n}.issubset(set(s1.keys())) and {y, n}.issubset(set(s2.keys())):
        if s1[x] == a and s2[y] == b:
            return int(s1[n]) == int(s2[n]) + int(m)
    return True

def clue_6(s1, s2, x, a, y, b, n, m):
    if {x, n}.issubset(set(s1.keys())) and {y, n}.issubset(set(s2.keys())):
        if s1[x] == a and s2[y] == b:
            return int(s1[n]) == int(s2[n]) - int(m)
    return True

def clue_7(s1, s2, x, a, y, b, n):
    if {x, n}.issubset(set(s1.keys())) and {y, n}.issubset(set(s2.keys())):
        if s1[x] == a and s2[y] == b:
            return int(s1[n]) > int(s2[n])
    return True

def clue_8(s1, s2, x, a, y, b, n):
    if {x, n}.issubset(set(s1.keys())) and {y, n}.issubset(set(s2.keys())):
        if s1[x] == a and s2[y] == b:
            return int(s1[n]) < int(s2[n])
    return True

def clue_9(s1, s2, x, a, y, b, z, c, t, d):
    if {x, z, t}.issubset(set(s1.keys())) and {y, z, t}.issubset(set(s2.keys())):
        if s1[x] == a and s2[y] == b:
            if s1 == s2:
                return False
            return (s1[z] == c and s2[t] == d) or (s1[t] == d and s2[z] == c)
    return True

def clue_10(s1, s2, s3, x, a, y, b, z, c):
    if {x}.issubset(set(s1.keys())) and {y}.issubset(set(s2.keys())) and {z}.issubset(set(s3.keys())):
        if s1[x] == a and s2[y] == b and s3[z] == c:
            return s1!=s2 and s2!=s3 and s1!=s3
        
    return True

def isConsistent(subjects):
    for clue in clues:
        if clue[0] == 1:
            for subject in subjects:
                if not clue_1(subject, clue[1][0], clue[1][1], clue[1][2], clue[1][3]):
                    return False

        elif clue[0] == 2:
            for subject in subjects:
                if not clue_2(subject, clue[1][0], clue[1][1], clue[1][2], clue[1][3]):
                    return False
                    
        elif clue[0] == 3:
            for subject in subjects:
                if not clue_3(subject, clue[1][0], clue[1][1], clue[1][2], clue[1][3], clue[1][4], clue[1][5]):
                    return False

        elif clue[0] == 4:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_4(s1, s2, clue[1][0], clue[1][1], clue[1][2], clue[1][3], clue[1][4]):
                        return False

        elif clue[0] == 5:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_5(s1, s2, clue[1][0], clue[1][1], clue[1][2], clue[1][3], clue[1][4], clue[1][5]):
                        return False

        elif clue[0] == 6:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_6(s1, s2, clue[1][0], clue[1][1], clue[1][2], clue[1][3], clue[1][4], clue[1][5]):
                        return False

        elif clue[0] == 7:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_7(s1, s2, clue[1][0], clue[1][1], clue[1][2], clue[1][3], clue[1][4]):
                        return False
        
        elif clue[0] == 8:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_8(s1, s2, clue[1][0], clue[1][1], clue[1][2], clue[1][3], clue[1][4]):
                        return False
        
        elif clue[0] == 9:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_9(s1, s2, clue[1][0], clue[1][1], clue[1][2], clue[1][3], clue[1][4], clue[1][5], clue[1][6], clue[1][7]):
                        return False

        elif clue[0] == 10:
            for s1 in subjects:
                for s2 in subjects:
                    for s3 in subjects:
                        if not clue_10(s1, s2, s3, clue[1][0], clue[1][1], clue[1][2], clue[1][3], clue[1][4], clue[1][5]):
                            return False
    
    for s1 in subjects:
        for s2 in subjects:
            for val in s2.values():
                if val in s1.values() and s1!=s2:
                    return False
        
    return True

def find_empty(subjects, attributes):
    i = 0
    for subject in subjects:
        for attr in attributes:
            if not {attr}.issubset(set(subject.keys())):
                
                return (i, attr)
        i+=1
    return None


def solve(subjects, data):
    attributes = list(data.keys())
    find = find_empty(subjects,attributes)
    if not find:
        return True
    else:
        subject_no, attr = find

    for a in data[attr]:
        subjects[subject_no][attr] = a
        if isConsistent(subjects):
            if solve(subjects, data):
                return True
        
        subjects[subject_no].pop(attr)

    return False

def show_result(subjects, data):
    attributes = list(data.keys())
    attributes_line = ""
    space = 12

    for attr in attributes:
        attributes_line += attr

        for i in range(space - len(attr)):   
            attributes_line += " "

        if len(attributes) > attributes.index(attr) + 1:
            attributes_line += "| "
    print(attributes_line)

    print('-------------------------------------------------')
    
    for subject in subjects:
        subject_line = ""
        for val in subject.values():
            subject_line += val
            
            for i in range(space - len(val)):   
                subject_line += " "

            if len(subject.values()) > list(subject.values()).index(val) + 1:
                subject_line += "| "

        print(subject_line)


clue_files = glob.glob("clues-*.txt")
data_files = glob.glob("data-*.txt")

available_problems = []

for filename in clue_files:
    problem_no = filename[6:7]
    data_filename = "data-" + problem_no + ".txt"
    if data_filename in data_files:
        available_problems.append(problem_no)
    

print("The problems available in your directory: " + str(available_problems))

problem_input = input("Choose a problem: ")

if problem_input in available_problems:
    data_file_name = 'data-' + problem_input + '.txt'
    clue_file_name = 'clues-' + problem_input + '.txt'
else:
    print("Wrong input")
    exit()

print("\nHere is the solution for the problem defined in " + data_file_name + " and " + clue_file_name + ":")

data_input_str = open(data_file_name).read()
clue_input_str = open(clue_file_name).read()

data = data_parser(data_input_str)

clues = []
clue_input_list = clue_input_str.split('\n')
for line in clue_input_list:
    if(len(line) > 0):
        clues.append(clue_parser(line))

subjects = []
for attr in list(data.keys()):
    subjects.append({})

solve(subjects, data)
show_result(subjects, data)
