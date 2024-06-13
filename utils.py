
import locale
import re
import datetime
from dateutil.relativedelta import relativedelta
import arrow

def convert_to_normal_format(number_str):
    number_str = remove_non_numeric(number_str)
    # Remove commas from the input string
    number_str = number_str.replace(",", "")

    # try:
    #     # Try to set locale to 'en_US.UTF-8'
    #     locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')
    # except locale.Error:
    #     # Fallback to a different locale if 'en_US.UTF-8' is not supported
    #     locale.setlocale(locale.LC_NUMERIC, 'C')

    # Convert the processed string to a float
    number_float = float(number_str)

    # Check if the number is an integer
    if number_float.is_integer():
        formatted_number = str(int(number_float))
    else:
        # Convert the number to a string using locale formatting
        formatted_number = locale.format_string("%.2f", number_float, grouping=True)

    # Replace dot with comma and comma with dot
    # formatted_number = formatted_number.replace(",", ";").replace(".", ",").replace(";", ".")

    return formatted_number

def remove_non_numeric(string):
    # Remove non-numeric characters using regular expression
    return re.sub(r'[^\d.]+', '', string)

def extract_number_from_string(string):
    
    # Extract the number using regular expressions
    number_str = re.search(r'[\d,]+', string).group()
    
    # Remove commas from the number string and convert it to an integer
    number = int(number_str)
    return number


def convert_date_to_100_ns_intervals(date_string):
    # Parse the date string into a datetime object
    target_date = datetime.datetime.strptime(date_string, "%d-%m-%Y")
    print("Target Date:", target_date)
    
    # Define the starting date (epoch start)
    start_date = datetime.datetime(1, 1, 1)
    print("Start Date:", start_date)
    
    # Calculate the difference as a timedelta object
    delta = target_date - start_date
    print("Delta (Days):", delta.days)
    
    # Convert the difference to total seconds
    total_seconds = delta.total_seconds()
    print("Total Seconds:", total_seconds)
    
    # Convert total seconds to 100-nanosecond intervals
    total_intervals = total_seconds * 10_000_000  # 10 million 100-nanosecond intervals in a second
    
    # Return the result as an integer
    return int(total_intervals)


def convert_100_ns_intervals_to_date(intervals):
    try:
        print(intervals)
        # Convert the intervals to total seconds
        total_seconds = intervals / 10_000_000  # 10 million 100-nanosecond intervals in a second
        
        # Define the starting date (epoch start)
        start_date = datetime.datetime(1, 1, 1)
        
        # Calculate the target date by adding the total seconds to the start date
        target_date = start_date + datetime.timedelta(seconds=total_seconds)
        
        # Return the target date
        return target_date
    except Exception as e:
        return f"An error occurred: {e}"



def lexical_to_number(lexical):
    if lexical.strip().lower() == 'jackpot':
        return int(0)
    
    # Remove the dollar sign and any commas
    lexical = lexical.replace('$', '').replace(',', '').strip()
    
    # Dictionary to convert lexical units to numerical multipliers
    units = {
        'thousand': 1_000,
        'million': 1_000_000,
        'billion': 1_000_000_000,
        'trillion': 1_000_000_000_000
    }
    
    # Use regular expression to find the number and the unit
    match = re.match(r'([\d\.]+)\s*(\w+)?', lexical, re.IGNORECASE)
    if not match:
        raise ValueError("Input string is not in the expected format.")
    
    # Extract the number and the unit
    number, unit = match.groups()
    
    # Convert the number part to float
    number = float(number)
    
    # If there's no unit, return the number as int if possible
    if unit is None:
        return int(number) if number.is_integer() else number
    
    # Convert the unit to lower case and get the corresponding multiplier
    unit = unit.lower()
    multiplier = units.get(unit, 1)  # Default to 1 if unit is not found
    
    # Calculate the final value
    final_value = number * multiplier
    
    # Return the final value as int if it's a whole number, else as float
    return int(final_value) if final_value.is_integer() else final_value