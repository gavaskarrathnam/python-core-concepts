from flask import Flask, render_template
app = Flask(__name__)

#
@app.route("/v1/gsthm")
def guestHome():
    links = ["https://www.youtube.com", "https://www.python.org"]
    return render_template('homepage.html', links=links) #pages under templates dir.

if __name__ == '__main__':
    app.run(debug=True)
