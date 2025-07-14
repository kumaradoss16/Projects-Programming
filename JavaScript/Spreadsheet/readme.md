📊 Functional Programming Spreadsheet
=====================================

A simple, client-side web-based spreadsheet application built primarily with JavaScript, showcasing functional programming concepts and a custom formula evaluation engine. This project allows users to input values and basic formulas into cells, which are then dynamically calculated and displayed.

✨ Features
----------

*   **Grid Layout:** A basic spreadsheet grid with labeled columns (A-J) and rows (1-99).
    
*   **Cell Input:** Users can type values directly into cells.
    
*   **Formula Evaluation:** Supports basic mathematical operations and a variety of built-in spreadsheet-like functions. Formulas must start with an = sign.
    
*   **Function Support:** Includes implementations for:
    
    *   **Mathematical:** SUM, AVERAGE, MEAN, MEDIAN, MODE, MAX, MIN, SQRT, ROUND, CEIL, VARIANCE, STANDARDDEVIATION
        
    *   **Logical:** EVEN, SOMEEVEN, EVERYEVEN (filters/checks for even numbers)
        
    *   **Utility:** FIRSTTWO, LASTTWO, HAS2, INCREMENT, RANDOM, RANGE, NODUPES
        
    *   **Date/Time:** TODAY, YEAR, MONTH, DAY, DATE, HOUR, MINUTE, SECOND, TIME
        
*   **Operator Precedence:** Handles basic operator precedence for \*, /, +, -.
    
*   **Cell Referencing:** Supports direct cell references (e.g., A1, B5) and cell ranges (e.g., SUM(A1:C1)).
    
*   **Dynamic Updates:** Cell values update automatically when their dependencies change (though full dependency graph tracking is simplified).
    
*   **Functional Programming Paradigm:** The core logic heavily utilizes functional concepts like immutability (where appropriate), higher-order functions (map, reduce, filter), and pure functions.
    

🚀 Technologies Used
--------------------

*   **HTML5:** Provides the structural markup for the spreadsheet grid and its labels.
    
*   **CSS3:** Styles the spreadsheet, defining the grid layout, cell appearance, and overall visual presentation.
    
*   **JavaScript (ES6+):** The primary language for all application logic, including:
    
    *   DOM manipulation for grid creation.
        
    *   Custom formula parsing and evaluation engine.
        
    *   Implementation of all spreadsheet functions.
        
    *   Extensive use of array methods (map, reduce, filter, sort, find, slice, some, every, includes, Set).
        
    *   Regular expressions for parsing formulas and cell references.
        
    *   Currying for creating composable and specialized functions.
        

📁 Project Structure
--------------------

*   index.html: The main HTML file that sets up the basic page structure, including the
    
    title and the main div#container where the spreadsheet grid is dynamically built by JavaScript.
    ===============================================================================================
    
*   style.css: Contains all the CSS rules for styling the spreadsheet. This includes display: grid for the main container, styles for cell labels, input fields, and general typography.
    
*   script.js: The core of the application. It contains:
    
    *   Implementations of various mathematical and utility functions (e.g., sum, average, median, mode, variance, standardDeviation, max, min, sqrt, round, ceil, isEven).
        
    *   infixToFunction: Maps operators to their corresponding functions.
        
    *   infixEval, highPrecedence: Logic for evaluating arithmetic expressions with operator precedence.
        
    *   spreadsheetFunctions: An object mapping function names (like sum, average) to their JavaScript implementations.
        
    *   range, charRange, rangeFromString: Utilities for generating numerical and character ranges.
        
    *   idToText, elemValue, addCharacters: Functions for handling cell ID to value lookups and expanding cell ranges into lists of values, often using currying.
        
    *   evalFormula: The main formula evaluation engine that recursively expands ranges, cell references, and applies functions.
        
    *   window.onload: Initializes the spreadsheet grid by creating labels and input fields.
        
    *   update: The event handler for cell changes, triggering formula evaluation.
        

⚙️ Setup and Installation
-------------------------

To run this project locally, follow these simple steps:

1.  git clone https://github.com/YOUR\_USERNAME/YOUR\_REPO\_NAME.git
    
2.  cd YOUR\_REPO\_NAME _(Replace YOUR\_USERNAME and YOUR\_REPO\_NAME with your actual GitHub username and repository name.)_
    
3.  **Open in Browser:**
    
    *   Simply open the index.html file in your preferred web browser. No server setup is required as it's a client-side application.
        

💡 Usage
--------

1.  **Navigate the Grid:** The spreadsheet grid will load automatically.
    
2.  **Enter Values:** Click on any cell and type a number or text.
    
3.  **Enter Formulas:** To enter a formula, start the input with an equals sign (=).
    
    *   **Basic Arithmetic:** =10+20, =A1\*B2, =(5+3)/2
        
    *   **Functions:** =SUM(A1,B1,C1), =AVERAGE(A1:A5), =MEDIAN(B1:B3,C1,D1)
        
    *   **Cell References:** Use A1, B2, etc.
        
    *   **Cell Ranges:** Use A1:B5 within functions that accept ranges.
        
4.  **Evaluate:** After typing a formula, press Enter or click outside the cell. The cell will display the calculated result.