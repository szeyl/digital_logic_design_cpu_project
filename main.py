import re

separators = ", ", " "
input_file = 'input.txt'
lines = []
output = []


def find_twos_complement(str):
    n = len(str)

    # Traverse the string to get first
    # '1' from the last of string
    i = n - 1
    while i >= 0:
        if str[i] == '1':
            break

        i -= 1

    # If there exists no '1' concatenate 1
    # at the starting of string
    if i == -1:
        return '1' + str

    # Continue traversal after the
    # position of first '1'
    k = i - 1
    while k >= 0:

        # Just flip the values
        if str[k] == '1':
            str = list(str)
            str[k] = '0'
            str = ''.join(str)
        else:
            str = list(str)
            str[k] = '1'
            str = ''.join(str)

        k -= 1

    # return the modified string
    return str


def check_negative(immediate_value):
    if int(immediate_value) < 0:
        temp_value = format(int(immediate_value), "8b")
        str_value = str(temp_value)
        tc = find_twos_complement(str_value)
        return int(tc)
    else:
        temp_immediate_value = format(int(immediate_value), "08b")
        return str(temp_immediate_value)


def custom_split(separator_list, str_to_split):
    # create regular expression dynamically
    regular_exp = '|'.join(map(re.escape, separator_list))
    return re.split(regular_exp, str_to_split)


def add(destination, first_register, second_register, ):
    temp_destination = format(int(destination[1]), "03b")
    temp_first_value = format(int(first_register[1]), "03b")
    temp_second_value = format(int(second_register[1]), "03b")
    total_value = "1111100" + str(temp_destination) + str(temp_first_value) + str(temp_second_value)
    print("ADD")
    print(total_value)
    global output
    output.append(total_value)
    return 0


def addi(destination, first_register, immediate_value):
    temp_destination = format(int(destination[1]), "03b")
    temp_first_value = format(int(first_register[1]), "03b")
    temp_immediate_value = check_negative(immediate_value)
    total_value = "00" + str(temp_destination) + str(temp_first_value) + str(temp_immediate_value)
    print("ADDI")
    print(total_value)
    global output
    output.append(total_value)
    return 0


def and_def(destination, first_register, second_register):
    temp_destination = format(int(destination[1]), "03b")
    temp_first_value = format(int(first_register[1]), "03b")
    temp_second_value = format(int(second_register[1]), "03b")
    total_value = "1111110" + str(temp_destination) + str(temp_first_value) + str(temp_second_value)
    print("AND")
    print(total_value)
    global output
    output.append(total_value)
    return 0


def andi(destination, first_register, immediate_value):
    temp_destination = format(int(destination[1]), "03b")
    temp_first_value = format(int(first_register[1]), "03b")
    temp_immediate_value = check_negative(immediate_value)
    total_value = "01" + str(temp_destination) + str(temp_first_value) + str(temp_immediate_value)
    print("ANDI")
    print(total_value)
    global output
    output.append(total_value)
    return 0


def ld(destination, value):
    temp_destination = format(int(destination[1]), "03b")
    temp_value = format(int(value), "010b")
    total_value = "100" + str(temp_destination) + str(temp_value)
    print("LD")
    print(total_value)
    global output
    output.append(total_value)
    return 0


def st(source_register, displacement):
    temp_first_value = format(int(source_register[1]), "03b")
    temp_value = format(int(displacement), "010b")
    total_value = "101" + str(temp_first_value) + str(temp_value)
    print("ST")
    print(total_value)
    global output
    output.append(total_value)
    return 0


def cmp(first_register, second_register):
    temp_first_value = format(int(first_register[1]), "03b")
    temp_second_value = format(int(second_register[1]), "03b")
    total_value = "1111000000" + str(temp_first_value) + str(temp_second_value)
    print("CMP")
    print(total_value)
    global output
    output.append(total_value)
    return 0


def jump(address):
    global output
    if int(address) < 0:
        temp_value = format(int(address), "010b")
        str_value = str(temp_value)
        tc = find_twos_complement(str_value)
        total_value = "110000" + str(tc)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    else:
        temp_address = format(int(address), "010b")
        total_value = "110000" + str(temp_address)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    return 0


def je(address):
    global output
    if int(address) < 0:
        temp_value = format(int(address), "010b")
        str_value = str(temp_value)
        tc = find_twos_complement(str_value)
        total_value = "110010" + str(tc)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    else:
        temp_address = format(int(address), "010b")
        total_value = "110010" + str(temp_address)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    return 0


def ja(address):
    global output
    if int(address) < 0:
        temp_value = format(int(address), "010b")
        str_value = str(temp_value)
        tc = find_twos_complement(str_value)
        total_value = "110100" + str(tc)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    else:
        temp_address = format(int(address), "010b")
        total_value = "110100" + str(temp_address)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    return 0


def jae(address):
    global output
    if int(address) < 0:
        temp_value = format(int(address), "010b")
        str_value = str(temp_value)
        tc = find_twos_complement(str_value)
        total_value = "110110" + str(tc)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    else:
        temp_address = format(int(address), "010b")
        total_value = "110110" + str(temp_address)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    return 0


def jb(address):
    global output
    if int(address) < 0:
        temp_value = format(int(address), "010b")
        str_value = str(temp_value)
        tc = find_twos_complement(str_value)
        total_value = "111000" + str(tc)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    else:
        temp_address = format(int(address), "010b")
        total_value = "111000" + str(temp_address)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    return 0


def jbe(address):
    global output
    if int(address) < 0:
        temp_value = format(int(address), "010b")
        str_value = str(temp_value)
        tc = find_twos_complement(str_value)
        total_value = "111010" + str(tc)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    else:
        temp_address = format(int(address), "010b")
        total_value = "111010" + str(temp_address)
        print("JUMP")
        print(total_value)
        output.append(total_value)
    return 0


def load_file(file_name):
    global lines
    file_opener = open(file_name)
    for line in file_opener:
        lines.append(line)
    file_opener.close()


load_file(input_file)

for line in lines:
    tokens = custom_split(separators, line)

    operand = tokens[0]

    if operand == "ADD":
        add(tokens[1], tokens[2], tokens[3])
    elif operand == "ADDI":
        addi(tokens[1], tokens[2], tokens[3])
    elif operand == "AND":
        and_def(tokens[1], tokens[2], tokens[3])
    elif operand == "ANDI":
        andi(tokens[1], tokens[2], tokens[3])
    elif operand == "LD":
        ld(tokens[1], tokens[2])
    elif operand == "ST":
        st(tokens[1], tokens[2])
    elif operand == "CMP":
        cmp(tokens[1], tokens[2])
    elif operand == "JUMP":
        jump(tokens[1])
    elif operand == "JE":
        je(tokens[1])
    elif operand == "JA":
        ja(tokens[1])
    elif operand == "JAE":
        jae(tokens[1])
    elif operand == "JB":
        jb(tokens[1])
    elif operand == "JBE":
        jbe(tokens[1])
    else:
        print("UNKNOWN OPERAND !!!")


def pad_to_4_digits(hex_number):
    padded = hex_number[2:]
    for i in range(4 - len(padded)):
        padded = '0' + padded
    return padded


output_file_opener = open('output.hex', 'w')

output_file_opener.write('v2.0 raw\n')
for outputs in output:
    hexadecimal = pad_to_4_digits(hex(int(outputs, 2)))
    output_file_opener.write(hexadecimal + "\n")

output_file_opener.close()
