$(document).ready( function() {
  $('.field').hide();
  $('.answer').hide();
  $('.flash-card').hide();
  $('.get-card').click( function() {
    $.get('/main/' + this.id, function(data) {
      var card = data.card
      console.log(card)
      if (data.card === '0') {
        $('#type').empty();
        $('.field').hide();
        $('.answer').hide();
        $('.flash-card').hide();
        $('#panel-text').html(
          '<p>There are no cards in this deck yet.</p>'
        );
      }
      else {
        $('#type').empty();
        $('.field').hide();
        $('.answer').hide();
        $('#panel-text').empty();
        $('.flash-card').show();
        console.log(card)
        for (key in card) {
          $('#' + key).html(card[key]);
          $('.' + key).show();
        }
      }
    });
  });
});
