$(document).ready( function() {
  $('.get-card').click( function() {
    $.get('/main/' + this.id, function(data) {
      $('#flash_card').empty()
      for (key in data.card) {
        $('#flash_card').append(
          '<tr class="click"><td>' + key + '</td><td>' + data.card[key] + '</td></tr>'
        );
      }
    });
  });
});
