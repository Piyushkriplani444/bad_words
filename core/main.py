import argparse
from check_bad_word import check_bad_word


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--text",
		help = "Enter the text to check and remove bad words",
		type = str,
		required = True)
	parser.add_argument("--path",
		help = "Enter the path of bad word dataset",
		type = str,
		required = True)

	args = parser.parse_args()
	text = args.text
	path = args.path

	result, bad_bool = check_bad_word(text, path)

	if bad_bool==True:
		print("!!Warning bad word(s) are present!!")
	
	print(result)
