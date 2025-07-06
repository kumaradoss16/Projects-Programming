Number Sorter: Project Documentation
------------------------------------

This project is a web-based tool for sorting numbers using common algorithms. Users input up to six numbers, and the application sorts and displays them.

### Project Files

*   **index.html**: Sets up the web page. It contains the input fields for numbers, a "SORT" button, and an area to display the sorted output. It visually represents arrays with brackets.
    
*   **style.css**: Styles the application. It defines colors, fonts, layout (using Flexbox), and ensures responsiveness for different screen sizes. It also styles the input/output arrays to look like code.
    
*   **script.js**: Handles the logic. It reads numbers from the input, applies a sorting algorithm (currently Selection Sort, but also includes Bubble Sort and Insertion Sort), and updates the display with the sorted result.
    

### Sorting Algorithms Included:

*   **Bubble Sort**: Compares and swaps adjacent elements repeatedly until the array is sorted.
    
*   **Selection Sort**: Finds the minimum element in the unsorted part and places it at the beginning of the sorted part.
    
*   **Insertion Sort**: Builds the sorted array one item at a time by inserting each element into its correct position in the already sorted portion.
    

### How to Use

1.  **Download/Clone**: Get the project files.
    
2.  **Open index.html**: Open this file in your web browser.
    
3.  **Interact**: Enter numbers in the fields and click "SORT." To change the sorting algorithm, edit script.js.