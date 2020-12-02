import os
import json
from random import choice, randint
from datetime import datetime

import crud
import server
import model
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
    first_name, last_name, email, username, password, zipcode = (user['first_name'], user['last_name'], 
    user['email'], user['username'], user['password'], user['zipcode'])

    db_user = crud.create_user(first_name, last_name, email, username, password, zipcode)
        
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

db.session.commit()

sarah = db.session.query(model.User).filter_by(first_name='Sarah').one()
tegan = db.session.query(model.Child).filter_by(child_name='Tegan').one()
finley = db.session.query(model.Child).filter_by(child_name='Finley').one()

sarah.children.append(tegan)
sarah.children.append(finley)

dione = db.session.query(model.User).filter_by(first_name='Dione').one()  
cassie = db.session.query(model.Child).filter_by(child_name='Cassie').one()
dione.children.append(cassie)
bond=db.session.query(model.Child).filter_by(child_name='Bond').one()
dione.children.append(bond)

brooks = db.session.query(model.User).filter_by(first_name='Brooks').one()  
merrel = db.session.query(model.Child).filter_by(child_name='Merrel').one()
brooks.children.append(merrel)


enid = db.session.query(model.User).filter_by(first_name='Enid').one()  
sean = db.session.query(model.Child).filter_by(child_name='Sean').one()
enid.children.append(sean)


avrit = db.session.query(model.User).filter_by(first_name='Avrit').one()  
tove = db.session.query(model.Child).filter_by(child_name='Tove').one()
avrit.children.append(tove)


golda = db.session.query(model.User).filter_by(first_name='Golda').one() 
cort = db.session.query(model.Child).filter_by(child_name='Cort').one()
golda.children.append(cort)

trina = db.session.query(model.User).filter_by(first_name='Trina').one() 
bertine = db.session.query(model.Child).filter_by(child_name='Bertine').one()
trina.children.append(bertine)


pepi = db.session.query(model.User).filter_by(first_name='Pepi').one()  
chase = db.session.query(model.Child).filter_by(child_name='Chase').one()
pepi.children.append(chase)

christean = db.session.query(model.User).filter_by(first_name='Christean').one()
tracee = db.session.query(model.Child).filter_by(child_name='Tracee').one()
christean.children.append(tracee) 

susannah = db.session.query(model.User).filter_by(first_name='Susannah').one()
georgie = db.session.query(model.Child).filter_by(child_name='Georgie').one()
susannah.children.append(georgie)  

adoree = db.session.query(model.User).filter_by(first_name='Adoree').one()  
daryl = db.session.query(model.Child).filter_by(child_name='Daryl').one()
adoree.children.append(daryl)

benny = db.session.query(model.User).filter_by(first_name='Benny').one()
gordon = db.session.query(model.Child).filter_by(child_name='Gordon').one()
benny.children.append(gordon)

livia = db.session.query(model.User).filter_by(first_name='Livia').one()
gerald = db.session.query(model.Child).filter_by(child_name='Gerald').one()
livia.children.append(gerald)  

yoshiko = db.session.query(model.User).filter_by(first_name='Yoshiko').one()
ernesto = db.session.query(model.Child).filter_by(child_name='Ernesto').one()
yoshiko.children.append(ernesto)  

randie = db.session.query(model.User).filter_by(first_name='Randie').one()
jasen = db.session.query(model.Child).filter_by(child_name='Jasen').one()
randie.children.append(jasen)  

john = db.session.query(model.User).filter_by(first_name='John').one()
nickolai = db.session.query(model.Child).filter_by(child_name='Nickolai').one()
john.children.append(nickolai)  

niki = db.session.query(model.User).filter_by(first_name='Niki').one()
noelle = db.session.query(model.Child).filter_by(child_name='Noelle').one()
hugh = db.session.query(model.Child).filter_by(child_name='Hugh').one()
niki.children.append(noelle)
niki.children.append(hugh)

rochelle = db.session.query(model.User).filter_by(first_name='Rochelle').one()
fran = db.session.query(model.Child).filter_by(child_name='Francesca').one()
rochelle.children.append(fran)  

shadow = db.session.query(model.User).filter_by(first_name='Shadow').one()
esdras = db.session.query(model.Child).filter_by(child_name='Esdras').one()
shadow.children.append(esdras)  

wendy = db.session.query(model.User).filter_by(first_name='Wendy').one()
steve = db.session.query(model.Child).filter_by(child_name='Steve').one()
wendy.children.append(steve)  

