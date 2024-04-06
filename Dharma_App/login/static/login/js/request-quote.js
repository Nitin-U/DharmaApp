// Function to initialize date picker and set min date to today
function initializeDatepicker() {
    var today = new Date().toISOString().split('T')[0]; // Get today's date in YYYY-MM-DD format
    document.getElementById('start_date').setAttribute('min', today);
    document.getElementById('end_date').setAttribute('min', today);
}

// Call the initializeDatepicker function when the page is loaded
window.onload = function() {
    initializeDatepicker();
};

function getDays() {
    var start_date = new Date(document.getElementById('start_date').value);
    var end_date = new Date(document.getElementById('end_date').value);
    var time_diff = end_date.getTime() - start_date.getTime();
    var days_diff = time_diff / (1000*3600*24);
    document.getElementById('days').value = days_diff;
    toggleDaysLabel(); // Call the function to toggle the label visibility
}

function toggleDaysLabel() {
    var daysInput = document.getElementById('days');
    var daysLabel = document.getElementById('days_label');
    
    if (daysInput.value !== '') {
        daysLabel.style.display = 'none'; // Hide the label if input has value
    } else {
        daysLabel.style.display = 'block'; // Show the label if input is empty
    }
}