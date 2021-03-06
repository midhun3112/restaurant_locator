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

$('.menu-image-formset').formset({
    addText: 'Add',
    deleteText: 'Remove'
});