georgia = db.session.query(model.User).filter_by(first_name='Georgia').one()
derry = db.session.query(model.Child).filter_by(child_name='Derry').one()
alfy = db.session.query(model.Child).filter_by(child_name='Alfy').one()
georgia.children.append(derry)
georgia.children.append(alfy)

bay = db.session.query(model.User).filter_by(first_name='Bay').one()
bebe = db.session.query(model.Child).filter_by(child_name='Bebe').one()
bay.children.append(bebe)

salli = db.session.query(model.User).filter_by(first_name='Salli').one()
missy = db.session.query(model.Child).filter_by(child_name='Missy').one()
christine = db.session.query(model.Child).filter_by(child_name='Christine').one()
salli.children.append(missy)
salli.children.append(christine)

hunt = db.session.query(model.User).filter_by(first_name='Hunt').one()
jessica = db.session.query(model.Child).filter_by(child_name='Jessica').one()
leroy = db.session.query(model.Child).filter_by(child_name='Leroy').one()
hunt.children.append(jessica)
hunt.children.append(leroy)

elden = db.session.query(model.User).filter_by(first_name='Elden').one()
lenee = db.session.query(model.Child).filter_by(child_name='Lenee').one()
griff = db.session.query(model.Child).filter_by(child_name='Griff').one()
elden.children.append(lenee)
elden.children.append(griff)

rachel = db.session.query(model.User).filter_by(first_name='Rachel').one()
calvin = db.session.query(model.Child).filter_by(child_name='Calvin').one()
rachel.children.append(calvin)

jackie = db.session.query(model.User).filter_by(first_name='Jackie').one()
micah = db.session.query(model.Child).filter_by(child_name='Micah').one()
ethan = db.session.query(model.Child).filter_by(child_name='Ethan').one()
jackie.children.append(micah)
jackie.children.append(ethan)

dee = db.session.query(model.User).filter_by(first_name='Dee').one()
mikey = db.session.query(model.Child).filter_by(child_name='Mikey').one()
susanna = db.session.query(model.Child).filter_by(child_name='Susanna').one()
skippy= db.session.query(model.Child).filter_by(child_name='Skippy').one()
dee.children.append(mikey)
dee.children.append(susanna)
dee.children.append(skippy)

megan = db.session.query(model.User).filter_by(first_name='Megan').one()
allison = db.session.query(model.Child).filter_by(child_name='Allison').one()
elliott = db.session.query(model.Child).filter_by(child_name='Elliott').one()
megan.children.append(allison)
megan.children.append(elliott)

drawing = db.session.query(model.Interest).filter_by(interest_name='drawing').one()
painting = db.session.query(model.Interest).filter_by(interest_name='painting').one()
craft = db.session.query(model.Interest).filter_by(interest_name='paper craft').one()
pottery = db.session.query(model.Interest).filter_by(interest_name='pottery').one()
photography = db.session.query(model.Interest).filter_by(interest_name='photography').one()
knitting = db.session.query(model.Interest).filter_by(interest_name='knitting').one()
sewing = db.session.query(model.Interest).filter_by(interest_name='sewing').one()
water_play = db.session.query(model.Interest).filter_by(interest_name='water play').one()
bubbles = db.session.query(model.Interest).filter_by(interest_name='bubbles').one()
camping = db.session.query(model.Interest).filter_by(interest_name='camping').one()
gardening = db.session.query(model.Interest).filter_by(interest_name='gardening').one()
nature_play = db.session.query(model.Interest).filter_by(interest_name='nature activities').one() 
dress_up = db.session.query(model.Interest).filter_by(interest_name='dress up').one()
role_play = db.session.query(model.Interest).filter_by(interest_name='role play').one()
puppets = db.session.query(model.Interest).filter_by(interest_name='puppets').one()
dancing = db.session.query(model.Interest).filter_by(interest_name='dancing').one()
singing = db.session.query(model.Interest).filter_by(interest_name='singing').one()
music = db.session.query(model.Interest).filter_by(interest_name='music').one()
storytelling = db.session.query(model.Interest).filter_by(interest_name='storytelling').one()
baking = db.session.query(model.Interest).filter_by(interest_name='baking').one()
magic = db.session.query(model.Interest).filter_by(interest_name='magic').one()
experiments = db.session.query(model.Interest).filter_by(interest_name='experiments').one()
programming = db.session.query(model.Interest).filter_by(interest_name='programming').one()
star_gazing = db.session.query(model.Interest).filter_by(interest_name='star gazing').one()
active_play = db.session.query(model.Interest).filter_by(interest_name='active play').one()
sports = db.session.query(model.Interest).filter_by(interest_name='sports').one()
yoga = db.session.query(model.Interest).filter_by(interest_name='yoga').one()





