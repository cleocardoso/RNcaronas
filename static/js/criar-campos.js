
$(document).ready(function(){
    if($("#relatorio").length){
        hide('show-datas')
        hide('show-cidade')
    }
});

function hide(id){
     $("#"+id).hide();
}

function show(id){
     $("#"+id).show();
}

$("#filter-data").click(function(){
    show("show-datas");
    hide("show-cidade");

})

$("#filter-cidade").click(function(){
    show("show-cidade");
    hide("show-datas");
})