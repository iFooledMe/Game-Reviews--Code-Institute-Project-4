$(document).ready(function () {
    // Close/Expand Button - Close specified element class(data-target)
    // in specified element id (data-id)
    $('.expand-button').click(function () {
        var id = '#' + $(this).data('id');
        var target_open_1 = '.' + $(this).data('targetopenone');
        var target_open_2 = '.' + $(this).data('targetopentwo');
        var target_close_1 = '.' + $(this).data('targetcloseone');
        var target_close_2 = '.' + $(this).data('targetclosetwo');
        console.log('Close: ' + id + ' ' + target_close_1);
        console.log('Close: ' + id + ' ' + target_close_2);
        console.log('Open: ' + id + ' ' + target_open_1);
        console.log('Open: ' + id + ' ' + target_open_2);

        if (target_close_1 != '.undefined') {
            $(id + ' ' + target_close_1).hide();
        }

        if (target_open_1 != '.undefined') {
            $(id + ' ' + target_open_1).show();
        }

        if (target_close_2 != '.undefined') {
            $(id + ' ' + target_close_2).hide();
        }
        if (target_open_2 != '.undefined') {
            $(id + ' ' + target_open_2).show();
        }
    });

    /* Auto submit SortShowForm on any change in the form */
    $('.SortShowForm-auto-submit').change(function () {
        $('#SortShowForm').submit();
    });
});
