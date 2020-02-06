def DecToBin (n):
    if n<0:
        return "must be a positive integer"
    elif n==0:
        return "0"
    else:
        return DecToBin(n//2) + str(n%2)
inputVal = int(input("Enter number here: "))            
print(DecToBin(inputVal))
