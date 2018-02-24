var swiper2 = new Swiper('.s2', {
    // pagination: '.swiper-pagination',
    slidesPerView: 1,
    // paginationClickable: true,
    // spaceBetween: 30,
    // freeMode: true,
    // breakpoints: {
    //     3000: {
    //         slidesPerView: 1,
    //         spaceBetween: 130
    //     },
    //     1500: {
    //         slidesPerView: 1,
    //         spaceBetween: 30
    //     },
    //     1024: {
    //         slidesPerView: 1,
    //         spaceBetween: 30
    //     },
    //     768: {
    //         slidesPerView: 1,
    //         spaceBetween: 20
    //     },
    //     640: {
    //         slidesPerView: 1,
    //         spaceBetween: 10
    //     },
    //     320: {
    //         slidesPerView: 1,
    //         spaceBetween: 10
    //     }
    // }
});
    var swiper1 = new Swiper('.s1', {
        pagination: '.swiper-pagination',
        slidesPerView: 3,
        paginationClickable: true,
        spaceBetween: 30,
        // freeMode: true,
        breakpoints: {
            1500: {
                slidesPerView: 3,
                spaceBetween: 30
            },
            1024: {
                slidesPerView: 3,
                spaceBetween: 30
            },
            768: {
                slidesPerView: 2,
                spaceBetween: 20
            },
            640: {
                slidesPerView: 1,
                spaceBetween: 10
            },
            320: {
                slidesPerView: 1,
                spaceBetween: 10
            }
        }
    });
