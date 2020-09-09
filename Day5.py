# -*- coding: utf-8 -*-

"""

Assignment 1

"""
lst = [1,2,3,4,5,6]
   
inp = [2,3,4,6]
def Check( lst , inp):
    flag = "It's a Match"
    if(inp[0] in lst):
            j = lst.index(inp[0])
            j = j+1
            for i in range(1 , len(inp)):
                
                if(lst[j] == inp[i]):
                    i = i + 1
                    j = j + 1
                else:
                    flag = "It's Gone"
                    break             
                
    print (flag)

Check(lst , inp)    

"""
Assignment 2

"""

def checkPrime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if(num%i == 0):
            return False
        else:
            i = i+1
    
    return True       

lst = list(filter(checkPrime,list(range(1,2500))))
print(lst[:20])

"""

Assignment 3

"""

lst = list(map( lambda x:x.title() , ["hey this is sai" , "i am in mumbai"]))
print(lst)


