from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask import render_template

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'db4free.net'
app.config['MYSQL_USER'] = 'adhishreep_472'
app.config['MYSQL_PASSWORD'] = 'adhishree@472'
app.config['MYSQL_DB'] = 'test_db11'

mysql = MySQL(app)



@app.route('/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return jsonify(users)

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/users', methods=['POST'])
def create_user():
    try:
        id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users (id, name, email) VALUES (%s, %s, %s)", (id, name, email))
        mysql.connection.commit()
        cur.close()
        return jsonify({'message': 'User created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    name = request.json['name']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, user_id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'User updated successfully'})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (user_id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run()
