//togle down menu
  $(document).ready(function(){
    $("#flip").click(function(){
        $("#panel").slideToggle("slow");
    });
});

  $(document).ready(function(){
        $("#flip").click(function(){
            $(this).html($(this).html() == 'Close window <span class="glyphicon glyphicon-triangle-top"></span>' ?
             'Weather for all week <span class="glyphicon glyphicon-triangle-bottom"></span> ' : 'Close window <span class="glyphicon glyphicon-triangle-top"></span>');
        });
});