from flask import Flask, request, render_template_string
import random

# Generate a random number and store it in a global variable
random_number = random.randint(0, 9)

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Guess the Number</title>
</head>
<body>
    <h1>Guess a number between 0 and 9</h1>
    <form action="/guess" method="post">
        <input type="number" name="guess" min="0" max="9" required>
        <button type="submit">Submit Guess</button>
    </form>
    {% if message %}
        <h2 style="color: {{ color }}">{{ message }}</h2>
        <img src="{{ image_url }}" />
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/guess', methods=['POST'])
def guess_number():
    guess = int(request.form.get('guess'))
    if guess > random_number:
        message = "Too high, try again!"
        color = "purple"
        image_url = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    elif guess < random_number:
        message = "Too low, try again!"
        color = "red"
        image_url = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    else:
        message = "You found me!"
        color = "green"
        image_url = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
    
    return render_template_string(HTML_TEMPLATE, message=message, color=color, image_url=image_url)

if __name__ == "__main__":
    app.run(debug=True)
