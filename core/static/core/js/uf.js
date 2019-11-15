$(function() {
    $.getJSON('https://www.mindicador.cl/api', function(data) {
        var indicador = data;

        $('#uf').html('UF: ' + '$ ' + (indicador.uf.valor))
        $('#utm').html('UTM: ' + '$ ' + (indicador.utm.valor))
        $('#dolar').html('DOLAR: ' + '$ ' + (indicador.dolar.valor))

    });
});