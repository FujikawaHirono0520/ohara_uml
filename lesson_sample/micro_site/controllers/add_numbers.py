from app_logic import get_addition, set_first_value, set_second_value
from utils import parse_post, render_template


def add_numbers_data(environ):
    result = get_addition()
    first = ""
    second = ""
    method = environ["REQUEST_METHOD"]
    if method == "POST":
        data = parse_post(environ)
        first = data.get("first_value", [""])[0]
        second = data.get("second_value", [""])[0]
        set_first_value(first)
        set_second_value(second)
        result = get_addition()

    return render_template("boundaries/add_numbers_data.html", first=first, second=second, result=result)
