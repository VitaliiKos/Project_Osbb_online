from enum import Enum


class RegEx(Enum):
    PASSWORD = (
        r'^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])([^\s]){5,16}$',
        [
            'password must contain 1 number(0-9)',
            'password must contain 1 uppercase letter',
            'password must contain 1 lowercase letter',
            'password must contain 1 non-alpha numeric number',
            'password is 5-16 characters with no space',
        ]
    )
    NAME = (
        r'^[a-zA-Z]{2,20}$',
        'only letters min 2 max 20 ch'
    )
    SURNAME = (
        r'^[a-zA-Z]{2,20}$',
        'only letters min 2 max 20 ch'
    )
    PHONE = (
        r'^\d{9}$',
        'invalid phone number Ex. 97 999 99 99 '
    )
    BRAND = (
        r'^[a-zA-Z]{2,20}$',
        'min 2 max 20ch'
    )
    OIL = (
        r'^[a-zA-Z]{2,20}$',
        'min 2 max 20ch'
    )
    GEARBOX = (
        r'^[a-zA-Z]{2,20}$',
        'min 2 max 20ch'
    )
    CAR_MODEL = (
        r'^[a-zA-Z0-9]{2,20}$',
        'min 2 max 20ch'
    )
    CAR_BODY = (
        r'^[a-zA-Z]{2,20}$',
        'min 2 max 20ch'
    )
    PROF_NAME = (
        r'^[a-zA-Z]{2,20}$',
        'only letters min 2 max 20 ch'
    )
    SELLER_DIRECTION = (
        r'^[a-zA-Z]{2,20}$',
        'only letters min 2 max 20 ch'
    )
    METER_SERIAL_NUMBER = (
        r'^[a-zA-Z0-9]{6}$',
        'serial number must contain 6 characters or digits with no space',
    )
    METER_TYPE = (
        r'^[a-zA-Z]{2,20}$',
        'only letters min 2 max 20 ch'
    )
    METER_READINGS = (
        r'^\d{6}$',
        'readings is 6 characters with no space',
    )

    def __init__(self, pattern: str, msg: str | list[str]):
        self.pattern = pattern
        self.msg = msg
