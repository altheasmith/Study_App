$(document).ready( function() {
  $('.form').hide();
  $('#bac').click( function() {
    $('#bac_form').show();
  });
  $('#vir').click( function() {
    $('#vir_form').show();
  });
  $('#fun').click( function() {
    $('#fun_form').show();
  });
  $('#par').click( function() {
    $('#par_form').show();
  });
  $('#dis').click( function() {
    $('#dis_form').show();
  });
  $('#dru').click( function() {
    $('#dru_form').show();
  });

  $('#bac-submit').click( function(event) {
    event.preventDefault();
    $.post(data)
  });
  $('#vir').click( function() {
    $('#vir_form').show();
  });
  $('#fun').click( function() {
    $('#fun_form').show();
  });
  $('#par').click( function() {
    $('#par_form').show();
  });
  $('#dis').click( function() {
    $('#dis_form').show();
  });
  $('#dru').click( function() {
    $('#dru_form').show();
  });
})
