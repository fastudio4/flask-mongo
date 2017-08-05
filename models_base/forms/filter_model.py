from .lable_and_message import *
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField

class FilterModels(FlaskForm):

    first_name = StringField(label=name, render_kw={'placeholder': name, 'class': 'form-control'})
    last_name = StringField(label=subname, render_kw={'placeholder': subname,  'class': 'form-control'})

    gender = SelectField(label=gender, choices=[('None', all_), ('female', female), ('male', male)])

    height_min = IntegerField(render_kw={'class': 'form-control', 'placeholder': min_value})
    height_max = IntegerField(render_kw={'class': 'form-control', 'placeholder': max_value})

    weight_min = IntegerField(render_kw={'class': 'form-control', 'placeholder': min_value})
    weight_max = IntegerField(render_kw={'class': 'form-control', 'placeholder': max_value})

    shoe_min = IntegerField(render_kw={'class': 'form-control', 'placeholder': min_value})
    shoe_max = IntegerField(render_kw={'class': 'form-control', 'placeholder': max_value})

    breast_min = IntegerField(render_kw={'class': 'form-control', 'placeholder': min_value})
    breast_max = IntegerField(render_kw={'class': 'form-control', 'placeholder': max_value})

    waist_min = IntegerField(render_kw={'class': 'form-control', 'placeholder': min_value})
    waist_max = IntegerField(render_kw={'class': 'form-control', 'placeholder': max_value})

    thighs_min = IntegerField(render_kw={'class': 'form-control', 'placeholder': min_value})
    thighs_max = IntegerField(render_kw={'class': 'form-control', 'placeholder': max_value})

    age_min = IntegerField(render_kw={'class': 'form-control', 'placeholder': min_value})
    age_max = IntegerField(render_kw={'class': 'form-control', 'placeholder': max_value})

