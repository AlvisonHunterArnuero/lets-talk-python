from datetime import datetime
import re

# -------- File Operations ---------
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)


# -------- String Manipulation ---------
def reverse_string(string):
    return string[::-1]


def count_words(string):
    words = string.split()
    return len(words)


# --------  Mathematical Operations ---------
def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def find_maximum(numbers):
    return max(numbers)


# --------  Date and Time Functions ---------


def get_current_date():
    return datetime.now().date()


def format_date(date, format='%Y-%m-%d'):
    return date.strftime(format)


# --------  Data Validation ---------
def is_email_valid(email):
    # Perform email validation logic
    email_pattern = r'^[\w.-]+@[\w.-]+\.\w+$'
    return re.match(email_pattern, email) is not None

def is_phone_number_valid(phone_number):
    # Perform phone number validation logic
    phone_pattern = r'^\d{3}-\d{3}-\d{4}$'
    return re.match(phone_pattern, phone_number) is not None

def validate_input(pattern, input_string):
    # Validate the input string against a given pattern
    return re.match(pattern, input_string) is not None

