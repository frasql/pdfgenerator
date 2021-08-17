from flask import Flask, render_template, flash, redirect, url_for
import pdfkit
import os
from pathlib import Path


BASEDIR = Path(__file__).resolve().parent

app = Flask(__name__)
app.config["SECRET_KEY"] = "frefergergerbe"

@app.route("/")
def homepage():
    return render_template("homepage.html")



# route that generates a pdf file and save it in a specific position
@app.route('/generate_pdf/')
def generate_pdf():
    # fetch your data from db
    data = ["some data", "other data", "another data", "something else"]
    template = render_template('pdf_report.html', data=data)
    # save your html file in a specific location and serve it in another function or directly with a background function
    pdfkit.from_string(template, os.path.join(BASEDIR, f'static/pdf/pdf_generated.pdf'))
    flash("Pdf Generated!!!!!!")
    return redirect(url_for('homepage'))
    
    
    
if __name__ == "__main__":
    app.run(port=5000, debug=True)
