from .image_save import save_image
from . import app, base
from flask import render_template
from .forms import ModelsForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ModelsForm()
    if form.validate_on_submit() and form.validate_on_base():
        image_path = save_image(form.first_name.data, form.last_name.data, form.base_photo.data)
        model = base.db.models
        model.insert({
            'first_name': form.first_name.data,
            'last_name': form.last_name.data,
            'base_photo': image_path
        })
        return render_template('page_masage_complite.html', title='Форма отправленна')
    return render_template('forms.html', form=form, title='Form model')

@app.route('/admin')
def admin():
    all_models = base.db.models.find({})
    return render_template('list_models.html', title='Model base', all_models=all_models)