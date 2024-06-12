$(document).ready(function() {
    $('#subscription-form').on('submit', function(event) {
        event.preventDefault();
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),  // Используем URL из атрибута action формы
            data: $(this).serialize(),
            headers: {
                'X-CSRFToken': csrftoken
            },
            success: function(response) {
                $('#subscription-message').text('Спасибо за подписку!');
            },
            error: function(response) {
                $('#subscription-message').text('Ошибка при подписке.');
            }
        });
    });
});
