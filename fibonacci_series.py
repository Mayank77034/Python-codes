def recur_fibo(n):
    if n>=1:
        return n
    else :
        return recur_fibo(n-1)+recur_fibo(n-2)
    if n<= 0:
        print("enter a positive number")
    else:
        print("fibonacci series")
    for i in range (n):
        print(recur_fibo(i))       
    
