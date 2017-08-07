from . import app, base
from flask import render_template, request
from .forms import ModelsForm, FilterModels
from datetime import date
from pprint import pprint


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ModelsForm()
    if form.validate_on_submit() and form.validate_on_base():
        model = base.db.models
        model.insert_one(form.dict_data())
        return render_template('page_masage_complite.html', title='Форма отправленна')
    return render_template('forms.html', form=form, title='Форма модели')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    filter = FilterModels()
    if request.method == 'POST':
        pprint(filter.parse_request_filter())
    all_models = base.db.models.find({})
    return render_template('list_models.html', title='Model base', all_models=all_models, filter=filter)

@app.route('/admin/<slug>')
def model_params(slug):
    model = base.db.models.find_one({'folder_slug': slug})
    if model is not None:
        date_now = date.today()
        return render_template('model_params.html', model=model, date_now=date_now)

@app.route('/admin/<slug>/update', methods=['GET', 'POST'])
def update_model(slug):
    model = base.db.models.find_one({'folder_slug': slug})