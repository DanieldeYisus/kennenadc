function validarFormulario() {

    //Sacando valor de los campos
    var nombre = document.getElementById("nombre").value;
    var txtNombre = document.getElementById("nombre");
    var correo = document.getElementById("mail").value;
    var txtCorreo = document.getElementById("mail");
    var telefono = document.getElementById("telefono").value;
    var txtTelefono = document.getElementById("telefono");
    var mensaje = document.getElementById("mensaje").value;
    var txtMensaje = document.getElementById("mensaje");

    //validar nombre
    if (nombre == null || nombre.length == 0 || /^\s+$/.test(nombre)) {
        alert('ERROR: El campo nombre no puede estar vacio');
        txtNombre.classList.add('error');
        txtNombre.classList.remove('exito');
        return false;

    } else {
        txtNombre.classList.remove('error');
        txtNombre.classList.add('exito');

    }

    //validar correo
    if (correo == null || correo.length == 0 || !(/\S+@\S+\.\S+/.test(correo))) {
        alert('ERROR: Debe escribir un correo válido');
        txtCorreo.classList.add('error');
        txtCorreo.classList.remove('exito');
        return false;

    } else {
        txtCorreo.classList.remove('error');
        txtCorreo.classList.add('exito');
    }

    //validar telefono
    if (telefono == null || telefono.length == 0 || isNaN(telefono)) {
        alert('ERROR:  Debe ingresar un número de teléfono válido');
        txtTelefono.classList.add('error');
        txtTelefono.classList.remove('exito');
        return false;

    } else {
        txtTelefono.classList.remove('error');
        txtTelefono.classList.add('exito');
    }

    //validar mensaje
    if (mensaje == null || mensaje.length == 0) {
        alert('ERROR: Debe escribir algún mensaje');
        txtMensaje.classList.add('error');
        txtMensaje.classList.remove('exito');
        return false;

    } else {
        txtMensaje.classList.remove('error');
        txtMensaje.classList.add('exito');
    }

    // alert('CORRECTO: Enviando Formulario de Contacto...');
    // return true;

}