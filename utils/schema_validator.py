from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
	page: int
	per_page: int
	total: int
	total_pages: int
	data: list

class CreateUserResponse(BaseModel):
	name: str
	job: str
	id: Optional[str]
	createdAt: Optional[str]

class LoginSuccessResponse(BaseModel):
	token: str

class LoginFailureResponse(BaseModel):
	error: str
