import sys

def data_parser(input_str):
    input_list = input_str.split('\n')
    data = {}
    for line in input_list:
        if not len(line) > 1:
            break
        attr_input_list = line.split(",")
        attr_name = attr_input_list[0]
        domains = attr_input_list[1:]
        data[attr_name] = domains
    return data

def clue_parser(line):
    line_elements = line.split(" ")
    if line_elements[0] == "if":
        equality = line_elements[1].split('=')
        x = equality[0]
        a = equality[1]

        if line_elements[3] == "not":
            equality = line_elements[4].split('=')
            y = equality[0]
            b = equality[1]

            return [2, [x, a, y, b]]

        elif line_elements[3] == "either":
            equality = line_elements[4].split('=')
            y = equality[0]
            b = equality[1]

            equality = line_elements[6].split('=')
            z = equality[0]
            c = equality[1]

            return [3, [x, a, y, b, z, c]]
        
        else:
            equality = line_elements[3].split('=')
            y = equality[0]
            b = equality[1]

            return [1, [x, a, y, b]]

    elif line_elements[0] == "one":
        equalities = line_elements[2][1:-1].split(',')

        equality = equalities[0]
        x = equality[0]
        a = equality[1]

        equality = equalities[1]
        y = equality[0]
        b = equality[1]

        equality = line_elements[5]
        z = equality[0]
        c = equality[1]

        equality = line_elements[7]
        t = equality[0]
        d = equality[1]

        return [9, [x, a, y, b, z, c, t, d]]

    elif line_elements[0][0] == "{":
        equalities = line_elements[0][1:-1].split(',')

        equality = equalities[0]
        x = equality[0]
        a = equality[1]

        equality = equalities[1]
        y = equality[0]
        b = equality[1]

        equality = equalities[2]
        z = equality[0]
        c = equality[1]

        return [10, [x, a, y, b, z, c]]

    else:
        tmp = line_elements[0].split('(')
        n = tmp[0]
        equality = tmp[1][:-1].split('=')
        x = equality[0]
        a = equality[1]

        if line_elements[1] == '>':
            tmp = line_elements[2].split('(')
            equality = tmp[1][:-1].split("=")
            y = equality[0]
            b = equality[1]

            return [7, [x, a, y, b, n]]

        elif line_elements[1] == '<':
            tmp = line_elements[2].split('(')
            equality = tmp[1][:-1]
            y = equality[0]
            b = equality[1]

            return [8, [x, a, y, b, n]]

        else:
            tmp = line_elements[2].split('(')
            equality = tmp[1][:-1].split('=')

            y = equality[0]
            b = equality[1]

            if len(line_elements) > 3:
                m = int(line_elements[4])
                if line_elements[3] == '+':
                    return [5, 2, [x, a, y, b, n, m]]
                elif line_elements[3] == '-':
                    return [6, 2, [x, a, y, b, n, m]]
            else:
                return [4, [x, a, y, b, n]]

def clue_1(s, x, a, y, b):
    if {x, y}.issubset(set(s.keys())):
        print(s[x])
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
        if s1[x] == a and s2[y] == b and s1 != s2:
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
    return True



data_file_name = sys.argv[1]
clue_file_name = sys.argv[2]

data_input_str = open("files/" + data_file_name).read()
clue_input_str = open("files/" + clue_file_name).read()

data = data_parser(data_input_str)

clues = []

clue_input_list = clue_input_str.split('\n')

for line in clue_input_list:
    if(len(line) > 0):
        clues.append(clue_parser(line))


subjects = [{},{},{},{}]

first_attr = list(data.keys())[0]

i = 0
for val in data[first_attr]:
    subjects[i][first_attr] = val
    i+=1
i=0
for val in data['owners']:
    subjects[i]['owners'] = val
    i+=1
i=0 
for val in data['breeds']:
    subjects[i]['breeds'] = val
    i+=1
i=0
for val in data['dogs']:
    subjects[i]['dogs'] = val
    i+=1


print(subjects)
print(isConsistent(subjects))