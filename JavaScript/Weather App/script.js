const apiKey = "7e060b2a9f3c2571fc87821fc1727213";
const apiUrl = "https://api.openweathermap.org/data/2.5/weather?units=metric&q=";

const searchBox = document.querySelector(".search input");
const searchBtn = document.querySelector(".search button");
const weatherIcon = document.querySelector(".weather-icon");

// 'async' keyword makes this funtion return an Promise automatically.
async function checkWeather(city) {
    const response = await fetch(apiUrl + city + `&appid=${apiKey}`);
    
    if(response.status == 404) {
        document.querySelector(".error").style.display = "block";
        document.querySelector(".weather").style.display = "none";
    } else {
        var data = await response.json();   // 'data' variable store weather information for particular city.

        // update the city, temperature, humidity and wind value by api.
        document.querySelector(".city").innerHTML = data.name;   
        document.querySelector(".temp").innerHTML = Math.round(data.main.temp) + "°C";
        document.querySelector(".humidity").innerHTML = data.main.humidity + "%";
        document.querySelector(".wind").innerHTML = data.wind.speed + "km/h";

        // Update the images according to the weather condition.
        const weatherConditions = ["Clouds", "Clear", "Rain", "Drizzle", "Mist", "Snow", "Thunderstorm", "Fog"];
        if(weatherConditions.includes(data.weather[0].main)) {    // method checks if an array contains a specific element and returns true or false.
            weatherIcon.src = `images/${data.weather[0].main}.png`;
        } else {
            weatherIcon.src = "images/default.png";
        }

        document.querySelector(".weather").style.display = "block";
        document.querySelector(".error").style.display = "none";
    }
}
searchBtn.addEventListener("click", () => {
    checkWeather(searchBox.value);
})
