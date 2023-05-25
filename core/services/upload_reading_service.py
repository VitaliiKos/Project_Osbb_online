import os
from uuid import uuid1


def upload_to(instance, file: str) -> str:
    ext = file.split('.')[-1]
    return os.path.join(instance.meter_readings.meter.user.profile.surname, 'meter_readings_photo', f'{uuid1()}.{ext}')
