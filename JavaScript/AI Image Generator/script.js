const themeToggle = document.querySelector(".theme-toggle");
const promptInput = document.querySelector(".prompt-input");   // for <textarea> tag
const promptForm = document.querySelector(".prompt-form");
const promptBtn = document.querySelector(".prompt-btn");
const generateBtn = document.querySelector(".generate-btn");
const modelSelect = document.getElementById("model-select");
const countSelect = document.getElementById("count-select");
const ratioSelect = document.getElementById("ratio-select");
const gridGallery = document.querySelector(".gallery-grid");
const API_KEY = "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";   // Hugging face Website API key

const examplePrompt = [
    "A futuristic city at sunset, neon lights, flying cars, cinematic.",
    "A cozy cottage in a magical forest, glowing mushrooms, soft light, fantasy art.",
    "A majestic lion roaring on a savanna, golden hour, realistic, wildlife photography.",
    "An astronaut floating in space, looking at Earth, vibrant nebula, surreal.",
    "A serene Japanese garden, cherry blossoms, koi pond, peaceful, watercolor style.",
    "A cyberpunk hacker in a dark room, glowing screens, rain outside, gritty, digital painting.",
    "A cute robot holding a flower, whimsical, pastel colors, cartoon style.",
    "A vintage car driving on a desert road, dusty, retro photography.",
    "An ancient wizard casting a spell, glowing staff, mystical ruins, epic fantasy.",
    "A minimalist abstract painting, geometric shapes, muted earth tones."
];

// Set theme based on saved preference or system default.
(() => {
    const savedTheme = localStorage.getItem("theme");   // Check if you-ve saved a theme preference before (dark or light).
    const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;   // Check if your computer's OS prefers a dark theme.
    // If you saved "dark" before use dark OR if you haven't saved anything, use whatever your computer prefers (dark or light).
    const isDarkTheme = savedTheme === "dark" || (!savedTheme && systemPrefersDark);
    document.body.classList.toggle("dark-theme", isDarkTheme);
    themeToggle.querySelector("i").className = isDarkTheme ? "fa-solid fa-sun" : "fa-solid fa-moon";
})();  // The () at the end immediately executes this function.
// Switch between light and dark.
const toggleTheme = () => {
    const isDarkTheme = document.body.classList.toggle("dark-theme");
    localStorage.setItem("theme", isDarkTheme ? "dark" : "light");
    themeToggle.querySelector("i").className = isDarkTheme ? "fa-solid fa-sun" : "fa-solid fa-moon";
};

// Calculate width/height based on chosen ratio
const getImageDimensions = (aspectRatio, baseSize = 512) => {
    const [width, height] = aspectRatio.split("/").map(Number);    // e.g. "16/9" =>  ["16", "9"];  .map(Number) -> converts each string in the array to a number ([16, 9])
    const scaleFactor = baseSize / Math.sqrt(width * height);

    // Calculate Initial Dimensions:
    let calculateWidth = Math.round(width * scaleFactor);
    let calculateHeight = Math.round(height * scaleFactor);
    // Ensure dimensions are multiples of 16 (AI Models requirements)
    calculateWidth = Math.floor(calculateWidth / 16) * 16;
    calculateHeight = Math.floor(calculateHeight / 16) * 16;
    return { width: calculateWidth, height: calculateHeight };
}

// Replace loading spinner with the actual image
const updateImageCard = (imgIndex, imgUrl) => {
    const imgCard = document.getElementById(`img-card-${imgIndex}`);
    if (!imgCard) return;
    imgCard.classList.remove("loading");
    imgCard.innerHTML = ` <img src="${imgUrl}" class="result-img">
                            <div class="img-overlay">
                                <a href="${imgUrl}" class="img-download-btn" download="${Date.now()}.png">
                                    <i class="fa-solid fa-download"></i>
                                </a>
                            </div>`
}

// Send request to Hugging Face API to create images
const generateImage = async (selectedModel, imageCount, aspectRatio, promptText) => {
    // Construct API URL:
    const MODEL_URL = `https://api-inference.huggingface.co/models/${selectedModel}`;
    // Get Image Dimensions:
    const { width, height } = getImageDimensions(aspectRatio);
    generateBtn.setAttribute("disabled", "true");
    // Create a array of image generation promises
    const imagePromises = Array.from({ length: imageCount }, async (_, i) => {    // Creates a new array with 'imageCount' empty slots.  For each slot it creates an 'async' function (Single image generation request).
        // Send individual image generation request to the AI model API
        try {
            const response = await fetch(MODEL_URL, {
                headers: {
                    Authorization: `Bearer ${API_KEY}`,
                    "Content-Type": "application/json",
                    "x-use-cache": "false",   // Prevents API from returning cached results for the same prompt.
                },
                method: "POST",
                // Reference of Hugging Face website
                body: JSON.stringify({   // Converts JS onject into a JSON string for the request body.
                    inputs: promptText,
                    parameters: { width, height },
                    response_format: "blob",
                    model: selectedModel
                    // options: { wait_for_model: true, user_cache: false },
                }),
            });
            // If the request fails, it will throw an error.
            if (!response.ok) throw new Error((await response.json())?.error);   //  safely access properties deep inside objects without checking if each part of the "chain" exists.
            // Convert response to an image URL and update the image card.
            const result = await response.blob();    // attempts to parse the body of the response as a Blob (Binary Large Object)
            updateImageCard(i, URL.createObjectURL(result));
        } catch (error) {
            console.log(error);
            const imgCard = document.getElementById(`img-card-${i}`);
            imgCard.classList.replace("loading", "error");
            imgCard.querySelector(".status-text").textContent = "Generation failed! Check console for more details.";
        }
    })
    generateBtn.removeAttribute("disabled");
    await Promise.allSettled(imagePromises);

};

// Create placeholder cards with loading spinners
const createImageCards = (selectedModel, imageCount, aspectRatio, promptText) => {
    gridGallery.innerHTML = "";
    for (let i = 0; i < imageCount; i++) {
        gridGallery.innerHTML +=
            `<div class="img-card loading" id="img-card-${i}" style="aspect-ratio: ${aspectRatio}">
                <div class="status-container">
                    <div class="spinner"></div>
                    <i class="fa-solid fa-triangle-exclamation"></i>
                    <p class="status-text">Generating...</p>
                </div>
            </div>`;
    }
    generateImage(selectedModel, imageCount, aspectRatio, promptText);
};

// Handle form submission
const handleFormSubmit = (e) => {
    e.preventDefault();   // Prevent form from submitting
    // Get form values
    const selectedModel = modelSelect.value;
    const imageCount = parseInt(countSelect.value) || 1;
    const aspectRatio = ratioSelect.value || "1/1";
    const promptText = promptInput.value.trim();   // 'trim' method removes whitespace from ends of the string.

    createImageCards(selectedModel, imageCount, aspectRatio, promptText);

}

// Fill prompt input with random example
promptBtn.addEventListener("click", () => {
    const prompt = examplePrompt[Math.floor(Math.random() * examplePrompt.length)];
    promptInput.value = prompt;    // Sets the 'value' property of that input element to the randomly selected prompt string.
    promptInput.focus();   // 'focus' method sets the focus of the promptInput element
})

promptForm.addEventListener("submit", handleFormSubmit);
themeToggle.addEventListener("click", toggleTheme);