from flask import current_app as app


from flask_wtf import FlaskForm
from wtforms.fields import (
    FormField,
    StringField,
    BooleanField,
    FieldList,
    SubmitField,
    SelectField,
    PasswordField,
)
from wtforms.fields import DateField, EmailField
from wtforms.validators import DataRequired, Length, Optional, Email
from wtforms.widgets import HiddenInput

from .models import *
def strip_filter(value):
    if value is not None and hasattr(value, 'strip'):
        return value.strip()
    return value


class BugFixForm(FlaskForm):
    # with this, we append one filter to all fields, ignoring only the ones
    # that are not designed for using filters
    # see: http://stackoverflow.com/a/28015147
    class Meta:
        def bind_field(self, form, unbound_field, options):
            if unbound_field.field_class in [FieldList, SelectField, FormField]:
                return unbound_field.bind(form=form, **options)
            else:
                filters = unbound_field.kwargs.get('filters', [])
                filters.append(strip_filter)
                return unbound_field.bind(form=form, filters=filters, **options)

class RegisterForm(BugFixForm):
    firstname = StringField("Vorname",
                            [DataRequired(message="Bitte gib deinen Vornamen an."),
                             Length(min=2,
                                    max=80,
                                    message="Dein Vorname muss aus mindestens 2 Zeichen bestehen und darf "
                                            "maximal 80 Zeichen lang sein.")])

    lastname = StringField("Nachname",
                           [DataRequired(message="Bitte gibt deinen Nachnamen an."),
                            Length(min=2,
                                   max=40,
                                   message="Dein Nachname muss aus mindestens 2 Zeichen bestehen und darf "
                                           "maximal 40 Zeichen lang sein.")])

    email = EmailField('E-Mail-Address',
                       [DataRequired("Du musst deine E-Mail-Adresse angeben."),
                        Email("Bitte gibt eine gültige E-Mail-Adresse an.")])

    remember_me = BooleanField("Angemeldet bleiben")

    btn_safe = SubmitField("Registrieren")


class LoginForm(BugFixForm):
    email = EmailField('E-Mail-Address',
                       [DataRequired("Du musst deine E-Mail-Adresse angeben."),
                        Email("Bitte gibt eine gültige E-Mail-Adresse an.")])

    remember_me = BooleanField("Angemeldet bleiben")

    btn_safe = SubmitField("Login")

