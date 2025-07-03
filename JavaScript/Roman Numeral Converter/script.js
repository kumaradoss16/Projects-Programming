const form = document.getElementById("form");
const convertBtn = document.getElementById("convert-btn");
const output = document.getElementById("output");
const clearBtn = document.getElementById("cancel-btn");
const numberInput = document.getElementById("number");

const convertToRoman = num => {
    const ref = [
        ['M', 1000],
        ['CM', 900],
        ['D', 500],
        ['CD', 400],
        ['C', 100],
        ['XC', 90],
        ['L', 50],
        ['XL', 40],
        ['X', 10],
        ['IX', 9],
        ['V', 5],
        ['IV', 4],
        ['I', 1]
    ];

    const res = [];

    ref.forEach(function (arr) {
        while (num >= arr[1]) {
            res.push(arr[0]);
            num -= arr[1];
        }
    })

    return res.join('');
}

const isValid = (str, int) => {
    let errTxt = "";
    if (!str || str.match(/[e.]/g)) {
        errTxt = "Please enter a valid number";
    } else if (int < 1) {
        errTxt = "Please enter a number greater than or equal to 1";
    } else if (int > 10000) {
        errTxt = "Please enter a number less than or equal to 10000"
    } else {
        return true;
    }

    output.innerText = errTxt;
    output.classList.add("alert");

    return false;
}

const clearOutput = () => {
    output.innerText = "";
    output.classList.remove("alert");
}

clearBtn.addEventListener("click", () => {
    output.classList.remove("hidden");
    numberInput.value = "";
    clearOutput();
})

form.addEventListener("submit", e => {
    e.preventDefault();
    updateUI();
})

convertBtn.addEventListener("click", () => {
    updateUI();
})

const updateUI = () => {
    const numStr = document.getElementById("number").value;
    const int = parseInt(numStr, 10);

    output.classList.remove("hidden");
    clearOutput();

    if (isValid(numStr, int)) {
        output.innerText = convertToRoman(int);
    }
}

// Event listener for the Enter key press in the input field
numberInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        updateUI();
    }
});