from gsflask import app,db
from flask import render_template
from gsflask.form import OrderForm
from gsflask.models import WorkOrder

@app.route('/',methods=['GET','POST'])
def index():
    form=OrderForm()
    if form.validate_on_submit():
        order1=WorkOrder(Area=form.Area.data,Service=form.Service.data,ContactNumber=form.ContactNumber.data)
        db.session.add(order1)
        db.session.commit()
        return 'Your request is registered and you will get a call in 15 minutes'
    return render_template('index.html',form=form)
