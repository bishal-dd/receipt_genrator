$(document).ready(function() {
   // Try showing the modal directly
   function getCurrentDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = (today.getMonth() + 1).toString().padStart(2, "0");
    const day = today.getDate().toString().padStart(2, "0");
    return `${year}-${month}-${day}`;
  }

  function validate() {
        if ($('#recipient_phone').val() === '') {
              // Display the Bootstrap modal using jQuery
              $('#validationModal').modal('show');
              $('#validationErrorMessage').text('Phone number cannot be empty.');
              return false;
            }
        else if($('#recipient_name').val() === ''){
          // Display the Bootstrap modal using jQuery
          $('#validationModal').modal('show');
          $('#validationErrorMessage').text('Name cannot be empty.');
          return false;
        }
        else if($('#amount').val() === ''){
          // Display the Bootstrap modal using jQuery
          $('#validationModal').modal('show');
          $('#validationErrorMessage').text('Name cannot be empty.');
          return false;
        }
        else{
            return true;
        }
  }
     $("#generate_pdf").on("click", function (e) {
        e.preventDefault(); // Prevent the default form submission

         if(validate()){
             $("#data_form").submit();
            $("#data_form")[0].reset();
            $("#dateInput").val(getCurrentDate());
            $("#totalAmount, #totalAmountpaid").text("");
         }

     })

      $("#save_data").on("click", function (e) {
        e.preventDefault(); // Prevent the default form submission
        var formData = $("form").serialize();
         if(validate()){
                $.ajax({
                type: "POST",
                url: "/save_receipt/", // Replace with your actual URL
                data: formData,
                success: function(response) {
                    $('#successModal').modal('show');
                    $('#validationSuccessMessage').text('Your data was saved');
                    $("#data_form")[0].reset();
                    $("#dateInput").val(getCurrentDate());
                    $("#totalAmount, #totalAmountpaid").text("");
                },
                error: function(error) {
                  // Handle any errors that occur during the AJAX request
                  alert("Error while saving data: " + error.responseText);
                }
            });
         }

     })

});