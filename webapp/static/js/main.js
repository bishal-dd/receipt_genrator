$(document).ready(function() {

    // START SET CURRENT DATE
        // Get the current date in the "YYYY-MM-DD" format
        function getCurrentDate() {
          const today = new Date();
          const year = today.getFullYear();
          const month = (today.getMonth() + 1).toString().padStart(2, '0');
          const day = today.getDate().toString().padStart(2, '0');
          return `${year}-${month}-${day}`;
        }

        // Set the default value of the date input field to today's date
        $("#dateInput").val(getCurrentDate());

    // END SET CURRENT DATE

    // START PAYMENT MODE
         // Listen for changes in the select element
        $("#paymentMode").on("change", function() {
            var selectedOption = $(this).val(); // Get the selected option's value

            // Check if "Bank Transfer" is selected
            if (selectedOption === "Bank Transfer") {
                $("#journalNumber").show(); // Show the "Journal Number" input field
            } else {
                $("#journalNumber").hide(); // Hide the "Journal Number" input field for other options
            }
        });

    // END PAYMENT MODE

    // START CALCULATE AMOUNT
       $("#rate, #quantity").on("input", function() {
            var rate = parseFloat($("#rate").val());
            var quantity = parseFloat($("#quantity").val());
            var calculatedAmount = rate * quantity;

             if(isNaN(calculatedAmount))
                {
                    calculatedAmount = rate;
                }
            // Set the content of the #amount element
            $("#amount").text(calculatedAmount);
        });

    // END CALCULATE AMOUNT

    // START ADD COL


   $("#addRowButton").click(function() {
            event.preventDefault(); // Prevent the default behavior

            // Clone the first row
            var newRow = $(".data-row:first").clone();

            // Clear input values in the cloned row
            newRow.find(".rate-input, .quantity-input").val('');
            newRow.find(".amount-text").text('0');


            // Append the cloned row to the table
            $(".data-row:last").after(newRow);
        });

        // Calculate amounts when rate and quantity change
        $("tbody").on("input", ".rate-input, .quantity-input", function() {
            var row = $(this).closest("tr");
            var rate = parseFloat(row.find(".rate-input").val());
            var quantity = parseFloat(row.find(".quantity-input").val());
            var amount = isNaN(rate) || isNaN(quantity) ? '' : rate * quantity;
            row.find(".amount-text").text(amount);


             // Calculate the total amount
            var totalAmount = 0;
            $(".amount-text").each(function() {
                var rowAmount = parseFloat($(this).text());
                if (!isNaN(rowAmount)) {
                    totalAmount += rowAmount;
                }
            });

            // Update the Total Amount cell
            $("#totalAmount, #totalAmountpaid").text("Nu. " + totalAmount.toFixed(2)); // Format the total amount

        });

    // END ADD COL

    // START IMAGE UPLOAD
            $("#logo_upload").change(function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    $("#uploaded_logo").attr("src", e.target.result);
                    $("#uploaded_logo").show();
                    $("#uploaded_logo").css("display", "inline-block"); // Remove 'display: none;'
                    $(".logo_upload_label").hide();
                };
                reader.readAsDataURL(file);
            }
        });

        $("#signature_upload").change(function() {
            const file = this.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    $("#uploaded_signature").attr("src", e.target.result);
                    $("#uploaded_signature").show();
                    $("#uploaded_signature").css("display", "inline-block"); // Remove 'display: none;'
                    $(".signature_upload_label").hide();
                };
                reader.readAsDataURL(file);
            }
        });
    // END IMAGE UPLOAD
});