cassie.interests.append(drawing)
cassie.interests.append(dancing) 
cassie.interests.append(storytelling) 

merrel.interests.append(experiments) 
merrel.interests.append(active_play) 
merrel.interests.append(photography) 

sean.interests.append(puppets)
sean.interests.append(water_play) 
sean.interests.append(star_gazing) 

tove.interests.append(pottery)
tove.interests.append(experiments)
tove.interests.append(craft)

cort.interests.append(singing)
cort.interests.append(camping)
cort.interests.append(star_gazing)

bertine.interests.append(yoga)
bertine.interests.append(dress_up) 
bertine.interests.append(programming) 

chase.interests.append(programming)
chase.interests.append(music) 
chase.interests.append(photography) 

tracee.interests.append(knitting) 
tracee.interests.append(sewing) 
tracee.interests.append(craft) 

georgie.interests.append(nature_play) 
georgie.interests.append(yoga)
georgie.interests.append(water_play)

daryl.interests.append(painting) 
daryl.interests.append(craft) 
daryl.interests.append(drawing) 

gordon.interests.append(programming) 
gordon.interests.append(active_play) 
gordon.interests.append(sports) 

gerald.interests.append(water_play) 
gerald.interests.append(sports) 
gerald.interests.append(experiments) 

ernesto.interests.append(magic) 
ernesto.interests.append(baking) 
ernesto.interests.append(craft) 

jasen.interests.append(sports) 
jasen.interests.append(camping) 
jasen.interests.append(nature_play) 

nickolai.interests.append(magic) 
nickolai.interests.append(storytelling) 
nickolai.interests.append(programming) 

christine.interests.append(star_gazing) 
christine.interests.append(camping)
christine.interests.append(active_play)

fran.interests.append(water_play) 
fran.interests.append(bubbles) 
fran.interests.append(drawing) 

esdras.interests.append(painting) 
esdras.interests.append(photography) 
esdras.interests.append(active_play) 

bond.interests.append(experiments)
bond.interests.append(sports) 
bond.interests.append(camping) 

derry.interests.append(programming) 
derry.interests.append(active_play) 
derry.interests.append(photography) 

bebe.interests.append(dancing) 
bebe.interests.append(drawing)
bebe.interests.append(painting)

missy.interests.append(storytelling)
missy.interests.append(yoga)
missy.interests.append(singing)

jessica.interests.append(pottery) 
jessica.interests.append(music) 
jessica.interests.append(dancing) 

leroy.interests.append(programming) 
leroy.interests.append(experiments) 
leroy.interests.append(singing) 

lenee.interests.append(drawing) 
lenee.interests.append(painting) 
lenee.interests.append(pottery) 

alfy.interests.append(sports) 
alfy.interests.append(magic) 
alfy.interests.append(water_play) 

griff.interests.append(sports) 
griff.interests.append(drawing)
griff.interests.append(camping)

mikey.interests.append(baking) 
mikey.interests.append(camping) 
mikey.interests.append(star_gazing) 

susanna.interests.append(sewing) 
susanna.interests.append(knitting) 
susanna.interests.append(pottery) 

skippy.interests.append(puppets) 
skippy.interests.append(magic) 
skippy.interests.append(drawing) 

allison.interests.append(dress_up) 
allison.interests.append(role_play) 
allison.interests.append(singing) 

elliott.interests.append(pottery) 
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

steve.interests.append(baking) 
steve.interests.append(programming)
steve.interests.append(magic)

construction=model.Material.query.get(1)
cardboard=model.Material.query.get(2)
crayons = model.Material.query.get(3)
markers= model.Material.query.get(4)
c_pencils=model.Material.query.get(5)
chalk=model.Material.query.get(6)
w_paint = model.Material.query.get(7)
wash_paint=model.Material.query.get(8)
a_paint=model.Material.query.get(9)

activity_1= model.Activity.query.get(1)
activity_1.materials.append(construction)
activity_1.materials.append(markers)
activity_1.materials.append(w_paint)
activity_1.interests.append(drawing)
activity_1.interests.append(dancing)

activity_2= model.Activity.query.get(2)
activity_2.materials.append(cardboard)
activity_2.materials.append(c_pencils)
activity_2.materials.append(wash_paint)
activity_2.interests.append(painting)
activity_2.interests.append(magic)

activity_3= model.Activity.query.get(3)
activity_3.materials.append(crayons)
activity_3 .materials.append(construction)
activity_3.materials.append(cardboard)
activity_3.interests.append(photography)
activity_3.interests.append(drawing)

megan.activities.append(activity_1)
megan.activities.append(activity_3)
sarah.activities.append(activity_2)

db.session.commit()