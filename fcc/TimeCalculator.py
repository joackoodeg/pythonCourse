def add_time(start, duration, start_day=None):
    # Convert start time to minutes
    start_time_parts = start.split()
    start_hour, start_minute = map(int, start_time_parts[0].split(':'))
    start_period = start_time_parts[1]
    if start_period == 'PM':
        start_hour += 12
    start_minutes = start_hour * 60 + start_minute

    # Convert duration to minutes
    duration_hour, duration_minute = map(int, duration.split(':'))
    duration_minutes = duration_hour * 60 + duration_minute

    # Calculate new time in minutes
    total_minutes = start_minutes + duration_minutes

    # Calculate new time
    new_hour = total_minutes // 60 % 24
    new_minute = total_minutes % 60
    new_period = 'AM' if new_hour < 12 else 'PM'

    # Adjust hour to 12-hour format
    if new_hour > 12:
        new_hour -= 12
    elif new_hour == 0:
        new_hour = 12

    # Calculate days later
    days_later = total_minutes // 1440

    # Adjust day of the week if provided
    if start_day:
        start_day = start_day.lower().capitalize()
        days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        start_index = days_of_week.index(start_day)
        new_day_index = (start_index + days_later) % 7
        new_day = days_of_week[new_day_index]

    # Construct result string
    result = f"{new_hour}:{new_minute:02d} {new_period}"
    if start_day:
        result += f", {new_day}"
    if days_later == 1:
        result += " (next day)"
    elif days_later > 1:
        result += f" ({days_later} days later)"

    return result

if __name__ == "__main__":
    print(add_time('3:00 PM', '3:10'))
    # Returns: 6:10 PM  
    