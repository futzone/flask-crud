import sqlite3
from typing import List, Optional
from student import Student
from datetime import datetime
import contextlib

class Database:
    """Ma'lumotlar bazasi boshqaruv klassi"""
    
    def __init__(self, db_name: str = 'students.db'):
        self.db_name = db_name
        self.init_database()
    
    def get_connection(self):
        """Ma'lumotlar bazasiga ulanish"""
        conn = sqlite3.connect(self.db_name)
        conn.row_factory = sqlite3.Row
        return conn
    
    def init_database(self):
        """Ma'lumotlar bazasi jadvalini yaratish"""
        try:
            with self.get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        firstname TEXT NOT NULL,
                        lastname TEXT NOT NULL,
                        birth_date TEXT NOT NULL,
                        step TEXT NOT NULL,
                        address TEXT NOT NULL,
                        created_date TEXT NOT NULL
                    )
                ''')
        except Exception as e:
            print(f"Database Initialization Error: {e}")
    
    def create_student(self, student: Student) -> int:
        """Yangi o'quvchi qo'shish"""
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO students (firstname, lastname, birth_date, step, address, created_date)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                student.firstname,
                student.lastname,
                student.birth_date,
                student.step,
                student.address,
                student.created_date
            ))
            student_id = cursor.lastrowid
            conn.commit()
            return student_id
        except Exception as e:
            print(f"Create Student Error: {e}")
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def get_all_students(self) -> List[Student]:
        """Barcha o'quvchilarni olish"""
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students ORDER BY created_date DESC')
            rows = cursor.fetchall()
            
            students = []
            for row in rows:
                student = Student(
                    id=row['id'],
                    firstname=row['firstname'],
                    lastname=row['lastname'],
                    birth_date=row['birth_date'],
                    step=row['step'],
                    address=row['address'],
                    created_date=row['created_date']
                )
                students.append(student)
            return students
        finally:
            conn.close()
    
    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        """ID bo'yicha o'quvchini olish"""
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM students WHERE id = ?', (student_id,))
            row = cursor.fetchone()
            
            if row:
                return Student(
                    id=row['id'],
                    firstname=row['firstname'],
                    lastname=row['lastname'],
                    birth_date=row['birth_date'],
                    step=row['step'],
                    address=row['address'],
                    created_date=row['created_date']
                )
            return None
        finally:
            conn.close()
    
    def update_student(self, student_id: int, student: Student) -> bool:
        """O'quvchi ma'lumotlarini yangilash"""
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE students
                SET firstname = ?, lastname = ?, birth_date = ?, step = ?, address = ?
                WHERE id = ?
            ''', (
                student.firstname,
                student.lastname,
                student.birth_date,
                student.step,
                student.address,
                student_id
            ))
            
            affected_rows = cursor.rowcount
            conn.commit()
            return affected_rows > 0
        except Exception as e:
            print(f"Update Student Error: {e}")
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def delete_student(self, student_id: int) -> bool:
        """O'quvchini o'chirish"""
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM students WHERE id = ?', (student_id,))
            
            affected_rows = cursor.rowcount
            conn.commit()
            return affected_rows > 0
        except Exception as e:
            print(f"Delete Student Error: {e}")
            conn.rollback()
            raise e
        finally:
            conn.close()
    
    def search_students(self, query: str) -> List[Student]:
        """O'quvchilarni qidirish"""
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            search_query = f'%{query}%'
            cursor.execute('''
                SELECT * FROM students
                WHERE firstname LIKE ? OR lastname LIKE ? OR address LIKE ?
                ORDER BY created_date DESC
            ''', (search_query, search_query, search_query))
            
            rows = cursor.fetchall()
            
            students = []
            for row in rows:
                student = Student(
                    id=row['id'],
                    firstname=row['firstname'],
                    lastname=row['lastname'],
                    birth_date=row['birth_date'],
                    step=row['step'],
                    address=row['address'],
                    created_date=row['created_date']
                )
                students.append(student)
            return students
        finally:
            conn.close()
