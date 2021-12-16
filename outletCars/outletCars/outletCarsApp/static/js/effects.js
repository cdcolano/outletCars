$(document).ready(function() {


    
    $(document).ready(function(){
      $(".info-coche").hide();
    })

    

    $(".mostrarmenos").click(function(){
      $(".info-coche").slideUp(500)
    });
    $(".mostrarmas").click(function(){
      $(".info-coche").slideDown(500)
    });

   

    $("div.posts > h1.content-subhead").click(function () {
      $("div.post-description").slideUp();
    });
  
    $("div.posts > h1.content-subhead").dblclick(function () {
      $("div.post-description").slideDown();
    });
    
   });