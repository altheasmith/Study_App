$(document).ready( function() {
  $('.field').hide();
  $('.answer').hide();
  $('.flash-card').hide();
  $('.get-card').click( function() {
    $.get(this.id, function(data) {
      var card = data.card
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
        for (key in card) {
          $('#' + key).html(card[key]);
          $('.' + key).show();
        }
        $('.answer').hide();
        $('#id').show();
        $('.field').click( function() {
          var class_list = $(this).attr('class').split(' ');
          $('#' + class_list[1]).show();
        });
      }
    });
  });
});
