from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = '4e0cd9227855bf155a7510cb8c81db0e01ba1c1799eb248b'  # Change this to a secure key
app.config['MYSQL_HOST'] = 'db4free.net'
app.config['MYSQL_USER'] = 'adhishreep_472'
app.config['MYSQL_PASSWORD'] = 'adhishree@472'
app.config['MYSQL_DB'] = 'test_db11'

mysql = MySQL(app)

# Form to update the word
class UpdateWordForm(FlaskForm):
    word = StringField('Word')
    submit = SubmitField('Update')

# Home page
@app.route('/')
def home():
    return render_template("home.html")

# API endpoint to get the word from the database
@app.route('/api/word', methods=['GET', 'POST'])
def word():
    if request.method == "GET":
        return render_template('word.html')
    else:
        cur = mysql.connection.cursor()
        cur.execute('SELECT col_1 FROM test_table')
        word = cur.fetchone()[0]
        cur.close()
        return render_template('word.html', word=word)


# Admin portal to update the word in the database
@app.route('/admin', methods=['GET', 'POST'])
def admin_portal():
    form = 0
    message = ""
    if request.method == "GET":
        return render_template('admin.html')
    else:
        form = UpdateWordForm()
        if form.validate_on_submit():
            word = form.word.data
            cur = mysql.connection.cursor()
            cur.execute('UPDATE test_table SET col_1 = %s', (word,))
            mysql.connection.commit()
            cur.close()
            message = 'Word updated successfully!'
        return render_template('admin.html', form=form, message=message)

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
