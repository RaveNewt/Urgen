$('.page-scroll').on('click', function(e){
    
    var tujuan = $(this).attr('href');
    console.log(tujuan);

    var elemenTujuan = $(tujuan)

    $('body').animate({
        scrollTop: elemenTujuan.offset().top - 140
    });

    e.preventDefault();
});

