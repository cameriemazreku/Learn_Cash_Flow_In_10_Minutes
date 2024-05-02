function selectOption(option) {
    var optionBoxes = document.querySelectorAll('.option-box');
        
    // Remove selected class from all option boxes
    optionBoxes.forEach(function(box) {
        box.classList.remove('selected');
    });
        
    // Add selected class to the parent label of the clicked radio button
    option.parentNode.classList.add('selected');
}

function validateForm() {
    var selectedOption = document.querySelector('input[name="selected_option"]:checked');
    if (!selectedOption) {
        document.getElementById('error-message').style.display = 'block';
        return false; // Prevent form submission
    }
    return true; // Allow form submission
}

