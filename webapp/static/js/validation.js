$(document).ready(function () {
  // Try showing the modal directly
  function getCurrentDate() {
    const today = new Date();
    const year = today.getFullYear();
    const month = (today.getMonth() + 1).toString().padStart(2, "0");
    const day = today.getDate().toString().padStart(2, "0");
    return `${year}-${month}-${day}`;
  }

  function validate() {
    if ($("#recipient_phone").val() === "") {
      // Display the Bootstrap modal using jQuery
      $("#validationModal").modal("show");
      $("#validationErrorMessage").text(
        "Phone number of client cannot be empty."
      );
      return false;
    } else if ($("#recipient_name").val() === "") {
      // Display the Bootstrap modal using jQuery
      $("#validationModal").modal("show");
      $("#validationErrorMessage").text("Name of client cannot be empty.");
      return false;
    } else if ($("#amount").val() === "") {
      // Display the Bootstrap modal using jQuery
      $("#validationModal").modal("show");
      $("#validationErrorMessage").text("Amount cannot be empty.");
      return false;
    } else if (
      $("#paymentMode").val() === "Bank Transfer" &&
      $("#journalNumber").val() === ""
    ) {
      // Display the Bootstrap modal using jQuery
      $("#validationModal").modal("show");
      $("#validationErrorMessage").text("Jrnl Number cannot be empty.");
      return false;
    } else {
      return true;
    }
  }

  $("#generate_pdf").on("click", function (e) {
    e.preventDefault(); // Prevent the default form submission

    if (validate()) {
      $("#data_form").submit();
      setTimeout(function () {
        window.location.href = "/";
      }, 2000);
    }
  });
  // Function to convert and append image to FormData as a data URL

  $("#save_data").on("click", function (e) {
    e.preventDefault(); // Prevent the default form submission
    // Create a FormData object to handle the form data
    var formData = new FormData($("form")[0]);

    //  // Convert and append the logo image
    //  var logoImageInput = null;
    //  if ($("#logo_edit").length) {
    //    logoImageInput = $("#logo_edit")[0].files[0];
    //  } else if ($("#logo_upload").length) {
    //    logoImageInput = $("#logo_upload")[0].files[0];
    //    console.log(logoImageInput)
    //  }
    //
    //  // Convert and append the logo image URL to formData
    //  if (logoImageInput) {
    //    convertAndAppendImage(formData, "logo_image", logoImageInput);
    //  }
    //
    //  // Convert and append the signature image
    //  var signInput = null;
    //  if ($("#signature_edit").length) {
    //    signInput = $("#signature_edit")[0].files[0];
    //  } else if ($("#signature_upload").length) {
    //    signInput = $("#signature_upload")[0].files[0];
    //  }
    //
    //  // Convert and append the signature image URL to formData
    //  if (signInput) {
    //    convertAndAppendImage(formData, "signature_image", signInput);
    //  }

    // Append the image file to the FormData object
    var logoImageInput = $("#logo_edit").val;
    var logoImagenew = $("#logo_upload").val;
    if (logoImageInput) {
      formData.append("logo_image", logoImageInput);
    } else if (logoImagenew) {
      formData.append("logo_image", logoImagenew);
    }

    var signInput = $("#signature_edit").val;
    var signInputNew = $("#signature_upload").val;
    if (signInput) {
      formData.append("signature_image", signInput);
    } else if (signInputNew) {
      formData.append("signature_image", signInputNew);
    }

    if (validate()) {
      $.ajax({
        type: "POST",
        url: "/save_receipt/", // Replace with your actual URL
        data: formData,
        processData: false,
        contentType: false,
        cache: false,
        enctype: "multipart/form-data",
        success: function (response) {
          if (response.message === "Trial attempts up") {
            window.open("/trial_period/", "_blank");
          } else {
            $("#successModal").modal("show");
            $("#validationSuccessMessage").text("Your data was saved");
            setTimeout(function () {
              window.location.href = "/";
            }, 2000);
          }
        },
        error: function (error) {
          // Handle any errors that occur during the AJAX request
          alert("Error while saving data: " + error.responseText);
        },
      });
    }
  });

  function convertAndAppendImage(formData, fieldName, file) {
    var reader = new FileReader();
    reader.onload = function (event) {
      // Append the base64-encoded data to the FormData object
      formData.append(fieldName, event.target.result);
    };
    reader.readAsDataURL(file);
  }
});
