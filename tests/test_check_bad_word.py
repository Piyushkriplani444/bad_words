from core.check_bad_word import check_bad_word

def test_bad_words():
	input_text1 = "You are an ass"
	input_text2 = "You are so cool"
	path = './core/data/badwords.txt'

	output_text1, output_bool1 = check_bad_word(input_text1, path)
	output_text2, output_bool2 = check_bad_word(input_text2, path)

	expected_text1 = "You are an $$$"
	expected_bool1 = True
	expected_text2 = "You are so cool"
	expected_bool2 = False

	assert output_text1 == expected_text1
	assert output_bool1 == expected_bool1
	assert output_text2 == expected_text2
	assert output_bool2 == expected_bool2