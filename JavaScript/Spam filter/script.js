const messageInput = document.getElementById("message-input");
const result = document.getElementById("result");
const checkMessageButton = document.getElementById("check-message-btn");

// Handling common character substitution and optional spaces/punctuation
const createFlexibleRegex = (word) => {
    // Map common spammer substitutions
    const substitutions = {
        'a': '[a@4]',
        'e': '[e3]',
        'i': '[i1!|]',
        'o': '[o0]',
        's': '[s5$]',
        't': '[t7]',
        'l': '[l1]',
        'c': '[c{(]',
        'k': '[k{[(]', // Added for 'stock'
        'u': '[u]', // Can add more if common
        'y': '[y]', // Can add more if common
        'd': '[d]', // Can add more if common
        'r': '[r]' // Can add more if common
    };

    // Build the regex pattern by replacing characters with their substitution class
    let pattern = word.split("").map(char => {
        const lowerChar = char.toLowerCase();
        return (substitutions[lowerChar] || char) + "[^a-zA-Z0-9$]*";  // ['f[^a-zA-Z0-9]*', 'r[^a-zA-Z0-9]*', '[e3][^a-zA-Z0-9]*', '[e3][^a-zA-Z0-9]*']
    }).join("");     // f[^a-zA-Z0-9]*r[^a-zA-Z0-9]*[e3][^a-zA-Z0-9]*[e3][^a-zA-Z0-9]*

    pattern = pattern.slice(0, -"[^a-zA-Z0-9$]*".length);     // f[^a-zA-Z0-9]*r[^a-zA-Z0-9]*[e3][^a-zA-Z0-9]*[e3]

    return new RegExp(`(?:^|//W)${pattern}(?:\\W|$)`, "i");
};


const denyList = [
    // Financial / Money related
    createFlexibleRegex('free money'),
    createFlexibleRegex('make money'),
    createFlexibleRegex('cash now'),
    createFlexibleRegex('earn money'),
    createFlexibleRegex('financial freedom'),
    createFlexibleRegex('investment opportunity'),
    createFlexibleRegex('credit card'),
    createFlexibleRegex('loan'),
    createFlexibleRegex('debt'),
    createFlexibleRegex('win'),
    createFlexibleRegex('prize'),
    createFlexibleRegex('winner'),
    createFlexibleRegex('claim'),
    createFlexibleRegex('congratulations'),
    createFlexibleRegex('limited time'),
    createFlexibleRegex('exclusive offer'),
    createFlexibleRegex('discount'),
    createFlexibleRegex('guarantee'),
    createFlexibleRegex('risk free'),
    createFlexibleRegex('no cost'),
    createFlexibleRegex('urgent'),
    createFlexibleRegex('act now'),
    createFlexibleRegex('click here'),
    createFlexibleRegex('subscribe'),
    createFlexibleRegex('unlimited'),
    createFlexibleRegex('miracle'),
    createFlexibleRegex('lose weight'),
    createFlexibleRegex('viagra'),
    createFlexibleRegex('cialis'),
    createFlexibleRegex('pharmacy'),
    createFlexibleRegex('sex'),
    createFlexibleRegex('adult'),
    createFlexibleRegex('naked'),
    createFlexibleRegex('porn'),
    createFlexibleRegex('gambling'),
    createFlexibleRegex('casino'),
    createFlexibleRegex('lotto'),
    createFlexibleRegex('sweepstakes'),
    createFlexibleRegex('bitcoin'),
    createFlexibleRegex('crypto'),
    createFlexibleRegex('blockchain'),
    createFlexibleRegex('stock alert'), // specific phrase
    createFlexibleRegex('dear friend'), // specific phrase

    // Common scam phrases/requests
    createFlexibleRegex('please help'),
    createFlexibleRegex('assist me'),
    createFlexibleRegex('kindly respond'),
    createFlexibleRegex('verify account'),
    createFlexibleRegex('security alert'),
    createFlexibleRegex('account suspended'),
    createFlexibleRegex('unusual activity'),
    createFlexibleRegex('password reset'),
    createFlexibleRegex('confirm details'),
    createFlexibleRegex('your bank'),
    createFlexibleRegex('nigerian prince'), // A classic!
    createFlexibleRegex('inheritance'),
    createFlexibleRegex('lottery'),
    createFlexibleRegex('government grant'),

    // Numeric patterns for money amounts
    // This is more robust than a simple dollarRegex
    /\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?\s*(?:usd|eur|gbp|dollars?|pounds?|euros?|million|billion|thousand)/i,
    /\$\s*\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?/i, // $ followed by numbers
    /£\s*\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?/i, // £ followed by numbers
    /€\s*\d{1,3}(?:[.,]\d{3})*(?:[.,]\d{2})?/i, // € followed by numbers

    // Excessive capitalization (e.g., "FREE MONEY" but not "USA")
    /\b[A-Z]{3,}\b(?:\s+\b[A-Z]{3,}\b){1,}/g, // Matches 2 or more consecutive words with 3+ uppercase letters
    // Suspicious URLs (basic, can be much more complex)
    /(?:https?:\/\/(?:bit\.ly|tinyurl\.com|goo\.gl|ow\.ly|t\.co)\/[a-zA-Z0-9]+)|(?:https?:\/\/[a-zA-Z0-9.-]+\.[a-z]{2,6}\/[^ ]{10,})/i,

    // Excessive punctuation
    /(\!{3,})|(\?{3,})|(\.{4,})|(\*{3,})/g,      // '!!!, ???, ...., ***'
    /(\${2,})/g, // $$$, etc.
];

const isSpam = (msg) => {
    let normalizeMsg = msg.toLowerCase()
        .replace(/\s+/g, "")    // Replace multiple spaces with single space
        .replace(/[\!\?\.\:\;\"\'\,]/g, "")     // Remove common punctuation

    return denyList.some(regex => regex.test(msg));
}

checkMessageButton.addEventListener("click", () => {
    if (messageInput.value.trim() === "") {
        alert("Please enter a message.");
        return;
    }

    const isSpamMsg = isSpam(messageInput.value);
    result.innerHTML = isSpamMsg
        ? `<span style="color: red;">Oh no! This looks like a spam message.</span>`
        : `<span style="color: green;">This message does not seem to contain any spam.</span>`;
    messageInput.value = "";
});