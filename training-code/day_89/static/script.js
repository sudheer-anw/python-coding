let typingTimer; // Timer identifier
const typingInterval = 5000; // 5 seconds

const editor = document.getElementById('editor');

// Function to clear the text area
function clearTextArea() {
    editor.value = '';
}

// Function to reset the timer
function resetTimer() {
    clearTimeout(typingTimer);
    typingTimer = setTimeout(clearTextArea, typingInterval);
}

// Add event listeners to reset the timer on user input
editor.addEventListener('input', resetTimer);

// Start the timer when the page loads
resetTimer();
