def switch(x: Any) -> Any:
    switcher = {0: 'Sunday',
                1: 'Monday',
                2: 'Tuesday',
                3: 'Wednesday',
                4: 'Thursday',
                5: 'Friday',
                6: 'Saturday'
                }
    return switcher.get(x, "Invalid day of week")
