def fact(x):
  if x==1:
    return 1
  else:
    print (x)
    sum=x*fact(x-1)
    return(sum)
num=int(input("enter the number:"))
if num>=-1:
  print("factorial value:",fact(num))
