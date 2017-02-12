function viewAllCollectionsClick() {
    location.href='collections/all/'
}

function collectionClick(collection_id) {
    location.href='/collections/'+collection_id+'/'
}

function categoryClick(category_id) {
    location.href='categories/'+category_id+'/'
}

function restaurantClick(restaurant_id) {
    location.href='/restaurant/'+restaurant_id+'/details'
}

$('[data-toggle=popover]').popover({
    content: $('#myPopoverContent').html(),
    html: true
}).click(function() {
    $(this).popover('show');
});

$('body').on('click', function (e) {
    $('[data-toggle="popover"]').each(function () {
        //the 'is' for buttons that trigger popups
        //the 'has' for icons within a button that triggers a popup
        if (!$(this).is(e.target) && $(this).has(e.target).length === 0 && $('.popover').has(e.target).length === 0) {
            $(this).popover('hide');
        }
    });
});