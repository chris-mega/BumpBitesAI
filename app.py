from flask import Flask, request, jsonify
from ai_recipes import get_ai_recipe

app = Flask(__name__)

@app.route('/get_recipe', methods=['POST'])
def get_recipe_endpoint():
    preferences = request.json['preferences']
    aversions = request.json['aversions']
    vitamins_needed = request.json['vitamins_needed']

    if not preferences or not aversions or not vitamins_needed:
        return jsonify({'error': 'Missing required parameters'}), 400

    recipe = get_ai_recipe(preferences, aversions, vitamins_needed)
    return recipe


if __name__ == '__main__':
    app.run(debug=True)