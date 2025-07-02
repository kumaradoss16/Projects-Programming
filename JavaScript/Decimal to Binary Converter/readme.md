Decimal to Binary Converter: Project Documentation
--------------------------------------------------

This project provides a simple web-based Decimal to Binary Converter with an animated visualization of the recursive call stack. It's designed to help understand how recursion works, specifically in the context of converting a decimal number to its binary representation.

### Project Structure

The project consists of three core files:

1.  **index.html**: The main HTML file that provides the user interface.
    
2.  **style.css**: Defines the visual styling and layout of the web application.
    
3.  **script.js**: Contains the JavaScript logic for the conversion, animation, and user interaction.
    

### File Descriptions

#### 1\. index.html

This file sets up the basic structure of the web page.

*   **Purpose**: Provides the user interface elements, including an input field for the decimal number, a "Convert" button, an output area for the result, and a dedicated container for the call stack animation.
    
*   **Key Elements**:
    
    *   Decimal to Binary Converter: The main title of the application.
        
    *   : Contains the label, input field (id="number-input"), and button (id="convert-btn") for user input.
        
    *   : Houses the output element (id="result") where the final binary number is displayed, and the div (id="animation-container") which serves as the visual representation of the call stack.
        
    *   Links to style.css for styling and script.js for functionality.
        

#### 2\. style.css

This file dictates the visual appearance and responsiveness of the converter.

*   **Purpose**: Styles the HTML elements to create an intuitive and visually appealing user interface. It also includes styles for the animation frames to simulate the push and pop operations on the call stack.
    
*   **Key Styling Aspects**:
        
    *   **Layout**: Employs Flexbox for responsive centering and arrangement of elements, especially for the input container and the main body.
        
    *   **Color Scheme**: Utilizes a dark blue background with light grey text and an orange accent color for buttons, borders, and highlights.
        
    *   **Animation Container (#animation-container)**: Styled to resemble a stack, with flex-direction: column-reverse to visually represent new frames being "pushed" onto the top. It also includes styles for animation-frame, active, returned, and removed classes to facilitate CSS transitions for the animation effects (fade-in, slide-in, color changes, fade-out).
        

#### 3\. script.js

This is the core logic file that handles the decimal to binary conversion and the animation.

*   **Purpose**: Manages user input, performs the decimal to binary conversion using recursion, records the steps of the recursive calls, and orchestrates the visual animation of the call stack.
    
*   **Key Functions and Logic**:
    
    *   **DOM Element Selection**: Selects necessary HTML elements (numberInput, convertBtn, result, animationContainer) for manipulation.
        
    *   **decimalToBinary(input)**: The original, pure recursive function that calculates the binary representation of a decimal number. This is used for the actual computation.
        
    *   **animationSteps (Global Array)**: Stores objects representing each step of the animation (add frame, update frame, remove frame).
        
    *   **currentAnimationDelay & animationStepDuration**: Global variables to manage the timing and sequencing of animation events.
        
    *   **decimalToBinaryAnimated(input)**: A modified recursive function that not only calculates the binary result but also **records detailed steps for the animation** in the animationSteps array. Each call records an 'add' (function call), 'update' (function returns), and 'remove' (function finishes) step.
        
    *   **showAnimation(inputInt)**:
        
        *   Clears previous animation.
            
        *   Resets animation state variables (animationSteps, currentAnimationDelay).
            
        *   Calls decimalToBinaryAnimated() to populate the animationSteps array.
            
        *   Adds a finalResult step to display the final binary output after the animation.
            
        *   Iterates through animationSteps and uses setTimeout to execute each step with its calculated delay, visually updating the animationContainer by adding, updating, and removing p elements representing stack frames.
            
    *   **checkUserInput()**:
        
        *   Validates user input to ensure it's a non-negative decimal number.
            
        *   Triggers the showAnimation() function with valid input.
            
        *   Clears the input field.
            
    *   **Event Listeners**:
        
        *   Attaches click event to convertBtn to call checkUserInput.
            
        *   Attaches keydown event to numberInput to trigger checkUserInput when the "Enter" key is pressed.
            

### How to Run

1.  **Clone or Download**: Get the project files onto your local machine.
    
2.  **Open index.html**: Simply open the index.html file in any modern web browser.
    
3.  **Interact**: Enter a decimal number in the input field and click "Convert" or press "Enter" to see the binary conversion and the call stack animation.
