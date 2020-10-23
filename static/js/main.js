$(document).ready(function () {

    // #region ==== Run functions =============================================================/
    set_genre_filters();
    // #endregion
    // ======================================================================================= /

    // #region ==== Close/Expand Button - Close specified element class(data-target) ==========/
    // in specified element id (data-id)
    $('.expand-button').click(function () {
        var id = '#' + $(this).data('id');
        var target_open_1 = '.' + $(this).data('targetopenone');
        var target_open_2 = '.' + $(this).data('targetopentwo');
        var target_close_1 = '.' + $(this).data('targetcloseone');
        var target_close_2 = '.' + $(this).data('targetclosetwo');

        if (target_close_1 != '.undefined') {
            $(id + ' ' + target_close_1).slideUp('slow');
        }

        if (target_open_1 != '.undefined') {
            $(id + ' ' + target_open_1).slideDown('slow');
        }

        if (target_close_2 != '.undefined') {
            $(id + ' ' + target_close_2).slideUp('slow');
        }
        if (target_open_2 != '.undefined') {
            $(id + ' ' + target_open_2).slideDown('slow');
        }
    });
    // #endregion
    // ======================================================================================= /

    // #region ==== Auto submit SortShowForm on any change in the form ========================/
    $('.SortShowForm-auto-submit').change(function () {
        $('#SortShowForm').submit();
    });
    // #endregion
    // ======================================================================================= /

    // #region ==== Genre Tags on change ======================================================/
    
    // Set all or none genre filters DEPENDING ON GENRE_ALL checkbox
    function set_genre_filters() {
        if ($('#genre_all').prop('checked')) {
            console.log('1');
            $(".genre-filter-checkbox").prop("checked", true);
        } else {
            console.log('0');
            $(".genre-filter-checkbox").prop("checked", false);
        }
    }

    // On GENRE_ALL click
    $('#genre_all').click(function (){
        set_genre_filters();
    });

    // Set genre_all on/off DEPENDING ON GENRE-FILTER-CHECKBOX
    function set_genre_all_filter() {
        if ($('.genre-filter-checkbox').prop('checked')) {
            console.log('1');
            $("#genre_all").prop("checked", false);
        } 
    }

    // On GENRE-FILTER-CHECKBOX click
    $('.genre-filter-checkbox').click(function (){
        set_genre_all_filter();
    });


    // #endregion
    // ======================================================================================= /

    // #region ==== Initialize Bootstrap Tooltip ============================================= /
    $('[data-toggle="tooltip"]').tooltip();
    // #endregion
    // ======================================================================================= /

    // #region ==== Change Avatar window open/close ========================================== /
    $('.change-avatar-button').click(function () {
        var action = $(this).data('action');
        if (action == 'open') {
            $('.select-avatar-window').css('display', 'block');
        } else if (action == 'close') {
            $('.select-avatar-window').css('display', 'none');
        } else {
            $('.select-avatar-window').css('display', 'none');
        }
    });
    // #endregion
    // ======================================================================================= /

    // #region ==== Top Info Close ========================================== /
    $('.top-info-close-link').click(function () {
        $('.top-info-container').slideUp('slow');
    });
    // #endregion
    // ======================================================================================= /
});