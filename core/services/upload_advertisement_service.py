import os
from uuid import uuid1


def upload_to(instance, file: str) -> str:
    ext = file.split('.')[-1]
    print(ext)
    print('#########7########', instance)
    return os.path.join(instance.advertisement.user.profile.surname, 'advertisement_photo', f'{uuid1()}.{ext}')
