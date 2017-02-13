$(document).ready(function(){
    //FANCYBOX
    //https://github.com/fancyapps/fancyBox
    $(".fancybox").fancybox({
        openEffect: "none",
        closeEffect: "none"
    });
});

$(function(){
  $('.lightbox').click(function(event){
    event.preventDefault();
    // need to be able to get the link target
    $link = $(event.target).closest('a');

    $.getJSON($link.attr('href'), function(menu_image){
      // map the json to an array that fancybox can use
      images = $(menu_image.images).map(function(key, image)){
        return({ href: image.url });
      });

      console.log(images);
      // => [{href: 'image1.jpg'},{href: 'image2.jpg'},{href: 'image3.jpg'}]

      // show the lightbox
      $.fancybox.open(images);
    });
  });
});

$("#triggerGallery").click(function (e) {
    e.preventDefault();
    $(".images").eq(0).trigger("click");
})
$(".grouped_elements").fancybox();


