$('#phoneNumberModal').on('show.bs.modal', function(event) {
    var hyperlink = $(event.relatedTarget) // Item that triggered the modal
    var restaurant = hyperlink.data('res-name') // Extract info from data-* attributes
    var phone_number = hyperlink.data('phone-no-str') // Extract info from data-* attributes

    var modal = $(this)
    modal.find('.modal-title').text(restaurant)
        modal.find('.modal-body input').val(phone_number)
})
