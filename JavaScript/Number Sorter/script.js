const sortButton = document.getElementById("sort");

const sortInputArray = (event) => {
    event.preventDefault();
    const inputValues = [...document.getElementsByClassName("values")].map(dropdown => Number(dropdown.value));     // ['5', '8', '4', '0', '7', '2'] -> [5, 8, 4, 0, 7, 2]
    const sortedValues = selectionSort(inputValues);
    updateUI(sortedValues);
}

// Update the display with the sorted numbers.
const updateUI = (array = []) => {
    // To perform iterating over arrays.
    array.forEach((num, i) => {
        const outputValueNode = document.getElementById(`output-value-${i}`);
        outputValueNode.innerText = num;     // output section can be updated by input array.
    });
}

// Bubble sorting algorithm
const bubbleSort = (array) => {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length - 1; j++) {
            if (array[j] > array[j + 1]) {
                const temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
    return array;
}

// Selection Sorting Algorithm
const selectionSort = (array) => {
    for (let i = 0; i < array.length; i++) {
        let minIndex = i;
        for (let j = i + 1; j < array.length; j++) {
            if (array[j] < array[minIndex]) {     // array[j] -> second element, array[minIndex] -> first element in the array.
                minIndex = j;
            }
        }
        const temp = array[i];
        array[i] = array[minIndex];
        array[minIndex] = temp;
    }
    return array;
}

// Insertion Sorting Algorithm
const insertionSort = (array) => {
    for (let i = 1; i < array.length; i++) {
        const currValue = i;
        let j = i - 1;
        while (j >= 0 && array[j] > currValue) {
            array[j + 1] = array[j];
        }
        array[j + 1] = currValue;
    }
    return array;
}

sortButton.addEventListener("click", sortInputArray);