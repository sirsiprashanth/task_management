from fastapi import APIRouter


router = APIRouter(
    prefix="/auth"
)


@router.post('/login')
async def login_user():
    return "Login user working"


# login POST
# google_login GET
# facbook_login GET
# create_account POST
