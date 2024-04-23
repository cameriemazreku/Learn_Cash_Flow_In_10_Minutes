from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dictionary to store quiz answers
quiz_answers = {}

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/learn')
def learn():
    return render_template('learning.html')

# @app.route('/learn/<int:lesson_number>')
# def learn(lesson_number):
#     # Here you can implement the logic to fetch the learning material for the specified lesson_number
#     # For now, just rendering the learning page
#     return render_template('learning.html')

@app.route('/quiz/<int:question_number>', methods=['GET', 'POST'])
def quiz(question_number):
    if request.method == 'POST':
        # Collecting quiz answers from the form
        for key, value in request.form.items():
            quiz_answers[key] = value

        if question_number == 10:
            return redirect(url_for('quiz_result'))
        else:
            next_question_number = question_number + 1
            return redirect(url_for('quiz', question_number=next_question_number))
    else:
        # Here you can implement the logic to fetch the quiz questions for the specified question_number
        # For now, just rendering the quiz page
        return render_template('quiz.html', question_number=question_number)

@app.route('/result')
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
    for question, user_answer in quiz_answers.items():
        if user_answer == correct_answers[question]:
            score += 1
            results[question] = {'user_answer': user_answer, 'correct': True}
        else:
            results[question] = {'user_answer': user_answer, 'correct_answer': correct_answers[question]}

    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
