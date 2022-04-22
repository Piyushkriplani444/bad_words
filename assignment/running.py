from check_bad_word import check_bad_word


text = "You are man"
bad_bool=False

result, bad_bool = check_bad_word(text,'data/badwords.txt')

if(bad_bool == True ):
	print("Bad Word are present")
else:
	print("No Bad Word are present ")

print(result)