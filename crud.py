from model import User, Child, Activity, UserActivity, Material, TimePeriod, Interest, Comment
from settings import db, connect_to_db
from datetime import date, datetime
import json
from sqlalchemy.sql import func, desc



##CREATE OBJECTS#
###################################################################################################

def create_activity(activity_name, min_cost, max_cost, min_age, max_age, location, effort_rating, keywords, activity_description):
    """Create and return a new activity."""

    activity = Activity(activity_name=activity_name,min_cost=min_cost, max_cost=max_cost, min_age=min_age, max_age=max_age, location=location, effort_rating=effort_rating, keywords=keywords, activity_description=activity_description)

    db.session.add(activity)
    db.session.commit()

    return activity

def create_user(first_name,last_name, email, username, password, zipcode, photo="/static/img/woman13.png"):
    """Create and return a new user."""

    user = User(first_name=first_name, last_name=last_name, email=email, username=username,  
                password=password, zipcode=zipcode, photo=photo)

    db.session.add(user)
    db.session.commit()

    return user

def create_child(child_name, birthdate, gender, photo):
    """Create and return a new user."""

    child = Child(child_name=child_name, birthdate=birthdate, gender=gender, photo=photo)

    db.session.add(child)
    db.session.commit()

    return child

def create_interest(interest_name):
    """Create and return a new user."""

    interest=Interest(interest_name=interest_name)

    db.session.add(interest)
    db.session.commit()

    return interest

def create_comment(comment_text, star_rating):

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

def get_child_by_id(child_id):

    child=db.session.query(Child).filter_by(child_id=child_id).first()

    return child

def get_all_activities():

    return Activity.query.all()


def get_activity_age_interest(child_id):

    child = db.session.query(Child).filter_by(child_id=child_id).first()

    child_age = calculate_age(child.birthdate)

    interests=[]
    for interest in child.interests:
        interests.append(interest.interest_id)

    q = db.session.query(Activity).filter((Activity.min_age <= child_age) & (Activity.max_age >= child_age))
    q= q.join("activities_interests","interests").filter(Interest.interest_id.in_(interests))
    
    return q


def calculate_age(born):
    today = date.today()
    born = datetime.strptime(born, "%m/%d/%Y")

    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def create_activity_description(activity_name, overview, overview_pic, step_1, photo_1, step_2, photo_2, step_3, photo_3, step_4, photo_4, step_5, photo_5,
step_6, photo_6):

    activity_description= {"overview": {
                                    "Overview": overview, 
                                    "photo": overview_pic
                                }, 
                                "step_1": {
                                    "Step 1":step_1, 
                                    "photo":photo_1
                                }, 
                                "step_2": {
                                    "Step 2":step_2, 
                                    "photo":photo_2
                                }, 
                                "step_3":{
                                    "Step 3":step_3, 
                                    "photo": photo_3
                                }, 
                                "step_4": {
                                    "Step 4":step_4, 
                                    "photo": photo_4
                                }, 
                                "step_5": {
                                    "Step 5":step_5, 
                                    "photo": photo_5
                                }, 
                                "step_6": {
                                    "Step 6":step_6, 
                                    "photo": photo_6
                                }
                            }

    return activity_description


def filter_and_get_activities(datastring, materials, interests, time_periods, effort_rating, min_cost, max_cost, min_age, max_age, hiddenField):

    activities_query = db.session.query(Activity)

    if hiddenField != None:
        activities_query = activities_query.filter(Activity.keywords.contains(hiddenField))

    if effort_rating:
        activities_query = (
            activities_query.filter(Activity.effort_rating.in_(effort_rating))
        )
    
    if min_cost:
        activities_query = (
            activities_query.filter(Activity.min_cost <= min_cost)
        )
    if max_cost:
        activities_query = (
            activities_query.filter(Activity.max_cost <= max_cost)
        )

    if min_age:
        activities_query = (
            activities_query.filter(Activity.min_age <= min_age)
        )
    if max_age: 
        activities_query = (
            activities_query.filter(Activity.max_age >= max_age)
        )

    if materials:
        activities_query = (
            activities_query
                .join("activities_materials", "materials")
                .filter(Material.material_id.in_(materials))
        )
    if interests:
        activities_query=(
            activities_query
            .join("activities_interests","interests")
            .filter(Interest.interest_id.in_(interests))
        )
    if time_periods:
        activities_query = (
            activities_query
            .join("activities_time_periods","time_periods")
            .filter(TimePeriod.time_period_id.in_(time_periods))
        )       
    return activities_query

