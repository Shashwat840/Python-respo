dictonary = {"Name":"Shahwat","Age":22,"City":"Ahemdabad"}
file = open("Files/file1.txt","w")
for i in dictonary.items():
    print(f"{i[0]} : {i[1]}",file = file)
file.close()