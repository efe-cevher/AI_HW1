import sys

data_file_name = sys.argv[1]
clue_file_name = sys.argv[2]

data_input_list = open("files/" + data_file_name).read().split("\n")
clue_input_list = open("files/" + clue_file_name).read().split("\n")

data = {}
constraints = []

for line in data_input_list:
    attr_input_list = line.split(",")
    attr_name = attr_input_list[0]
    domains = attr_input_list[1:]
    data[attr_name] = domains

for line in clue_input_list:

    if not len(line) > 1:
        break

    line_elements = line.split(" ")
    if line_elements[0] == "if":
        equality = line_elements[1].split('=')
        x = equality[0]
        a = equality[1]

        if line_elements[3] == "not":
            equality = line_elements[4].split('=')
            y = equality[0]
            b = equality[1]

            constraint = lambda s : s[x]!=a or s[y]!=b

        elif line_elements[3] == "either":
            equality = line_elements[4].split('=')
            y = equality[0]
            b = equality[1]

            equality = line_elements[6].split('=')
            z = equality[0]
            c = equality[1]

            constraint = lambda s : s[x]!=a or (s[y]==b ^ s[z]==c)
        
        else:
            equality = line_elements[3].split('=')
            y = equality[0]
            b = equality[1]

            constraint = lambda s : s[x]!=a or s[y]==b

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

        constraint = lambda s1,s2 : (s1==s2) or (s1[x]!=a or s2[y]!=b) or (s1[z]==c and s2[t]==d) or (s1[t]==d and s2[z]==c)

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
        
        constraint = lambda s1,s2,s3 : (not (s1[x]==a and s2[y]==b and s3[z]==c)) or (s1!=s2 and s2!=s3 and s1!=s3)

    else:
        tmp = line_elements[0].split('(')
        n1 = tmp[0]
        equality = tmp[1][:-1]
        x = equality[0]
        a = equality[1]

        if line_elements[1] == '>':
            tmp = line_elements[2].split('(')
            n2 = tmp[0]
            equality = tmp[1][:-1]
            y = equality[0]
            b = equality[1]

            constraint = lambda s1,s2 : (s1[x]!=a or s2[y]!=b) or s1[n1]>s2[n2]  

        elif line_elements[1] == '<':
            tmp = line_elements[2].split('(')
            n2 = tmp[0]
            equality = tmp[1][:-1]
            y = equality[0]
            b = equality[1]

            constraint = lambda s1,s2 : (s1[x]!=a or s2[y]!=b) or s1[n1]<s2[n2]

        else:
            tmp = line_elements[2].split('(')
            n2 = tmp[0]
            equality = tmp[1][:-1]
            y = equality[0]
            b = equality[1]

            if len(line_elements) > 3:
                m = int(line_elements[4])

                if line_elements[3] == '+':
                    constraint = lambda s1,s2 : (s1[x]!=a or s2[y]!=b) or s1[n1]==s2[n2]+m
                    constraints.append(constraint)
                else:
                    constraint = lambda s1,s2 : (s1[x]!=a or s2[y]!=b) or s1[n1]==s2[n2]-m
                    constraints.append(constraint)
            else:
                constraint = lambda s1,s2 : (s1[x]!=a or s2[y]!=b) or s1[n1]==s2[n2]
            
    constraints.append(constraint)
