try:    
    li = [10,20,30,40,50]
    print(li[50])
except IndexError as e:
    print(e)
except:
    print("Error dectected")