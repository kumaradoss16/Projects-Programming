🖼️ AI Image Generator
======================

A modern and responsive web application that allows users to generate images from text prompts using various AI models. It features a clean interface, theme toggling, and dynamic image generation with aspect ratio and count controls.

✨ Features
----------

*   **Text-to-Image Generation:** Input a descriptive text prompt to generate unique images.
    
*   **Multiple AI Models:** Choose from a selection of popular AI image generation models (e.g., FLUX.1-dev, Stable Diffusion XL, Openjourney, Kandinsky 2.2, Segmind Stable Diffusion 1B).
    
*   **Image Count Control:** Generate up to 4 images at once from a single prompt.
    
*   **Aspect Ratio Selection:** Choose the desired aspect ratio for your generated images (Square, Landscape, Portrait).
    
*   **Random Prompt Suggestion:** A "dice" button provides random example prompts to inspire creativity.
    
*   **Dynamic Loading States:** Displays loading spinners and error messages during image generation.
    
*   **Image Download:** Easily download generated images.
    
*   **Theme Toggle:** Switch between a light and dark theme for a personalized viewing experience.
    
*   **Responsive Design:** Optimized for seamless use across desktop and mobile devices.
    

🚀 Technologies Used
--------------------

*   **HTML5:** Provides the semantic structure of the web application.
    
*   **CSS3:** Styles the application, including responsive design, custom dropdowns, loading animations, and theme management using CSS variables.
    
*   **JavaScript (ES6+):** Handles all interactive logic, including form submission, API calls to Hugging Face, dynamic image rendering, and theme toggling.
    
*   **Hugging Face Inference API:** The backend service used for AI image generation.
    
*   **Font Awesome:** For various icons used throughout the interface.
    

📁 Project Structure
--------------------
*   index.html: The main HTML file that structures the AI Image Generator, including the header, prompt input area, model/count/ratio selectors, and the image gallery grid.
    
*   style.css: Contains all the CSS rules for styling the application. This includes global variables for theming, responsive adjustments, custom styles for inputs and buttons, and animations for loading states and hover effects.
    
*   script.js: Implements the core JavaScript logic. This includes handling user input, making asynchronous requests to the Hugging Face API, processing generated image data, dynamically updating the UI with images, and managing theme preferences via local storage.
    

⚙️ Setup and Installation
-------------------------

To run this project locally, follow these steps:

1.  git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
2.  cd YOUR_REPO_NAME (Replace YOUR_USERNAME and YOUR_REPO_NAME with your actual GitHub username and repository name.)
    
3.  **Get a Hugging Face API Key:**
    
    *   Go to Hugging Face Website: https://huggingface.co/settings/tokens
        
    *   Sign up or log in.
        
    *   Generate a new access token (ensure it has "read" permissions, or "write" if you plan to use models that require it, though "read" is usually sufficient for inference).
        
    *   **Important:** Keep your API key secure and do not expose it publicly in client-side code if deploying to production without a proxy. For local development, it's fine.
        

💡 Usage
--------

1.  **Enter a Prompt:** Type a detailed description of the image you want to generate in the text area. You can also click the "dice" icon to get a random example prompt.
    
2.  **Select Options:** Choose your preferred AI model, the number of images you want to generate, and the desired aspect ratio from the dropdowns.
    
3.  **Generate Image:** Click the "Generate" button. Placeholder loading cards will appear, and once the images are ready, they will replace the loading spinners.
    
4.  **Download Image:** Hover over a generated image and click the download icon to save it to your device.
    
5.  **Toggle Theme:** Use the moon/sun icon in the header to switch between light and dark themes.
