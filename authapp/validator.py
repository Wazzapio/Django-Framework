from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_first_name(value):
    if value.isdigit():
        raise ValidationError(
            _(f'Имя не может быть только цифрами'),
            params={'value': value}
        )
    if not value.isalpha():
        raise ValidationError(
            _(f'Имя не может содержать цифры'),
            params={'value': value}
        )

def validate_last_name(value):
    if value.isdigit():
        raise ValidationError(
            _(f'Фамилия не может быть только цифрами'),
            params={'value': value}
        )
    if not value.isalpha():
        raise ValidationError(
            _(f'Фамилия не может содержать цифры'),
            params={'value': value}
        )

# def validate_image(value):
#     if value.size > 300000:
#         raise ValidationError(
#             _(f'Размер картинки больше 300КБ'),
#             params={'value': value}
#         )