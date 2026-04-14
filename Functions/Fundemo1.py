def getFullName(**kwargs):
    
    def find():
        # name = kwargs.get("name").lower()
        # lname = kwargs.get("lname").lower()
        # return f"{name}-{lname}"
        return "-".join(list(kwargs.values()))
    return find()

print(getFullName(name="MahendraSingh",lname="Dhoni",nickname = "Theli"))
#output mahedrasing-dhoni