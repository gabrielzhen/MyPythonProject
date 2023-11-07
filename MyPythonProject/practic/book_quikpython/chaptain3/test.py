def collatz(number):
    if number%2==0:
        return number/2
    else:
        return 3*number+1
try:
    b=int(input("please input number"))
    while b!=1:
     b=collatz(b)
     print(b)
except ValueError:
    print('please enter number')


