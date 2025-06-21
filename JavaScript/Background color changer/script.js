function getRandomColor() {
    const digits = "0123456789ABCDEF";
    let color = "#";
    for (let i = 0; i < 6; i++) {
        color += digits[Math.floor(Math.random() * 16)];
    }
    return color;
}

const randomColors = Array(100).fill().map(getRandomColor);

function getRandomIndex() {
    const randomIndex = Math.floor(randomColors.length * Math.random());
    return randomIndex;
}

const body = document.querySelector("body");
const bgHexCodeSpanElement = document.querySelector("#bg-hex-code");

function changeBackgroundColor() {
    const color = randomColors[getRandomIndex()];
    bgHexCodeSpanElement.innerText = color;
    body.style.backgroundColor = color; 
}

const btn = document.querySelector("#btn");
btn.onclick = changeBackgroundColor;
