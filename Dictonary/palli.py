# users =["amit","sumit","raj","parth","jay","sneha","kunal"]

# userPalli={i:i if i == i[::-1]  else "not pallindrom" for i in users}
# print(userPalli)

# number=[1,2,25,26,100,90]
# oddeven={i:"even" if i%2==0 else "odd" for i in number}
# print(oddeven)

marks = {"Samir": 85, "Rahul": 40, "Aman": 72}
marks = {i: "pass" if j > 60 else "fail" for i, j in marks.items()}
print(marks)

data = {'a':1,'b':2,'c':3}
print(data)
data = {j:i for i,j in data.items()}
print(data)

posNeg = {'a':10 , 'b':-5,'c':20,'d':-2}
print(posNeg)
data ={i:j*-1 if j<0 else j for i,j in posNeg.items()}
print(data)

cityList = {'name':'shashwat','city':'ahemdabad'}
cityList = {i.upper():j for i,j in cityList.items()}
print(cityList)