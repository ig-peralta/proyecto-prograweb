$(document).ready(() => {
    $.validator.addMethod("rutChileno", (value, element) => {
        var rutPattern = /^\d{7,8}-[\dK]$/;
        if (!rutPattern.test(value)) {
            return false;
        }
        var rutSinGuion = value.replace("-", "");
        var rut = rutSinGuion.slice(0, -1);
        var dv = rutSinGuion.slice(-1);
        var factor = 2;
        var sum = 0;
        for (var i = rut.length - 1; i >= 0; i--) {
            sum += parseInt(rut.charAt(i)) * factor;
            factor = factor === 7 ? 2 : factor + 1;
        }
        var dvCalculado = 11 - (sum % 11);
        dvCalculado = dvCalculado === 11 ? "0" : dvCalculado === 10 ? "K" : dvCalculado.toString();
        return dv === dvCalculado;
    }, "El RUT no es válido (escriba sin puntos y con guión)");

    $.validator.addMethod("validEmail", (value, element) => {
        var regex = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z\-0-9]{2,}))$/;
        return regex.test(value);
    }, 'El formato del correo no es válido');

    $.validator.addMethod("onlyLetters", function(value, element) {
        return this.optional(element) || /^[a-zA-ZÀ-ÿ\u00f1\u00d1]+(\s*[a-zA-ZÀ-ÿ\u00f1\u00d1]*)*[a-zA-ZÀ-ÿ\u00f1\u00d1]+$/.test(value);
    }, "Sólo se permiten letras y espacios en blanco.");

    $("#updateProfileForm").validate({
        rules: {
            rut: {
                required: true,
                rutChileno: true
            },
            name: {
                required: true,
                onlyLetters: true
            },
            lastName: {
                required: true,
                onlyLetters: true
            },
            email: {
                required: true,
                validEmail: true,
            },
            address: {
                required: true,
                maxlength: 255,
            },
            password: {
                required: true,
                minlength: 5,
                maxlength: 15,
            },
            password2: {
                required: true,
                minlength: 5,
                maxlength: 15,
                equalTo: "#password",
            },
        },
        messages: {
            rut: {
                required: "El RUT es un campo requerido",
                rutChileno: "El RUT no es válido (escriba sin puntos y con guión)"
            },
            name: {
                required: "El nombre es un campo requerido",
                soloLetras: "El nombre sólo puede contener letras y espacios en blanco",
            },
            lastName: {
                required: "El apellido es un campo requerido",
                soloLetras: "El apellido sólo puede contener letras y espacios en blanco",
            },
            email: {
                required: "El correo es un campo requerido",
                email: "El formato del correo no es válido",
            },
            address: {
                required: "La dirección es un campo requerido",
                maxlength: "La dirección debe tener un máximo de 100 caracteres",
            },
            password: {
                required: "La contraseña es un campo requerido",
                minlength: "La contraseña debe tener un mínimo de 5 caracteres",
                maxlength: "La contraseña debe tener un máximo de 15 caracteres",
            },
            password2: {
                required: "Repetir contraseña es un campo requerido",
                minlength: "Repetir contraseña debe tener un mínimo de 5 caracteres",
                maxlength: "Repetir contraseña debe tener un máximo de 15 caracteres",
                equalTo: "Debe repetir la contraseña escrita anteriormente",
                },
        },
    });

    $("#reset").on("click", () => {
        $("#updateProfileForm").validate().resetForm();
    });
});