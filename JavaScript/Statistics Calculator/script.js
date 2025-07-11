// Function to calculate the mean of an array of numbers
const getMean = (array) => array.reduce((acc, el) => acc + el, 0) / array.length;

// Function to calculate the Median of an array of numbers
const getMedian = (array) => {
    const sorted = array.toSorted((a, b) => a - b);
    if (sorted.length % 2 === 0) {
        return getMean([sorted[sorted.length / 2], sorted[sorted.length / 2 - 1]]);
    } else {
        return sorted[Math.floor(sorted.length / 2)];
    }
}

// Function to calculate the mode of an array of numbers
const getMode = (array) => {
    const counts = {};     // counts = { a: 5, b: 3, c: 8 };;
    array.forEach(el => counts[el] = counts[el] ? counts[el] + 1 : 1);
    // Object.values(counts) -> [5, 3, 8]
    // Set { 2 }
    // 1
    if (new Set(Object.values(counts)).size === 1) {
        return "--";
    }
    // Object.keys(counts) -> ['a', 'b', 'c']
    // .sort((a, b) => counts[b] - counts[a]) -> ['c', 'a', 'b']
    // [0] -> 'c'
    // counts[b] - counts[a] -> Sorts the keys based on their corresponding values in descending order.
    const highest = Object.keys(counts).sort((a, b) => counts[b] - counts[a])[0];     //[a, b, c]
    const mode = Object.keys(counts).filter(el => counts[el] === counts[highest]);
    return mode.join(", ");
}

// Function to calculate the range of an array of numbers
const getRange = (array) => {
    const smallest = Math.min(...array);
    const largest = Math.max(...array);
    return largest - smallest;
}

// Function to calculate the variance of an array of numbers
const getVariance = (array) => {
    const mean = getMean(array);
    const variance = array.reduce((acc, el) => {
        const difference = el - mean;
        const squared = difference ** 2;
        return acc + squared;
    }, 0) / array.length;
    return variance;
}

// Function to calculate the Standard Deviation of an array of numbers
const getStandardDeviation = (array) => {
    const variance = getVariance(array);
    const standardDeviation = Math.sqrt(variance);
    return standardDeviation;
}

const calculate = () => {
    // Used to get the entered value from the input field with id "numbers"
    const value = document.querySelector("#numbers").value;
    const array = value.split(/,\s*/g);     // Split the input string into an array using comma and optional space as a delimiter.
    const numbers = array.map(el => Number(el)).filter(el => !isNaN(el));      // Convert each element to a number and filter out any non-numeric values (Method Chaining).
    const mean = getMean(numbers);
    const median = getMedian(numbers);
    const mode = getMode(numbers);
    const range = getRange(numbers);
    const variance = getVariance(numbers);
    const standardDeviation = getStandardDeviation(numbers);

    document.querySelector("#mean").textContent = mean;     // Display the calculated mean in the element with id "mean".\
    document.querySelector("#median").textContent = median;
    document.querySelector("#mode").textContent = mode;
    document.querySelector("#range").textContent = range;
    document.querySelector("#variance").textContent = variance;
    document.querySelector("#standardDeviation").textContent = standardDeviation;

}