def get_and_edit_activity(activity_id, activity_name, min_age, max_age, min_cost, max_cost, location, effort_rating, keywords,
overview, overview_pic, step_1, photo_1, step_2, photo_2, step_3, photo_3, step_4, photo_4, step_5, photo_5,
step_6, photo_6):

    activity = get_activity_by_id(activity_id)

    if activity_name:
        activity.activity_name= activity_name 
    if overview:
        activity.activity_description['overview']['Overview'] = overview
    if overview_pic:
        activity.activity_description['overview']['Overview'] = overview_pic 
    if step_1: 
        activity.activity_description['step_1']['Step 1'] = step_1 
    if photo_1: 
        activity.activity_description['step_1']['photo'] = photo_1
    if step_2: 
        activity.activity_description['step_2']['Step 2'] = step_2 
    if photo_2: 
        activity.activity_description['step_2']['photo'] = photo_2
    if step_3: 
        activity.activity_description['step_3']['Step 3'] = step_3 
    if photo_3: 
        activity.activity_description['step_3']['photo'] = photo_3
    if step_4: 
        activity.activity_description['step_4']['Step 4'] = step_4 
    if photo_4: 
        activity.activity_description['step_4']['photo'] = photo_4 
    if step_5: 
        activity.activity_description['step_5']['Step 5'] = step_5 
    if photo_5: 
        activity.activity_description['step_5']['photo'] = photo_5 
    if step_6: 
        activity.activity_description['step_6']['Step 6'] = step_6 
    if photo_6: 
        activity.activity_description['step_6']['photo'] = photo_6 
    if keywords: 
        activity.keywords = keywords 
    if location: 
        activity.location = location 
    if min_cost: 
        activity.min_cost = min_cost
    if max_cost: 
        activity.max_cost = max_cost
    if min_age: 
        activity.min_age = min_age
    if max_age: 
        activity.max_age = max_age
    if effort_rating: 
        activity.effort_rating = effort_rating

    db.session.commit()
    
    return activity


def get_avg_star_rating(activity_id):

    avg_rating=db.session.query(func.avg(Comment.star_rating)).join("activities_comments","activities").filter(Activity.activity_id == activity_id)
    avg_rating=avg_rating.scalar()
    
    if avg_rating != None: 
        avg_rating=float(avg_rating)
    else:
        avg_rating=0
    
    return avg_rating

def get_rating_count(activity_id):

    rating_count=db.session.query(func.count(Comment.star_rating)).join("activities_comments","activities").filter(Activity.activity_id == activity_id)
    rating_count=rating_count.scalar()

    return rating_count

def get_recent_activities():

    recent_activities=Activity.query.order_by(desc(Activity.timestamp)).limit(3).all()

    return recent_activities

def is_fav(user_id,activity_id):

    user=User.query.get(user_id)
    activity=Activity.query.get(activity_id)

    fav=UserActivity.query.filter((UserActivity.user_id==user_id) & (UserActivity.activity_id==activity_id)).first()

    if fav:
        return 1
    else:
        return 0
    

def unfav(user_id, activity_id):

    user=User.query.get(user_id)
    activity=Activity.query.get(activity_id)

    fav=UserActivity.query.filter((UserActivity.user_id==user_id) & (UserActivity.activity_id==activity_id)).first()
    db.session.delete(fav)
    db.session.commit()




####################################################################################################

if __name__ == '__main__':
    from server import app
    connect_to_db(app)