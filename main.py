from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the home page"

@app.route('/about',methods=['GET','POST'])
def about():
    if request.method == 'POST':
        return "You are in the about section and you are using POST method"
    else:
        return "This time you are in the about section and you are using GET method"


@app.route('/profile/<username>')
def profile(username):
    return "Hey how are you <b><i>%s</i></b> " % username

@app.route('/template_engine/')
def template_engine():
    return render_template("template_engine.html")

@app.route('/test/')
def test():
    return  render_template("test.html")


if __name__ == "__main__":
    app.run(debug=True)



