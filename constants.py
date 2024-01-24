from datetime import datetime

# schemas/charityproject, schemas/donation
PR_NAME_MIN_LEN = 1
PR_NAME_MAX_LEN = 100
PR_DESC_MIN_LEN = 1
DON_COMMENT_MIN_LEN = 1
FULL_AMOUNT_GT = 0
CREATE_DATE = datetime.now().isoformat(timespec="seconds")
INVESTED_AMOUNT_DEFAULT = 0

# models/custombase
FULLY_INVESTED_DEFAULT = False
CREATE_DATE_DEFAULT = datetime.utcnow
CLOSE_DATE_DEFAULT = None
# models/donation
USER_ID_FK_MD = "user.id"
USER_ID_FK_NAME = "fk_donation_user_id_user"

# core/user
BEARER_TRANSPORT = "auth/jwt/login"
LIFETIME_SECONDS = 3600
AUTH_BACKEND_NAME = "jwt"
PASSWORD_MIN_LEN = 3
# core/config
APP_TITLE = "Поддержка котиков QRKot"
DATABASE_URL = "sqlite+aiosqlite:///./fastapi.db"
SECRET = "SECRET"
ENV_FILE_NAME = ".env"

# api/validators
NAME_DUPLICATE_EXCEPTION = "Проект с таким именем уже существует!"
PROJECT_NOT_EXISTS_EXCEPTION = "Благотворительный проект не найден!"
CLOSED_PROJECT_EXCEPTION = "Закрытый проект нельзя редактировать!"
FULL_AMOUNT_EXCEPTION = "Требуемая сумма не может быть меньше внесённой!"
DELETE_PROJECT_EXCEPTION = (
    "В проект были внесены средства, не подлежит удалению!"
)
NOT_INVESTED_YET = 0

# api/routers
CHARITY_PROJECT_ROUTER_PREFIX = "/charity_project"
CHARITY_PROJECT_ROUTER_TAG = "Charity Projects"
DONATION_ROUTER_PREFIX = "/donation"
DONATION_ROUTER_TAG = "Donations"

# api/endpoints/user
USER_AUTH_ROUTER_PREFIX = "/auth/jwt"
USER_AUTH_ROUTER_TAG = "auth"
USER_REGISTER_ROUTER_PREFIX = "/auth"
USER_REGISTER_ROUTER_TAG = "auth"
USERS_PREFIX = "/users"
USERS_TAG = "users"
DELETE_ROUTE = "/users/{id}"
DELETE_TAG = "users"
DELETE_USER_EXCEPTION = "Удаление пользователей запрещено!"
