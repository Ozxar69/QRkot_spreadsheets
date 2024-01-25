from datetime import datetime

from aiogoogle import Aiogoogle
from sqlalchemy import func

from app.core.config import settings
from constants import (
    COLLECTION_TIME_LABEL,
    COLUMN_COUNT,
    DESCRIPTION_LABEL,
    FORMAT,
    GOOGLE_DRIVE_OBJ,
    GOOGLE_DRIVE_VERSION,
    GOOGLE_SHEETS_OBG,
    GOOGLE_SHEETS_VERSION,
    MAJOR_DIMENSION,
    NAME_LABEL,
    PERMISSION_FIELD,
    PERMISSION_ROLE,
    PERMISSION_TYPE,
    PROP_LOCALE,
    PROP_TITLE,
    ROW_COUNT,
    SHEET_ID,
    SHEET_TITLE,
    SHEET_TYPE,
    SPREADSHEET_ID,
    TABLE_VALUE_COL_1,
    TABLE_VALUE_COL_2,
    TABLE_VALUE_COL_3,
    TABLE_VALUE_DESC,
    VALUE_INPUT_OPTION,
    VALUES_RANGE,
)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    """Создает документ."""
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover(
        GOOGLE_SHEETS_OBG,
        GOOGLE_SHEETS_VERSION,
    )
    spreadsheet_body = {
        "properties": {
            "title": PROP_TITLE + now_date_time,
            "locale": PROP_LOCALE,
        },
        "sheets": [
            {
                "properties": {
                    "sheetType": SHEET_TYPE,
                    "sheetId": SHEET_ID,
                    "title": SHEET_TITLE,
                    "gridProperties": {
                        "rowCount": ROW_COUNT,
                        "columnCount": COLUMN_COUNT,
                    },
                }
            }
        ],
    }
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    return response[SPREADSHEET_ID]


async def set_user_permissions(
    spreadsheet_id: str,
    wrapper_services: Aiogoogle,
) -> None:
    """Предоставляет права доступа."""
    permissions_body = {
        "type": PERMISSION_TYPE,
        "role": PERMISSION_ROLE,
        "emailAddress": settings.email,
    }
    service = await wrapper_services.discover(
        GOOGLE_DRIVE_OBJ,
        GOOGLE_DRIVE_VERSION,
    )
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields=PERMISSION_FIELD,
        )
    )


async def spreadsheets_update_value(
    spreadsheet_id: str,
    charity_projects: list[dict],
    wrapper_services: Aiogoogle,
) -> None:
    """Обновляет данные в google-таблице."""
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover(
        GOOGLE_SHEETS_OBG,
        GOOGLE_SHEETS_VERSION,
    )

    table_values = [
        [PROP_TITLE, now_date_time],
        [TABLE_VALUE_DESC],
        [TABLE_VALUE_COL_1, TABLE_VALUE_COL_2, TABLE_VALUE_COL_3],
    ]

    for item in charity_projects:
        new_row = [
            item[NAME_LABEL],
            item[COLLECTION_TIME_LABEL],
            item[DESCRIPTION_LABEL],
        ]
        table_values.append(new_row)

    update_body = {"majorDimension": MAJOR_DIMENSION, "values": table_values}
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range=VALUES_RANGE.format(len(table_values)),
            valueInputOption=VALUE_INPUT_OPTION,
            json=update_body,
        )
    )


async def calculate_collection_time(
    create_date: datetime,
    close_date: datetime,
):
    """Получает время, затраченное на сбор пожертвований."""
    return func.julianday(close_date) - (func.julianday(create_date))
