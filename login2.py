def ValidPassword(password):
    correctlength=False
    has_uppercase=False
    has_lowercase=False
    has_digit=False
    
    if len(password)>=7:
        correctlength=True
        for ch in password:
            if ch.islower():
                has_lowercase=True
            if ch.isupper():
                has_uppercase=True
            if ch.isdigit():
                has_digit=True
    if correctlength and has_uppercase and has_lowercase and has_digit:
        is_valid=True
    else:
        is_valid=False 
    return is_valid 

