$(document).ready(() => {
    $.validator.addMethod("percentage", (value, element) => {
        var parts = value.split('%');
        console.log(parts)
        if (parts[0]>=0 && parts[0]<=100 && parts[1]=='') {
            return true;
        }
        else {
            return false
        }
    });

    $("#productForm").validate({
        rules: {
            name: {
                required: true,
            },
            descSub: {
                percentage: true,
            },
            descOferta: {
                percentage: true,
            },
        },
        messages: {
            name: {
                required: "El nombre es un campo requerido",
            },
            descSub: {
                percentage: "Error porcentaje, no se permiten decimales y debe incluir símbolo '%' (Ej: 15%)",
            },
            descOferta: {
                percentage: "Error porcentaje, no se permiten decimales y debe incluir símbolo '%' (Ej: 15%)",
            },
        },
    });

    $("#reset").on("click", () => {
        $("#updateProfileForm").validate().resetForm();
    });
});