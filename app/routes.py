from flask import render_template, request, session, jsonify
import requests
from app import app

# OpenTDB API URL
API_URL = "https://opentdb.com/api.php?amount=10&type=multiple"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_game', methods=['POST'])
def start_game():
    session.clear()
    response = requests.get(API_URL)
    data = response.json()
    questions = data['results']
    session['questions'] = questions
    session['score'] = 0
    session['current_question'] = 0
    return jsonify({'status': 'success'})

@app.route('/submit', methods=['POST'])
def submit():
    selected_option = request.form['option']
    current_question = session['current_question']
    questions = session['questions']
    correct_answer = questions[current_question]['correct_answer']

    if selected_option == correct_answer:
        session['score'] += 1

    session['current_question'] += 1
    if session['current_question'] < len(questions):
        next_question = questions[session['current_question']]
        options = next_question['incorrect_answers'] + [next_question['correct_answer']]
        return jsonify({
            'next_question': {
                'question': next_question['question'],
                'options': options
            },
            'q_num': session['current_question'] + 1
        })
    else:
        score = session['score']
        if score <= 5:
            message = "Failed, score too low"
        elif 5 < score < 10:
            message = "Good, you can do better next time"
        else:
            message = "Congratulations, you rock"
        return jsonify({
            'score': score,
            'message': message
        })
