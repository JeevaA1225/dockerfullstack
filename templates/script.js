document.addEventListener('DOMContentLoaded', function() {
    const button = document.getElementById('clickButton');
    const displayText = document.getElementById('displayText');

    button.addEventListener('click', function() {
        displayText.textContent = 'Button clicked!';
    });
});
