from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="users"
)

# Helper function to execute queries
def execute_query(query, params=None):
    cursor = db.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    db.commit()
    return cursor

# Route for '/hello'
@app.route('/hello')
def hello():
    return "Hello, World!"

# Route for '/users'
@app.route('/users')
def users():
    query = "SELECT * FROM users"
    cursor = execute_query(query)
    users_data = cursor.fetchall()
    return render_template('users.html', users=users_data)

# Route for '/new_user'
@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s)"
        params = (name, email, age)
        execute_query(query, params)
        return "User added successfully!"

    return render_template('new_user.html')

# Route for '/users/<id>'
@app.route('/users/<int:user_id>')
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = %s"
    params = (user_id,)
    cursor = execute_query(query, params)
    user_data = cursor.fetchone()
    if not user_data:
        return jsonify({"error": "User not found"}), 404
    return render_template('user_details.html', user=user_data)

# Error handling for 404 - Not Found
@app.errorhandler(404)
def page_not_found(error):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
