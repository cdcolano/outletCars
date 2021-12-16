$(document).ready(function() {
   
    $('section#site_content2>ul>li.listaCoche>div.Matricula>a').each(function () {
      var href = $(this).attr("href");
      alert(href)
      href = href.replace("coches", "cochesAjax");
      $(this).qtip({
         content: {
            url: href,
            method: 'get'
         }
      });
    });
  
  });