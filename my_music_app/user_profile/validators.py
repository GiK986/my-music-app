# validate_username is a function that we have to define in validators.py

from django.core.exceptions import ValidationError


def validate_username(value):
    if len(value) < 2:
        raise ValidationError("Username must be more than 2 characters long")
    if not (value.isalnum() or "_" in value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
