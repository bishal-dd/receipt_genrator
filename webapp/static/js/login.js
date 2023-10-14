$(document).ready(function() {
    // START LOGIN POPUP WINDOW
     $("#googleLink").on("click", function (event) {

        event.preventDefault();  // Prevent the default link behavior

        // URL to open in the popup
        var url = $(this).attr("href");

        // Define the dimensions of the popup window
        var width = 400;
        var height = 400;

        // Calculate the position of the popup in the center of the screen
        var left = (window.innerWidth - width) / 2;
        var top = (window.innerHeight - height) / 2;

        // Open the popup window
        window.open(url, 'Popup', 'width=' + width + ',height=' + height + ',left=' + left + ',top=' + top);

        // If the login is successful, close the window
    if (loginSuccessful) {
        window.close();
    }
    });


    // END LOGIN POPUP WINDOW
});