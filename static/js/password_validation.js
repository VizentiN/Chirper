document.addEventListener('DOMContentLoaded', function() {
    var passwordInput = document.getElementById('id_password1');
    var confirmPasswordInput = document.getElementById('id_password2');
    
    passwordInput.onkeyup = validatePassword;
    confirmPasswordInput.onkeyup = validateConfirmPassword;

    function validatePassword() {
        var strength = 0;
        var password = passwordInput.value;
        if (password.length > 5) strength += 1;
        if (password.match(/(?=.*[0-9])/)) strength += 1;
        if (password.match(/(?=.*[!@#$%^&*])/)) strength += 1;
        if (password.match(/(?=.*[a-z])/)) strength += 1;
        if (password.match(/(?=.*[A-Z])/)) strength += 1;

        if (strength < 3) {
            passwordInput.style.borderColor = "red";
        } else {
            passwordInput.style.borderColor = "green";
        }
    }

    function validateConfirmPassword() {
        if (confirmPasswordInput.value !== passwordInput.value) {
            confirmPasswordInput.style.borderColor = "red";
        } else {
            confirmPasswordInput.style.borderColor = "green";
        }
    }
});