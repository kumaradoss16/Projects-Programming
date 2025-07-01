const themeToggle = document.querySelector(".theme-toggle");
const teamNameElement = document.getElementById("team"); // Renamed to avoid conflict with team property
const typeOfSportElement = document.getElementById("sport"); // Renamed
const worldCupYearElement = document.getElementById("year"); // Renamed
const headCoachElement = document.getElementById("coach"); // Renamed
const playerCardsContainer = document.getElementById("player-cards"); // Renamed for clarity
const playersDropdownList = document.getElementById("players");
const teamSelectDropdown = document.getElementById("team-select"); // New: reference for team selection dropdown

// Define all cricket teams
const allCricketTeams = [
    {
        team: "India",
        sport: "Cricket",
        year: 2024, // Updated to 2024
        isWorldCupWinner: false, // Not World Cup 2024 winner yet
        headCoach: {
            coachName: "Gautam Gambhir", // Updated coach
        },
        players: [
            { name: "Rohit Sharma", position: "batsman", number: 45, isCaptain: true, nickname: "Hitman" },
            { name: "Hardik Pandya", position: "all-rounder", number: 33, isCaptain: false, nickname: "N/A" },
            { name: "Virat Kohli", position: "batsman", number: 18, isCaptain: false, nickname: "Cheeku" },
            { name: "Suryakumar Yadav", position: "batsman", number: 63, isCaptain: false, nickname: "SKY" },
            { name: "Yashasvi Jaiswal", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Rishabh Pant", position: "wicketkeeper", number: 17, isCaptain: false, nickname: "N/A" },
            { name: "Sanju Samson", position: "wicketkeeper", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Shivam Dube", position: "all-rounder", number: 25, isCaptain: false, nickname: "N/A" },
            { name: "Axar Patel", position: "all-rounder", number: 20, isCaptain: false, nickname: "N/A" },
            { name: "Ravindra Jadeja", position: "all-rounder", number: 8, isCaptain: false, nickname: "Jaddu" },
            { name: "Kuldeep Yadav", position: "bowler", number: 23, isCaptain: false, nickname: "Chinaman" },
            { name: "Yuzvendra Chahal", position: "bowler", number: 3, isCaptain: false, nickname: "N/A" },
            { name: "Arshdeep Singh", position: "bowler", number: 2, isCaptain: false, nickname: "N/A" },
            { name: "Mohammed Siraj", position: "bowler", number: 13, isCaptain: false, nickname: "Miyaan" },
            { name: "Jasprit Bumrah", position: "bowler", number: 93, isCaptain: false, nickname: "Jassi" }
        ]
    },
    {
        team: "Sri Lanka",
        sport: "Cricket",
        year: 2024, // Updated to 2024
        isWorldCupWinner: false, // Not World Cup 2024 winner yet
        headCoach: {
            coachName: "Sanath Jayasuriya", // Updated coach
        },
        players: [
            { name: "Charith Asalanka", position: "batsman", number: 16, isCaptain: true, nickname: "N/A" }, // Updated captain
            { name: "Kusal Mendis", position: "wicketkeeper", number: 99, isCaptain: false, nickname: "N/A" },
            { name: "Pathum Nissanka", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Dhananjaya de Silva", position: "all-rounder", number: 75, isCaptain: false, nickname: "N/A" },
            { name: "Kamindu Mendis", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Dunith Wellalage", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Dasun Shanaka", position: "all-rounder", number: 27, isCaptain: false, nickname: "N/A" },
            { name: "Angelo Mathews", position: "all-rounder", number: 69, isCaptain: false, nickname: "N/A" },
            { name: "Nuwan Thushara", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Dilshan Madushanka", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Maheesh Theekshana", position: "bowler", number: 1, isCaptain: false, nickname: "N/A" },
            { name: "Dushmantha Chameera", position: "bowler", number: 90, isCaptain: false, nickname: "N/A" },
            { name: "Kasun Rajitha", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Sadeera Samarawickrama", position: "wicketkeeper", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Wanindu Hasaranga", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" } // Added as a player, not captain for this squad
        ]
    },
    {
        team: "Australia",
        sport: "Cricket",
        year: 2024, // Using current year for "recent"
        isWorldCupWinner: false, // Not for 2024, but keeping the property
        headCoach: {
            coachName: "Andrew McDonald",
        },
        players: [
            { name: "Pat Cummins", position: "bowler", number: 30, isCaptain: true, nickname: "N/A" },
            { name: "Steve Smith", position: "batsman", number: 49, isCaptain: false, nickname: "Smudge" },
            { name: "Travis Head", position: "batsman", number: 62, isCaptain: false, nickname: "N/A" },
            { name: "Marnus Labuschagne", position: "batsman", number: 33, isCaptain: false, nickname: "Marnus" },
            { name: "Alex Carey", position: "wicketkeeper", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Josh Inglis", position: "wicketkeeper", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Glenn Maxwell", position: "all-rounder", number: 32, isCaptain: false, nickname: "The Big Show" },
            { name: "Marcus Stoinis", position: "all-rounder", number: 17, isCaptain: false, nickname: "Stoin" },
            { name: "Mitchell Starc", position: "bowler", number: 56, isCaptain: false, nickname: "N/A" },
            { name: "Josh Hazlewood", position: "bowler", number: 38, isCaptain: false, nickname: "N/A" },
            { name: "Adam Zampa", position: "bowler", number: 46, isCaptain: false, nickname: "Zamps" },
            { name: "Cameron Green", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "David Warner", position: "batsman", number: 31, isCaptain: false, nickname: "Davey" },
            { name: "Nathan Ellis", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Sean Abbott", position: "bowler", number: "N/A", isCaptain: false, nickname: "Abbott" }
        ]
    },
    {
        team: "England",
        sport: "Cricket",
        year: 2024, // Using current year for "recent"
        isWorldCupWinner: false, // Not for 2024, but keeping the property
        headCoach: {
            coachName: "Brendon McCullum",
        },
        players: [
            { name: "Ben Stokes", position: "all-rounder", number: 55, isCaptain: true, nickname: "N/A" },
            { name: "Joe Root", position: "batsman", number: 66, isCaptain: false, nickname: "N/A" },
            { name: "Zak Crawley", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Ollie Pope", position: "batsman", number: 80, isCaptain: false, nickname: "N/A" },
            { name: "Jonny Bairstow", position: "wicketkeeper", number: 51, isCaptain: false, nickname: "Jonny B" },
            { name: "Jos Buttler", position: "wicketkeeper", number: 63, isCaptain: false, nickname: "N/A" }, // Jos Buttler is white-ball captain, Ben Stokes is Test captain
            { name: "Moeen Ali", position: "all-rounder", number: 18, isCaptain: false, nickname: "Moeen" },
            { name: "Chris Woakes", position: "bowler", number: 19, isCaptain: false, nickname: "Woakesy" },
            { name: "Mark Wood", position: "bowler", number: 36, isCaptain: false, nickname: "Woody" },
            { name: "James Anderson", position: "bowler", number: "N/A", isCaptain: false, nickname: "Jimmy" },
            { name: "Stuart Broad", position: "bowler", number: 8, isCaptain: false, nickname: "Broad" }, // Assuming he's still in the "recent" context for some formats
            { name: "Jofra Archer", position: "bowler", number: 22, isCaptain: false, nickname: "N/A" },
            { name: "Harry Brook", position: "batsman", number: 88, isCaptain: false, nickname: "N/A" },
            { name: "Sam Curran", position: "all-rounder", number: 58, isCaptain: false, nickname: "N/A" },
            { name: "Adil Rashid", position: "bowler", number: 95, isCaptain: false, nickname: "Rash" }
        ]
    },
    {
        team: "South Africa",
        sport: "Cricket",
        year: 2024,
        isWorldCupWinner: false,
        headCoach: {
            coachName: "Shukri Conrad",
        },
        players: [
            { name: "Temba Bavuma", position: "batsman", number: 46, isCaptain: true, nickname: "N/A" },
            { name: "Quinton de Kock", position: "wicketkeeper", number: 12, isCaptain: false, nickname: "Quinny" },
            { name: "Aiden Markram", position: "batsman", number: 4, isCaptain: false, nickname: "N/A" },
            { name: "David Miller", position: "batsman", number: 10, isCaptain: false, nickname: "Killer Miller" },
            { name: "Heinrich Klaasen", position: "wicketkeeper", number: 45, isCaptain: false, nickname: "N/A" },
            { name: "Rassie van der Dussen", position: "batsman", number: 17, isCaptain: false, nickname: "Rassie" },
            { name: "Marco Jansen", position: "all-rounder", number: 27, isCaptain: false, nickname: "N/A" },
            { name: "Kagiso Rabada", position: "bowler", number: 25, isCaptain: false, nickname: "KG" },
            { name: "Anrich Nortje", position: "bowler", number: 24, isCaptain: false, nickname: "N/A" },
            { name: "Keshav Maharaj", position: "bowler", number: 6, isCaptain: false, nickname: "Kesh" },
            { name: "Tabraiz Shamsi", position: "bowler", number: 99, isCaptain: false, nickname: "Shamo" },
            { name: "Gerald Coetzee", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Reeza Hendricks", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Lungi Ngidi", position: "bowler", number: 22, isCaptain: false, nickname: "N/A" },
            { name: "Tristan Stubbs", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" }
        ]
    },
    {
        team: "New Zealand",
        sport: "Cricket",
        year: 2024,
        isWorldCupWinner: false,
        headCoach: {
            coachName: "Rob Walter",
        },
        players: [
            { name: "Kane Williamson", position: "batsman", number: 22, isCaptain: true, nickname: "N/A" },
            { name: "Devon Conway", position: "wicketkeeper", number: 88, isCaptain: false, nickname: "N/A" },
            { name: "Tom Latham", position: "wicketkeeper", number: 48, isCaptain: false, nickname: "N/A" },
            { name: "Daryl Mitchell", position: "all-rounder", number: 77, isCaptain: false, nickname: "N/A" },
            { name: "Glenn Phillips", position: "all-rounder", number: 40, isCaptain: false, nickname: "N/A" },
            { name: "Rachin Ravindra", position: "all-rounder", number: 4, isCaptain: false, nickname: "N/A" },
            { name: "Mitchell Santner", position: "all-rounder", number: 74, isCaptain: false, nickname: "N/A" },
            { name: "Trent Boult", position: "bowler", number: 18, isCaptain: false, nickname: "N/A" },
            { name: "Tim Southee", position: "bowler", number: 23, isCaptain: false, nickname: "N/A" },
            { name: "Lockie Ferguson", position: "bowler", number: 69, isCaptain: false, nickname: "N/A" },
            { name: "Matt Henry", position: "bowler", number: 15, isCaptain: false, nickname: "N/A" },
            { name: "Ish Sodhi", position: "bowler", number: 13, isCaptain: false, nickname: "N/A" },
            { name: "Michael Bracewell", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Mark Chapman", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Will Young", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" }
        ]
    },
    {
        team: "Afghanistan",
        sport: "Cricket",
        year: 2024,
        isWorldCupWinner: false,
        headCoach: {
            coachName: "Jonathan Trott",
        },
        players: [
            { name: "Rashid Khan", position: "bowler", number: 19, isCaptain: true, nickname: "N/A" },
            { name: "Rahmanullah Gurbaz", position: "wicketkeeper", number: 21, isCaptain: false, nickname: "N/A" },
            { name: "Ibrahim Zadran", position: "batsman", number: 8, isCaptain: false, nickname: "N/A" },
            { name: "Najibullah Zadran", position: "batsman", number: 50, isCaptain: false, nickname: "N/A" },
            { name: "Mohammad Nabi", position: "all-rounder", number: 7, isCaptain: false, nickname: "N/A" },
            { name: "Gulbadin Naib", position: "all-rounder", number: 9, isCaptain: false, nickname: "N/A" },
            { name: "Azmatullah Omarzai", position: "all-rounder", number: 28, isCaptain: false, nickname: "N/A" },
            { name: "Karim Janat", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Mujeeb Ur Rahman", position: "bowler", number: 11, isCaptain: false, nickname: "N/A" },
            { name: "Noor Ahmad", position: "bowler", number: 15, isCaptain: false, nickname: "N/A" },
            { name: "Naveen-ul-Haq", position: "bowler", number: 98, isCaptain: false, nickname: "N/A" },
            { name: "Fazalhaq Farooqi", position: "bowler", number: 44, isCaptain: false, nickname: "N/A" },
            { name: "Fareed Ahmad Malik", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Nangyal Kharoti", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Mohammad Ishaq", position: "wicketkeeper", number: "N/A", isCaptain: false, nickname: "N/A" }
        ]
    },
    {
        team: "Bangladesh",
        sport: "Cricket",
        year: 2024,
        isWorldCupWinner: false,
        headCoach: {
            coachName: "Phil Simmons",
        },
        players: [
            { name: "Najmul Hossain Shanto", position: "batsman", number: 15, isCaptain: true, nickname: "N/A" },
            { name: "Taskin Ahmed", position: "bowler", number: 3, isCaptain: false, nickname: "N/A" },
            { name: "Litton Das", position: "wicketkeeper", number: 28, isCaptain: false, nickname: "N/A" },
            { name: "Shakib Al Hasan", position: "all-rounder", number: 75, isCaptain: false, nickname: "N/A" },
            { name: "Towhid Hridoy", position: "batsman", number: 2, isCaptain: false, nickname: "N/A" },
            { name: "Mahmudullah Riyad", position: "all-rounder", number: 30, isCaptain: false, nickname: "N/A" },
            { name: "Mustafizur Rahman", position: "bowler", number: 90, isCaptain: false, nickname: "Fizz" },
            { name: "Shoriful Islam", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Tanzid Hasan Tamim", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Soumya Sarkar", position: "all-rounder", number: 59, isCaptain: false, nickname: "N/A" },
            { name: "Jaker Ali Anik", position: "wicketkeeper", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Tanvir Islam", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Shak Mahedi Hasan", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Rishad Hossain", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Tanzim Hasan Sakib", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" }
        ]
    },
    {
        team: "Netherlands",
        sport: "Cricket",
        year: 2024,
        isWorldCupWinner: false,
        headCoach: {
            coachName: "Ryan Cook",
        },
        players: [
            { name: "Scott Edwards", position: "wicketkeeper", number: 4, isCaptain: true, nickname: "N/A" },
            { name: "Max O'Dowd", position: "batsman", number: 10, isCaptain: false, nickname: "N/A" },
            { name: "Michael Levitt", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Teja Nidamanuru", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Bas de Leede", position: "all-rounder", number: 1, isCaptain: false, nickname: "N/A" },
            { name: "Logan van Beek", position: "all-rounder", number: 9, isCaptain: false, nickname: "N/A" },
            { name: "Sybrand Engelbrecht", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Wesley Barresi", position: "wicketkeeper", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Aryan Dutt", position: "bowler", number: 18, isCaptain: false, nickname: "N/A" },
            { name: "Paul van Meekeren", position: "bowler", number: 22, isCaptain: false, nickname: "N/A" },
            { name: "Vivian Kingma", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Saqib Zulfiqar", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Tim Pringle", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Vikramjit Singh", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Kyle Klein", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" }
        ]
    },
    {
        team: "Pakistan",
        sport: "Cricket",
        year: 2024,
        isWorldCupWinner: false,
        headCoach: {
            coachName: "Mike Hesson", // White-ball coach
        },
        players: [
            { name: "Babar Azam", position: "batsman", number: 56, isCaptain: true, nickname: "Bobby" },
            { name: "Mohammad Rizwan", position: "wicketkeeper", number: 16, isCaptain: false, nickname: "N/A" },
            { name: "Shaheen Afridi", position: "bowler", number: 10, isCaptain: false, nickname: "N/A" },
            { name: "Fakhar Zaman", position: "batsman", number: 39, isCaptain: false, nickname: "N/A" },
            { name: "Shadab Khan", position: "all-rounder", number: 7, isCaptain: false, nickname: "N/A" },
            { name: "Haris Rauf", position: "bowler", number: 150, isCaptain: false, nickname: "N/A" },
            { name: "Naseem Shah", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Iftikhar Ahmed", position: "all-rounder", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Imad Wasim", position: "all-rounder", number: 5, isCaptain: false, nickname: "N/A" },
            { name: "Saim Ayub", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Azam Khan", position: "wicketkeeper", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Usman Khan", position: "batsman", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Abbas Afridi", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Abrar Ahmed", position: "bowler", number: "N/A", isCaptain: false, nickname: "N/A" },
            { name: "Mohammad Amir", position: "bowler", number: 5, isCaptain: false, nickname: "N/A" }
        ]
    }
];

// Initially set the current team to India
let currentTeam = allCricketTeams[0]; // Start with India
let currentFilter = "all";   // Stores the current active filter.

// Freeze the team data to prevent accidental modifications
allCricketTeams.forEach(team => Object.freeze(team));
allCricketTeams.forEach(team => team.players.forEach(player => Object.freeze(player)));

// Function to render team information and player cards
const renderTeamData = (teamObject) => {
    const { sport, team, year, headCoach, players } = teamObject;
    const { coachName } = headCoach;

    // Display team's information on the screen.
    typeOfSportElement.textContent = sport;
    // teamNameElement.textContent = team;
    worldCupYearElement.textContent = year;
    headCoachElement.textContent = coachName;

    // Clear previous player cards
    playerCardsContainer.innerHTML = "";

    applyFilterAndRenderPlayers(currentFilter);

}

// Function to set player cards (now takes an array of players)
const setPlayerCards = (arr = currentTeam.players) => {
    playerCardsContainer.innerHTML += arr.map(({ name, position, number, isCaptain, nickname }) => {
        return `
        <div class="player-card">
        <h2>${name}${isCaptain ? " (Captain) " : ""}</h2>
        <p>Position: <span class="position-${position}">${position}</span></p>
        <p>Number: ${number}</p>
        <p>Nickname: ${nickname !== "N/A" ? nickname : "N/A"}</p>
        </div>
    `;
    }).join("");
};

// Function to filter and render players based on the current filter.
const applyFilterAndRenderPlayers = (filterValue) => {
    let filteredPlayers = currentTeam.players;   // Start with all players of the current team
    switch (filterValue) {
        case "nickname":
            filteredPlayers = currentTeam.players.filter((player) => player.nickname !== "N/A");
            break;
        case "batsman":
            filteredPlayers = currentTeam.players.filter((player) => player.position === "batsman");
            break;
        case "bowler":
            filteredPlayers = currentTeam.players.filter((player) => player.position === "bowler");
            break;
        case "wicketkeeper":
            filteredPlayers = currentTeam.players.filter((player) => player.position === "wicketkeeper");
            break;
        case "all-rounder":
            filteredPlayers = currentTeam.players.filter((player) => player.position === "all-rounder");
            break;
        case "all":
        default:
            // No filtering needed, use all players
            break;
    }

    playerCardsContainer.innerHTML = "";   // Clear existing cards before rendering.
    setPlayerCards(filteredPlayers);
};


// Event listener for player filter dropdown
playersDropdownList.addEventListener("change", (e) => {
    currentFilter = e.target.value;   // Update the current filter
    applyFilterAndRenderPlayers(currentFilter);
});

// Event listener for team selection dropdown
teamSelectDropdown.addEventListener("change", (e) => {
    const selectedTeamName = e.target.value;
    currentTeam = allCricketTeams.find(team => team.team === selectedTeamName);
    if (currentTeam) {
        renderTeamData(currentTeam);
    }
});

// Theme Toggle Logic
const toggleTheme = () => {
    const isDarkTheme = document.body.classList.toggle("dark-theme");
    localStorage.setItem("theme", isDarkTheme ? "dark" : "light");
    themeToggle.querySelector("i").className = isDarkTheme ? "fa-solid fa-sun" : "fa-solid fa-moon";
};

themeToggle.addEventListener("click", toggleTheme);

// Initialize theme and display initial team data on page load
(() => {
    const savedTheme = localStorage.getItem("theme");
    const systemPrefersDark = window.matchMedia("(prefers-color-scheme: dark)").matches;
    const isDarkTheme = savedTheme === "dark" || (!savedTheme && systemPrefersDark);
    document.body.classList.toggle("dark-theme", isDarkTheme);
    themeToggle.querySelector("i").className = isDarkTheme ? "fa-solid fa-sun" : "fa-solid fa-moon";

    // Render the initial team (India) when the page loads
    renderTeamData(currentTeam);
})();
