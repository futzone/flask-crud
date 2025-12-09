from datetime import datetime
from typing import Optional

class Student:
    """O'quvchi klassi - talaba ma'lumotlarini saqlash uchun"""
    
    def __init__(
        self,
        firstname: str,
        lastname: str,
        birth_date: str,
        step: str,
        address: str,
        id: Optional[int] = None,
        created_date: Optional[str] = None
    ):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.birth_date = birth_date
        self.step = step
        self.address = address
        self.created_date = created_date or datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def to_dict(self):
        """Student obyektini lug'atga aylantirish"""
        return {
            'id': self.id,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'birth_date': self.birth_date,
            'step': self.step,
            'address': self.address,
            'created_date': self.created_date
        }
    
    @staticmethod
    def from_dict(data: dict):
        """Lug'atdan Student obyekti yaratish"""
        return Student(
            id=data.get('id'),
            firstname=data['firstname'],
            lastname=data['lastname'],
            birth_date=data['birth_date'],
            step=data['step'],
            address=data['address'],
            created_date=data.get('created_date')
        )
    
    def __repr__(self):
        return f"Student(id={self.id}, firstname='{self.firstname}', lastname='{self.lastname}')"
