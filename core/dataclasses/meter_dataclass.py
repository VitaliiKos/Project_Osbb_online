from dataclasses import dataclass


@dataclass
class Meter:
    id: int
    type: str
    serial_number: str
