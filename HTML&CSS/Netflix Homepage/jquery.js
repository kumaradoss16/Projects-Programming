$(document).ready(function() {
    // Loop through all questions (assuming they have ids ques1, ques2, etc.)
    for (let i = 1; i <= 6; i++) {
        $(`#ques${i}`).click(function() {
            // Slide toggle the corresponding answer with class .a1, .a2, etc.
            $(`.a${i}`).slideToggle(100, function() {
                // Apply CSS changes after sliding
                $(this).css({
                    "padding": "30px 30px",
                    "max-height": "600px"
                });
            });

            // Toggle a 'rotated' class to the SVG icon for rotation
            $(this).find(".size-6").toggleClass("rotated");
        });
    }

    $(".s1, .s3").dblclick(function(){
        alert("Video can't be play.");
    });

    $(".theme-toggle").click(function() {
        $("body").toggleClass("dark-theme light-theme"); // Toggle between light and dark classes
        
        // Update SVG fill based on current theme
        if ($("body").hasClass("dark-theme")) {
            $(this).find("svg").css("fill", "#ffffff"); 
            $("input").css({
                "background-color": "transparent", 
                "color": "#ffffff"
            });

            $(".down").css({
                "color": "white" // Change text color for dark theme
            });

            $(".select1").css({
                "color": "black" // Change text color for dark theme
            });

            $(".svg").css({
                "fill": "white" // Change text color for dark theme
            });
        } else {
            $(this).find("svg").css("fill", "#000000"); // Dark color for light theme
            $("input").css({
                "background-color": "#ffffff", 
                "color": "#000000"
            });

            $(".down").css({
                "color": "white" // Change text color for dark theme
            });

            $(".select1").css({
                "color": "black" // Change text color for dark theme
            });
        }
    });

    // Input focus and blur event handling
    $("input").focus(function() {
        if ($("body").hasClass("dark-theme")) {
            $(this).css({
                "padding-top": "19px",
                "padding-bottom": "11px",

                "background-color": "black" // Dark background for dark theme
            });
           
        } else {
            $(this).css({
                "padding-top": "19px",
                "padding-bottom": "11px",
                "background-color": "white" // Light background for light theme
            });
            $(".down").css({
                "color": "#000000" // Change text color for light theme
            });

        }
    }).blur(function() {
        if ($("body").hasClass("dark-theme")) {
            $(this).css({
                "background-color": "#ffffff",
            });
            $(".down").css({
                "color": "#ffffff" // Keep text color white for dark theme
            });
        } else {
            $(this).css({
                "background-color": "transparent" // Reset to white background for light theme
            });
            $(".down").css({
                "color": "#ffffff" // Reset text color to black for light theme
            });
        }
    });
});
    
    
