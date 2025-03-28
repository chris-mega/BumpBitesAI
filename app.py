from dotenv import load_dotenv, find_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
load_dotenv(find_dotenv())

from ai_recipes import get_ai_recipe
from database import insert_user, get_user
import json

app = Flask(__name__)
CORS(app)

pregnancy_data = {}
with open('data/pregnancy.json') as f:
    pregnancy_data = json.load(f)

@app.route('/get_recipe', methods=['POST'])
def get_recipe_endpoint():
    data = request.json
    preferences = data['preferences']
    aversions = data['aversions']
    vitamins_needed = data['vitamins_needed']

    if not preferences or not aversions or not vitamins_needed:
        return jsonify({'error': 'Missing required parameters'}), 400

    recipe = get_ai_recipe(preferences, aversions, vitamins_needed)
    return recipe

@app.route('/get_lucky_recipe', methods=['POST'])
def get_lucky_recipe():
    data = request.json
    user_id = data['user_id']

    if not user_id:
        return jsonify({'error': 'Missing required parameters'}), 400

    user = get_user(user_id)
    recipe = get_ai_recipe(user["preferences"], user["aversions"], pregnancy_data["vitamins"], user["weeks_pregnant"])
    return recipe, 200

@app.route('/create_user', methods=['POST'])
def create_user_endpoint():
    user_data = request.json

    name = user_data['name']
    preferences = user_data['preferences']
    aversions = user_data['aversions']
    weeks_pregnant = user_data['weeks_pregnant']

    if not preferences or not aversions or not name:
        return jsonify({'error': 'Missing required parameters'}), 400

    try:
        user_data = insert_user(preferences, aversions, name, weeks_pregnant)
        return user_data, 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
