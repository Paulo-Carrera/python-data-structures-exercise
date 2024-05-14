def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days_of_week = [
        1,
        'Sunday',
        2,
        'Monday',
        3,
        'Tuesday',
        4,
        'Wednesday',
        5,
        'Thursday',
        6,
        'Friday',
        7,
        'Saturday'
    ]
    if day_of_week in days_of_week and type(day_of_week) == int:
        index = days_of_week.index(day_of_week)
        return days_of_week[index+1]
    # if day_of_week in days_of_week and type(day_of_week) == str :
    #     index = days_of_week.index(day_of_week)
    #     return days_of_week[index - 1]
    else :
        print("Invalid input.")
        return None

