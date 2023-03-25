from fastapi import APIRouter


router = APIRouter(
    prefix="/user_managment"
)



@router.post('/user')
def create_user():
    return{'test'}
    




# Geting authenticated user GET
# Get user by id GET
# Get all users GET
# Update authenticated user PUT
# Delete authenticated user DELETE
