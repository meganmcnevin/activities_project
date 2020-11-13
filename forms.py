from flask_wtf import FlaskForm
from wtforms import Form, StringField, SelectField, DecimalField, RadioField, SelectMultipleField, TextAreaField, IntegerField, PasswordField, widgets, SubmitField, BooleanField, validators
from flask_table import Table, Col, LinkCol
# from passlib.hash import sha256_crypt


class ActivitySearchForm(Form):
    choices = [('Name','Name'),('Description','Description'),('Effort','Effort')]
    select = SelectField('Search for activity:', choices=choices)
    search = StringField('')


class ActivityForm(Form):
    interest_types = [('Drawing','Drawing'), ('Painting','Painting'), ('Paper Craft','Paper Craft'), ('Pottery','Pottery'), ('Photography','Photography'), 
                        ('Knitting','Knitting'), ('Sewing','Sewing'), ('Water Play','Water Play'), ('Bubbles','Bubbles'), ('Camping','Camping'),
                        ('Nature play','Nature play'),('Dress up','Dress up'),( 'Role play','Role play'),('Puppets','Puppets'),
                        ('Dancing','Dancing'),('Singing','Singing'),('Music','Music'),('Storytelling','Storytelling'),('Baking','Baking'),
                        ('Magic','Magic'),('Scientific Experiments','Scientific Experiments'),('Programming','Programming'),('Star gazing','Star gazing'),
                        ('Sports','Sports'),('Active play','Active play'),('Yoga','Yoga')]
    time_period = [('Winter','Winter'),('Spring','Spring'),('Summer','Summer'),('Fall','Fall')]
    effort_rating=[('Quick and Easy','Quick and Easy'),('A little involved','A little involved'),('Somewhat time intensive','Somewhat time intensive'),('Maximum effort required','Maximum effort required')]
    activity_name = StringField('Activity Name')
    activity_description = TextAreaField('Description')
    interest_name = SelectMultipleField('Interest', choices = interest_types)
    time_period = SelectMultipleField('Time of Year', choices=time_period)
    min_cost=IntegerField('Minimum Cost')
    max_cost=IntegerField('Maximum Cost')
    min_age=IntegerField('Minimum Age')
    max_age=IntegerField('Maximum Age')
    effort_rating=SelectField('Effort involved',choices=effort_rating)
    

    def set_choices(self):
        self.interests.choices = [(i.interest_id,i.interest_name) for i in Interest.query.all()]
        

def save_user_changes(user, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    user.first_name  = form.first_name.data
    user.last_name  = form.last_name.data
    user.email = form.email.data
    user.password = sha256_crypt.encrypt((str(form.password.data)))
    user.zipcode=form.zipcode.data

    if new:
        # Add the new album to the database
        db.session.add(user)
    # commit the data to the database
    db.session.commit()

def save_changes(activity, form, new=False):
    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    
    timeperiod = TimePeriod()
    timeperiod.time_period = form.time_period.data

    activity=Activity()
    activity.activity_name = form.activity_name.data
    activity.activity_description = form.activity_description.data
    activity.min_cost = form.min_cost.data
    activity.max_cost = form.max_cost.data
    activity.min_age = form.min_age.data
    activity.max_age = form.max_age.data
    activity.effort_rating = form.effort_rating.data
    activity.photo_path = form.photo_path.data

    if new:
        # Add the new activity to the database
        db.session.add(activity)
    
    interest_name=form.interest_name.data
    

    for i in interest_name:
        i=i.lower()
        interest = db.session.query(Interest).filter_by(interest_name=i).first()
        print(interest)
        activity.interest.append(interest)
    # commit the data to the database
    db.session.commit()

class Results(Table):
    activity_id = Col('Id', show=False)
    activity_name = Col('Activity Name')
    activity_description = Col('Description')
    min_cost = Col('Minimum Cost')
    max_cost = Col('Maximum Cost')
    min_age = Col('Minimum Age')
    max_age = Col('Maximum Age')
    effort_rating = Col('Effort')
    edit = LinkCol('Edit', 'edit', url_kwargs=dict(activity_id='activity_id'))
    delete = LinkCol('Delete', 'delete', url_kwargs=dict(activity_id='activity_id'))


class RegistrationForm(Form):
    first_name = StringField('First Name', [validators.Length(min=2, max=20)])
    last_name = StringField('Last Name', [validators.Length(min=2, max=20)])
    email = StringField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    zipcode=IntegerField('Zip Code')

class LoginForm(FlaskForm):
    email = StringField('Username',[validators.Required()])
    password = PasswordField('Password',[validators.Required()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

if __name__ == '__main__':
    from server import app
    connect_to_db(app)