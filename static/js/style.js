//togle down menu
  $(document).ready(function(){
    $("#flip").click(function(){
        $("#panel").slideToggle("slow");
    });
});

  $(document).ready(function(){
        $("#flip").click(function(){
            $(this).html($(this).html() == '<span class="glyphicon glyphicon-triangle-top"></span>' ?
             '<span class="glyphicon glyphicon-triangle-bottom"></span> ' : '<span class="glyphicon glyphicon-triangle-top"></span>');
        });
});