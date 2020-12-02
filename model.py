from settings import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import joinedload,backref
from datetime import datetime
import json
import pprint




class Activity(db.Model):

    __tablename__ = "activities"
        
    activity_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    activity_name = db.Column(db.String())
    min_cost = db.Column(db.Integer)
    max_cost = db.Column(db.Integer)
    min_age = db.Column(db.Integer)
    max_age = db.Column(db.Integer)
    location = db.Column(db.String())
    effort_rating = db.Column(db.String())
    keywords = db.Column(db.String())
    activity_description = db.Column(db.JSON())
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    interests = db.relationship("Interest",
                            secondary="activities_interests", back_populates="activities")
    users = db.relationship("User",
                            secondary="users_activities", back_populates="activities")
    materials = db.relationship("Material",
                            secondary="activities_materials", back_populates="activities")
    time_periods = db.relationship("TimePeriod",
                            secondary="activities_time_periods", back_populates="activities")
    comments = db.relationship("Comment",
                            secondary="activities_comments", back_populates="activities")

    activities_interests = db.relationship("ActivityInterest", back_populates="activities", cascade="all, delete")
    activities_time_periods= db.relationship("ActivityTimePeriod", back_populates="activities", cascade="all, delete")
    activities_comments= db.relationship("ActivityComment", back_populates="activities", cascade="all, delete")
    users_activities= db.relationship("UserActivity", back_populates="activities", cascade="all, delete")
    activities_materials= db.relationship("ActivityMaterial", back_populates="activities", cascade="all, delete")



    def __repr__(self):
        return f'<Activity activity_id={self.activity_id} name={self.activity_name}>'



        
class Interest(db.Model):

    __tablename__ = "interests"

    interest_id = db.Column(db.Integer,
                            autoincrement=True,
                            primary_key=True)
    interest_name = db.Column(db.String())

    children = db.relationship("Child",
                            secondary="children_interests", back_populates="interests")    
    activities = db.relationship("Activity",
                            secondary="activities_interests", back_populates="interests")
    time_periods = db.relationship("TimePeriod",
                            secondary="interests_time_periods", back_populates="interests")


    activities_interests = db.relationship("ActivityInterest", back_populates="interests", cascade="all, delete")
    children_interests= db.relationship("ChildInterest", back_populates="interests", cascade="all, delete")
    interests_time_periods= db.relationship("InterestsTimePeriod", back_populates="interests", cascade="all, delete")

    def __repr__(self):
        return f'<Interest interest_id={self.interest_id} name={self.interest_name}>'

    def __init__(self,interest_name):
        self.interest_name=interest_name

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        primary_key=True,
                        autoincrement=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    username = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    zipcode = db.Column(db.Integer)
    photo = db.Column(db.String())


    children = db.relationship("Child",
                            secondary="users_children", back_populates="users", cascade="all, delete")
    comments = db.relationship("Comment",
                            secondary="users_comments", back_populates="users", cascade="all, delete")
    activities = db.relationship("Activity",
                            secondary="users_activities", back_populates="users", cascade="all, delete")  
    users_activities= db.relationship("UserActivity", back_populates="users", cascade="all, delete")
    users_comments= db.relationship("UserComment", back_populates="users", cascade="all, delete")
    users_children= db.relationship("UserChild", back_populates="users", cascade="all, delete")
    
    def __repr__(self):
        return f'<User user_id={self.user_id} first_name={self.first_name} last_name={self.last_name} email={self.email}>'


class Child(db.Model):
    """A child of User"""

    __tablename__ = "children"

    child_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    child_name = db.Column(db.String())
    birthdate = db.Column(db.String())
    gender = db.Column(db.String())
    photo = db.Column(db.String())

    interests = db.relationship("Interest",
                            secondary="children_interests", back_populates="children")
    users = db.relationship("User",
                            secondary="users_children", back_populates="children") 

    users_children= db.relationship("UserChild", back_populates="children", cascade="all, delete")
    children_interests= db.relationship("ChildInterest", back_populates="children", cascade="all, delete")

    
    def __repr__(self):
        return f'<Child child_id={self.child_id} name={self.child_name}>'

class Comment(db.Model):
    """A comment"""

    __tablename__ = "comments"

    comment_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    comment_text = db.Column(db.Text())
    star_rating = db.Column(db.Integer)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    users = db.relationship("User",
                            secondary="users_comments", back_populates="comments", cascade="all, delete") 
    activities = db.relationship("Activity",
                            secondary="activities_comments",back_populates="comments", cascade="all, delete") 
    activities_comments= db.relationship("ActivityComment", back_populates="comments", cascade="all, delete")
    users_comments= db.relationship("UserComment", back_populates="comments", cascade="all, delete")
    


    def __repr__(self):
        return f'<Comment comment_id={self.comment_id} name={self.star_rating}>'

