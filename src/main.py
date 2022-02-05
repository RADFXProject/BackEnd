from fastapi import FastAPI, Depends, HTTPException
from .auth import AuthHandler
from .schemas import AuthDetails, CreateUserDetails, Facility, User, Affiliation, Project, Request, Token
from fastapi.middleware.cors import CORSMiddleware
from .MessageGenerator import MessageGenerator

import mysql.connector

app = FastAPI(title="Radfx API")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="radfx"
)


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


auth_handler = AuthHandler()
users = []
projects = []
requests = []
affiliations = []
facilities = []

@app.get('/')
def get_users():
    return users


@app.post('/register', status_code=200)
def register(auth_details: CreateUserDetails):
    mycursor = mydb.cursor()
    
    
    sql = "SELECT * FROM user WHERE email = %s"
    val = (auth_details.email, )
    mycursor.execute(sql, val)
    mycursor.fetchone()
    if mycursor.rowcount > 0:
        raise HTTPException(status_code=400, detail='Username is taken')
    
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    print(hashed_password)
    sql = "INSERT INTO user (first_name, last_name, email, role_id, password) VALUES (%s, %s, %s, %s, %s)"
    val = (auth_details.first_name, auth_details.last_name, auth_details.email, "0", hashed_password)
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

    MessageGenerator.welcomeTester(auth_details.email)
    return


@app.post('/login')
def login(auth_details: AuthDetails):    
    user = None
    
    mycursor = mydb.cursor()

    sql = "SELECT password FROM user WHERE email = %s"
    val = (auth_details.username, )
    mycursor.execute(sql, val)
    myresults = mycursor.fetchone()
    tvar = auth_handler.get_password_hash(auth_details.password)
    tvar2 = auth_handler.get_password_hash(auth_details.password)

    if (mycursor.rowcount == 0) or (not auth_handler.verify_password(auth_details.password, myresults[0])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')

    token = auth_handler.encode_token(auth_details.username)
    return print(Token(access_token=token, token_type="bearer", user=auth_details.username))


@app.get('/unprotected')
def unprotected():
    return { 'hello': 'world' }


@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }


@app.post('/user', status_code=200)
def post_user(response_details: User):
    users.append({
        'id': len(users),
        'affiliation_id': int(response_details.affiliation_id),
        'user_name': response_details.user_name,
        'full_name': response_details.full_name,
        'first_name': response_details.first_name,
        'last_name': response_details.last_name,
        'created_at': response_details.created_at,
        'updated_at': response_details.updated_at,
        'phone_number': response_details.phone_number,
        'email': response_details.email,
        'verified_at': response_details.verified_at,
        'disabled_at': response_details.disabled_at,
        'deleted_at': response_details.deleted_at,
        'role': response_details.role
    })
    return


@app.get("/user/{user_id}", status_code=200)
async def get_user(user_id):
    response = [x for x in users if x['id'] == int(user_id)]
    return response


@app.put("/user/{user_id}", status_code=200)
async def update_user(user_id, response_details: User):
    deletion_set = set([int(user_id)])  
    for i in reversed(range(len(users))):
        if users[i]['id'] in deletion_set:
            del(users[i])
    users.append({
        'id': int(user_id),
        'affiliation_id': int(response_details.affiliation_id),
        'user_name': response_details.user_name,
        'full_name': response_details.full_name,
        'first_name': response_details.first_name,
        'last_name': response_details.last_name,
        'created_at': response_details.created_at,
        'updated_at': response_details.updated_at,
        'phone_number': response_details.phone_number,
        'email': response_details.email,
        'verified_at': response_details.verified_at,
        'disabled_at': response_details.disabled_at,
        'deleted_at': response_details.deleted_at,
        'role': response_details.role
    })
    return 


@app.delete("/user/{user_id}", status_code=200)
async def delete_user(user_id):
    deletion_set = set([int(user_id)])  
    for i in reversed(range(len(users))):
        if users[i]['id'] in deletion_set:
            del(users[i])
    return  users


@app.get('/users')
def get_users():
    return users


@app.post('/facility', status_code=200)
def post_facility(response_details: Facility):
    facilities.append({
        'id': len(facilities),
        'name': response_details.name,
        'full_name': response_details.full_name,
        'description': response_details.description,
        'accelerator': response_details.accelerator,
        'hours_of_operation': response_details.hours_of_operation
    })
    return 


