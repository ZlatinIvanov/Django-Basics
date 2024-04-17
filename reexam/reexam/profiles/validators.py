from django.core.exceptions import ValidationError


def validate_name_capital_letter(name):
    is_valid = name[0].isupper()

    if not is_valid:
        raise ValidationError("Name must start with a capital letter!")

