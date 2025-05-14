from flask import Flask, render_template, request, jsonify
import sqlite3
import random
import time

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('bible_game.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Single-player mode
@app.route('/single-player', methods=['GET', 'POST'])
def single_player():
    if request.method == 'GET':
        conn = get_db_connection()
        question = conn.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT 1').fetchone()
        conn.close()
        start_time = time.time()
        return render_template('single_player.html', question=question, start_time=start_time)
    elif request.method == 'POST':
        answer = request.form['answer']
        question_id = request.form['question_id']
        start_time = float(request.form['start_time'])
        end_time = time.time()
        time_taken = end_time - start_time

        conn = get_db_connection()
        question = conn.execute('SELECT * FROM questions WHERE id = ?', (question_id,)).fetchone()
        conn.close()
        correct = (answer == question['correct_answer'])
        return jsonify({
            'correct': correct,
            'reference': question['reference'],
            'time_taken': time_taken
        })

# Multiplayer mode
@app.route('/multiplayer', methods=['GET', 'POST'])
def multiplayer():
    if request.method == 'GET':
        return render_template('multiplayer.html')
    elif request.method == 'POST':
        # Placeholder for multiplayer logic
        return jsonify({"message": "Multiplayer mode logic to be implemented."})

if __name__ == '__main__':
    app.run(debug=True)