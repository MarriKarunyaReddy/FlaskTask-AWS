from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# Connect to MySQL RDS
db = pymysql.connect(
    host="<RDS-ENDPOINT>",
    user="admin",
    password="adminpassword",
    database="todo_db"
)
cursor = db.cursor()

# Home Route (Show Tasks)
@app.route('/')
def home():
    cursor.execute("SELECT id, task, status, created_at, completed_at FROM todos")
    tasks = cursor.fetchall()
    return render_template("index.html", tasks=tasks)

# Add Task Route
@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    cursor.execute("INSERT INTO todos (task) VALUES (%s)", (task,))
    db.commit()
    return redirect('/')

# Complete Task Route
@app.route('/complete/<int:id>')
def complete_task(id):
    cursor.execute("UPDATE todos SET status='completed', completed_at=NOW() WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

# Edit Task Route
@app.route('/edit/<int:id>', methods=['POST'])
def edit_task(id):
    new_task = request.form['task']
    cursor.execute("UPDATE todos SET task=%s WHERE id=%s", (new_task, id))
    db.commit()
    return redirect('/')

# Delete Task Route
@app.route('/delete/<int:id>')
def delete_task(id):
    cursor.execute("DELETE FROM todos WHERE id=%s", (id,))
    db.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

