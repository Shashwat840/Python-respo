# numbs = [10,20,30,40,-10,0,-2,0]
# print(numbs)
# numdif = ["postive" if i>0 else("Zero" if i ==0 else "Neagative") for i in numbs]
# print(numdif)

# charaters = ["Ram" , "Shayam" , "Mohan" , "Rahul" , "mam" , "mama"]
# charChosse = [i for i in charaters if i == i[::-1]]
# print(charChosse)

# sales= [100,20,45,67,89,120,89,78]
# sales50 =[i for i in sales if i>50]
# print(sales50)
# evenoddsalses = ["even" if i %2 ==0 else "odd" for i in sales]
# #evenoddsalses = ["even" if i %2 ==0 else "odd" for i in sales if i>50]
# print(evenoddsalses)

units=[190,100,200,300,334,70,50,400,450,10,110]

#give 20 % discount if unit us above 200 else 10% disaocunt give  after discount list
#["171","90",160]....
unitssperate=[(i - (i*0.1)) if i>200 else (i - (i*0.2)) for i in units]
print(unitssperate)
