from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()
#can create more model in own file and import here
class Reptile(db.Model):
    __tablename__ =  'reptiles' 
    
    id = db.Column(db.Integer, primary_key = True) 
    reptile = db.Column(db.String(250)) 
    reptile_description = db.Column(db.Text) 

    