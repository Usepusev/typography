// Получение CSRF токена из cookie
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

$(document).ready(function() {
    $('.btn-delete').click(function(event) {
        event.preventDefault();
        const url = $(this).attr('href');
        const row = $(this).closest('tr');
        $.ajax({
            url: url,
            type: 'POST',
            data: {
                csrfmiddlewaretoken: csrftoken
            },
            success: function(response) {
                if (response.success) {
                    row.remove();
                } else {
                    alert('Ошибка при удалении элемента.');
                }
            }
        });
    });
});
