$(document).ready(() => {
    $.validator.addMethod("validEmail", (value, element) => {
        var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z\-0-9]{2,}))$/;
        return regex.test(value);
    }, 'El formato del correo no es válido');

    $("#loginForm").validate({
        rules: {
            email: {
                required: true,
                validEmail: true,
            },
            password: {
                required: true,
            },
        },
        messages: {
            correo: {
                required: "El correo es un campo requerido",
                email: "El formato del correo no es válido",
            },
            password: {
                required: "La contraseña es un campo requerido",
            },
        },
    });
});