document.addEventListener('DOMContentLoaded', function() {
    var form = document.getElementById('signupForm');
    var signupUrl = form.getAttribute('data-signup-url');
    var homeUrl = form.getAttribute('data-home-url');

    form.onsubmit = function(event) {
        event.preventDefault();
        var formData = new FormData(form);
        
        fetch(signupUrl, {
            method: 'POST',
            body: formData,
            headers: {
                'X-CSRFToken': formData.get('csrfmiddlewaretoken')
            },
            credentials: 'same-origin'
        }).then(response => response.json())
        .then(data => {
            if (data.success) {
                window.location.href = homeUrl;
            } else {
                var errorsContainer = document.getElementById('signupErrors');
                errorsContainer.innerHTML = '';
                if (data.errors) {
                    Object.keys(data.errors).forEach(function(key) {
                        var errorParagraph = document.createElement('p');
                        errorParagraph.textContent = key + ": " + data.errors[key];
                        errorsContainer.appendChild(errorParagraph);
                    });
                } else {
                    var errorParagraph = document.createElement('p');
                    errorParagraph.textContent = "Erro desconhecido.";
                    errorsContainer.appendChild(errorParagraph);
                }
            }
        }).catch(error => console.error('Error:', error));
    };
});