import re
email_regex = r'^[a-zA-Z0-9_]+@[a-zA-Z]+\.[a-zA]+$'
pass_regex = r'^[a-zA-Z0-9_]+$'
phone_regex =r'[0-9]+$'

def ID(id):
    global row
    row = []
    row.insert(0,id)
       
   


def names(fname,lname) :
    if fname.isalpha() and lname.isalpha()and row[:1]:
        if len(fname) > 3 and len(lname) > 3: 
            row.insert(1,fname)
            row.insert(2,lname)
            return 1
    return 0

def email(ema):
    if isinstance(ema,str):
        if re.fullmatch(email_regex, ema) and row[:2]:
            if ema[0].isalpha():
                row.insert(3,ema)
                return 1
    return 0


def passw(passw):
    if isinstance(passw,str)and row[:3]:
        #  print("YESSSSSSSSS")
         upper = any(char.isupper() for char in passw)
         lower = any(char.islower() for char in passw)
         digt = any(dig.isdigit() for dig in passw )
         if passw[0].isalpha() and upper and lower and re.fullmatch(pass_regex,passw) and len(passw)>=5:  
             row.insert(4,passw)
             return 1
    return 0


def phone(mob):
    if isinstance(mob,str) and row[:4]:
        egy_regex = r'[0-2]'
        if re.fullmatch(phone_regex,mob) and mob[:2] == '01'and re.fullmatch(egy_regex,mob[2]) and len(mob) == 11:
            row.insert(5,mob)
            return tuple(row)
    return 0


             


