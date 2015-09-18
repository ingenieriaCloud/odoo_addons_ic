//comun
function toggleData(){
    if($('#btn_toggle').val().indexOf('+') >= 0){
        $('#btn_toggle').val('- Ocultar')
        $('#data').show();
    }else{
        $('#btn_toggle').val('+ Ver')
        $('#data').hide();
    }
}

//Pintura
var data_pintura = '<div class="row" style="padding-top:10px;" id="zona_f_#INDEX#"> <div class="col-md-3 col-xs-2" style="text-align: right;">#TIPO#</div> <div class="col-md-2 col-xs-3"><input type="text" style="max-width: 100px;" id="largo_f#INDEX#" onchange="recalculeDataPintura(this);"/></div> <div class="col-md-2 col-xs-3"><input type="text" style="max-width: 100px;" id="ancho_f#INDEX#" onchange="recalculeDataPintura(this);"/></div> <div class="col-md-5 col-xs-4"> <select name="type_f#INDEX#" id="type_f#INDEX#" onchange="recalculeDataPintura(this);"> <option value="1">Todo</option> <option value="2">Solo Paredes</option> <option value="3">Solo Techo</option> </select> <a href="#" class="btn btn-xs btn-danger" name="del_fila_#INDEX#" id="del_fila_#INDEX#" style="margin-left:10px" title="Eliminar elemento" onclick="deleteFilaPintura(this)"><b> - </b></a> </div> </div>';
var data_pintura_index = 4;

function addElementPintura(){
    $('#elmentTypeAdvancePintura').val('');
    $('#addElementTypePintura option[value=""]').prop('selected', true);
    $('#elmentTypeAdvancePintura').hide();
    $('#addElementPintura').modal('show');
}

