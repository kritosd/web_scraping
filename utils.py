
import locale
import re

def convert_to_normal_format(number_str):
    number_str = remove_non_numeric(number_str)
    # Remove commas from the input string
    number_str = number_str.replace(",", "")

    try:
        # Try to set locale to 'en_US.UTF-8'
        locale.setlocale(locale.LC_NUMERIC, 'en_US.UTF-8')
    except locale.Error:
        # Fallback to a different locale if 'en_US.UTF-8' is not supported
        locale.setlocale(locale.LC_NUMERIC, 'C')

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