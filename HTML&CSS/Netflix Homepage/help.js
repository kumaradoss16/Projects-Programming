const accountCheckbox = document.getElementById('account');
    const payingCheckbox = document.getElementById('paying');

    // Function to handle checkbox click event
    function handleCheckboxClick(clickedCheckbox, otherCheckbox) {
        clickedCheckbox.addEventListener('change', () => {
            if (clickedCheckbox.checked) {
                otherCheckbox.checked = false; // Uncheck the other checkbox
            }
        });
    }

    // Initialize event listeners for both checkboxes
    handleCheckboxClick(accountCheckbox, payingCheckbox);
    handleCheckboxClick(payingCheckbox, accountCheckbox);