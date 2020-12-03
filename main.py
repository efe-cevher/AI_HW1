import sys

data_file_name = sys.argv[1]
clue_file_name = sys.argv[2]

data_input_str = open("files/" + data_file_name).read()
clue_input_str = open("files/" + clue_file_name).read()

data_input_list = data_input_str.split("\n")
clue_input_list = clue_input_str.split("\n")

attr_input_list = data_input_list[0].split(",")

attr_a = attr_input_list[0]
attr_a_values = attr_input_list[1:]

attr_b = attr_input_list[1]
attr_b_values = attr_input_list[1:]

attr_c = attr_input_list[2]
attr_c_values = attr_input_list[1:]

attr_d = attr_input_list[3]
attr_d_values = attr_input_list[1:]