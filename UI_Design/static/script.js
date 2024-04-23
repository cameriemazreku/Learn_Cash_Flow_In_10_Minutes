document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('quizForm').addEventListener('submit', function(event) {
        // Get all question elements
        var questions = document.querySelectorAll('.question');
        var unanswered = false;
        // Check each question group for checked radio buttons
        questions.forEach(function(question) {
            var radioButtons = question.querySelectorAll('input[type="radio"]');
            var checked = false;
            radioButtons.forEach(function(button) {
                if (button.checked) {
                    checked = true;
                }
            });
            // If no radio button is checked in any question group, set unanswered to true
            if (!checked) {
                unanswered = true;
            }
        });
        // If any question is left unanswered, prevent form submission
        if (unanswered) {
            event.preventDefault();
            alert('Please answer all questions before submitting.');
        }
    });
});
