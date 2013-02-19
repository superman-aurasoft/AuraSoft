jQuery ->
    $active_menu = $($('input[name="active_menu"]').val())
    $active_menu.removeClass('inactive')
    $active_menu.addClass('active')