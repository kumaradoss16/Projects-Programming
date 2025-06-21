const playlistSongs = document.getElementById("playlist-songs");
const playButton = document.getElementById("play");
const pauseButton = document.getElementById("pause");
const nextButton = document.getElementById("next");
const previousButton = document.getElementById("previous");
const shuffleButton = document.getElementById("shuffle");

// Create an array to store all the songs
const allSongs = [
    {
        id: 0,
        title: "Sunny Bliss",
        artist: "Top flow",
        duration: "1:35",
        src: "Songs/sunny-bliss.mp3"
    },
    {
        id: 1,
        title: "Future Design",
        artist: "penguinmusic",
        duration: "1:14",
        src: "Songs/future-design.mp3"
    },
    {
        id: 2,
        title: "Alone",
        artist: "BoDleasons",
        duration: "1:32",
        src: "Songs/alone.mp3"
    },
    {
        id: 3,
        title: "Spring Energy",
        artist: "Grand_project",
        duration: "2:38",
        src: "Songs/spring-energy.mp3"
    },
    {
        id: 4,
        title: "Clover Feast",
        artist: "Top-Flow",
        duration: "1:25",
        src: "Songs/clover-feast.mp3"
    },
    {
        id: 5,
        title: "Spinning Head",
        artist: "Gvidon",
        duration: "2:03",
        src: "Songs/spinning-head.mp3"
    },
    {
        id: 6,
        title: "Don't Talk",
        artist: "Cosmonkey",
        duration: "1:50",
        src: "Songs/dont-talk.mp3"
    },
    {
        id: 7,
        title: "Risk",
        artist: "StudioKolomna",
        duration: "1:12",
        src: "Songs/risk.mp3"
    },
    {
        id: 8,
        title: "AMALGAM",
        artist: "Rockot",
        duration: "4:14",
        src: "Songs/amalgam.mp3"
    },
    {
        id: 9,
        title: "Titanium",
        artist: "ALiliabeats",
        duration: "1:46",
        src: "Songs/titanium.mp3"
    },
    {
        id: 10,
        title: "Sport Trailes Beat",
        artist: "Audiogreen",
        duration: "1:45",
        src: "Songs/sport-trailer-beat.mp3"
    },
    {
        id: 11,
        title: "Hard Work",
        artist: "Lite Saturation",
        duration: "1:21",
        src: "Songs/hard-work.mp3"
    },
    {
        id: 12,
        title: "Hard to Break",
        artist: "MusicLFiles",
        duration: "2:07",
        src: "Songs/hard-to-break.mp3"
    },
    {
        id: 13,
        title: "Fires and Energy",
        artist: "lemonmusicstudio",
        duration: "2:57",
        src: "Songs/fire-and-energy.mp3"
    },
    {
        id: 14,
        title: "Discipline",
        artist: "OctoSound",
        duration: "1:36",
        src: "Songs/discipline.mp3"
    },
    {
        id: 15,
        title: "Gamebackground",
        artist: "jumingbunning",
        duration: "4:00",
        src: "Songs/game-background.mp3"
    },
    {
        id: 16,
        title: "Stranger Things",
        artist: "Music_Unlimited",
        duration: "2:36",
        src: "Songs/stranger-things-.mp3"
    },
    {
        id: 17,
        title: "Tower Defense",
        artist: "nickpanck620",
        duration: "3:52",
        src: "Songs/tower-defense.mp3"
    },
    {
        id: 18,
        title: "Best Game Console",
        artist: "DJARTMUSIC",
        duration: "1:26",
        src: "Songs/best-game-console.mp3"
    }
];

// Web Audio API
const audio = new Audio();
let userData = {  // Object used to track of the songs, the current song playing, and the time of the current song to store this information.
    songs: [...allSongs],    // This property used if the users will be able to shuffle and delete songs from the playlist, it will help to create a copy of the 'allSongs' array without mutating the original by spread operator[...].
    currentSong: null,  // This property used to store the current song information.
    songCurrentTime: 0,  // This property track its current song playback time.
}; 

