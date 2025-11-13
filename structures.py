from dataclasses import dataclass
from typing import Optional

@dataclass
class Student:
    name: str
    group: int
    course: int
    age: int
    average_grade: float
