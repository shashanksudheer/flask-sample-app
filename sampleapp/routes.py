import os

from flask import redirect, render_template, url_for
from flask import current_app as app
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

from .form import MainForm
from .models import db, Questions
from .js import createModelsFromJSON, openJSON, writeModelsToJSON, writeJSON

# index route
@app.route('/', methods=('GET', 'POST'))
def index():
    form = MainForm()
    if form.validate_on_submit():
        f = form.q1Asset.data
        if f:
            filename = secure_filename(f.filename)
            filepath = os.path.join(
                app.instance_path, 'assets', filename
            )
        f.save(filepath)
        firstq = Questions(
            id="sustain_question_1",
            question="5S seems to be the way of life rather than a routine",
            uresponse=form.q1.data,
            unotes=form.q1Notes.data,
            uasset=filepath if filepath else "na"
        )

        f = form.q2Asset.data
        if f:
            filename = secure_filename(f.filename)
            filepath = os.path.join(
                app.instance_path, 'assets', filename
            )
        secondq = Questions(
            id="sustain_question_2",
            question="Success stories are being displayed (i.e., before and after)",
            uresponse=form.q2.data,
            unotes=form.q2Notes.data,
            uasset=filepath if filepath else "na"
        )

        f = form.q3Asset.data
        if f:
            filename = secure_filename(f.filename)
            filepath = os.path.join(
                app.instance_path, 'assets', filename
            )
        thirdq = Questions(
            id="sustain_question_3",
            question="Rewards and recognition is part of the 5S system",
            uresponse=form.q3.data,
            unotes=form.q3Notes.data,
            uasset=filepath if filepath else "na"
        )
        db.session.add(firstq)
        db.session.add(secondq)
        db.session.add(thirdq)
        db.session.commit()
        return redirect(url_for('/'))
    return render_template('index.html', form=form)