// playSong Function implementing the functionality for playing the displayed songs.
const playSong = (id) =>{
    const song = userData?.songs.find((song) => song.id === id);
    audio.src = song.src;   // audio element where to find the audio data for the selected song.
    audio.title = song.title;   // audio element what to display as the title of the song.
    // Check if no current song is playing or if the current song is different form the one that is baout to be played.
    if (userData?.currentSong === null || userData?.currentSong.id !== song.id) {
        audio.currentTime = 0;
    } else {
        // allow to resume the current song at the point where it was paused.
        audio.currentTime = userData?.songCurrentTime;
    }
    userData.currentSong = song;
    playButton.classList.add("playing");
    highlightCurrentSong();
    setPlayerDisplay();
    setPlayButtonAccessibleText();
    audio.play();
    
}

// pauseSong() arrow function used to pausing the currently playing song.
const pauseSong = () => {
    userData.songCurrentTime = audio.currentTime;  // To store the current time of the song when it is paused.
    playButton.classList.remove("playing");   // remove the 'playing' class from the 'playButton'.
    audio.pause();   // Pause the song by using pause() method.
};

// playNextSong() arrow function used to playing the next song.
const playNextSong = () => {
    if (userData?.currentSong === null) {   // check if there's no current song playing in the 'userData' object.
    playSong(userData?.songs[0].id);
    } else {
        const currentSongIndex = getCurrentSongIndex();
        const nextSong = userData?.songs[currentSongIndex + 1];   // Used to retrieve the next song in the playlist.
        playSong(nextSong.id);   // call the playSong() function to play a next song.
    }
};

// playPreviousSong() arrow function used to play the previous song.
const playPreviousSong = () => {
    if (userData?.currentSong === null) {   // check if there's no current song playing in the 'userData' object its exit the function.
        return;
    } else {
        const currentSongIndex = getCurrentSongIndex();
        const previousSong = userData?.songs[currentSongIndex - 1];
        playSong(previousSong.id);
    }
};

// shuffle arrow function is reponsible for shuffling the songs in the playlist.
const shuffle = () => {
    userData?.songs.sort(() => Math.random() - 0.5);
    // when the shuffle button is pressed, to set the current song and time to nothing. 
    userData.currentSong = null;
    userData.songCurrentTime = 0;
    renderSongs(userData?.songs);
    pauseSong();
    setPlayerDisplay();
    setPlayButtonAccessibleText();
};

// deleteSong arrow function used to delete the song you want.
const deleteSong = (id) => {
    // filter() method to remove the sond object that matches the id parameter form the 'userData?.songs' array
    userData.songs = userData?.songs.filter((song) => song.id !== id);
    renderSongs(userData?.songs);
    highlightCurrentSong();
    setPlayButtonAccessibleText();
    // Before delete the song check if the song is currently playing.
    if (userData?.currentSong?.id === id) {
        userData.currentSong = null;
        userData.songCurrentTime = 0;
        pauseSong();
        setPlayerDisplay();
    }
};

// setPlayerDisplay() arrow function used to display the current song title and artist in the player display.
const setPlayerDisplay = () => {
    const playingSong = document.getElementById("player-song-title");
    const songArtist = document.getElementById("player-song-artist");
    const currentTitle = userData?.currentSong?.title;
    const currentArtist = userData?.currentSong?.artist; 
    playingSong.textContent = currentTitle ? currentTitle : "";
    songArtist.textContent = currentArtist ? currentArtist : "";
};

// highlightCurrentSong arrow function to create a highlight any song that is being played.
const highlightCurrentSong = () => {
    const playlistSongElements = document.querySelectorAll('.playlist-song');   // indicate the highlight to the 'li' element (song playing in the playlist).
    const songToHighlight = document.getElementById(`song-${userData?.currentSong?.id}`);   // get the id of the currently playing song.
    playlistSongElements.forEach((songEl) => {
        songEl.removeAttribute('aria-current'); 
    });
    // To add the attribute back to the currently playing song.
    if (songToHighlight) {
        songToHighlight.setAttribute("aria-current", "true");
    }
};

