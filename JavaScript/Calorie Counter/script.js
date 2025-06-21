// Get references to important DOM elements
const calorieCounter = document.getElementById('calorie-counter');
const budgetNumberInput = document.getElementById('budget');
const entryDropdown = document.getElementById('entry-dropdown');
const addEntryButton = document.getElementById('add-entry');
const clearButton = document.getElementById('clear');
const output = document.getElementById('output');

let isError = false; // Tracks if any invalid input is found

// Removes unwanted characters like +, - and spaces from a string
function cleanInputString(str) {
    const regex = /[+\-\s]/g; // matches +, - and whitespace
    return str.replace(regex, "");
}

// Checks if a string contains scientific notation, which is considered invalid
function isInvalidInput(str) {
    const regex = /\d+e\d+/i; // matches formats like 1e5
    return str.match(regex);
}

// Dynamically adds a new input set (name + calories) for the selected meal type
function addEntry() {
    const targetInputContainer = document.querySelector(`#${entryDropdown.value} .input-container`);
    const entryNumber = targetInputContainer.querySelectorAll('input[type="text"]').length + 1;

    // HTML template for a new entry
    const HTMLString = `
    <label for="${entryDropdown.value}-${entryNumber}-name">Entry ${entryNumber} Name</label>
    <input type="text" id="${entryDropdown.value}-${entryNumber}-name" placeholder="Name" />
    <label for="${entryDropdown.value}-${entryNumber}-calories">Entry ${entryNumber} Calories</label>
    <input
        type="number"
        min="0"
        id="${entryDropdown.value}-${entryNumber}-calories"
        placeholder="Calories"
    />`;

    targetInputContainer.insertAdjacentHTML('beforeend', HTMLString);
}

// Handles form submission and performs all calorie calculations
function calculateCalories(e) {
    e.preventDefault(); // Prevent default form submit behavior (page reload)
    isError = false; // Reset error flag

    // Collect input fields from all meal categories and exercise
    const breakfastNumberInputs = document.querySelectorAll("#breakfast input[type='number']");
    const lunchNumberInputs = document.querySelectorAll("#lunch input[type='number']");
    const dinnerNumberInputs = document.querySelectorAll("#dinner input[type='number']");
    const snacksNumberInputs = document.querySelectorAll("#snacks input[type='number']");
    const exerciseNumberInputs = document.querySelectorAll("#exercise input[type='number']");

    // Calculate total calories for each category
    const breakfastCalories = getCaloriesFromInputs(breakfastNumberInputs);
    const lunchCalories = getCaloriesFromInputs(lunchNumberInputs);
    const dinnerCalories = getCaloriesFromInputs(dinnerNumberInputs);
    const snacksCalories = getCaloriesFromInputs(snacksNumberInputs);
    const exerciseCalories = getCaloriesFromInputs(exerciseNumberInputs);
    const budgetCalories = getCaloriesFromInputs([budgetNumberInput]);

    if (isError) {
        return; // Stop calculation if there was any error in input
    }

    // Total calories consumed (excluding exercise)
    const consumedCalories = breakfastCalories + lunchCalories + dinnerCalories + snacksCalories;
    // Remaining calories after subtracting consumed and adding burned (exercise)
    const remainingCalories = budgetCalories - consumedCalories + exerciseCalories;
    const surplusOrDeficit = remainingCalories < 0 ? "Surplus" : "Deficit";

    // Update the output HTML
    output.innerHTML = `
    <span class="${surplusOrDeficit.toLowerCase()}">${Math.abs(remainingCalories)} Calorie ${surplusOrDeficit}</span>
    <hr>
    <p>${budgetCalories} Calories Budgeted</p>
    <p>${consumedCalories} Calories Consumed</p>
    <p>${exerciseCalories} Calories Burned</p>
    `;
    output.classList.remove('hide');
}

// Helper function to sum and validate input calories
function getCaloriesFromInputs(list) {
    let calories = 0;

    for (const item of list) {
        const currVal = cleanInputString(item.value); // Clean up input
        const invalidInputMatch = isInvalidInput(currVal); // Check for scientific notation

        if (invalidInputMatch) {
            alert(`Invalid Input: ${invalidInputMatch[0]}`); // Warn user
            isError = true;
            return null; // Stop further processing
        }
        calories += Number(currVal); // Add valid input to total
    }

    return calories;
}

// Clears all inputs and output display
function clearForm() {
    const inputContainers = Array.from(document.querySelectorAll('.input-container'));
    for (const container of inputContainers) {
        container.innerHTML = ''; // Clear all dynamically added inputs
    }

    budgetNumberInput.value = ''; // Reset calorie budget input
    output.innerText = ''; // Clear result display
    output.classList.add('hide'); // Hide the result section
}

// Attach event listeners to buttons and form
addEntryButton.addEventListener("click", addEntry);
calorieCounter.addEventListener("submit", calculateCalories);
clearButton.addEventListener("click", clearForm);
