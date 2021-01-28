from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FileField
from wtforms.validators import DataRequired


class MainForm(FlaskForm):
    q1 = SelectField('5S seems to be the way of life rather than a routine:', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    q1Notes = StringField('Notes', render_kw={"placeholder" : "Notes"})
    q1Asset = FileField('Upload Asset')
    q2 = SelectField('Success stories are being displayed (i.e., before and after):', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    q2Notes = StringField('Notes', render_kw={"placeholder" : "Notes"})
    q2Asset = FileField('Upload Asset')
    q3 = SelectField('Rewards and recognition is part of the 5S system:', choices=[('yes', 'Yes'), ('no', 'No')], validators=[DataRequired()])
    q3Notes = StringField('Notes', render_kw={"placeholder" : "Notes"})
    q3Asset = FileField('Upload Asset')