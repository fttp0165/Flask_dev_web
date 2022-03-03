from flask import Flask, render_template, url_for, redirect


app=Flask(__name__)



# @app.route("/<name>")
# def test(name=None):
#     if name==None:
#         return "Hi !!"
#     return "Hello " + name+' !!'


@app.route('/')
def index():
	return render_template('index.html')


@app.route('/second')
def test_s():
	return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(debug=True)
