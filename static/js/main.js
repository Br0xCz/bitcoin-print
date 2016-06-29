$(document).ready(function () {

    $("#carousel").owlCarousel({
        navigation: true, // Show next and prev buttons
        slideSpeed: 300,
        paginationSpeed: 400,
        singleItem: true
    });

});

printerStateCallback = function (data) {
    data = JSON.parse(data);
    if(data['ready']){
        
    }
    else{
        
    }
};

getPrinterState = function () {
    $.ajax({
        type: 'GET',
        url: '/api/ready',
        success: printerStateCallback
    })
};

interval(1800, getPrinterState());