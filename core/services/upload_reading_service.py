import os
from uuid import uuid1


def upload_to(instance, file: str) -> str:
    ext = file.split('.')[-1]
    return os.path.join(instance.meter.user.profile.surname, 'meter_photos', f'{uuid1()}.{ext}')
