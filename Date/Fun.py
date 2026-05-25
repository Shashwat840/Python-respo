import time
def function1():
    print("Function 1 is called")
    with open("time.txt", "a") as file:
        file.write(f"Function 1 called at: {time.strftime('%H:%M:%S')}\n")
def function2():
    print("Function 2 is called")
    with open("time.txt", "a") as file:
        file.write(f"Function 2 called at: {time.strftime('%H:%M:%S')}\n")
def function3():
    print("Function 3 is called")
    with open("time.txt", "a") as file:
        file.write(f"Function 3 called at: {time.strftime('%H:%M:%S')}\n")  
def function4():
    print("Function 4 is called")
    with open("time.txt", "a") as file:
        file.write(f"Function 4 called at: {time.strftime('%H:%M:%S')}\n")  
while True:
    function1()
    time.sleep(1)
    function2()
    time.sleep(1)
    function3()
    time.sleep(1)
    function4()
    time.sleep(1)
    break