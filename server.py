from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template
import crud 
from settings import app, connect_to_db, db
from model import  User, Child, UserChild, Interest, Activity, Comment, Material, TimePeriod
from datetime import date
from forms import ActivitySearchForm, save_changes, Results
from flask_table import Table, Col


# @app.route('/setsession')
# def setsession():
#     session['Username'] = 'Admin'
#     return f"The session has been Set"
 
# @app.route('/getsession')
# def getsession():
#     if 'Username' in session:
#         Username = session['Username']
#         return f"Welcome {Username}"
#     else:
#         return "Welcome Anonymous"
 
# @app.route('/popsession')
# def popsession():
#     session.pop('Username',None)
#     return "Session Deleted"
###################################################################################################


@app.route('/', methods =['GET', 'POST'])
def index():
    # Check if user is loggedin

    search = ActivitySearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
        return render_template('index.html', form=search, name=session['name'])

    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('index.html', form=search, name=session['name'])
    # User is not loggedin redirect to login page
    if request.method == 'GET':
        return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login Form"""
    if request.method == 'GET':
        return render_template('login.html')
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user=db.session.query(User).filter_by(email=email).first()
        
        if user.email == email:
            if password == user.password:
                session['loggedin'] = True
                session['email']= user.email
                session['id'] = user.user_id
                session['name'] = user.first_name
                # return render_template('profile.html', user=user, name=session['name'])
                return redirect('/profile')
        else:
            return 'Incorrect username/password'
    
    return redirect('/')

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     search = ActivitySearchForm(request.form)
#     if request.method == 'POST':
#         return search_results(search)
#     return render_template('index.html', form=search)

@app.route('/profile')
def profile():
    # Check if user is loggedin
    if 'loggedin' in session:
        # We need all the account info for the user so we can display it on the profile page

        user = crud.get_user_by_id(session['id'])
        children=user.children
        
        # Show the profile page with account info
        return render_template('profile.html', user=user, children=children, name=session['name'])
    # User is not loggedin redirect to login page
    return render_template('login.html')

def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('name', None)
   # Redirect to login page
   return render_template('login.html')


###################################################################################################


@app.route('/register' , methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
 
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email=request.form['email']
        password = request.form['password']
        zipcode = request.form['zipcode']

        db.session.add(user)
        db.session.commit()
        
        return render_template('/login.html')

@app.route('/add_child' , methods = ['GET','POST'])
def add_child():

    user = crud.get_user_by_id(session['id'])
    if request.method == 'GET':
        return render_template('add_child.html')
 
    if request.method == 'POST':
        child_name=request.form['child_name']
        birthdate=request.form['birthdate']
        gender = request.form['gender']
        interests = request.form.getlist('interests[]')
        
        add_child = crud.create_child(child_name,birthdate,gender)
        
        db.session.add(add_child)
        
        for i in interests:
            interest = db.session.query(Interest).filter_by(interest_name=i).first()
            add_child.interests.append(interest)
        
        user.children.append(add_child)
        db.session.commit()

        return redirect('/success')



###################################################################################################

@app.route('/new_activity' , methods = ['GET','POST'])
def new_activity():
    """Add a new Activity"""

    materials=Material.query.all()
    interests=Interest.query.all()
    time_periods=TimePeriod.query.all()

    if request.method == 'GET':
        
        return render_template('new_activity.html', materials=materials, interests=interests, time_periods=time_periods)
 
    if request.method == 'POST':
        activity_name= request.form['activity_name']
        overview= request.form['overview']
        overview_pic= request.form['overview_pic']
        step_1 = request.form['step_1']
        photo_1= request.form['photo_1']
        step_2 = request.form['step_2']
        photo_2 = request.form['photo_2']
        step_3 = request.form['step_3']
        photo_3= request.form['photo_3']
        step_4 = request.form['step_4']
        photo_4 = request.form['photo_4']
        step_5 = request.form['step_5']
        photo_5 = request.form['photo_5']
        step_6 = request.form['step_6']
        photo_6 = request.form['photo_6']

        location = request.form['location']
        min_cost=request.form['min_cost']
        max_cost=request.form['max_cost']
        min_age=request.form['min_age']
        max_age=request.form['max_age']
        effort_rating=request.form['effort_rating']

        materials = request.form.getlist('materials[]')
        interests = request.form.getlist('interests[]')
        time_periods = request.form.getlist('time_periods[]')

        
        activity_description=crud.create_activity_description(activity_name, min_age, max_age, min_cost, max_cost, location, effort_rating,
        overview, overview, step_1, photo_1, step_2, photo_2, step_3, photo_3, step_4, photo_4, step_5, photo_5,
        step_6, photo_6)

        
        activity = crud.create_activity(activity_name, min_age, max_age, min_cost, max_cost, location,
                    effort_rating, activity_description)
        db.session.add(activity)
        db.session.commit()

        if interests:
            for interest_id in interests:
                if interest_id != None:
                    interest = Interest.query.get(interest_id)
                    activity.interests.append(interest)
                    db.session.commit()
            
        if materials:
            for material_id in materials:
                if material_id  != None:
                    material = Material.query.get(material_id)
                    activity.materials.append(material)
                    db.session.commit()
        
        if time_periods:
            for time_period_id in time_periods:
                if time_period_id != None:
                    time_period = TimePeriod.query.get(time_period_id)
                    activity.time_periods.append(time_period)
                    db.session.commit()
        db.session.commit()

        return render_template('/success.html')
    


###################################################################################################

@app.route('/activity/<activity_id>')
def show_activity(activity_id):
    """Show details on a particular activity."""

    activity = crud.get_activity_by_id(activity_id)

    return render_template('activity.html', activity=activity)

@app.route('/activity/add_comment/<activity_id>' , methods = ['GET','POST'])
def add_comment(activity_id):

    activity = crud.get_activity_by_id(activity_id)
    user = crud.get_user_by_id(session['id'])
       
    if request.method == 'GET':
        return render_template('activity.html', activity=activity)
 
    if request.method == 'POST':
        comment_text=request.form['comment']
        star_rating=request.form['rating']
                
        add_comment = crud.create_comment(comment_text,star_rating)
        
        db.session.add(add_comment)
        
        user.comments.append(add_comment)
        activity.comments.append(add_comment)
        db.session.commit()

        return render_template('success.html')

@app.route('/activity/add_favorite/<activity_id>' , methods = ['GET','POST'])
def fav_activity(activity_id):

    activity = crud.get_activity_by_id(activity_id)
    user = crud.get_user_by_id(session['id'])
       
    if request.method == 'GET':
        return render_template('activity.html', activity=activity)
 
    if request.method == 'POST':
        
        user.activities.append(activity)
        db.session.commit()

        return render_template('success.html')


@app.route('/success')
def success():
    return render_template('success.html')


###################################################################################################
@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search_string:
        if search.data['select'] == 'Name':
            qry = db.session.query(Activity).filter(
                Activity.activity_name.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Description':
            qry = db.session.query(Activity).filter(
                Activity.activity_description.contains(search_string))
            results = qry.all()
        elif search.data['select'] == 'Effort':
            qry = db.session.query(Activity).filter(
                Activity.effort_rating.contains(search_string))
            results = qry.all()
        else:
            qry = db.session.query(Activity)
            results = qry.all()
    else:
        qry = db.session.query(Activity)
        results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        table = Results(results)
        table.border=True
        return render_template('results.html', results=results, table=table)


@app.route('/advanced_search')
def display_search_page():
    """Show search form to search for activities."""

    materials=Material.query.all()
    interests=Interest.query.all()
    time_periods=TimePeriod.query.all()

    return render_template('advanced_search.html', materials=materials, interests=interests, time_periods=time_periods)


@app.route('/filter')
def filter_results():

    materials = request.args.getlist('materials[]')
    interests = request.args.getlist('interests[]')
    time_periods = request.args.getlist('time_periods[]')
    effort_rating = request.args.getlist('effort_rating[]')
    
    # results = crud.filter_and_get_activities(materials, interests, time_periods)
    
    activities_query = db.session.query(Activity)

    if effort_rating:
        activities_query = (
            activities_query.filter(Activity.effort_rating.in_(effort_rating))
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

        
    return render_template('filter.html', results=activities_query.all())
    

######################################################################################################

"""ADMIN TOOLS"""""

@app.route('/item/<int:activity_id>', methods=['GET', 'POST'])
def edit(activity_id):
    qry = db.session.query(Activity).filter(
                Activity.activity_id==activity_id)
    activity = qry.first()
    if activity:
        form = ActivityForm(formdata=request.form, obj=activity)
        if request.method == 'POST' and form.validate():
            # save edits
            save_changes(activity, form)
            flash('Activity updated successfully!')
            return redirect('/')
        return render_template('edit_activity.html', form=form)
    else:
        return 'Error loading #{activity_id}'.format(activity_id=activity_id)


@app.route('/delete/<int:activity_id>', methods=['GET', 'POST'])
def delete(activity_id):
    """
    Delete the item in the database that matches the specified
    id in the URL
    """
    qry = db.session.query(Activity).filter(
        Activity.activity_id==activity_id)
    activity = qry.first()
    if activity:
        form = ActivityForm(formdata=request.form, obj=activity)
        if request.method == 'POST' and form.validate():
            # delete the item from the database
            db.session.delete(activity)
            db.session.commit()
            flash('Activity deleted successfully!')
            return redirect('/')
        return render_template('delete_activity.html', form=form)
    else:
        return 'Error deleting #{activity_id}'.format(activity_id=activity_id)

###################################################################################################

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')