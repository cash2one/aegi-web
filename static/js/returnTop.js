$(window).scroll(function(){
   var sc=$(window).scrollTop();
   var rwidth=$(window).width()
   if(sc>0){
    $("#returnTop").css("display","block");
    $("#returnTop").css("left",(rwidth-56)+"px")
   }else{
   $("#returnTop").css("display","none");
   }
 })
 $("#returnTop").click(function(){
   var sc=$(window).scrollTop();
   $('body,html').animate({scrollTop:0},500);
  


 })




