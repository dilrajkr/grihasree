from gsflask import db

class WorkOrder(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    Area=db.Column(db.String,nullable=False)
    Service=db.Column(db.String,nullable=False)
    ContactNumber=db.Column(db.String(10),nullable=False)

    def __repr__(self):
        return f'{self.Area}:{self.Service}:{self.ContactNumber}'