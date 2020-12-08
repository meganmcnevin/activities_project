# 🎈 While'd Child <br>


### About

While'd Child is a web app to help busy parents and caregivers plan fun and engaging activities for the children in their lives. 
While there are no end of websites with activity ideas, it takes time to sort through ideas. If you find a promising post, you still have to
download all the ads and pictures, close the pop ups,  scroll down through blogger's personal story to pick out the activity steps and then 
determine if you have the right materials for the activity on hand or if your kids would even be interested. 

I created While’d Child to help solve these problems! 

### Features

__All users__<br>
- [x] Search for an activity by keyword.<br>
- [x] Filter activities by rating, age range, cost, indoor or outdoor location, interests, materials required, and the time of year best suited for the activity.<br>
- [x] View activities, ratings, and comments.<br><br>
  
__Registered users__<br>
- [x] User registration, log in, and profile editing capabilities<br>
- [x] Attach individual children, ages and interests, to the profile<br>
- [x] Generate a suggested list of activities for each child based on age and interest.<br>
- [x] Favorite an activity or comment on and rate an activity.<br><br>
 
__Administrators__<br>
- [x] Create a new activity to add to the database.<br>
- [x] Edit or delete an existing activity.<br>


### Demo

#### Homepage
<img src="https://github.com/M-McNevin/readmeimages/blob/main/2020-12-08_16-36-55.gif">

#### Filtered Search
<img src="https://github.com/M-McNevin/readmeimages/blob/main/2020-12-08_16-37-54.gif">

#### An Activity
<img src="https://github.com/M-McNevin/readmeimages/blob/main/2020-12-08_16-35-31.gif">

### Tech Stack<br>
> SQLAlchemy<br>
> Python<br>
> Flask<br>
> Jinja<br>
> Javascript<br>
> JQuery/AJAX<br>
> Bootstrap<br>
> CSS<br>
> HTML<br>
 
(Dependencies are listed in requirements.txt)

### Structure

While'dChild has not yet been deployed, so here is how to run the app locally on your machine.

Install PostgreSQL and Python. <br>
Clone or fork this repo. <br>
Set up and activate a python virtualenv, and install all dependencies. <br>
```
pip install -r requirements.txt
```
Make sure you have PostgreSQL running. Create a new database in psql named kidactivities.<br>

Run seed_database.py. This will create the tables required automatically and seed the database with activity information.<br>

```
python3 seed_database.py
```

Start up the flask server, and you are ready to go!
```
python3 server.py
```

### Version 2.0
- [ ] Enable registered users to create and edit their own activities
- [ ] Add social features, such as upvoting
- [ ] Provide the option to upload photos
- [ ] Include information about events and other happenings around the Twin Cities metro area with Google Maps integration. 
- [ ] Oauth 2.0 authorization

# Author
Megan McNevin is a software engineer in Minneapolis, MN.
