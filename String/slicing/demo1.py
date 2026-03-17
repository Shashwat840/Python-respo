#range(sp,ep,step)
#string support neg indexing..

data="java"
print(data)
print(data[0]," - ",data[-4])
print(data[1]," - ",data[-3])
print(data[2]," - ",data[-2])
print(data[3]," -- ",data[-1])

#simple slicing...
text = "PythonProgramming"
print(text[0:6]) #0,1,2,3,4,5

#skip start
#if we skip start it will automatically start from 0 index
print(text[:6]) #0,1,2,3,4,5

#skip end
#if we skip end then it will take last index automatically 
print(text[1:]) #1,2,3,4,.....len

#fullstring...
#if no value is there before of after colon whole string is printed 
print(text[:])
x = text[:]
print(x)


#neg index
#it will start seaching from last index 
print(text[:-6]) #0_____________________ -6-5-4-3-2-1
print(text[-13:-6]) #-13,-12,-11,10,-9,-8,-7,-6


#step parametre
# it defines the incerement or decrement of string
text = "abcdef"
print(text[::2]) #0 1 2 3 4 5......... increment 2
#ace
print(text[::3]) #Increment of 3  
# It is very useful as it reverses the string
print(text[::-1])