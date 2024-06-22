from flask import Flask,request, render_template


STATIC_FOLDER = 'templates/assets'
app = Flask(__name__,static_folder=STATIC_FOLDER)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
