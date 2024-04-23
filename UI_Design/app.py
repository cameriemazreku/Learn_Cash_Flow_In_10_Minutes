from flask import Flask, render_template, request, redirect, url_for, jsonify, Response

app = Flask(__name__, static_url_path='/static')

# Dictionary to store quiz answers
quiz_answers = {}

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn')
def learn():
    # Here you can implement the logic to fetch the learning material for the specified lesson_number
    # For now, just rendering the learning page
    return render_template('learning.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    return render_template('quiz.html')

@app.route('/result', methods=['POST'])
def quiz_result():
    correct_answers = {
        'question1': 'B',
        'question2': 'C',
        'question3': 'A',
        'question4': 'B',
        'question5': 'D',
        'question6': 'A',
        'question7': 'D',
        'question8': 'C',
        'question9': 'B',
        'question10': 'A'
    }
    score = 0
    results = {}
    for question in correct_answers:
        user_answer = request.form.get(question)  # Get user's answer for the current question
        if user_answer == correct_answers[question]:
            score += 1
            results[question] = {'user_answer': user_answer, 'correct': True, 'correct_answer': correct_answers[question]}
        else:
            results[question] = {'user_answer': user_answer, 'correct': False, 'correct_answer': correct_answers[question]}

    return render_template('result.html', results=results, score=score)

if __name__ == '__main__':
    app.run(debug=True)
