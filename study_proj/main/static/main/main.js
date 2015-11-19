$(document).ready( function() {
  $('.get-card').click( function() {
    $.get('/main/' + this.id, function(data) {
      console.log(data.card)
      if (data.card === '0') {
        $('#panel').html(
          '<p>There are no cards in this deck yet.</p>'
        );
      }
      else {
        $('#flash_card').empty()
        for (key in data.card) {
          $('#flash_card').append(
            '<tr class="click"><td>' + key + '</td><td>' + data.card[key] + '</td></tr>'
          );
        }
      }
    });
  });
});
