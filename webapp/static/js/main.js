$(document).ready(function () {
  // START CANVAS
  const canvas = $("#signatureCanvas")[0];
  const context = canvas.getContext("2d");
  let drawing = false;

  $("#signatureCanvas").mousedown(function () {
    drawing = true;
  });

  $("#signatureCanvas").mousemove(function (event) {
    if (!drawing) return;

    context.lineWidth = 2;
    context.strokeStyle = "black";
    context.lineCap = "round";

    context.lineTo(
      event.clientX - canvas.getBoundingClientRect().left,
      event.clientY - canvas.getBoundingClientRect().top
    );
    context.stroke();
    context.beginPath();
    context.moveTo(
      event.clientX - canvas.getBoundingClientRect().left,
      event.clientY - canvas.getBoundingClientRect().top
    );
  });

  $("#signatureCanvas").mouseup(function () {
    drawing = false;
    context.beginPath();
  });

  $("#clearButton").click(function (e) {
    e.preventDefault();
    e.stopPropagation(); // Stop event propagation to prevent further default behavior
    context.clearRect(0, 0, canvas.width, canvas.height);
  });

  $("#clear_button_outside").click(function (e) {
    e.preventDefault();
    $("#signatureImage").attr("src", ""); // Set the src attribute to an empty string
    $("#signatureImageEdit").attr("src", ""); // Set the src attribute to an empty string
    $("#SignImage").val("");
    $("#clear_button_outside").hide(); // Hide the element
    context.clearRect(0, 0, canvas.width, canvas.height);
    $(".signature_upload_label").show();
  });

  // Function to check if the canvas is blank
  function isCanvasBlank(canvas) {
    const context = canvas.getContext("2d");
    const pixelData = context.getImageData(
      0,
      0,
      canvas.width,
      canvas.height
    ).data;
    for (let i = 0; i < pixelData.length; i++) {
      if (pixelData[i] !== 0) {
        return false; // The canvas is not blank
      }
    }
    return true; // The canvas is blank
  }

  // Function to save the signature as an image
  $("#saveButton").on("click", function (e) {
    e.preventDefault();
    if (isCanvasBlank(canvas)) {
      $("#signatureImage").attr("src", ""); // Set the src attribute to an empty string
    } else {
      const canvas = document.getElementById("signatureCanvas");
      const signatureImage = canvas.toDataURL("image/png");
      // Update the src attribute of the existing signatureImage element
      $("#signatureImage").css("display", "inline-block"); // Remove 'display: none;'
      $("#signatureImage").attr("src", signatureImage);
      $("#signatureImageEdit").attr("src", signatureImage);
      $("#SignImage").attr("value", signatureImage);
      $("#clear_button_outside").css("display", "inline-block"); // Remove 'display: none;'
      $("#closeButton").click(); // Trigger a click on the close button
      $("#signatureModal").modal("hide"); // Close the modal
      $(".signature_upload_label").hide(); // Hide the label
    }
  });

  // END CANVAS

  // START SET CURRENT DATE
  // Get the current date in the "YYYY-MM-DD" format
  function getCurrentDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = (today.getMonth() + 1).toString().padStart(2, "0");
    const day = today.getDate().toString().padStart(2, "0");
    return `${year}-${month}-${day}`;
  }

  // Set the default value of the date input field to today's date
  $("#dateInput").val(getCurrentDate());

   if ($("#paymentMode").val === "Bank Transfer") {
      $("#journalNumber").show(); // Show the "Journal Number" input field
    }
  // START PAYMENT MODE  // Listen for changes in the select element
  $("#paymentMode").on("change", function () {
    var selectedOption = $(this).val(); // Get the selected option's value

    // Check if "Bank Transfer" is selected
    if (selectedOption === "Bank Transfer") {
      $("#journalNumber").show(); // Show the "Journal Number" input field
    } else {
      $("#journalNumber").hide();
      $("#journalNumber").val(""); // Hide the "Journal Number" input field for other options
    }
  });
  // END PAYMENT MODE

  // START CALCULATE AMOUNT
  $("#rate, #quantity").on("input", function () {
    var rate = parseFloat($("#rate").val());
    var quantity = parseFloat($("#quantity").val());
    var calculatedAmount = rate * quantity;

    if (isNaN(calculatedAmount)) {
      calculatedAmount = rate;
    }
    // Set the content of the #cost_amount element
    $("#cost_amount").val(calculatedAmount);
  });
  // END CALCULATE AMOUNT

  // START ADD COL
  $("#addRowButton").click(function (event) {
    event.preventDefault(); // Prevent the default behavior

    // Clone the first row
    var newRow = $(".data-row:first").clone();

    // Clear input values in the cloned row
    newRow.find(".rate-input, .quantity-input, #description").val("");
    newRow.find("#cost_amount").val("0");

    // Append the cloned row to the table
    $(".data-row:last").after(newRow);
  });

  // Calculate amounts when rate and quantity change
  $("tbody").on("input", ".rate-input, .quantity-input", function () {
    var row = $(this).closest("tr");
    var rate = parseFloat(row.find(".rate-input").val());
    var quantity = parseFloat(row.find(".quantity-input").val());
    var amount = isNaN(rate) || isNaN(quantity) ? "" : rate * quantity;
    row.find("#cost_amount").val(amount);

    // Calculate the total amount
    var totalAmount = 0;
    $(".data-row").each(function () {
      var rowAmount = parseFloat($(this).find("#cost_amount").val());
      if (!isNaN(rowAmount)) {
        totalAmount += rowAmount;
      }
    });

    // Update the Total Amount cell
    $("#totalAmount, #totalAmountpaid").text("Nu. " + totalAmount.toFixed(2));
    $("#totalamount").val(totalAmount);
  });

  // END ADD COL

  // START IMAGE UPLOAD
  $("#logo_upload, #logo_edit").change(function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        $("#uploaded_logo").attr("src", e.target.result);
        $("#uploaded_logo").show();
        $("#edited_logo").attr("src", e.target.result);
        $("#logo_edit").val(e.target.result);
        $("#uploaded_logo").css("display", "inline-block"); // Remove 'display: none;'
        $(".logo_upload_label").hide();
      };
      reader.readAsDataURL(file);
    }
  });

  $("#signature_upload, #signature_edit").change(function () {
    const file = this.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = function (e) {
        $("#uploaded_signature").attr("src", e.target.result);
        $("#edited_signature").attr("src", e.target.result);
        $("#signature_edit").val(e.target.result);
        $("#uploaded_signature").show();
        $("#uploaded_signature").css("display", "inline-block"); // Remove 'display: none;'
        $(".signature_upload_label").hide();
      };
      reader.readAsDataURL(file);
    }
  });
  // END IMAGE UPLOAD
});
