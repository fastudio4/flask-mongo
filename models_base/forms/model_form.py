from models_base import base
from .lable_and_message import *
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DateField, SubmitField, IntegerField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired, Length, Email


class ModelsForm(FlaskForm):

    first_name = StringField(label=name,
                             validators=[Length(min=2,max=50), InputRequired(message_required)],
                             render_kw={'placeholder': name,
                                        'class': 'form-control'})
    last_name = StringField(label=subname,
                            validators=[Length(min=2, max=50), InputRequired(message_required)],
                            render_kw={'placeholder': subname,
                                       'class': 'form-control'})
    date_birth = DateField(label=birth,
                           validators=[InputRequired(message_required)],
                           render_kw={'placeholder': format_date,
                                      'class': 'form-control'},
                           format='%d.%m.%Y')
    gender_sex = SelectField(label=gender, validators=[InputRequired(message_required)],
                         choices=[('female', female), ('male', male)],
                         render_kw={'class': 'form-control'})
    base_photo = FileField(label=photo,
                           validators=[FileRequired(message_required), FileAllowed(['jpg', 'jpeg', 'JPEG'], message=message_image_format)])
    telephone = StringField(label=phone,
                             validators=[InputRequired(message_required), Length(min=13, max=13, message=message_phone)],
                             render_kw={'value': '+380',
                                        'class': 'form-control',
                                        'maxlength':13})
    email = StringField(label=e_mail,
                        validators=[InputRequired(message_required), Email(message_email)],
                        render_kw={'class': 'form-control',
                                   'placeholder': e_mail})
    skype_contacts = StringField(label=skype,
                                 render_kw={'class': 'form-control',
                                            'placeholder': skype})
    facebook_contacts = StringField(label=facebook,
                                    render_kw={'class': 'form-control',
                                               'placeholder': facebook})
    height = IntegerField(label=height_cm,
                          validators=[InputRequired(message_required)],
                          render_kw={'class': 'form-control',
                                     'placeholder': '175'})
    weight = IntegerField(label=weight_kg,
                          validators=[InputRequired(message_required)],
                          render_kw={'class': 'form-control',
                                     'placeholder': '54'})
    model_size = StringField(label=model_s, render_kw={'class': 'form-control',
                                     'placeholder': model_s_plc})
    shoe_size = IntegerField(label=shoe_s,
                             validators=[InputRequired(message_required)],
                             render_kw={'class': 'form-control',
                                        'placeholder': '36'})
    additional = TextAreaField(label=add,
                               render_kw={'class': 'form-control',
                                          'placeholder': add_place,
                                          'rows': 3})
    submit = SubmitField(label=submit, render_kw={'class': 'btn btn-primary btn-lg',
                                    'value': button_submit})

    def validate_on_base(self):
        if base.db.models.find_one({'first_name': self.first_name.data, 'last_name': self.last_name.data}):
            self.first_name.errors.append(message_already_exist)
            self.last_name.errors.append(message_already_exist)
            return False
        return True