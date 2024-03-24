# COMP9021 24T1
# Assignment 1 *** Due Monday 25 March (Week 7) @ 9.00am
import sys
import re

romanlist = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
             (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
romanalpha = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
clasic_roman_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def please_convert():
    # detect form of input
    string_o = input('How can I help you? ')
    string_c = string_o.split()
    if len(string_o) <= 14 or string_c[0] != 'Please' or string_c[1] != 'convert':
        print("I don\'t get what you want, sorry mate!")
        sys.exit()
    elif len(string_c) < 3 or len(string_c) > 5:
        print("I don\'t get what you want, sorry mate!")
        sys.exit()

    # first kind of input
    if len(string_c) == 3:
         convert_1(string_c[2])
    if len(string_c) == 5:
        if string_c[3] != 'using':
            print("I don\'t get what you want, sorry mate!")
            sys.exit()
        else:
            convert_2(string_c[2],string_c[4])
    if len(string_c) == 4:
        if string_c[3] != 'minimally':
            print("I don\'t get what you want, sorry mate!")
            sys.exit()
        else:
            convert_3(string_c[2])



def int_to_roman(input):
    result = ''
    for digit, roman in romanlist:
        count = input // digit
        input = input % digit
        result += roman * count
        if input == 0:
            break
    return result


# the first kind of input
def convert_1(input):
    input_1 = input
    flag_1 = input_1.isdigit()
    flag_2 = input_1.isalpha()

    if flag_1 == True:  # number to roman number
        if input_1[0] == '0' or int(input_1) > 3999 or int(input_1) <= 0:
            print('Hey, ask me something that\'s not impossible to do!')
            sys.exit()
        else:
            result = ''
            input_1 = int(input_1)
            for digit, roman in romanlist:
                count = input_1 // digit
                input_1 = input_1 % digit
                result += roman * count
                if input_1 == 0:
                    break
            print('Sure! It is', result)
            sys.exit()

    elif flag_2 == True:
        for e in input_1:
            if e not in romanalpha:
                print('Hey, ask me something that\'s not impossible to do!')
                sys.exit()
        if is_roman_number(input_1):
            print('Sure! It is', roman_to_int(input_1,clasic_roman_dict))
            sys.exit()
        else:
            print('Hey, ask me something that\'s not impossible to do!')
            sys.exit()

# is valid roman number
def is_roman_number(num):

    pattern = re.compile(r"""    
                                ^M{0,3}
                                (CM|CD|D?C{0,3})?
                                (XC|XL|L?X{0,3})?
                                (IX|IV|V?I{0,3})?$
            """, re.VERBOSE)

    if re.match(pattern, num):
        return True
    return False

# roman number to int
def roman_to_int(string,roman_alpha):
    result = 0
    for i in range(len(string)-1):
        if roman_alpha[string[i]] < roman_alpha[string[i+1]]:
            result -= roman_alpha[string[i]]
        else:
            result += roman_alpha[string[i]]
    result += roman_alpha[string[-1]]
    return result

# the secon kind of input
def convert_2(input,form):
    flag_1 = input.isdigit()
    flag_2 = input.isalpha()
    flag_3 = form.isalpha()

    if flag_1 == True and flag_3 == True:
        for e in form:
            if form.count(e) > 1:
                print('Hey, ask me something that\'s not impossible to do!')
                sys.exit()

        if input[0] == '0' or int(input) < 0:
            print('Hey, ask me something that\'s not impossible to do!')
            sys.exit()
        else :
            input =int(input)
            l1,l2,l3,l4 = customise_dict(form)
            # print(l1)
            result = ''
            for digit, roman in l1:
                count = input // digit
                input = input % digit
                result += roman * count
                if input == 0:
                    break
            if isvaild_a2r(result):
                print('Sure! It is', result)
                sys.exit()
            else:
                print('Hey, ask me something that\'s not impossible to do!')
                sys.exit()

    elif flag_2 == True and flag_3 == True:
        for e in form:
            if form.count(e) > 1:
                print('Hey, ask me something that\'s not impossible to do!')
                sys.exit()

        temp_list = []
        for letter in form:
            temp_list.append(letter)
        for e in input:
            if e not in temp_list:
                print('Hey, ask me something that\'s not impossible to do!')
                sys.exit()
        l1, l2, l3, l4 = customise_dict(form)
        # print(l2)

        if is_five_repeated(input,l2):
            print('Hey, ask me something that\'s not impossible to do!')
            sys.exit()

        result = 0
        result = roman_to_int(input,l2)

        detect_string = ''
        detect_result = result
        for digit, roman in l1:
            count = detect_result // digit
            detect_result = detect_result % digit
            detect_string += roman * count
            if detect_result == 0:
                break

        if detect_string == input:
            print('Sure! It is', result)
            sys.exit()
        else :
            print('Hey, ask me something that\'s not impossible to do!')
            sys.exit()

    else:
        print('Hey, ask me something that\'s not impossible to do!')
        sys.exit()

def customise_dict(string):
    string = ''.join(reversed(string))
    dict_list = []
    dict_list_reverseindex = []
    for i in range(len(string)):
        if i%2 == 0:
            digit =pow(10,i//2)
            letter = string[i]
            temp = (digit,letter)
            temp_r = (letter,digit)
            dict_list.append(temp)
            dict_list_reverseindex.append(temp_r)
        if i % 2 == 1:
            digit = pow(10,i//2) * 5
            letter = string[i]
            temp = (digit, letter)
            temp_r = (letter, digit)
            dict_list.append(temp)
            dict_list_reverseindex.append(temp_r)


    sim_dict = dict(dict_list_reverseindex)

    # special composite character
    for i in range(len(dict_list)):
        if i%2 == 0 and i != 0:
            digit = int(dict_list[i][0])-int(dict_list[i-2][0])
            letter = dict_list[i-2][1]+dict_list[i][1]
            temp = (digit, letter)
            dict_list.append(temp)
        elif i%2 == 1:
            digit = int(dict_list[i][0]) - int(dict_list[i - 1][0])
            letter = dict_list[i - 1][1] + dict_list[i][1]
            temp = (digit, letter)
            dict_list.append(temp)

    dict_list = sorted(dict_list)
    dict_list_a2r = reversed(dict_list)
    com_dict = dict(dict_list)

    return dict_list_a2r,sim_dict,dict_list,com_dict

def isvaild_a2r(string):
    pin = 0
    for s in reversed(string):
        if string.count(s)>=4:
            if string[string.index(s):len(string)-pin] == s*4:
                return False
        pin += 1
    return True

def is_five_repeated(input, dict):
    not_repeated_list = []
    for key,value in dict.items():
        value = str(value)
        if value[0] == '5':
            not_repeated_list.append(key)

    for e in input:
        if e in not_repeated_list and input.count(e)>1:
            return True
    return False

def convert_3(input):
    if input.isalpha() == False:
        print('Hey, ask me something that\'s not impossible to do!')
        sys.exit()
    else:
        roman_list_record = []
        for i in range(1,101):
            roman_list_record.append(int_to_roman(i))
        # print(roman_list_record)
        valid_pattern_list = []
        for r in roman_list_record:
            valid_pattern_list.append(get_pattern(r))
        # print(valid_pattern_list)
        block = ''
        detect_pin = 0
        result = []
        for s in reversed(input):
            if input.count(s) > 1 and s not in block:
                start = input.index(s)
                end = len(input) - detect_pin
                circle = input[start:end]
                detect_pin += len(circle)
                for i in circle:
                    if input.count(i) - circle.count(i) != 0:
                        print('Hey, ask me something that\'s not impossible to do!')
                        sys.exit()
                if get_pattern(circle) in valid_pattern_list:
                    if get_pattern(circle + block) in valid_pattern_list:
                        block = circle + block
                    else:
                        result.append(block)
                        block = circle
                else:
                    print('Hey, ask me something that\'s not impossible to do!')
                    sys.exit()
            if input.count(s) == 1 and s not in block:
                detect_pin += 1
                if get_pattern(s + block) in valid_pattern_list:
                    block = s + block
                else:
                    result.append(block)
                    block = s
        result.append(block)
        # print(result)
        form = ''
        for i in range(len(result)):

            if i == 0:
                form = match_smallest_romanpattern(result[i],valid_pattern_list,roman_list_record)
                # print(form)
            else:
                temp = match_smallest_romanpattern(result[i],valid_pattern_list,roman_list_record)
                # print(temp)
                #  if letter in form is repeated word and it cann't be symbol for presenting number starting with 5
                # it means this letter cannot be in even position
                for i in temp:
                    if input.count(i) > 1:
                        temp_r = ''.join(reversed(temp))
                        if (len(form)+temp_r.index(i)+1) % 2 == 1:
                            form = temp + form
                            # print(form)
                        else:
                            form = temp + '_' +form
        # print(form)

        l1, l2, l3, l4 = customise_dict(form)
        # print(l2)

        if is_five_repeated(input, l2):
            print('Hey, ask me something that\'s not impossible to do!')
            sys.exit()

        f_result = 0
        f_result = roman_to_int(input, l2)
        # print(f_result)

        detect_string = ''
        detect_result = f_result
        for digit, roman in l1:
            count = detect_result // digit
            detect_result = detect_result % digit
            detect_string += roman * count
            if detect_result == 0:
                break

        if detect_string == input:
            print("Sure! It is " + str(f_result) + " using " + form)
            sys.exit()
        else:
            print('Hey, ask me something that\'s not impossible to do4!')
            sys.exit()

def get_pattern(string):
    pattern = []
    for s in string:
        pattern.append(string.count(s))
    return pattern

def match_smallest_romanpattern(string,valid_pattern,roman_list):
    part_form = ''
    index = valid_pattern.index(get_pattern(string))
    origin_roman_seq = roman_list[index]
    for i in reversed(romanalpha):
        if i in origin_roman_seq:
            part_form += string[origin_roman_seq.index(i)]
        else:
            part_form += '_'
    part_form = part_form.lstrip('_')
    return part_form

please_convert()