// Arrow Function used to display the songs in the UI (User Inteface)
const renderSongs = (array) => {
    const songsHTML = array.map((song) => {  // This Variable show the title, artist, duration of each song and a delete button by map() method to add new HTML for each song.
        return `<li id="song-${song.id}" class="playlist-song">
                    <button class="playlist-song-info" onclick="playSong(${song.id})">
                        <span class="playlist-song-title">${song.title}</span>
                        <span class="playlist-song-artist">${song.artist}</span>
                        <span class="playlist-song-duration">${song.duration}</span>
                    </button>
                    <button class="playlist-song-delete" onclick="deleteSong(${song.id})" aria-label="Delete ${song.title}">
                        <svg width="20" height="20" viewBox="0 0 16 16" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="8" cy="8" r="8" fill="#4d4d62"/><path fill-rule="evenodd" clip-rule="evenodd" d="M5.32587 5.18571C5.7107 4.90301 6.28333 4.94814 6.60485 5.28651L8 6.75478L9.39515 5.28651C9.71667 4.94814 10.2893 4.90301 10.6741 5.18571C11.059 5.4684 11.1103 5.97188 10.7888 6.31026L9.1832 7.99999L10.7888 9.68974C11.1103 10.0281 11.059 10.5316 10.6741 10.8143C10.2893 11.097 9.71667 11.0519 9.39515 10.7135L8 9.24521L6.60485 10.7135C6.28333 11.0519 5.7107 11.097 5.32587 10.8143C4.94102 10.5316 4.88969 10.0281 5.21121 9.68974L6.8168 7.99999L5.21122 6.31026C4.8897 5.97188 4.94102 5.4684 5.32587 5.18571Z" fill="white"/></svg>
                    </button>
                </li>`;
    }).join("");  // join() method is used to concatenate all the elements of an array into a single string.
    // To update the playlist in your HTML document to display the songs
    playlistSongs.innerHTML = songsHTML;   // This will insert the 'li' element you just create into the 'ul' element in the already provided HTML file.
    // if the playlist is empty to reset the userData object to its original state.
    if (userData?.songs.length === 0) {
        const resetButton = document.createElement("button");  // if the playlist is empty, to create a reset button element.
        const resetText = document.createTextNode("Reset Playlist");
        resetButton.id = "reset";
        resetButton.ariaLabel = "Reset playlist";
        resetButton.appendChild(resetText);
        playlistSongs.appendChild(resetButton);
        resetButton.addEventListener("click", () => {
            userData.songs = [...allSongs];
            renderSongs(sortSongs());
            setPlayButtonAccessibleText();
            resetButton.remove();
        });
    }
};

const setPlayButtonAccessibleText = () => {
    const song = userData?.currentSong || userData?.songs[0];
    playButton.setAttribute("aria-label", song?.title ? `Play ${song.title}` : "Play");
};

const getCurrentSongIndex = () => {
    return userData?.songs.indexOf(userData?.currentSong);
};

playButton.addEventListener("click", () => {
    if (userData?.currentSong == null) {
        playSong(userData?.songs[0].id);   // ensure the first song in the playlist is played first.
    } else {
        playSong(userData?.currentSong.id);
    }
});

pauseButton.addEventListener("click", pauseSong);
nextButton.addEventListener("click", playNextSong);
previousButton.addEventListener("click", playPreviousSong);
shuffleButton.addEventListener("click", shuffle);
audio.addEventListener("ended", () => {
    const currentSongIndex = getCurrentSongIndex();
    // check if there is a next song to play.
    const nextSongExists = userData.songs[currentSongIndex + 1] !== undefined;
    if (nextSongExists) {
    playNextSong();   // If played the next song is exists or otherwise doesn't. 
    } else {
        userData.currentSong = null;
        userData.songCurrentTime = 0;
        pauseSong();
        setPlayerDisplay();
        highlightCurrentSong();
        setPlayButtonAccessibleText();
    } 
});

// Arrow function used to display the list of songs on the screen.
const sortSongs = () => {
    // Sort the songs title by alphabetically 
    userData?.songs.sort((a, b) => {
        if (a.title < b.title) {
            return -1;     // a.title comes before b.title
        } if (a.title > b.title) {
            return 1;   // a.title comes after b.title
        }
        return 0;   // Leave the order
    });
    return userData?.songs;   
};

// Finally display the songs in the UI. (?. helps prevent errors when acessing nested properties that might be null or undefined)
renderSongs(sortSongs());   