@app.get('/facility/{facility_id}', status_code=200)
def get_facility(facility_id):
    response = [x for x in facilities if x['id'] == int(facility_id)]
    return response


@app.put('/facility/{facility_id}', status_code=200)
def update_facility(facility_id, response_details: Facility):
    return


@app.delete('/facility/{facility_id}', status_code=200)
def delete_facility(facility_id):
    deletion_set = set([int(facility_id)])   
    for i in reversed(range(len(facilities))):
        if facilities[i]['id'] in deletion_set:
            del facilities[i]
    return  facilities


@app.get('/facilities')
def get_facilities():
    return facilities 



@app.post('/affiliation', status_code=200)
def post_affiliation(response_details: Affiliation):
    affiliations.append({
        'id': len(affiliations),
        'name': response_details.name,
        'full_name': response_details.full_name,
        'description': response_details.description
    })
    return


@app.get('/affiliation/{affiliation_id}')
def get_affilitation(affiliation_id):
    response = [x for x in affiliations if x['id'] == int(affiliation_id)]
    return response


@app.put('/affiliation/{affiliation_id}', status_code=200)
def update_affilitation(affiliation_id, response_details: Affiliation):
    return 

@app.delete('/affiliation/{affiliation_id}')
def delete_affilitation(affiliation_id):
    deletion_set = set([int(affiliation_id)])   
    for i in reversed(range(len(affiliations))):  # thanks to @juanpa.arrivillaga for this bit 
        if affiliations[i]['id'] in deletion_set:
            del affiliations[i]
    return  affiliations

@app.get('/affiliations')
def get_affilitations():
    return affiliations


@app.post('/project', status_code=200)
def post_project(response_details: Project):
    projects.append({
        'id': len(projects),
        'project_name': response_details.project_name,
        'description': response_details.description,
        'program': response_details.program,
        'devices_under_test': response_details.devices_under_test,
        'purpose_of_test': response_details.purpose_of_test,
        'total_hours': response_details.total_hours,
        'vacuum': response_details.vacuum,
        'status': response_details.status,
        'created_at': response_details.created_at,
        'updated_at': response_details.updated_at,
        'submitted_at': response_details.submitted_at,
        'approved_at': response_details.approved_at,
        'completed_at': response_details.completed_at,
        'cancelled_at': response_details.cancelled_at,
        'test_start': response_details.test_start,
        'test_end': response_details.test_end,
        'is_public': response_details.is_public
    })
    return

@app.get('/project/{project_id}', status_code=200)
def get_project(project_id):
    response = [x for x in projects if x['id'] == int(project_id)]
    return response


@app.put('/project/{project_id}', status_code=200)
def update_project(project_id, response_details: Project):
    return 


@app.delete('/project/{project_id}', status_code=200)
def delete_project(project_id):
    deletion_set = set([int(project_id)])   
    for i in reversed(range(len(projects))):  # thanks to @juanpa.arrivillaga for this bit 
        if projects[i]['id'] in deletion_set:
            del projects[i]
    return  projects


@app.get('/project')
def get_projects():
    return projects


@app.post('/project/{project_id}/request', status_code=200)
def post_request(project_id, response_details: Request):
    requests.append({
        'id': len(requests),
        'project_id': int(project_id),
        'facility_id': response_details.facility_id,
        'energy_level': response_details.energy_level,
        'ions': response_details.ions,
        'integrator_id': response_details.integrator_id
    })
    return


# fetch data from requests table if the project_id and request_id match
@app.get('/project/{project_id}/request/{request_id}', status_code=200)
def get_request(project_id, request_id, response_details: Request):
    return


@app.put('/project/{project_id}/request{request_id}', status_code=200)
def update_request(project_id, request_id, response_details: Request):
    # find request with matching project_id and request_id and replace those values
    return


@app.delete('/project/{project_id}/request/{request_id}', status_code=200)
def delete_request(project_id, request_id, response_details: Request):
    # delete from request table if project_id and id match
    return


@app.get('/project/{project_id}/request')
def get_project_requests(project_id):
    return 