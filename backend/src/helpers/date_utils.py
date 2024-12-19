import pytz
from datetime import datetime, timedelta

# Get the current UTC date as a timezone-aware datetime
def get_current_date() -> datetime:
    return datetime.utcnow().replace(tzinfo=pytz.utc)

# Calculate the week number based on the given date
def get_week_number(date: datetime) -> int:
    # Get the current date
    current_date = get_current_date()

    # If the 'date' is naive, localize it to UTC
    if date.tzinfo is None:
        date = pytz.utc.localize(date)

    # Calculate the week number
    week_number = (current_date -date).days // 7 + 1

    return week_number

# Transform UTC to Toronto timezone
# Note: Need to think of data type for utc_date
def get_toronto_date(utc_date: datetime) -> datetime:
    # Set the Toronto timezone
    toronto = pytz.timezone('America/Toronto')

    # Check if the UTC date has timezone info
    if utc_date.tzinfo is None:
        utc_date = pytz.utc.localize(utc_date)

    # Convert UTC date to Toronto date
    toronto_date = utc_date.astimezone(toronto)

    return toronto_date

def format_date(date: datetime) -> str:
    # Get the month, day, time
    month = date.strftime("%B") # Full month name
    day = date.day
    time = date.strftime("%I:%M%p")  # 12-hour time with AM/PM

    # Add the suffix (st, nd, rd, th) based on the day
    suffix = 'th'
    if 4 <= day <= 20 or 24 <= day <= 30:  # Special cases (11th, 12th, etc.)
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(day % 10, 'th')

    # Format the date as 'December 31st 11:59PM'
    return f"{month} {day}{suffix} {time}"

def format_time_diff(date: datetime) -> str:
    # Get the time difference in seconds
    time_diff = (get_current_date() - date).total_seconds()

    # Calculate the days
    days = time_diff // (24 * 3600)
    time_diff = time_diff % (24 * 3600)

    # Calculate the hours
    hours = time_diff // 3600
    time_diff %= 3600

    # Calculate the minutes
    minutes = time_diff // 60

    # Format the time difference as '2DAYS 23:59'
    formatted_time_diff = f"{int(days)}DAYS {int(hours):02}:{int(minutes):02}"

    return formatted_time_diff
    
def get_deadline(date: datetime, week: int) -> datetime:
    # Calculate the deadline as 7 days from the given date
    deadline = date + timedelta(days=week * 7)

    return deadline