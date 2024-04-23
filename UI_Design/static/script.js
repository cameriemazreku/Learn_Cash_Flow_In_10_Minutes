document.getElementById('submitQuiz').addEventListener('click', function() {
    var score = 0;
    var totalQuestions = 10; // Assuming 10 questions
    var correctAnswers = ['B', 'A', 'C', 'B', 'D', 'A', 'C', 'B', 'D', 'A']; // Example correct answers
    var userAnswers = [];
    
    // Loop through each question and check answers
    for (var i = 1; i <= totalQuestions; i++) {
        var radios = document.getElementsByName('question' + i);
        for (var j = 0; j < radios.length; j++) {
            var radio = radios[j];
            if (radio.checked) {
                userAnswers.push(radio.value);
                // Check if the answer is correct
                if (radio.value === correctAnswers[i - 1]) {
                    score++;
                }
                break; // Only one option can be checked per question, so break the loop once we've found it
            }
            if (j === radios.length - 1) { // If we reach the end and none are selected
                userAnswers.push('N/A'); // No answer provided
            }
        }
    }
    
    // Display score
    var resultText = "Your score is: " + score + "/" + totalQuestions + "\n";
    resultText += "Your answers: " + userAnswers.join(', ') + "\n";
    resultText += "Correct answers: " + correctAnswers.join(', ') + "\n";
    
    // Highlight correct and incorrect answers
    for (var k = 0; k < totalQuestions; k++) {
        var questionStatus = userAnswers[k] === correctAnswers[k] ? "Correct" : "Incorrect";
        resultText += "Question " + (k + 1) + ": " + questionStatus + "\n";
    }
    
    alert(resultText);
});
