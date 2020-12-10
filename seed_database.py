import os
import json
from random import choice, randint
from datetime import datetime

import crud
import server
from model import Interest, User, Material, TimePeriod, Comment, Child, Activity
from settings import db, connect_to_db

os.system('dropdb kidactivities')
os.system('createdb kidactivities')

connect_to_db(server.app)
db.create_all()


with open('data/activities.json') as x:
    activity_info = json.loads(x.read())

activity_in_db =[]
for activity in activity_info:
    activity_name, min_cost, max_cost, min_age, max_age, location, effort_rating, keywords, activity_description, timestamp = (activity['activity_name'],activity['min_cost'],activity['max_cost'],activity['min_age'],
    activity['max_age'],activity['location'],activity['effort_rating'],activity['keywords'],activity['activity_description'], activity['timestamp'])
        
    db_activity = crud.create_activity(activity_name, min_cost,max_cost, min_age, max_age, location, effort_rating, keywords, activity_description)

    activity_in_db.append(db_activity)


with open('data/interest_info.json') as f:
    interest_info = json.loads(f.read())

interests_in_db =[]
for interest in interest_info:
    interest_name =(interest['interest_name'])
        
    db_interest = crud.create_interest(interest_name)

    interests_in_db.append(db_interest)

with open('data/user_data.json') as e:
    user_data = json.loads(e.read())

users_in_db = []
for user in user_data:
    first_name, last_name, email, username, password, zipcode, photo = (user['first_name'], user['last_name'], 
    user['email'], user['username'], user['password'], user['zipcode'], user['photo'])

    db_user = crud.create_user(first_name, last_name, email, username, password, zipcode, photo)
        
    users_in_db.append(db_user)

with open('data/child_data.json') as d:
    child_data = json.loads(d.read())

child_in_db = []
for child in child_data:
    child_name, birthdate, gender, photo = (child['child_name'], child['birthdate'], child['gender'], child['photo'])

    db_child = crud.create_child(child_name, birthdate, gender, photo)
        
    child_in_db.append(db_child)

with open('data/materials_info.json') as c:
    materials = json.loads(c.read())

materials_in_db = []

for material in materials:
    material_name, material_cost, material_url = (material['material_name'], material['material_cost'], material['material_url'])

    db_material = crud.create_material(material_name, material_cost, material_url)
    materials_in_db.append(db_material)

with open('data/time_period.json') as z:
    time_periods = json.loads(z.read())

time_periods_in_db = []

for time in time_periods:
    time_period_name = (time['time_period_name'])

    db_time_period = crud.create_time_period(time_period_name)
    time_periods_in_db.append(db_time_period)

with open('data/comments.json') as k:
    comments = json.loads(k.read())

comments_in_db=[]

for comment in comments:
    comment_text, star_rating =(comment['comment_text'], comment['star_rating'])

    db_comment=crud.create_comment(comment_text, star_rating)
    comments_in_db.append(db_comment)



db.session.commit()

sarah = db.session.query(User).filter_by(first_name='Sarah').first()
tegan = db.session.query(Child).filter_by(child_name='Tegan').first()
finley = db.session.query(Child).filter_by(child_name='Finley').first()

sarah.children.append(tegan)
sarah.children.append(finley)

niki = db.session.query(User).filter_by(first_name='Niki').first()
noelle = db.session.query(Child).filter_by(child_name='Noelle').first()
hugh = db.session.query(Child).filter_by(child_name='Hugh').first()
niki.children.append(noelle)
niki.children.append(hugh)

rachel = db.session.query(User).filter_by(first_name='Rachel').first()
calvin = db.session.query(Child).filter_by(child_name='Calvin').first()
rachel.children.append(calvin)

jackie = db.session.query(User).filter_by(first_name='Jackie').first()
micah = db.session.query(Child).filter_by(child_name='Micah').first()
ethan = db.session.query(Child).filter_by(child_name='Ethan').first()
jackie.children.append(micah)
jackie.children.append(ethan)


