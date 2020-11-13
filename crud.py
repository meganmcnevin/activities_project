from model import User, Child, Activity, Material, TimePeriod, Interest, Comment
from settings import db, connect_to_db
from datetime import date, datetime


##CREATE OBJECTS#
###################################################################################################

def create_activity(activity_name, min_cost, max_cost, min_age, max_age, location, effort_rating, activity_description):
    """Create and return a new activity."""

    activity = Activity(activity_name=activity_name,min_cost=min_cost, max_cost=max_cost, min_age=min_age, max_age=max_age, location=location, effort_rating=effort_rating, activity_description=activity_description)

    db.session.add(activity)
    db.session.commit()

    return activity

def create_user(first_name,last_name, email, password, zipcode):
    """Create and return a new user."""

    user = User(first_name=first_name, last_name=last_name, email=email, 
                password=password, zipcode=zipcode)

    db.session.add(user)
    db.session.commit()

    return user

def create_child(child_name, birthdate, gender):
    """Create and return a new user."""

    child = Child(child_name=child_name, birthdate=birthdate, gender=gender)

    db.session.add(child)
    db.session.commit()

    return child

def create_interest(interest_name):
    """Create and return a new user."""

    interest=Interest(interest_name=interest_name)

    db.session.add(interest)
    db.session.commit()

    return interest

def create_comment(comment_text,star_rating):

    comment = Comment(comment_text=comment_text,star_rating=star_rating)
    
    db.session.add(comment)
    db.session.commit()

    return comment

def create_time_period(time_period_name):

    time_period = TimePeriod(time_period_name=time_period_name)

    db.session.add(time_period)
    db.session.commit()

    return time_period 

def create_material(material_name, material_cost, material_url):


    material = Material(material_name=material_name, material_cost=material_cost, material_url=material_url)

    db.session.add(material)
    db.session.commit()

    return material


#FUNCTIONS#
###################################################################################################

def get_activity_by_id(activity_id):
    """Return a movie by primary key."""

    return Activity.query.get(activity_id)

def get_name_by_email(email):

    user_name=db.session.query(User).filter_by(email=email).first()

    return user_name.first_name

def get_user_by_id(user_id):

    user=db.session.query(User).filter_by(user_id=user_id).first()

    return user

def get_all_activities():

    return Activity.query.all()


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def create_activity_description(activity_name, min_age, max_age, min_cost, max_cost, location, effort_rating,
overview, overview_pic, step_1, photo_1, step_2, photo_2, step_3, photo_3, step_4, photo_4, step_5, photo_5,
step_6, photo_6):
    activity_description= {"activity_name":activity_name, "min_age": min_age, "max_age": max_age, 
                            "min_cost": min_cost, "max_cost": max_cost, "location": location, 
                            "effort_rating":effort_rating, "activity_description": {
                                "overview": {
                                    "Overview": overview, 
                                    "photo": overview_pic
                                }, 
                                "step_1": {
                                    "Step 1":step_1, 
                                    "photo":photo_1
                                }, 
                                "step_2": {
                                    "Step 1":step_2, 
                                    "photo":photo_2
                                }, 
                                "step_3":{
                                    "Step 1":step_3, 
                                    "photo": photo_3
                                }, 
                                "step_4": {
                                    "Step 1":step_4, 
                                    "photo": photo_4
                                }, 
                                "step_5": {
                                    "Step 1":step_5, 
                                    "photo": photo_5
                                }, 
                                "step_6": {
                                    "Step 1":step_6, 
                                    "photo": photo_6
                                }
                            }}

    return activity_description


def filter_and_get_activities(materials, interests, time_periods):
    pass

####################################################################################################


if __name__ == '__main__':
    from server import app
    connect_to_db(app)