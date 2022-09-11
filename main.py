import re #importing regex module
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"#made a variable,^ denotes "start with"+ denotes "addtion of condition "
                                                          # \backslash denotes 'search of a character' ? denotes " should be only 0 or 1"
user_email=str(input("enter your email: "))               #taking input from user
if re.search(email_condition,user_email):                 #introduced both variable to compare both along with if else condition 
    print("right email")
else:
    print('wrong email')

