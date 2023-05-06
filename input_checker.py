def check_letters_only(input):
    for c in range(len(input)):
        if not(ord(input[c]) >= 65 and ord(input[c]) <= 90) and  not(ord(input[c]) >= 97 and ord(input[c]) <= 122) and not(ord(input[c]) == 32):
            return 0
    return 1
def check_digits_only(input):
    for c in range(len(input)):
        if not(ord(input[c]) >= 48 and ord(input[c]) <= 57):
            return 0
    return 1

def check_phone_number(input):
    if input[0] != '0':
        return 0
    
    if len(input) != 11:
        return 0
    
    if check_digits_only(input) == 0:
        return 0
    return 1

def check_course_name(input):
    for c in range(len(input)):
        if not(ord(input[c]) >= 65 and ord(input[c]) <= 90) and  not(ord(input[c]) >= 97 and ord(input[c]) <= 122) and not(ord(input[c]) == 32) and not(ord(input[c]) >= 48 and ord(input[c]) <= 57):
            return 0
    return 1

def checkNotEmpty(input):
    if len(input) == 0:
        return 0
    return 1

def check_ID(input):
    if len(input) != 6:
        return 0
    if check_digits_only(input) == 0:
        return 0
    return 1
