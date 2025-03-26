from models import openai_response

def get_ai_recipe(preferences, aversions, vitamins_needed):
    prompt = f"""
    Suggest a recipe based on these criteria. Take in mind that the user is 12 weeks pregnant.:
    - Preferences: {preferences}
    - Avoid: {', '.join(aversions)}
    - Include foods high in: {', '.join(vitamins_needed)}

    Provide only the following 3 things: ingredients, instructions, and a nutritional breakdown. Provide a json response
    """
    response = openai_response(prompt)

    
    return response.strip("```json\n")

# Example usage
if __name__ == '__main__':
    recipe = get_ai_recipe("high-protein", ["mushrooms", "olives"], ["Vitamin D", "Iron", "Vitamin B12"])
    print(recipe)
