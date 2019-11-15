$(function() {
    $.getJSON('https://www.mindicador.cl/api', function(data) {
        var indicador = data;

        $('#uf-casa-index').html('UF: ' + +Math.round(330000 / indicador.uf.valor))
        $('#uf-dpto-index').html('UF: ' + +Math.round(205000000 / indicador.uf.valor))
        $('#uf-terr-index').html('UF: ' + +Math.round(170000000 / indicador.uf.valor))
        $('#uf').html('UF: ' + '$ ' + (indicador.uf.valor))
        $('#utm').html('UTM: ' + '$ ' + (indicador.utm.valor))
        $('#dolar').html('DOLAR: ' + '$ ' + (indicador.dolar.valor))
        $('#uf-casa-1').html('UF: ' + +Math.round(35000000 / indicador.uf.valor))
        $('#uf-casa-2').html('UF: ' + +Math.round(50000000 / indicador.uf.valor))
        $('#uf-casa-3').html('UF: ' + +Math.round(25000000 / indicador.uf.valor))
        $('#uf-dpto-1').html('UF: ' + +Math.round(150000000 / indicador.uf.valor))
        $('#uf-dpto-2').html('UF: ' + +Math.round(189000000 / indicador.uf.valor))
        $('#uf-dpto-3').html('UF: ' + +Math.round(100000000 / indicador.uf.valor))
        $('#uf-terr-1').html('UF: ' + +Math.round(350000000 / indicador.uf.valor))
        $('#uf-terr-2').html('UF: ' + +Math.round(245000000 / indicador.uf.valor))
        $('#uf-terr-3').html('UF: ' + +Math.round(165000000 / indicador.uf.valor))
    });
});