from flask import Flask, render_template, request, flash, session, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.mutable import Mutable
from jinja2 import Template
from settings import app, connect_to_db, db
from model import  User, Child, UserChild, Interest, Activity, Comment, Material, TimePeriod
from datetime import date
import json
import crud 


###################################################################################################


@app.route('/')
def index():
    # Check if user is logged in
    activities=crud.get_recent_activities()

    if 'loggedin' in session:
        return render_template('index.html', name=session['name'], activities=activities)
    else:
        return render_template('index.html', name="friend", activities=activities)

@app.route('/about')
def about():

    return render_template("about.html")

@app.route('/basic_search')
def search_results():

    basic_search = request.args['basic_search']

    materials=Material.query.all()
    interests=Interest.query.all()
    time_periods=TimePeriod.query.all()

    return render_template("advanced_search.html", basic_search=basic_search, materials=materials, interests=interests, time_periods=time_periods)



@app.route('/advanced_search')
def display_search_page():
    """Show search form to search for activities."""

    materials=Material.query.all()
    interests=Interest.query.all()
    time_periods=TimePeriod.query.all()

    return render_template('advanced_search.html', materials=materials, interests=interests, time_periods=time_periods)


@app.route('/filter', methods=['GET', 'POST'])
def filter_results():

    if request.method == 'GET':
        datastring = request.get_data()
        materials = request.args.getlist('materials[]')
        interests = request.args.getlist('interests[]')
        time_periods = request.args.getlist('time_periods[]')
        effort_rating = request.args.getlist('effort_rating[]')
        min_cost = request.form.get('min_cost')
        max_cost = request.form.get('max_cost')
        min_age = request.form.get('min_age')
        max_age = request.form.get('max_age')
        hiddenField = request.form.get('hiddenField')

        lst=[]
        activities_query = crud.filter_and_get_activities(datastring, materials, interests, time_periods, effort_rating, min_cost, max_cost, min_age, max_age, hiddenField) 

        for i in activities_query:
            lst.append({"activity_name": i.activity_name, "activity_description": i.activity_description, "keywords": i.keywords, "activity_id": i.activity_id})
        

        return jsonify({"activities":lst})

    if request.method == 'POST':
    
        return render_template("index.html")


###################################################################################################

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
                session['username']= user.username
                session['id'] = user.user_id
                session['name'] = user.first_name
                session['photo'] =user.photo
                
                return render_template('profile.html', user=user, name=session['name'])
        else:
            return 'Incorrect username/password'
    
    return redirect('/')


@app.route('/profile')
def profile():
    # Check if user is logged in and sthe profile page with account info
    if 'loggedin' in session:
    
        user = crud.get_user_by_id(session['id'])
        interests=Interest.query.all()
        children=user.children

        return render_template('profile.html', user=user, interests=interests, children=children, name=session['name'])
    
    # If user is not logged in redirect to login page
    return render_template('/')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('email', None)
    session.pop('id', None)
    session.pop('name', None)

# Redirect to login page
    return redirect('/')


###################################################################################################


