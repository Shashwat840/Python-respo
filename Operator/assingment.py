# the value in right side is stored in left side varible
a=100
b=200
'''
temp= a
a=b
b=temp
print(f"value of a :-{a} and value of b:- {b}")
'''
(a,b)=(b,a)
print(f"value of a :-{a} and value of b:- {b}")