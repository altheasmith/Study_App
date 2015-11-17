$(document).ready( function() {
  $('.form').hide();
  //JQuery to show the form requested by the button
  $('#bac').click( function() {
    $('.form').hide();
    $('#bac_form').show();
  });
  $('#vir').click( function() {
    $('.form').hide();
    $('#vir_form').show();
  });
  $('#fun').click( function() {
    $('.form').hide();
    $('#fun_form').show();
  });
  $('#par').click( function() {
    $('.form').hide();
    $('#par_form').show();
  });
  $('#dis').click( function() {
    $('.form').hide();
    $('#dis_form').show();
  });
  $('#dru').click( function() {
    $('.form').hide();
    $('#dru_form').show();
  });
  //JQuery for when form is submitted
  $('#bac-submit').click( function(event) {
    event.preventDefault();
    console.log('submitted form')
  });
  $('#vir-submit').click( function(event) {
    event.preventDefault();
    console.log('submitted form')
  });
  $('#fun-submit').click( function(event) {
    event.preventDefault();
    console.log('submitted form')
  });
  $('#par-submit').click( function(event) {
    event.preventDefault();
    console.log('submitted form')
  });
  $('#dis-submit').click( function(event) {
    event.preventDefault();
    console.log('submitted form')
  });
  $('#dru-submit').click( function(event) {
    event.preventDefault();
    console.log('submitted form')
  });
})
