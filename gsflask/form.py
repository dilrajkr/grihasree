from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SelectField,SubmitField
from wtforms.validators import DataRequired,Length

class OrderForm(FlaskForm):
    Area=SelectField(label='Area',validators=[DataRequired()],choices=['Kochi Corporation','Udayamperoor'])
    Service=SelectField(label='Service',validators=[DataRequired()] ,choices=['Plumber','Electrician'])
    ContactNumber=StringField(label='Contact Number',validators=[Length(min=5,max=10)])
    Submit=SubmitField(label='Get a call')