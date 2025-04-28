from flask import Flask, render_template, request, jsonify
import json
from helpers import Lexer

app = Flask(__name__)

# Load lexer specs from JSON file
with open('lexers.json', 'r') as f:
    lexer_data = json.load(f)

# Create lexer instances
lexers = {}
for name, data in lexer_data.items():
    spec_dict = data['spec']
    # Convert dict to list of (token, regex) pairs
    spec_list = list(spec_dict.items())
    lexers[name] = Lexer(spec_list)

@app.route("/", methods=['GET'])
def index():
    lexer_names = list(lexers.keys())
    return render_template("index.html", lexer_names=lexer_names)

@app.route("/lex", methods=['POST'])
def lex():
    data = request.get_json()
    code = data.get('code')
    lexer_choice = data.get('lexer')
    lexer = lexers.get(lexer_choice)

    if not lexer:
        return jsonify({'error': 'Invalid lexer selected'}), 400

    tokens = lexer.tokenize(code)
    # Convert tokens to a format that can be JSON serialized
    token_data = [{
        'type': token[0],
        'value': token[1],
        'line': token[2],
        'column': token[3]
    } for token in tokens]
    return jsonify({'lexemes': token_data})