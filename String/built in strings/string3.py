#boolean--> It will give answer in true or false
data = ""
#startswith--> It will check the frist letter of string and matches with given one
flag = data.startswith("j")
print(flag)
#startswith--> It will check the Last letter of string and matches with given one
print('endswith',data.endswith("a"))
# isalnum--> It will give true if string has both alphabet or numbers or any 
# one of them
print("isalnum",data.isalnum())
#isalpha--> If string has only alphabets then it will give true 
print("alpha...",data.isalpha())
#isnumberic/isdigit--> It will only give true if string has numeric values 
print("numric..",data.isnumeric())
#print(data.isdigit())
# islower--> if string consits of everything except capital letter then it will hit true
print("lower",data.islower()) #"abcd" #"abcd1" # "abc " # "Abc"
# islower--> if string consits of everything except small letter then it will hit true
print("upper",data.isupper())
#isspace--> If it has string consits of only space 
print("isspace",data.isspace()) #" "
#istitle-->It will check if frist letter of every word is capiatal
print("is title",data.istitle()) #
#isprintable--> It will give true for all values which is 
print(data.isprintable()) # \n 