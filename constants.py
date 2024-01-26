import os
from datetime import datetime

from dotenv import load_dotenv

load_dotenv()  # не могу использовать from app.core.config import settings
# из за ошибки циклических импортов

# services/google_api
#   spreadsheets_create
FORMAT = "%Y/%m/%d %H:%M:%S"
GOOGLE_SHEETS_OBG = "sheets"
GOOGLE_SHEETS_VERSION = "v4"
PROP_TITLE = "Отчёт от "
SPREADSHEET_ID = "spreadsheetId"
SPREADSHEET_BODY = {
    "properties": {
        "title": "Отчёт от ",
        "locale": "ru_RU",
    },
    "sheets": [
        {
            "properties": {
                "sheetType": "GRID",
                "sheetId": 0,
                "title": "Лист1",
                "gridProperties": {
                    "rowCount": 100,
                    "columnCount": 11,
                },
            }
        }
    ],
}

#   set_user_permissions
GOOGLE_DRIVE_OBJ = "drive"
GOOGLE_DRIVE_VERSION = "v3"
PERMISSION_FIELD = "id"

PERMISSION_BODY = {
    "type": "user",
    "role": "writer",
    "emailAddress": os.getenv("EMAIL"),
}

#   spreadsheets_update_value
TABLE_VALUE_DESC = "Топ проектов по скорости закрытия"
TABLE_VALUE_COL_1 = "Название проекта"
TABLE_VALUE_COL_2 = "Время сбора"
TABLE_VALUE_COL_3 = "Описание"
MAJOR_DIMENSION = "ROWS"
VALUES_RANGE = "A1:C{}"
VALUE_INPUT_OPTION = "USER_ENTERED"

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]
GOOGLE_SHEETS_URL = "https://docs.google.com/spreadsheets/d/"
SUMMARY = "Отчет по закрытым проектам"

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

# crud/charityproject
WAS_FULLY_INVESTED = 1
COLLECTION_TIME_FORMAT = "%d days, %H:%M:%S"
NAME_LABEL = "name"
DESCRIPTION_LABEL = "description"
COLLECTION_TIME_LABEL = "collection_time"

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
GOOGLE_API_VARIABLES = (
    "Невозможно сформировать отчет. Ошибка в конфигурационных параметрах. "
    "Проверьте настройки Google API."
)


# api/routers
CHARITY_PROJECT_ROUTER_PREFIX = "/charity_project"
CHARITY_PROJECT_ROUTER_TAG = "Charity Projects"
DONATION_ROUTER_PREFIX = "/donation"
DONATION_ROUTER_TAG = "Donations"
GOOGLE_ROUTER_PREFIX = "/google"
GOOGLE_ROUTER_TAG = "Google"

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

# api/endpoints/charityproject, donation, google_api
ROUTE_CLEAR = "/"
ROUTE_PROJECT_ID = "/{charity_project_id}"
ROUTE_MY = "/my"