@app.route('/register' , methods = ['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
 
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email=request.form['email']
        password = request.form['password']
        zipcode = request.form['zipcode']

        user = crud.create_user(first_name,last_name, email, username, password, zipcode)

        return render_template('/index.html')

@app.route('/add_child' , methods = ['GET','POST'])
def add_child():
    
    if 'loggedin' in session:
        user = crud.get_user_by_id(session['id'])

        if request.method == 'GET':
            interests=Interest.query.all()
            return render_template('add_child.html', user=user, interests=interests, name=session['name'])
    
        if request.method == 'POST':
            child_name=request.form['child_name']
            birthdate=request.form['birthdate']
            gender = request.form['gender']
            interests = request.form.getlist('interests[]')
            photo = request.form['photo']
            
            add_child = crud.create_child(child_name,birthdate,gender, photo)
            
            db.session.add(add_child)
            
            for i in interests:
                interest = db.session.query(Interest).filter_by(interest_id=i).first()
                add_child.interests.append(interest)
            
            user.children.append(add_child)
            db.session.commit()
            
            flash("Child added")
            return redirect(url_for('profile'))
            
    flash('Please login')
    return redirect('/login')

@app.route('/profile_edit', methods=['GET', 'POST'])
def profile_edit():

    user = crud.get_user_by_id(session['id'])

    if request.method == 'GET':
        return render_template('profile_edit.html', user=user, name=session['name'])

    if request.method == 'POST':
        
        last_name=request.form['last_name']
        email=request.form['email']
        password = request.form['password']
        zipcode = request.form['zipcode']


        if last_name:
            user.last_name = last_name
        if email:
            user.email= email  
        if password:
            user.password = password
        if zipcode:
            user.zipcode = zipcode

        db.session.commit()

        flash("Profile updated successfully!")
        return redirect(url_for('profile'))
        
        
    else:
        return render_template('index.html', user=user, name=session['name'])

@app.route('/edit_child/<child_id>', methods=['GET', 'POST'])
def edit_child(child_id):

    child= crud.get_child_by_id(child_id)
    interests=Interest.query.all()

    if request.method == 'GET':
        return render_template('edit_child.html', child=child, interests=interests)

    if request.method == 'POST':
        
        photo=request.form['photo']
        interests= request.form.getlist('interests[]')

        if photo:
            child.photo = photo
        
        if interests:
            for interest_id in interests:
                if interest_id != None:
                    interest = Interest.query.get(interest_id)
                    child.interests.append(interest)
                

        db.session.commit()
        
        flash("Child profile updated successfully!")
        return redirect(url_for('profile'))
        
        
    else:
        return render_template('profile.html', user=user, name=session['name'])

###################################################################################################

@app.route('/activity/<activity_id>')
def show_activity(activity_id):
    """Show details on a particular activity."""

    user_id=session['id']

    activity = crud.get_activity_by_id(activity_id)
    avg_rating = crud.get_avg_star_rating(activity_id)
    rating_count = crud.get_rating_count(activity_id)

    is_fav=crud.is_fav(user_id,activity_id)

    return render_template('activity.html', activity=activity, avg_rating=avg_rating, rating_count=rating_count, user=session['id'], is_fav=is_fav)



@app.route('/activity/add_comment/<activity_id>' , methods = ['GET','POST'])
def add_comment(activity_id):

    activity = crud.get_activity_by_id(activity_id)
    user = crud.get_user_by_id(session['id'])
    
    if request.method == 'GET':
        return render_template('activity.html', activity=activity)
 
    if request.method == 'POST':
        comment_text=request.form['comment']
        star_rating=request.form['rating']
                
        add_comment = crud.create_comment(comment_text, star_rating)
        
        db.session.add(add_comment)
        
        user.comments.append(add_comment)
        activity.comments.append(add_comment)
        db.session.commit()

        flash("Comment added")
        return redirect(url_for('show_activity', activity_id = activity_id))
        



@app.route('/activity/add_favorite/<activity_id>' , methods = ['GET','POST'])
def fav_activity(activity_id):

    activity = crud.get_activity_by_id(activity_id)
    user = crud.get_user_by_id(session['id'])
    
    if request.method == 'GET':
        return render_template('activity.html', activity=activity)

    if request.method == 'POST':
        
        user.activities.append(activity)
        db.session.commit()

        flash("Favorite added")
        return redirect(url_for('fav_activity', activity_id = activity_id))



@app.route('/suggest_activities')
def suggest_activities():
    child_id = request.args['personal_activity']

    personal_activity=crud.get_activity_age_interest(child_id)

    return render_template("suggested_activities.html", personal_activity=personal_activity, user=session['id'])



###################################################################################################

"""ADMIN TOOLS FOR ACTIVITY MANAGEMENT"""""

@app.route('/add_activity' , methods = ['GET','POST'])
def add_activity():
    """Add a new Activity"""

    materials=Material.query.all()
    interests=Interest.query.all()
    time_periods=TimePeriod.query.all()

    if request.method == 'GET':
        
        return render_template('add_activity.html', materials=materials, interests=interests, time_periods=time_periods)

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
        keywords= request.form['keywords']
        location = request.form['location']
        min_cost=request.form['min_cost']
        max_cost=request.form['max_cost']
        min_age=request.form['min_age']
        max_age=request.form['max_age']
        effort_rating=request.form['effort_rating']

        materials = request.form.getlist('materials[]')
        interests = request.form.getlist('interests[]')
        time_periods = request.form.getlist('time_periods[]')

        
        activity_description=crud.create_activity_description(activity_name,overview, overview_pic, step_1, photo_1, step_2, photo_2, step_3, photo_3, step_4, photo_4, step_5, photo_5, step_6, photo_6)

        
        activity = crud.create_activity(activity_name, min_age, max_age, min_cost, max_cost, location, effort_rating, keywords, activity_description)
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

        flash("Activity added")
        return redirect(url_for('add_activity'))
        
    else: 
        return redirect('/login')




@app.route('/edit_activity/<activity_id>' , methods = ['GET','POST'])
def edit_activity(activity_id):
    """Edit an existing Activity"""

    activity = crud.get_activity_by_id(activity_id)

    materials=Material.query.all()
    interests=Interest.query.all()
    time_periods=TimePeriod.query.all()

    if request.method == 'GET':
        
        return render_template('edit_activity.html', activity=activity, materials=materials, interests=interests, time_periods=time_periods)
    
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
        keywords= request.form['keywords']
        location = request.form['location']
        min_cost=request.form['min_cost']
        max_cost=request.form['max_cost']
        min_age=request.form['min_age']
        max_age=request.form['max_age']
        effort_rating=request.form['effort_rating']

        materials = request.form.getlist('materials[]')
        interests = request.form.getlist('interests[]')
        time_periods = request.form.getlist('time_periods[]')

        print("**********************************************************************")
        print(activity_id, activity_name, min_age, max_age, min_cost, max_cost, location, effort_rating, keywords, overview, overview_pic, step_1, photo_1, step_2, photo_2, step_3, photo_3, step_4, photo_4, step_5, photo_5, step_6, photo_6)
        print("**********************************************************************")

        if activity_name:
            activity.activity_name= activity_name 
        if overview:
            print("**********************************")
            print(overview)
            print("**********************************")
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

        if interests:
            interest_list=[]
            for interest in interests:
                interest_list.append(int(interest))
            activity.interests = interest_list
                
        if materials:
            material_list=[]
            for material in materials:
                material_list.append(int(material))
            activity.materials=material_list

        if time_periods:
            time_period_list=[]
            for time_period in time_periods:
                time_period_list.append(int(time_period))
            activity.time_periods=time_period_list

        db.session.commit()

        flash("Activity edited")
        return redirect(url_for('show_activity', activity_id=activity_id))


        
@app.route('/delete_activity/<activity_id>' , methods = ['POST'])
def delete_activity(activity_id):

    activity = crud.get_activity_by_id(activity_id)
    db.session.delete(activity)
    db.session.commit()

    flash("Activity deleted")
    return redirect('/')


###################################################################################################

if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')