$(document).ready(function () {
    // Close/Expand Button - Close specified element class(data-target)
    // in specified element id (data-id)
    $('.expand-button').click(function () {
        var id = '#' + $(this).data('id');
        var target_open = '.' + $(this).data('targetopen');
        var target_close = '.' + $(this).data('targetclose');
        $(id + ' ' + target_close).hide();
        $(id + ' ' + target_open).show();
    });
});
