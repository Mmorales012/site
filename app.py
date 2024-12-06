from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    # Altere o host para '0.0.0.0' para permitir acesso local
    app.run(debug=True, host='0.0.0.0')