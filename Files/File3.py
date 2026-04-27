file = open("demo3.txt","a")
while True:
    data = input("Enter name:- ")
    # print(data)
    if data == "exit":
        break

    file.write(f"\n{data}")

file.close()