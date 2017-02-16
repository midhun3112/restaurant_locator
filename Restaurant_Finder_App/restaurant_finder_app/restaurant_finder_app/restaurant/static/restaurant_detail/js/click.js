$('[data-toggle=popover]').popover({
    content: $('#openingTimesPopoverContent').html(),
    html: true
}).click(function() {
    $(this).popover('show');
});
