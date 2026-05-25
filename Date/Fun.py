import time
def function1():
    print("Function1 is called")
    with open("time.txt", "a") as file:
        file.write(f"function1 called at: {time.strftime('%H:%M:%S')}\n")
def function2():
    print("Function2 is called")
    with open("time.txt", "a") as file:
        file.write(f"function2 called at: {time.strftime('%H:%M:%S')}\n")
def function3():
    print("Function 3 is called")
    with open("time.txt", "a") as file:
        file.write(f"function3 called at: {time.strftime('%H:%M:%S')}\n")  
def function4():
    print("Function 4 is called")
    with open("time.txt", "a") as file:
        file.write(f"function4 called at: {time.strftime('%H:%M:%S')}\n")  
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