megan = db.session.query(User).filter_by(first_name='Megan').first()
allison = db.session.query(Child).filter_by(child_name='Allison').first()
elliott = db.session.query(Child).filter_by(child_name='Elliott').first()
megan.children.append(allison)
megan.children.append(elliott)

art= db.session.query(Interest).filter_by(interest_name='art').first()
drawing = db.session.query(Interest).filter_by(interest_name='drawing').first()
painting = db.session.query(Interest).filter_by(interest_name='painting').first()
craft = db.session.query(Interest).filter_by(interest_name='craft').first()
pottery = db.session.query(Interest).filter_by(interest_name='pottery').first()
photography = db.session.query(Interest).filter_by(interest_name='photography').first()
knitting = db.session.query(Interest).filter_by(interest_name='knitting').first()
sewing = db.session.query(Interest).filter_by(interest_name='sewing').first()
water_play = db.session.query(Interest).filter_by(interest_name='water play').first()
bubbles = db.session.query(Interest).filter_by(interest_name='bubbles').first()
camping = db.session.query(Interest).filter_by(interest_name='camping').first()
gardening = db.session.query(Interest).filter_by(interest_name='gardening').first()
nature_play = db.session.query(Interest).filter_by(interest_name='nature activities').first() 
dress_up = db.session.query(Interest).filter_by(interest_name='dress up').first()
imag_play = db.session.query(Interest).filter_by(interest_name='imaginative play').first()
puppets = db.session.query(Interest).filter_by(interest_name='puppets').first()
dancing = db.session.query(Interest).filter_by(interest_name='dancing').first()
singing = db.session.query(Interest).filter_by(interest_name='singing').first()
music = db.session.query(Interest).filter_by(interest_name='music').first()
storytelling = db.session.query(Interest).filter_by(interest_name='storytelling').first()
baking = db.session.query(Interest).filter_by(interest_name='baking').first()
magic = db.session.query(Interest).filter_by(interest_name='magic').first()
experiments = db.session.query(Interest).filter_by(interest_name='experiments').first()
programming = db.session.query(Interest).filter_by(interest_name='programming').first()
star_gazing = db.session.query(Interest).filter_by(interest_name='star gazing').first()
active_play = db.session.query(Interest).filter_by(interest_name='active play').first()
sports = db.session.query(Interest).filter_by(interest_name='sports').first()
yoga = db.session.query(Interest).filter_by(interest_name='yoga').first()
sensory = db.session.query(Interest).filter_by(interest_name='sensory play').first()
games=db.session.query(Interest).filter_by(interest_name='games').first()

allison.interests.append(experiments) 
allison.interests.append(imag_play) 
allison.interests.append(craft)
allison.interests.append(art)  

elliott.interests.append(sensory) 
elliott.interests.append(active_play) 
elliott.interests.append(water_play) 

tegan.interests.append(dress_up) 
tegan.interests.append(dancing)
tegan.interests.append(painting)

finley.interests.append(active_play) 
finley.interests.append(water_play)
finley.interests.append(baking)

micah.interests.append(active_play) 
micah.interests.append(sports)
micah.interests.append(craft)

calvin.interests.append(water_play) 
calvin.interests.append(active_play)
calvin.interests.append(painting)

ethan.interests.append(active_play) 
ethan.interests.append(music)
ethan.interests.append(singing)

noelle.interests.append(camping)
noelle.interests.append(sports) 
noelle.interests.append(storytelling) 

hugh.interests.append(sports) 
hugh.interests.append(programming) 
hugh.interests.append(photography) 



