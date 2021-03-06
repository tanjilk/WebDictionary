# Importing json to get the data
# Importing flask to make webpage
# Importing the difflib module to compare the words
import json
from flask import Flask
from flask import render_template
from flask import request
from difflib import get_close_matches
from flask import Markup

# Loads the json file
data = json.load(open('data.json'))

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

def definition_word(word):
	if word in data:
		return data[word]

@app.route('/dictionary/', methods=['POST'])
def dictionary():
	# Input value of the given input word
	word = request.form['word']
	#print(word)
	messages = definition_word(word)
	#print(messages)
	if type(messages) == list:
		return render_template('home.html', word=word, messages=messages)
		if word.title() in data:
			word = word.title()
			messages = definition_word(word)
			for message in messages:
				return render_template('home.html', word=word, message=message)
		elif word.upper() in data:
			word = word.upper()
			messages = definition_word(word)
			for message in messages:
				return render_template('home.html', word=word, message=message)
		else:
			message = Markup("The word doesn't exists. Please double check it.")
			return render_template('home.html', word=word, message=message)
		
	else:
		if type(messages) == type(None):
			if len(get_close_matches(word, data.keys())) > 0:
				word1 = get_close_matches(word, data.keys())[0]
				message = f'Do you mean <b>{word1}</b> instead of <i>"{word}"</i>?'
				return render_template('home.html', word1=word1, message=message)
			else:
				message = "The word doesn't exists. Please double check it."
				return render_template('home.html', word=word, message=message)
		else:
			message = "The word doesn't exists. Please double check it."
			return render_template('home.html', word=word, message=message)
	message = "Thanks for using this application!"
	return render_template('home.html', word = word, message = message)

if __name__ == '__main__':
	app.run(host='localhost', debug=True)