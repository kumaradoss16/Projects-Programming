const numberInput = document.getElementById("number-input");
const convertBtn = document.getElementById("convert-btn");
const result = document.getElementById("result");
const animationContainer = document.getElementById("animation-container"); // Ensure this HTML element exists

// Global array to store animation steps
const animationSteps = [];
let currentAnimationDelay = 0;
const animationStepDuration = 800; // Duration for each major step (push/pop)

// Original decimalToBinary function (for actual calculation)
const decimalToBinary = (input = 5) => {
    if (input === 0 || input === 1) {
        return String(input);
    } else {
        return decimalToBinary(Math.floor(input / 2)) + (input % 2);
    }
};

// Recursive function that also records animation steps
const decimalToBinaryAnimated = (input) => {
    // Generate a unique ID for each call frame to manage its DOM element
    const frameId = `frame-${input}-${Date.now() + Math.random()}`;

    // Step 1: Record the function call (push to stack visually)
    animationSteps.push({
        type: 'add',
        id: frameId,
        inputVal: input,
        delay: currentAnimationDelay
    });
    currentAnimationDelay += animationStepDuration; // Increment delay for next event

    let resultPart;
    if (input === 0 || input === 1) {
        resultPart = String(input); // Base case returns "0" or "1"
    } else {
        // Recursive call: this will add its own steps and return its part
        const recursiveResult = decimalToBinaryAnimated(Math.floor(input / 2));
        resultPart = recursiveResult + (input % 2);
    }

    // Step 2: Record the function return (update message on stack frame)
    animationSteps.push({
        type: 'update',
        id: frameId,
        msg: `decimalToBinary(${input}) returns '${resultPart}'`,
        delay: currentAnimationDelay
    });
    currentAnimationDelay += animationStepDuration * 0.7; // Shorter delay before removal

    // Step 3: Record removal from stack
    animationSteps.push({
        type: 'remove',
        id: frameId,
        delay: currentAnimationDelay
    });
    currentAnimationDelay += animationStepDuration * 0.3; // Very short delay after removal

    return resultPart; // Return the binary part for concatenation
};

// Function to orchestrate and display the animation
const showAnimation = (inputInt) => {
    result.innerText = "Call Stack Animation";
    animationContainer.innerHTML = ""; // Clear previous animation frames

    // Reset global animation state for a new animation sequence
    animationSteps.length = 0;
    currentAnimationDelay = 0;

    // Run the animated conversion to populate animationSteps
    const finalBinaryResult = decimalToBinaryAnimated(inputInt);

    // Add a final step to display the overall binary result
    animationSteps.push({
        type: 'finalResult',
        delay: currentAnimationDelay + animationStepDuration, // Ensure it appears after all frames are gone
        finalBinary: finalBinaryResult
    });

    // Execute each recorded animation step with its calculated delay
    animationSteps.forEach(step => {
        setTimeout(() => {
            if (step.type === 'add') {
                const p = document.createElement('p');
                p.id = step.id;
                p.className = 'animation-frame';
                p.textContent = `Calling decimalToBinary(${step.inputVal})...`;
                animationContainer.prepend(p); // Add to top of stack (visually)
                // Small delay to trigger CSS transition for fade-in/slide-in
                setTimeout(() => p.classList.add('active'), 10);
            } else if (step.type === 'update') {
                const p = document.getElementById(step.id);
                if (p) {
                    p.textContent = step.msg;
                    p.classList.add('returned'); // Add class to indicate return state (e.g., change color)
                }
            } else if (step.type === 'remove') {
                const p = document.getElementById(step.id);
                if (p) {
                    p.classList.remove('active'); // Remove active state
                    p.classList.remove('returned'); // Remove returned state
                    p.classList.add('removed'); // Add class for fade-out/slide-out effect
                    // Remove the element from DOM after its transition completes
                    p.addEventListener('transitionend', () => p.remove(), { once: true });
                    // Fallback remove in case transitionend doesn't fire (e.g., no transition)
                    setTimeout(() => p.remove(), animationStepDuration * 0.5);
                }
            } else if (step.type === 'finalResult') {
                // Display the final binary result
                result.textContent = `Binary: ${step.finalBinary}`;
                // Clear any remaining animation frames from the container
                animationContainer.innerHTML = "";
            }
        }, step.delay);
    });
};

// Function to validate user input and trigger animation
const checkUserInput = () => {
    const inputInt = parseInt(numberInput.value);

    // Input validation checks
    if (!numberInput.value || isNaN(inputInt) || inputInt < 0) {
        alert("Please provide a decimal number greater than or equal to 0");
        return; // Stop execution if input is invalid
    }

    // Trigger the animation for any valid input
    showAnimation(inputInt);

    // Clear the input field after triggering the animation
    numberInput.value = "";
};

// Event listener for the convert button click
convertBtn.addEventListener("click", checkUserInput);

// Event listener for the Enter key press in the input field
numberInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        checkUserInput();
    }
});
