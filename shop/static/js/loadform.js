var form = document.getElementById('myForm');
if (!request.user.is_authenticated) {
    form.style.display = 'none';
} else {
    form.style.display = 'block';
}
