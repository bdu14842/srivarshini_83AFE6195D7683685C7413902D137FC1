a=int(input("enter a number"))
if(a%400==0)and(a%200==0):
  print("it is a century year and also a leap year")
elif(a%4==0)and(a%100!=0):
  print("it is not a century year and also a leap year")
else:
  print("it is not a leap year")