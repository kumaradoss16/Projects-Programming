📧 Simple Spam Filter
=====================

A client-side web application built with HTML, CSS, and JavaScript that attempts to identify spam messages using a set of predefined regular expressions. It includes advanced pattern matching for common spammer obfuscation techniques.

✨ Features
----------

*   **Spam Detection:** Analyzes user-entered messages against a comprehensive list of spam-related keywords and patterns.
    
*   **Flexible Regex Matching:** Uses a custom function (createFlexibleRegex) to generate robust regular expressions that account for common spammer tricks like:
    
    *   Character substitutions (e.g., e for 3, s for 5, a for @).
        
    *   Interspersed non-alphanumeric characters (e.g., f.r.e.e money).
        
*   **Advanced Pattern Recognition:** Includes regexes for:
    
    *   Various financial and scam-related terms.
        
    *   Numeric patterns for currency amounts (e.g., $1000, £500).
        
    *   Excessive capitalization (e.g., FREE MONEY).
        
    *   Suspicious URL patterns (e.g., common URL shorteners, long obfuscated paths).
        
    *   Excessive punctuation (e.g., !!!, $$$).
        
*   **Real-time Feedback:** Instantly informs the user whether a message is likely spam or not.
    
*   **User-Friendly Interface:** A simple and clean design for easy message input and result display.
    
*   **Responsive Design:** Adapts to different screen sizes for a consistent user experience.
    

🚀 Technologies Used
--------------------

*   **HTML5:** Provides the semantic structure of the web application.
    
*   **CSS3:** Styles the application, defining its layout, colors, typography, and responsive behavior. It uses CSS variables for theme management.
    
*   **JavaScript (ES6+):** Implements the core spam detection logic, including the regular expression engine, string manipulation, and dynamic UI updates.
    

📁 Project Structure
--------------------

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   .  ├── index.html  ├── style.css  └── script.js   `

*   index.html: The main HTML file that structures the Spam Filter, including the header, message input area (textarea), check button, and the result display paragraph.
    
*   style.css: Contains all the CSS rules for styling the application. This includes global variables for color themes, responsive adjustments, and specific styles for the input, button, and result display.
    
*   script.js: Implements the core JavaScript logic. This file defines the createFlexibleRegex helper, the comprehensive denyList of spam patterns, the isSpam function for message analysis, and event listeners for user interaction.
    

⚙️ Setup and Installation
-------------------------

To run this project locally, follow these simple steps:

1.  git clone https://github.com/YOUR\_USERNAME/YOUR\_REPO\_NAME.gitcd YOUR\_REPO\_NAME_(Replace YOUR\_USERNAME and YOUR\_REPO\_NAME with your actual GitHub username and repository name.)_
    
2.  **Open in Browser:**
    
    *   Simply open the index.html file in your preferred web browser. No server setup is required as it's a client-side application.
        

💡 Usage
--------

1.  **Enter a Message:** Type or paste any phrase or message into the large text area.
    
2.  **Check Message:** Click the "Check message" button.
    
3.  **View Result:** The application will immediately display whether the message looks like spam or not below the button. The result text will be colored red for spam and green for non-spam.