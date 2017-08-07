from models_base import base
from re import findall
from .lable_and_message import *
from flask_wtf import FlaskForm
from models_base.image_save import save_image
from wtforms import StringField, SelectField, DateField, SubmitField, IntegerField, TextAreaField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import InputRequired, Length, Email, regexp, Optional


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
    model_size = StringField(label=model_s,
                             validators=[regexp(r'^\d{2,3}[-]\d{2,3}[-]\d{2,3}$',
                                                message=message_model_size_input_error),
                                         Optional()],
                             render_kw={'class': 'form-control',
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
        if base.db.models.find_one({'telephone': self.telephone.data}):
            self.telephone.errors.append(message_phone_exist)
            return False
        if base.db.models.find_one({'email': self.email.data}):
            self.email.errors.append(message_email_exist)
            return False
        return True

    def dict_data(self):
        new_model = dict()
        image_path = save_image(self.first_name.data, self.last_name.data, self.base_photo.data)
        for key, value in self.data.items():
            if key != 'csrf_token' \
                    and key != 'base_photo' \
                    and key != 'date_birth'\
                    and key != 'submit'\
                    and key != 'model_size':
                new_model[key] = value
        new_model['date_birth'] = {
            'year': self.date_birth.data.year,
            'month': self.date_birth.data.month,
            'day': self.date_birth.data.day
        }
        new_model['base_photo'] = image_path[0]
        new_model['folder_slug'] = image_path[1]
        new_model['model_size'] = self.parse_model_size()
        return new_model

    def parse_model_size(self):
        model_size = dict()
        if self.model_size.data != '':
            size = findall(r'\d{2,3}', self.model_size.data)
            model_size['breast'] = size[0]
            model_size['waist'] = size[1]
            model_size['thighs'] = size[2]
            return model_size
        else:
            return ''