from datetime import datetime, timezone
from enum import Enum
from typing import List, Optional, Set, Union
from pydantic import BaseModel


class AuthDetails(BaseModel):
    username: str
    password: str

class CreateUserDetails(BaseModel):
    email: str
    first_name: str
    last_name: str
    password: str

    class Config:
        orm_mode = True

class Facility(BaseModel):
    id: int
    name: str
    full_name: str
    description: str
    accelerator: str
    hours_of_operation: str

        
    
class User(BaseModel):
    id: int
    affiliation_id: int
    user_name: str
    full_name: str
    first_name: str
    last_name: str
    created_at: str
    updated_at: str
    phone_number: str
    email: str
    verified_at: str
    disabled_at: str
    deleted_at: str
    role: str

class Affiliation(BaseModel):
    id: str
    name: str
    full_name: str
    description: str
    #created_by: {}
    
    
class Project(BaseModel):
    id: int
    #created_by: {}
    project_name: str
    description: str
    program: str
    devices_under_test: str
    purpose_of_test: str
    total_hours: str
    vacuum: str
    status: str
    created_at: str
    updated_at: str
    submitted_at: str
    approved_at: str
    scheduled_at: str
    completed_at: str
    cancelled_at: str
    test_start: str
    test_end: str
    #requests: []
    is_public: str
    
class Request(BaseModel):
    id: int
    project_id: int
    facility_id: str
    energy_level: str
    ions: str
    integrator_id: str

#Evan 1/24/22 
class Token(BaseModel):
    access_token: str
    token_type: str
    user: str

