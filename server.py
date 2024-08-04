from flask import Flask, render_template, request, redirect, json
import csv

app = Flask(__name__)


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open('database.txt', 'a') as f:
        email = data.get("email")
        subject = data.get("subject")
        message = data.get("message")
        f.write(f"{email},{subject},{message}\n")


def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as f:
        email = data.get("email")
        subject = data.get("subject")
        message = data.get("message")
        csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # write_to_file(data)
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Did not save to database"

    else:
        return "Something went wrong, please try again"
