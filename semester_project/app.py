# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

recipes = [
    {'title': 'Sweet Strawberry Cheesecake', 'content': '...'},
    {'title': 'Chocolate Brownie', 'content': '...'},
    # Add more recipes as needed
]

# Route for the homepage
@app.route('/home')
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
# Add this route in your app.py
@app.route('/forgot_password')
def forgot_password():
    return render_template('forgot_password.html')
@app.route('/classic_pancakes')  # Adjust the route based on the recipe number
def classic_pancakes():
    return render_template('classic_pancakes.html')
@app.route('/avo_toast')  # Adjust the route based on the recipe number
def avo_toast():
    return render_template('Avocado_toast.html')
@app.route('/greek_yoghurt')  # Adjust the route based on the recipe number
def greek_yoghurt():
    return render_template('greek_yogurt.html')
@app.route('/breaky_burrito')  # Adjust the route based on the recipe number
def break_burrito():
    return render_template('burrito.html')
@app.route('/straw_cheesecake')  # Adjust the route based on the recipe number
def straw_cheesecake():
    return render_template('strawberry_cheesecake.html')


if __name__ == '__main__':
    app.run(debug=True)
