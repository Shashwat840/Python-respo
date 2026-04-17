def party_items(func):
    def inner():
        print("Items included Pizza burger cheesecake......")
        func()
    return inner 

@party_items
def throw_party():
    print("It's party time")

throw_party()