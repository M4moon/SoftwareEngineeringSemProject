# app.py
from flask import Flask, render_template

app = Flask(__name__)

recipes = [
    {'title': 'Sweet Strawberry Cheesecake', 'content': '...'},
    {'title': 'Chocolate Brownie', 'content': '...'},
    # Add more recipes as needed
]


# Route for the homepage
@app.route('/')
def index_page():
    return render_template('index.html')

# Route for the recipe page
@app.route('/recipe')
def recipe_page():
    # Correct template name: 'recipe.html'
    return render_template('recipe.html')
@app.route('/search')
def search():
    query = request.args.get('query')
    # Simple search logic: Check if the query is in the title of any recipe
    results = [recipe for recipe in recipes if query.lower() in recipe['title'].lower()]
    return render_template('search_results.html', query=query, results=results)


if __name__ == '__main__':
    app.run(debug=True)
