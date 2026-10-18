class DataTypeError(Exception):
    def __init__(self, *args):
        super().__init__(*args)

no = "HEy" 
try:
    if type(no) == int:
        raise DataTypeError("Invalid datatype")    
except DataTypeError as e:
    print(e)