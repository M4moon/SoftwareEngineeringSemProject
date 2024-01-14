# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

recipes = [
    'Avocado_toast.html',
    'beef_nihari.html',
    'burrito.html',
    'butter_chi_tacos.html',
    'cajun_pasta.html',
    'caprese_sandwich.html',
    'chi_curry.html',
    'chi_tikka_pizza.html',
    'chick_biryani.html',
    'chicken_salad.html',
    'classic_pancakes.html',
    'egg_cheese_sando.html',
    'greek_yogurt.html',
    'jollof.html',
    'lamb_gyro.html',
    'strawberry_cheesecake.html',
    'turkey_skewers.html'
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

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['query']
        matching_recipes = [recipe for recipe in recipes if search_term.lower() in recipe.lower()]
        return render_template('search_results.html', search_term=search_term, matching_recipes=matching_recipes)

    return render_template('search_results.html', search_term=None, matching_recipes=None)
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
@app.route('/egg_cheese_sando')  # Adjust the route based on the recipe number
def egg_cheese_sando():
    return render_template('egg_cheese_sando.html')
@app.route('/straw_cheesecake')  # Adjust the route based on the recipe number
def straw_cheesecake():
    return render_template('strawberry_cheesecake.html')
@app.route('/Chicken_Salad')  # Adjust the route based on the recipe number
def Chicken_Salad():
    return render_template('chicken_salad.html')
@app.route('/Caprese_Sando')  # Adjust the route based on the recipe number
def Caprese_Sando():
    return render_template('caprese_sandwich.html')
@app.route('/Turkey_Skewers')  # Adjust the route based on the recipe number
def Turkey_Skewers():
    return render_template('turkey_skewers.html')

@app.route('/Chi_biryani')  # Adjust the route based on the recipe number
def Chicken_Biryani():
    return render_template('chick_biryani.html')
@app.route('/Chi_Curry')  # Adjust the route based on the recipe number
def Chicken_Curry():
    return render_template('chi_curry.html')
@app.route('/Chi_Tikka_Pizza')  # Adjust the route based on the recipe number
def Chicken_Tikka_Pizza():
    return render_template('chi_tikka_pizza.html')
@app.route('/Butter_Chi_Tacos')  # Adjust the route based on the recipe number
def Butter_Chi_Tacos():
    return render_template('butter_chi_tacos.html')
@app.route('/Cajun_Pasta')  # Adjust the route based on the recipe number
def Cajun_Pasta():
    return render_template('cajun_pasta.html')
@app.route('/Lamb_Gyro')  # Adjust the route based on the recipe number
def Lamb_Gyro():
    return render_template('lamb_gyro.html')
@app.route('/Jollof')  # Adjust the route based on the recipe number
def Jollof():
    return render_template('jollof.html')
@app.route('/Nihari')  # Adjust the route based on the recipe number
def Beef_Nihari():
    return render_template('beef_nihari.html')

@app.route('/About')  # Adjust the route based on the recipe number
def About():
    return render_template('aboutus.html')




if __name__ == '__main__':
    app.run(debug=True)
