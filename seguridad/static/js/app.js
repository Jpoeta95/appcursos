function ingresar(){
    var var1 = $("#inputEmail").val();
    var var2 = $("inputPassword").val();
    $.post("logie","var1="+var1+"&var2="+var2,function(data){
        alert(data);
    })

}