construction=Material.query.get(1)
cardboard=Material.query.get(2)
crayons = Material.query.get(3)
markers= Material.query.get(4)
c_pencils=Material.query.get(5)
chalk=Material.query.get(6)
w_paint = Material.query.get(7)
wash_paint=Material.query.get(8)
a_paint=Material.query.get(9)
twine=Material.query.get(10)
yarn=Material.query.get(11)
felt=Material.query.get(12)
fabric=Material.query.get(13)
thread=Material.query.get(14)
playdough=Material.query.get(15)
p_sticks=Material.query.get(16)
clay=Material.query.get(17)
string=Material.query.get(18)
beads=Material.query.get(19)
glitter=Material.query.get(20)
pom=Material.query.get(21)
feathers=Material.query.get(22)
cotton=Material.query.get(23)
googly=Material.query.get(24)
foam=Material.query.get(25)
buttons=Material.query.get(26)
glue=Material.query.get(27)
pipe=Material.query.get(28)
podge=Material.query.get(29)
cement=Material.query.get(30)
scissors=Material.query.get(31)
p_brush=Material.query.get(32)
f_brush=Material.query.get(33)
ruler=Material.query.get(34)
ink=Material.query.get(35)
dye=Material.query.get(36)
paper=Material.query.get(37)
roll=Material.query.get(38)
c_stock=Material.query.get(39)
w_paper=Material.query.get(40)
tissue=Material.query.get(41)
c_filter=Material.query.get(42)
p_towels=Material.query.get(43)
contact_paper=Material.query.get(44)
freeze=Material.query.get(45)
p_bags=Material.query.get(46)
crepe=Material.query.get(47)
g_container=Material.query.get(48)
p_container=Material.query.get(49)
r_band=Material.query.get(50)
ziploc=Material.query.get(51)
noodle=Material.query.get(52)
cornstarch=Material.query.get(53)
bakingsoda=Material.query.get(54)
shavingcream=Material.query.get(55)
sand=Material.query.get(56)
water=Material.query.get(57)
f_coloring=Material.query.get(58)
ribbon=Material.query.get(59)
tape=Material.query.get(60)
balloons=Material.query.get(61)



anytime=TimePeriod.query.get(1)
winter=TimePeriod.query.get(2)
han=TimePeriod.query.get(3)
xmas=TimePeriod.query.get(4)
kwan=TimePeriod.query.get(5)
ny=TimePeriod.query.get(6)
mlk=TimePeriod.query.get(7)
vday=TimePeriod.query.get(8)
spring=TimePeriod.query.get(9)
stpat=TimePeriod.query.get(10)
easter=TimePeriod.query.get(11)
momsday=TimePeriod.query.get(12)
summer=TimePeriod.query.get(13)
feathers=TimePeriod.query.get(14)
independence=TimePeriod.query.get(15)
fall=TimePeriod.query.get(16)
halloween=TimePeriod.query.get(17)
thanksgiving=TimePeriod.query.get(18)


a1= Activity.query.get(1)
a1.time_periods.append(anytime)
a1.materials.append(c_stock)
a1.materials.append(scissors)
a1.interests.append(art)

a2= Activity.query.get(2)
a2.time_periods.append(anytime)
a2.materials.append(c_stock)
a2.materials.append(scissors)
a2.interests.append(art)


a3= Activity.query.get(3)
a3.time_periods.append(fall)
a3.materials.append(c_stock)
a3.materials.append(scissors)
a3.interests.append(art)


a4= Activity.query.get(4)
a4.time_periods.append(anytime)
a4.materials.append(cardboard)
a4.interests.append(experiments)

a5= Activity.query.get(5)
a5.time_periods.append(spring)
a5.materials.append(c_stock)
a5.materials.append(scissors)
a5.interests.append(art)

a6= Activity.query.get(6)
a6.time_periods.append(summer)
a6.interests.append(active_play)

a7= Activity.query.get(7)
a7.time_periods.append(spring)
a7.time_periods.append(momsday)
a7.materials.append(c_stock)
a7.materials.append(scissors)
a7.interests.append(art)

a8= Activity.query.get(8)
a8.time_periods.append(anytime)
a8.materials.append(cardboard)
a8.materials.append(string)
a8.interests.append(experiments)