function appendDataPintura(){
    var txt = '';
    if ($('#addElementTypePintura').find(":selected").val() == 'o'){
        txt = $('#elmentTypeAdvancePintura').val();
    }else{
        txt = $('#addElementTypePintura').find(":selected").text();
    }

    if(txt != ''){
        $('#elementsPintura').append(data_pintura.replace('#TIPO#', txt).replace(/#INDEX#/g,data_pintura_index));
        $('#addElementPintura').modal('hide');
        data_pintura_index = data_pintura_index + 1;
    }else{
        alert('Debe introducir la descripción de la estancia');
    }
}

function deleteFilaPintura(obj){
    index = $(obj).attr('id').substring(9, $(obj).attr('id').length);
    $("#zona_f_"+index).remove();
    recalculeDataPintura();
}

function showAdvancePintura(obj){
    if ($('#addElementTypePintura').find(":selected").val() == 'o'){
        $('#elmentTypeAdvancePintura').show();
    }else{
        $('#elmentTypeAdvancePintura').hide();
    }
}

function recalculeDataPintura(obj){
    data_total = 0;
    alto = 0;
    if(obj){
        if(!$.isNumeric($(obj).val())){
            if($(obj).val()){
                alert("El valor introducido no es un número válido, debe cumplir el formato NN.nn");
                $(obj).focus();
            }
        }
    }

    if(!$('#alto').val()){
        alert('En primer lugar debe introducir la altura de la vivienda.');
        $('#alto').focus();
    }
    else{
        alto = 	$('#alto').val();
        $( "select[id^='type_f']") .each(function( index ) {
            var i = $(this).attr('id').substring(6, 7);
            if($('#largo_f'+i).val() && $('#ancho_f'+i).val()){
                var tot = 0;
                if($(this).val() == 1){
                    tot = 2*($('#largo_f'+i).val() * alto) + 2*($('#ancho_f'+i).val() * alto);
                    tot = tot + ($('#largo_f'+i).val() * $('#ancho_f'+i).val());
                }
                if($(this).val() == 2){
                    tot = 2*($('#largo_f'+i).val() * alto) + 2*($('#ancho_f'+i).val() * alto);
                }
                if($(this).val() == 3){
                    tot = $('#largo_f'+i).val() * $('#ancho_f'+i).val();
                }

                data_total = data_total + tot
            }
        });
        $('#total').html(data_total.toFixed(2));
        $('input[name=add_qty]').val(Math.ceil(data_total.toFixed(2)));
    }

}

//Aislamiento
var data_aislamiento = '<div class="row" style="padding-top:10px;" id="zona_f_#INDEX#"> <div class="col-md-3 col-xs-2" style="text-align: right;">#TIPO#</div> <div class="col-md-4 col-xs-6"><input type="text" style="max-width: 100px;" id="largo_f#INDEX#" onchange="recalculeDataAislamiento(this);"/> <a href="#" class="btn btn-xs btn-danger" name="del_fila_#INDEX#" id="del_fila_#INDEX#" style="margin-left:10px" title="Eliminar pared" onclick="deleteFilaAislamiento(this)"><b> - </b></a></div></div>';
var data_aislamiento_index = 2;

function addElementAislamiento(){
    $('#elementsAislamiento').append(data_aislamiento.replace('#TIPO#', 'Pared').replace(/#INDEX#/g,data_aislamiento_index));
    data_aislamiento_index = data_aislamiento_index + 1;
}

function deleteFilaAislamiento(obj){
    index = $(obj).attr('id').substring(9, $(obj).attr('id').length);
    $("#zona_f_"+index).remove();
    recalculeDataAislamiento();
}

function showAdvanceAislamiento(obj){
    if ($('#addElementType').find(":selected").val() == 'o'){
        $('#elmentTypeAdvance').show();
    }else{
        $('#elmentTypeAdvance').hide();
    }
}

function recalculeDataAislamiento(obj){
    data_total = 0;
    alto = 0;
    if(obj){
        if(!$.isNumeric($(obj).val())){
            if($(obj).val()){
                alert("El valor introducido no es un número válido, debe cumplir el formato NN.nn");
                $(obj).focus();
            }
        }
    }
    if(!$('#alto').val()){
        alert('En primer lugar debe introducir la altura de la vivienda.');
        $('#alto').focus();
    }
    else{
        alto = 	$('#alto').val();
        $( "div[id^='zona_f_']") .each(function( index ) {
            var i = $(this).attr('id').substring(7, $(this).attr('id').length);
            if($('#largo_f'+i).val()){
                tot = ($('#largo_f'+i).val() * alto);
                data_total = data_total + tot
            }
        });
        $('#totalAislamiento').html(data_total.toFixed(2));
        $('input[name=add_qty]').val(Math.ceil(data_total.toFixed(2)));
    }
}

//solado/parquet
var data_suelo = '<div class="row" style="padding-top:10px;" id="zona_f_#INDEX#"> <div class="col-md-3 col-xs-2" style="text-align: right;">#TIPO#</div> <div class="col-md-2 col-xs-3"><input type="text" style="max-width: 100px;" id="largo_f#INDEX#" onchange="recalculeDataSuelo(this);"/></div> <div class="col-md-2 col-xs-3"><input type="text" style="max-width: 100px;" id="ancho_f#INDEX#" onchange="recalculeDataSuelo(this);"/><a href="#" class="btn btn-xs btn-danger" name="del_fila_#INDEX#" id="del_fila_#INDEX#" style="margin-left:10px" title="Eliminar elemento" onclick="deleteFilaSolado(this)"><b> - </b></a</div></div>';
var data_suelo_index = 4;

function addElementSuelo(){
    $('#elmentTypeAdvanceSuelo').val('');
    $('#addElementTypeSuelo option[value=""]').prop('selected', true);
    $('#elmentTypeAdvanceSuelo').hide();
    $('#addElementSuelo').modal('show');
}

function appendDataSuelo(){
    var txt = '';
    if ($('#addElementTypeSuelo').find(":selected").val() == 'o'){
        txt = $('#elmentTypeAdvanceSuelo').val();
    }else{
        txt = $('#addElementTypeSuelo').find(":selected").text();
    }

    if(txt != ''){
        $('#elementsSuelo').append(data_suelo.replace('#TIPO#', txt).replace(/#INDEX#/g,data_suelo_index));
        $('#addElementSuelo').modal('hide');
        data_suelo_index = data_suelo_index + 1;
    }else{
        alert('Debe introducir la descripción de la estancia');
    }
}

function deleteFilaSolado(obj){
    index = $(obj).attr('id').substring(9, $(obj).attr('id').length);
    $("#zona_f_"+index).remove();
    recalculeDataSuelo();
}

function showAdvanceSuelo(obj){
    if ($('#addElementTypeSuelo').find(":selected").val() == 'o'){
        $('#elmentTypeAdvanceSuelo').show();
    }else{
        $('#elmentTypeAdvanceSuelo').hide();
    }
}

function recalculeDataSuelo(obj){
    data_total = 0;
    if(obj){
        if(!$.isNumeric($(obj).val())){
            if($(obj).val()){
                alert("El valor introducido no es un número válido, debe cumplir el formato NN.nn");
                $(obj).focus();
            }
        }
    }

    $( "div[id^='zona_f']") .each(function( index ) {
        var i = $(this).attr('id').substring(7, $(this).attr('id').length);
        if($('#largo_f'+i).val() && $('#ancho_f'+i).val()){
            tot = $('#largo_f'+i).val() * $('#ancho_f'+i).val();
            data_total = data_total + tot
        }
    });

    $('#totalSuelo').html(data_total.toFixed(2));
    $('input[name=add_qty]').val(Math.ceil(data_total.toFixed(2)));

}

function showProduct(url){
    if(typeof data_total !== 'undefined'){
        $('#urlProduct').attr('href', url);
        $('#totalModalProduct').html('"' + Math.ceil(data_total.toFixed(2)) + '"');
        $('#showProductModal').modal('show');
    }else{
        alert("Debe calcular los metros de pintura, antes de ir al producto!");
    }
}

