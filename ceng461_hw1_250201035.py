import glob
#parse given data file
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

#parse line of a given clue file
def clue_parser(line):
    line_elements = line.split(" ")
    if line_elements[0] == "if":
        eq = line_elements[1].split('=')
        x, a = eq[0], eq[1]

        if line_elements[3] == "not":
            eq = line_elements[4].split('=')
            y, b = eq[0], eq[1]

            return [2, [x, a, y, b]]

        elif line_elements[3] == "either":
            eq = line_elements[4].split('=')
            y, b = eq[0], eq[1]

            eq = line_elements[6].split('=')
            z, c = eq[0], eq[1]

            return [3, [x, a, y, b, z, c]]
        
        else:
            eq = line_elements[3].split('=')
            y, b = eq[0], eq[1]

            return [1, [x, a, y, b]]

    elif line_elements[0] == "one":

        eq_list = line_elements[2][1:-1].split(',')
        
        eq = eq_list[0].split('=')
        x, a = eq[0], eq[1]

        eq = eq_list[1].split('=')
        y, b = eq[0], eq[1]

        eq = line_elements[5].split('=')
        z, c = eq[0], eq[1]

        eq = line_elements[7].split('=')
        t, d = eq[0], eq[1]

        return [9, [x, a, y, b, z, c, t, d]]

    elif line_elements[0][0] == "{":
        eq_list = line_elements[0][1:-1].split(',')

        eq = eq_list[0].split('=')
        x, a = eq[0], eq[1]

        eq = eq_list[1].split('=')
        y, b = eq[0], eq[1]

        eq = eq_list[2].split('=')
        z, c = eq[0], eq[1]
        
        return [10, [x, a, y, b, z, c]]

    else:
        tmp = line_elements[0].split('(')
        n = tmp[0]
        eq = tmp[1][:-1].split('=')
        x, a = eq[0], eq[1]

        if line_elements[1] == '>':
            tmp = line_elements[2].split('(')
            eq = tmp[1][:-1].split("=")
            y, b = eq[0], eq[1]

            return [7, [x, a, y, b, n]]

        elif line_elements[1] == '<':
            tmp = line_elements[2].split('(')
            eq = tmp[1][:-1]
            y, b = eq[0], eq[1]

            return [8, [x, a, y, b, n]]

        else:
            tmp = line_elements[2].split('(')
            eq = tmp[1][:-1].split('=')

            y, b = eq[0], eq[1]

            if len(line_elements) > 3:
                m = int(line_elements[4])

                if line_elements[3] == '+':
                    return [5, [x, a, y, b, n, m]]
                    
                elif line_elements[3] == '-':
                    return [6, [x, a, y, b, n, m]]
            else:
                return [4, [x, a, y, b, n]]

#corresponding function for each format of a clue
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

#check consistency for all the rules provided
def isConsistent(subjects, clues):
    for c in clues:
        if c[0] == 1:
            for subject in subjects:
                if not clue_1(subject, c[1][0], c[1][1], c[1][2], c[1][3]):
                    return False

        elif c[0] == 2:
            for subject in subjects:
                if not clue_2(subject, c[1][0], c[1][1], c[1][2], c[1][3]):
                    return False
                    
        elif c[0] == 3:
            for subject in subjects:
                if not clue_3(subject, c[1][0], c[1][1], c[1][2], c[1][3], c[1][4], c[1][5]):
                    return False

        elif c[0] == 4:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_4(s1, s2, c[1][0], c[1][1], c[1][2], c[1][3], c[1][4]):
                        return False

        elif c[0] == 5:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_5(s1, s2, c[1][0], c[1][1], c[1][2], c[1][3], c[1][4], c[1][5]):
                        return False

        elif c[0] == 6:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_6(s1, s2, c[1][0], c[1][1], c[1][2], c[1][3], c[1][4], c[1][5]):
                        return False

        elif c[0] == 7:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_7(s1, s2, c[1][0], c[1][1], c[1][2], c[1][3], c[1][4]):
                        return False
        
        elif c[0] == 8:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_8(s1, s2, c[1][0], c[1][1], c[1][2], c[1][3], c[1][4]):
                        return False
        
        elif c[0] == 9:
            for s1 in subjects:
                for s2 in subjects:
                    if not clue_9(s1, s2, c[1][0], c[1][1], c[1][2], c[1][3], c[1][4], c[1][5], c[1][6], c[1][7]):
                        return False

        elif c[0] == 10:
            for s1 in subjects:
                for s2 in subjects:
                    for s3 in subjects:
                        if not clue_10(s1, s2, s3, c[1][0], c[1][1], c[1][2], c[1][3], c[1][4], c[1][5]):
                            return False
                            
    #same value for different subjects is not legal
    for s1 in subjects:
        for s2 in subjects:
            if s1!=s2:
                for val in s2.values():
                    if val in s1.values():
                        return False

    return True

#find next empty variable
def find_empty(subjects, attributes):
    i = 0
    for subject in subjects:
        for attr in attributes:
            if not {attr}.issubset(set(subject.keys())):
                return (i, attr)
        i+=1
    return None

#solve recursively using backtracking
def solve(subjects, data, clues):
    attributes = list(data.keys())
    find = find_empty(subjects,attributes)
    if not find:
        return True
    else:
        subject_no, attr = find

    for a in data[attr]:
        subjects[subject_no][attr] = a
        
        if isConsistent(subjects, clues):
            if solve(subjects, data, clues):
                return True

        subjects[subject_no].pop(attr)

    return False

#print result in a cli graph
def show_result(subjects):
    attributes = list(subjects[0].keys())
    attributes_line = ""
    space = 12

    for attr in attributes:
        attributes_line += attr

        for i in range(space - len(attr) -20):   
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

#for sorting to make sure the subjects are in ascending order
def get_numeric_val(subject):
    attr = list(subject.keys())[0]
    return int(subject[attr])

#find files in directory
clue_files = glob.glob("clues-*.txt")
data_files = glob.glob("data-*.txt")

available_problems = []

for filename in clue_files:
    problem_no = filename[6:7]
    data_filename = "data-" + problem_no + ".txt"
    if data_filename in data_files:
        available_problems.append(problem_no)
    
available_problems.sort()

if len(available_problems) == 0:
    print("No problems in your working directory")
    exit()

print("The problems available in your directory: " + str(available_problems))

problem_input = input("Choose a problem: ")

if problem_input in available_problems:
    data_file_name = 'data-' + problem_input + '.txt'
    clue_file_name = 'clues-' + problem_input + '.txt'
else:
    print("Wrong input")
    exit()

print("\nHere is the solution for the problem defined in " + data_file_name + " and " + clue_file_name + ":\n")

data_input_str = open(data_file_name).read()
clue_input_str = open(clue_file_name).read()

# data held as a dictionary with attributes as keys
data = data_parser(data_input_str)

# a clue held as [clue_type_no, [args]]
clues = []
clue_input_list = clue_input_str.split('\n')
for line in clue_input_list:
    if(len(line) > 0):
        clues.append(clue_parser(line))

# a subject held as a dictionary with attributes as keys
subjects = []
for attr in list(data.keys()):
    subjects.append({})

solve(subjects, data, clues)

subjects.sort(key=get_numeric_val)

show_result(subjects)
