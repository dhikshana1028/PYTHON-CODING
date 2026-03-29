from datetime import datetime
a=input("enter the birth date in yyyy-mm-dd :")
b=input("enter the current date in yyyy-mm-dd :")
a1=datetime.strptime(a,"%Y-%m-%d")
b1=datetime.strptime(b,"%Y-%m-%d")
print(b1-a1)