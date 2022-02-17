from flask import Flask, app


app=Flask(__name__)

@app.route("/")

def test():
    return "Hi"

if __name__ == "__main__":
    app.run(debug=True)