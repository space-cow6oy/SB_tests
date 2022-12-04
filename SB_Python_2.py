from math import sqrt


def prime(num):

    if(num > 1):
        for i in range(2 , int(sqrt(num))+1):
            if(num % i == 0): 
                return False

        for i in range(2 , int(sqrt(num+2)) + 1 ):
            if(((num-2) % i == 0 ) and ((num+2) % i == 0)):
                return False
            else:
                return True
    
    else:
        return False

