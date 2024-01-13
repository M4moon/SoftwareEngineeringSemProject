# app.py
from flask import Flask, render_template, request, redirect, url_for

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

# Route for the search functionality
@app.route('/search')
def search():
    query = request.args.get('query')
    # Simple search logic: Check if the query is in the title of any recipe
    results = [recipe for recipe in recipes if query.lower() in recipe['title'].lower()]
    return render_template('search_results.html', query=query, results=results)

# Route for sign-in
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Retrieve the username and password from the form
        username = request.form.get('username')
        password = request.form.get('password')

        # Implement your sign-in logic here (e.g., check credentials)
        # For demonstration purposes, we'll just redirect to the homepage
        return redirect(url_for('index'))

    return render_template('signin.html')


if __name__ == '__main__':
    app.run(debug=True)
