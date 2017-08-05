import datetime
from .image_save import save_image
from . import app, base
from flask import render_template, request
from .forms import ModelsForm, FilterModels

from pprint import pprint


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ModelsForm()
    if form.validate_on_submit() and form.validate_on_base():
        image_path = save_image(form.first_name.data, form.last_name.data, form.base_photo.data)
        new_model = dict()
        for key, value in form.data.items():
            if key != 'csrf_token' and key != 'base_photo' and key != 'date_birth':
                new_model[key] = value
        new_model['date_birth'] = {
            'year': form.date_birth.data.year,
            'month': form.date_birth.data.month,
            'day': form.date_birth.data.day
        }
        new_model['base_photo'] = image_path
        model = base.db.models
        model.insert_one(new_model)
        print(new_model)
        return render_template('page_masage_complite.html', title='Форма отправленна')
    return render_template('forms.html', form=form, title='Form model')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    filter = FilterModels()
    if request.method == 'POST':
        request_dict = {}
        for key, value in filter.data.items():
            if value is not None and value != '' and key != 'csrf_token':
                request_dict[key] = value
        print(request_dict)
    all_models = base.db.models.find({})
    return render_template('list_models.html', title='Model base', all_models=all_models, filter=filter)