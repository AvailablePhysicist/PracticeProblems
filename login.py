def get_login_names(first, last, IDnumber):
    set1=first[0:4]
    set2=last[0:4]
    set3=IDnumber[-3:]
    fullID=set1+''+set2+''+set3
    return fullID
    