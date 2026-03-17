users =["amit","sumit","raj","parth","jay","sneha","kunal"]
userWithLen = {}
for i in users:
    userWithLen[i] = len(i)

print(userWithLen)

userWithIni = {i:i[0] for i in users}
print(userWithIni)