a9= Activity.query.get(9)
a9.time_periods.append(halloween)
a9.materials.append(googly)
a9.materials.append(a_paint)
a9.interests.append(craft)

a10= Activity.query.get(10)
a10.time_periods.append(xmas)
a10.materials.append(string)
a10.materials.append(ribbon)


a11= Activity.query.get(11)
a11.time_periods.append(anytime)
a11.materials.append(glitter)
a11.materials.append(felt)
a11.interests.append(imag_play)
a11.interests.append(sewing)
a11.interests.append(craft)

a12= Activity.query.get(12)
a12.time_periods.append(anytime)
a12.materials.append(cardboard)
a12.materials.append(glitter)
a12.materials.append(a_paint)
a12.interests.append(imag_play)
a12.interests.append(craft)

a13= Activity.query.get(13)
a13.time_periods.append(anytime)
a13.materials.append(f_brush)
a13.materials.append(a_paint)
a13.interests.append(art)

a14= Activity.query.get(14)
a14.time_periods.append(anytime)
a14.materials.append(water)
a14.interests.append(bubbles)

a15= Activity.query.get(15)
a15.time_periods.append(anytime)
a15.materials.append(w_paint)
a15.materials.append(a_paint)
a15.materials.append(paper)
a15.interests.append(art)
a15.interests.append(painting)
a15.interests.append(bubbles)


a16= Activity.query.get(16)
a16.time_periods.append(winter)
a16.time_periods.append(xmas)
a16.materials.append(water)
a16.materials.append(ribbon)
a16.interests.append(experiments)
a16.interests.append(art)
a16.interests.append(craft)

a17= Activity.query.get(17)
a17.time_periods.append(winter)
a17.materials.append(cardboard)
a17.materials.append(construction)
a17.interests.append(art)
a17.interests.append(craft)

a18= Activity.query.get(18)
a18.time_periods.append(fall)
a18.materials.append(clay)
a18.materials.append(a_paint)
a18.materials.append(string)
a18.interests.append(nature_play)
a18.interests.append(art)
a18.interests.append(craft)

a19= Activity.query.get(19)
a19.time_periods.append(spring)
a19.time_periods.append(summer)
a19.materials.append(cardboard)
a19.materials.append(balloons)
a19.materials.append(a_paint)
a19.interests.append(active_play)
a19.interests.append(games)
a19.interests.append(experiments)

a20= Activity.query.get(20)
a20.time_periods.append(anytime)
a20.materials.append(tape)
a20.materials.append(paper)
a20.interests.append(active_play)
a20.interests.append(games)

a21= Activity.query.get(21)
a21.time_periods.append(anytime)
a21.materials.append(tape)
a21.interests.append(active_play)
a21.interests.append(games)

a22= Activity.query.get(22)
a22.time_periods.append(anytime)
a22.materials.append(tape)
a22.interests.append(imag_play)

a23= Activity.query.get(23)
a23.time_periods.append(anytime)
a23.materials.append(tape)
a23.interests.append(active_play)
a23.interests.append(games)

a24= Activity.query.get(24)
a24.time_periods.append(anytime)
a24.materials.append(cardboard)
a24.materials.append(markers)
a24.materials.append(construction)
a24.interests.append(active_play)
a24.interests.append(games)

a25= Activity.query.get(25)
a25.time_periods.append(anytime)
a25.materials.append(tape)
a25.interests.append(active_play)
a25.interests.append(games)

a26= Activity.query.get(26)
a26.time_periods.append(anytime)
a26.materials.append(balloons)
a26.interests.append(active_play)
a26.interests.append(games)

a27=Activity.query.get(27)
a27.time_periods.append(anytime)
a27.materials.append(balloons)
a27.interests.append(active_play)
a27.interests.append(games)

a28= Activity.query.get(28)
a28.time_periods.append(anytime)
a28.interests.append(active_play)
a28.interests.append(games)