class Material(db.Model):
    """Activity materials"""

    __tablename__ = "materials"

    material_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    material_name = db.Column(db.String())
    material_cost = db.Column(db.Integer)
    material_url = db.Column(db.String())

    activities = db.relationship("Activity",
                            secondary="activities_materials", back_populates="materials", cascade="all, delete")
    activities_materials= db.relationship("ActivityMaterial", back_populates="materials", cascade="all, delete")

    def __repr__(self):
        return f'<Material material_id={self.material_id} name={self.material_name}>'

class TimePeriod(db.Model):
    """A time period in the year"""

    __tablename__ = "time_periods"

    time_period_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    time_period_name = db.Column(db.String())

    activities = db.relationship("Activity",
                            secondary="activities_time_periods", back_populates="time_periods", cascade="all, delete")
    interests = db.relationship("Interest",
                            secondary="interests_time_periods", back_populates="time_periods", cascade="all, delete")

    interests_time_periods= db.relationship("InterestsTimePeriod", back_populates="time_periods", cascade="all, delete")
    activities_time_periods= db.relationship("ActivityTimePeriod", back_populates="time_periods", cascade="all, delete")




    def __repr__(self):
        return f'<Time Period time_period_id={self.time_period_id} name={self.time_period_name}>'


""" Many to Many Bridge Tables"""

class ActivityInterest(db.Model):
    

    __tablename__ = "activities_interests"

    activity_interest_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interests.interest_id'), primary_key=True)

    activities= db.relationship(Activity, backref=backref("interests_assoc"))
    interests= db.relationship(Interest, backref=backref("activities_assoc"))

class ActivityMaterial(db.Model):
    

    __tablename__ = "activities_materials"

    activity_material_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), primary_key=True)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.material_id'), primary_key=True)

    activities= db.relationship(Activity, backref=backref("materials_assoc"))
    materials= db.relationship(Material, backref=backref("activities_assoc"))

class ChildInterest(db.Model):


    __tablename__ = "children_interests"

    child_interest_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interests.interest_id'), primary_key=True)

    children = db.relationship(Child, backref=backref("interests_assoc"))
    interests= db.relationship(Interest, backref=backref("children_assoc"))

class UserChild(db.Model):

    __tablename__ = "users_children"

    user_child_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    child_id = db.Column(db.Integer, db.ForeignKey('children.child_id'), primary_key=True)

    children = db.relationship(Child, backref=backref("users_assoc"))
    users= db.relationship(User, backref=backref("children_assoc"))

    def __repr__(self):
        return f'<UserChild id={self.user_child_id} user={self.user_id} child = {self.child_id}>'

class UserComment(db.Model):

    __tablename__ = "users_comments"

    user_comment_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'), primary_key=True)

    comments = db.relationship(Comment, backref=backref("users_assoc"))
    users= db.relationship(User, backref=backref("comments_assoc"))

class UserActivity(db.Model):

    __tablename__ = "users_activities"

    user_activity_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), primary_key=True)

    activities = db.relationship(Activity, backref=backref("users_assoc"))
    users= db.relationship(User, backref=backref("activities_assoc"))


class ActivityComment(db.Model):

    __tablename__ = "activities_comments"

    activity_comment_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), primary_key=True)
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.comment_id'), primary_key=True)

    activities = db.relationship(Activity, backref=backref("comments_assoc"))
    comments= db.relationship(Comment, backref=backref("activities_assoc"))

class ActivityTimePeriod(db.Model):
    """A time period in the year"""

    __tablename__ = "activities_time_periods"

    activity_time_period_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    activity_id = db.Column(db.Integer, db.ForeignKey('activities.activity_id'), primary_key=True)
    time_period_id = db.Column(db.Integer, db.ForeignKey('time_periods.time_period_id'), primary_key=True)

    activities = db.relationship(Activity, backref=backref("time_periods_assoc"))
    time_periods= db.relationship(TimePeriod, backref=backref("activities_assoc"))

class InterestsTimePeriod(db.Model):
    """A time period in the year"""

    __tablename__ = "interests_time_periods"

    interest_time_period_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    interest_id = db.Column(db.Integer, db.ForeignKey('interests.interest_id'), primary_key=True)
    time_period_id = db.Column(db.Integer, db.ForeignKey('time_periods.time_period_id'), primary_key=True)


    interests = db.relationship(Interest, backref=backref("time_periods_assoc"))
    time_periods= db.relationship(TimePeriod, backref=backref("interests_assoc"))


if __name__ == '__main__':
    from settings import app, connect_to_db
    connect_to_db(app)