from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/entrypage')
def entry_page() -> "html":
    return render_template('html_example.html', the_title = "~example~", picture_description = "HELLOOOOOOOOO")

app.run(debug = True) 