a29= Activity.query.get(29)
a29.time_periods.append(anytime)
a29.materials.append(paper)
a29.materials.append(markers)
a29.interests.append(games)
a29.interests.append(active_play)

a30= Activity.query.get(30)
a30.time_periods.append(spring)
a30.time_periods.append(summer)
a30.time_periods.append(fall)
a30.materials.append(paper)
a30.materials.append(markers)
a30.interests.append(nature_play)
a30.interests.append(experiments)
a30.interests.append(games)
a30.interests.append(active_play)

a31= Activity.query.get(31)
a31.time_periods.append(anytime)
a31.materials.append(clay)
a31.materials.append(w_paint)
a31.interests.append(sensory)
a31.interests.append(craft)

a32 = Activity.query.get(32)
a32.time_periods.append(spring)
a32.time_periods.append(summer)
a32.interests.append(active_play)
a32.interests.append(games)

a33 = Activity.query.get(33)
a33.time_periods.append(spring)
a33.time_periods.append(summer)
a33.materials.append(noodle)
a33.interests.append(active_play)
a33.interests.append(games)

a34= Activity.query.get(34)
a34.time_periods.append(summer)
a34.time_periods.append(spring)
a34.interests.append(sensory)
a34.interests.append(games)

a35 = Activity.query.get(35)
a35.time_periods.append(anytime)
a35.interests.append(experiments)

a36= Activity.query.get(36)
a36.time_periods.append(xmas)
a36.materials.append(glitter)
a36.materials.append(water)
a36.materials.append(g_container)
a36.interests.append(craft)

a37= Activity.query.get(37)
a37.time_periods.append(anytime)
a37.materials.append(noodle)
a37.interests.append(imag_play)

a38= Activity.query.get(38)
a38.time_periods.append(anytime)
a38.materials.append(noodle)
a38.interests.append(active_play)
a38.interests.append(imag_play)

a39= Activity.query.get(39)
a39.time_periods.append(summer)
a39.materials.append(noodle)
a39.materials.append(water)
a39.interests.append(imag_play)
a39.interests.append(sensory)
a39.interests.append(active_play)
a39.interests.append(water_play)

a40= Activity.query.get(40)
a40.time_periods.append(anytime)
a40.materials.append(string)
a40.materials.append(tape)
a40.interests.append(active_play)

a41= Activity.query.get(41)
a41.time_periods.append(xmas)
a41.materials.append(a_paint)
a41.materials.append(glitter)
a41.materials.append(g_container)
a41.interests.append(art)
a41.interests.append(craft)

a42= Activity.query.get(42)
a42.time_periods.append(anytime)
a42.time_periods.append(spring)
a42.time_periods.append(momsday)
a42.materials.append(g_container)
a42.materials.append(f_coloring)
a42.materials.append(water)
a42.interests.append(experiments)
a42.interests.append(art)


a43= Activity.query.get(43)
a43.time_periods.append(anytime)
a43.materials.append(sand)
a43.materials.append(p_container)
a43.interests.append(sensory)


a44= Activity.query.get(44)
a44.time_periods.append(anytime)
a44.materials.append(f_coloring)
a44.materials.append(glitter)
a44.materials.append(glue)
a44.interests.append(sensory)
a44.interests.append(experiments)


a45= Activity.query.get(45)
a45.time_periods.append(spring)
a45.time_periods.append(summer)
a45.materials.append(f_coloring)
a45.materials.append(shavingcream)
a45.interests.append(painting)
a45.interests.append(art)


a46 = Activity.query.get(46)
a46.time_periods.append(spring)
a46.time_periods.append(summer)
a46.time_periods.append(independence)
a46.materials.append(bakingsoda)
a46.materials.append(chalk)
a46.interests.append(experiments)


a47= Activity.query.get(47)
a47.time_periods.append(anytime)
a47.materials.append(p_towels)
a47.materials.append(f_coloring)
a47.materials.append(water)
a47.materials.append(g_container)
a47.interests.append(experiments)


