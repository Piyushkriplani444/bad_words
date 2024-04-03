from flask import Flask, jsonify, request
from check_bad_word import check_bad_word

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
	if(request.method == 'GET'):
		data = "Bad Word Api is Running Correctly"
		return jsonify({'data':data})


@app.route('/bad_words/',methods=['POST'])
def badwords():
	if(request.method == 'POST'):
		request_data = request.get_json()
		text = request_data['text']
		result, bad_bool = check_bad_word(text, './core/data/badwords.txt')
		bad_word_response = {
		'text': result,
		'bad': bad_bool
		}

		return jsonify(bad_word_response)


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000)