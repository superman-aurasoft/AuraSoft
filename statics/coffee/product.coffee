jQuery(document).ready ->
    if $('#countdown_dashboard').length > 0
        $('#countdown_dashboard').countDown
            targetDate:
                'day': 1
                'month': 4
                'year': 2013
                'hour': 10
                'min': 0
                'sec': 0
