const infixToFunction = {
    "+": (x, y) => x + y,
    "-": (x, y) => x - y,
    "*": (x, y) => x * y,
    "/": (x, y) => x / y,
}

const infixEval = (str, regex) => str.replace(regex, (_match, arg1, operator, arg2) => infixToFunction[operator](parseFloat(arg1), parseFloat(arg2)));

const highPrecedence = str => {
    const regex = /([\d.]+)([*\/])([\d.]+)/;
    const str2 = infixEval(str, regex);
    return str === str2 ? str : highPrecedence(str2);
}
// Sum function: This function takes an array of numbers and returns their sum.
const sum = nums => nums.reduce((acc, el) => acc + el, 0);

// Even function: This function checks if a number is even by using the modulo operator (%).
const isEven = num => num % 2 === 0;

// Average function: This function calculates the average of an array of numbers.
const average = nums => sum(nums) / nums.length;

const mean = nums => nums.reduce((acc, el) => acc + el, 0) / nums.length;

const median = nums => {
    const sorted = nums.slice().sort((a, b) => a - b);
    const length = sorted.length;
    const middle = length / 2 - 1;
    return isEven(length) ? average([sorted[middle], sorted[middle + 1]]) :
        sorted[Math.ceil(middle)];
}

const mode = nums => {
    const counts = {};     // counts = { a: 5, b: 3, c: 8 };;
    nums.forEach(el => counts[el] = counts[el] ? counts[el] + 1 : 1);
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

// Function to calculate the variance of an array of numbers
const variance = nums => {
    const m = mean(nums);
    const variance = nums.reduce((acc, el) => {
        const difference = el - m;
        const squared = difference ** 2;
        return acc + squared;
    }, 0) / nums.length;
    return variance;
}

// Function to calculate the Standard Deviation of an array of numbers
const standardDeviation = nums => {
    const v = variance(nums);
    const standardDeviation = Math.sqrt(v);
    return standardDeviation;
}

const max = nums => Math.max(...nums);

const min = nums => Math.min(...nums);

const sqrt = nums => Number.isNaN(nums) ? NaN : Math.sqrt(nums);

const round = nums => nums.map(num => Math.round(num));

const ceil = nums => nums.map(num => Math.ceil(nums));

const spreadsheetFunctions = {
    "": arg => arg,
    sum,
    average,
    median,
    mean,
    mode,
    variance,
    standardDeviation,
    max,
    min,
    sqrt,
    round,
    ceil,
    today: () => new Date(),
    year: () => new Date().getFullYear(),
    month: () => new Date().getMonth(),
    day: () => new Date().getDay(),
    date: () => new Date().getDate(),
    hour: () => new Date().getHours(),
    minute: () => new Date().getMinutes(),
    second: () => new Date().getSeconds(),
    time: () => new Date().getTime(),
    even: nums => nums.filter(isEven),
    someeven: nums => nums.some(isEven),
    everyeven: nums => nums.every(isEven),
    firsttwo: nums => nums.slice(0, 2),
    lasttwo: nums => nums.slice(-2),
    has2: nums => nums.includes(2),
    increment: nums => nums.map(num => num + 1),
    random: ([x, y]) => Math.floor(Math.random() * (y - x) + x),
    range: nums => range(...nums),
    nodupes: nums => [... new Set(nums)]
};

const applyFunction = str => {
    const noHigh = highPrecedence(str);
    const infix = /([\d.]+)([+-])([\d.]+)/;
    const str2 = infixEval(noHigh, infix);
    const functionCall = /([a-z0-9]*)\(([0-9., ]*)\)(?!.*\()/i;
    const toNumberList = args => args.split(",").map(parseFloat);
    const apply = (fn, args) => spreadsheetFunctions[fn.toLowerCase()](toNumberList(args));
    return str2.replace(functionCall, (match, fn, args) => spreadsheetFunctions.hasOwnProperty(fn.toLowerCase()) ? apply(fn, args) : match);
}

// end - start + 1: This calculates the number of elements that should be in the resulting array. For range(5, 9): 9 - 5 + 1 = 5
// Array(end - start + 1).fill(start) -> range(5, 9): [empty, empty, empty, empty, empty].fill(5) results in [5, 5, 5, 5, 5]
// [5, 5, 5, 5, 5].map((element, index) => element + index) -> [5, 6, 7, 8, 9]
const range = (start, end) => Array(end - start + 1).fill(start).map((element, index) => element + index);     // .fill() method which can be used to fill an array with a value.

const charRange = (start, end) => range(start.charCodeAt(0), end.charCodeAt(0)).map((code) => String.fromCharCode(code));

const evalFormula = (x, cells) => {
    // id: A unique identifier for that cell (e.g., "B1").
    // cell: In each iteration, cell represents the current object from the cells array (e.g., { id: "A1", value: 10 }, { id: "B1", value: "Hello" }).
    // Result: "Hello"
    const idToText = id => cells.find(cell => cell.id === id).value;
    const rangeRegex = /([A-J])([1-9][0-9]?):([A-J])([1-9][0-9]?)/gi;
    const rangeFromString = (num1, num2) => range(parseInt(num1), parseInt(num2));
    // elemValue(1)('A')  num = 1, character = 'A'
    // idToText("A1") -> the value of the cell with id "A1"
    const elemValue = num => character => idToText(character + num);
    // addCharacters('A')('C')(5)
    // character1 is assigned the value 'A'  && character2 is assigned the value 'C'.
    // charRange('A', 'C') ->['A', 'B', 'C']
    // addCharacters('A')('C')(1), it's essentially saying: "Give me the values from cells A1, B1, and C1
    const addCharacters = character1 => character2 => num => charRange(character1, character2).map(elemValue(num));
    // x: (e.g., "SUM(A1:C1,D5:F5)"
    // For A1:C1, char1 would be 'A', num1 would be '1', char2 would be 'C', num2 would be '1'.
    // For A1:C1, this would be rangeFromString("1", "1"), which returns [1].
    // . For example, if x was SUM(A1:C1) and A1=10, B1=20, C1=30, rangeExpanded might become SUM(10,20,30)
    const rangeExpanded = x.replace(rangeRegex, (_match, char1, num1, char2, num2) => rangeFromString(num1, num2).map(addCharacters(char1)(char2)));
    const cellRegex = /[A-J][1-9][0-9]?/gi;
    const cellExpanded = rangeExpanded.replace(cellRegex, match => idToText(match.toUpperCase()));
    const functionExpanded = applyFunction(cellExpanded);
    return functionExpanded === x ? functionExpanded : evalFormula(functionExpanded, cells);
}

// window is the global object that represents the browser window itself.
// .onload: This is an event handler property of the window object.
window.onload = () => {     // ensure that your JavaScript code runs only after the necessary HTML elements are available in the DOM.
    const container = document.getElementById("container");
    const createLabel = (name) => {
        const label = document.createElement("div");
        label.className = "label";     // set the class name for styling
        label.textContent = name;     // set the text content of the label to the provided name.
        container.appendChild(label);     // add the label element to the container element.
    }
    const letters = charRange("A", "J");
    letters.forEach(createLabel);
    range(1, 99).forEach(number => {
        createLabel(number);
        letters.forEach(letter => {
            const input = document.createElement("input");
            input.type = "text";
            input.id = letter + number;
            input.ariaLabel = input.id;
            input.onchange = update;
            container.appendChild(input);
        })
    })
}


const update = event => {
    const element = event.target;
    const value = element.value.replace(/\s/g, "");
    if (!value.includes(element.id) && value.startsWith('=')) {
        element.value = evalFormula(value.slice(1), Array.from(document.getElementById("container").children));
    }
}