a48= Activity.query.get(48)
a48.time_periods.append(anytime)
a48.materials.append(water)
a48.materials.append(f_coloring)
a48.materials.append(g_container)
a48.interests.append(experiments)


a50= Activity.query.get(49)
a50.time_periods.append(fall)
a50.materials.append(c_stock)
a50.materials.append(scissors)
a50.interests.append(craft)

a51 = Activity.query.get(50)
a51.time_periods.append(winter)
a51.time_periods.append(xmas)
a51.materials.append(w_paint)
a51.materials.append(bakingsoda)
a51.interests.append(experiments)

a52= Activity.query.get(51)
a52.time_periods.append(anytime)
a52.materials.append(f_coloring)
a52.materials.append(g_container)
a52.materials.append(cotton)
a52.interests.append(experiments)

a53= Activity.query.get(52)
a53.time_periods.append(anytime)
a53.materials.append(f_coloring)
a53.materials.append(water)
a53.materials.append(shavingcream)
a53.materials.append(g_container)
a53.interests.append(experiments)

a54 = Activity.query.get(53)
a54.time_periods.append(winter)
a54.interests.append(bubbles)
a54.interests.append(experiments)


a55 = Activity.query.get(54)
a55.time_periods.append(winter)
a55.materials.append(water)
a55.materials.append(balloons)
a55.materials.append(f_coloring)
a55.interests.append(active_play)


a56 = Activity.query.get(55)
a56.time_periods.append(fall)
a56.materials.append(pom)
a56.materials.append(pipe)
a56.interests.append(craft)
a56.interests.append(imag_play)


a57 = Activity.query.get(56)
a57.time_periods.append(winter)
a57.time_periods.append(xmas)
a57.materials.append(glue)
a57.materials.append(pipe)
a57.materials.append(glitter)
a57.materials.append(cardboard)
a57.materials.append(scissors)
a57.materials.append(tape)
a57.interests.append(craft)


a58 = Activity.query.get(57)
a58.time_periods.append(winter)
a58.time_periods.append(xmas)
a58.materials.append(scissors)
a58.materials.append(glue)
a58.materials.append(foam)
a58.materials.append(ribbon)
a58.materials.append(buttons)
a58.interests.append(craft)

a59 = Activity.query.get(58)
a59.time_periods.append(anytime)
a59.materials.append(p_container)
a59.materials.append(string)
a59.materials.append(yarn)
a59.interests.append(sensory)


a60 = Activity.query.get(59)
a60.time_periods.append(anytime)
a60.materials.append(p_container)
a60.materials.append(sand)
a60.materials.append(water)
a60.interests.append(sensory)


c1=Comment.query.get(1)
c2=Comment.query.get(2)
c3=Comment.query.get(3)
c4=Comment.query.get(4)
c5=Comment.query.get(5)
c6=Comment.query.get(6)
c7=Comment.query.get(7)
c8=Comment.query.get(8)
c9=Comment.query.get(9)
c10=Comment.query.get(10)



megan.activities.append(a48)
megan.activities.append(a58)
megan.activities.append(a56)
megan.activities.append(a55)
megan.activities.append(a54)
megan.activities.append(a53)

megan.comments.append(c1)
megan.comments.append(c2)
sarah.comments.append(c3)
sarah.comments.append(c4)
rachel.comments.append(c5)
rachel.comments.append(c6)
jackie.comments.append(c7)
jackie.comments.append(c8)
niki.comments.append(c9)
niki.comments.append(c10)

a48.comments.append(c1)
a48.comments.append(c3)
a48.comments.append(c5)
a48.comments.append(c7)
a48.comments.append(c9)
a59.comments.append(c2)
a59.comments.append(c4)
a59.comments.append(c6)
a59.comments.append(c8)
a59.comments.append(c10)
a60.comments.append(c1)
a60.comments.append(c3)
a60.comments.append(c5)
a60.comments.append(c7)
a60.comments.append(c9)

db.session.commit()