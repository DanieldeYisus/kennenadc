function validarNombre() {

    var nombre = document.getElementById("nombre").value;
    var txtNombre = document.getElementById("nombre");

    if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
        alert('ERROR: El campo nombre no puede estar vacio');
        txtNombre.classList.add('error');
        txtNombre.classList.remove('exito');

    } else {
        txtNombre.classList.remove('error');
        txtNombre.classList.add('exito');

    }
}

function validarCorreo() {

    var correo = document.getElementById("mail").value;
    var txtCorreo = document.getElementById("mail");

    if (correo == null || correo.length == 0 || !(/\S+@\S+\.\S+/.test(correo))) {
        alert('ERROR: Debe escribir un correo válido');
        txtCorreo.classList.add('error');
        txtCorreo.classList.remove('exito');

    } else {
        txtCorreo.classList.remove('error');
        txtCorreo.classList.add('exito');
    }
}

function validarTelefono() {

    var telefono = document.getElementById("telefono").value;
    var txtTelefono = document.getElementById("telefono");

    if (telefono == null || telefono.length == 0 || isNaN(telefono)) {
        alert('ERROR: Debe ingresar un número de teléfono válido');
        txtTelefono.classList.add('error');
        txtTelefono.classList.remove('exito');

    } else {
        txtTelefono.classList.remove('error');
        txtTelefono.classList.add('exito');
    }
}

function validarMensaje() {

    var mensaje = document.getElementById("mensaje").value;
    var txtMensaje = document.getElementById("mensaje");

    if (mensaje == null || mensaje.length == 0) {
        alert('ERROR: Debe escribir algún mensaje');
        txtMensaje.classList.add('error');
        txtMensaje.classList.remove('exito');

    } else {
        txtMensaje.classList.remove('error');
        txtMensaje.classList.add('exito');
    }
}