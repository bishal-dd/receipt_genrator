$(document).ready(function () {
  $('.yearpicker').datepicker({
    changeYear: true,
    showButtonPanel: true,
    dateFormat: 'yy',
    onClose: function(dateText, inst) {
      var year = $("#ui-datepicker-div .ui-datepicker-year :selected").val();
      $(this).datepicker('setDate', new Date(year, 1));
    }
  });

  $(".yearpicker").focus(function() {
    $(".ui-datepicker-month").hide();
    $(".ui-datepicker-calendar").hide();
  });

    $('.monthpicker').datepicker({
      dateFormat: 'MM', // Display only the month
      changeMonth: true,
      changeYear: false, // Hide the year dropdown
    });

});