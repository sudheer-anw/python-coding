from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for cafes
cafes = []

@app.route('/')
def index():
    return render_template('index.html', cafes=cafes)

@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    if request.method == 'POST':
        name = request.form.get('name')
        has_wifi = 'wifi' in request.form
        has_power = 'power' in request.form
        if name:
            cafes.append({'name': name, 'wifi': has_wifi, 'power': has_power})
        return redirect(url_for('index'))
    return render_template('add_cafe.html')

if __name__ == '__main__':
    app.run(debug=True)
