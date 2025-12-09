from flask import Flask, render_template, request, redirect, url_for, flash
from database import Database
from student import Student

app = Flask(__name__)
app.secret_key = 'maxfiy_kalit_uchun_buni_ozgartiring'  # Flash xabarlar uchun kerak

# Ma'lumotlar bazasi obyekti
db = Database()

@app.route('/')
def index():
    """Asosiy sahifa - Dashboard"""
    search_query = request.args.get('q', '')
    if search_query:
        students = db.search_students(search_query)
    else:
        students = db.get_all_students()
    
    return render_template('index.html', students=students, search_query=search_query)

@app.route('/add', methods=['POST'])
def add_student():
    """Yangi o'quvchi qo'shish"""
    try:
        student = Student(
            firstname=request.form['firstname'],
            lastname=request.form['lastname'],
            birth_date=request.form['birth_date'],
            step=request.form['step'],
            address=request.form['address']
        )
        db.create_student(student)
        flash('O\'quvchi muvaffaqiyatli qo\'shildi!', 'success')
    except Exception as e:
        print(f"Xatolik (Add Student): {e}")
        flash(f'Xatolik yuz berdi: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/edit/<int:student_id>', methods=['POST'])
def edit_student(student_id):
    """O'quvchi ma'lumotlarini yangilash"""
    try:
        student = Student(
            firstname=request.form['firstname'],
            lastname=request.form['lastname'],
            birth_date=request.form['birth_date'],
            step=request.form['step'],
            address=request.form['address']
        )
        db.update_student(student_id, student)
        flash('O\'quvchi ma\'lumotlari yangilandi!', 'success')
    except Exception as e:
        flash(f'Xatolik yuz berdi: {str(e)}', 'error')
    
    return redirect(url_for('index'))

@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    """O'quvchini o'chirish"""
    try:
        db.delete_student(student_id)
        flash('O\'quvchi o\'chirildi!', 'warning')
    except Exception as e:
        flash(f'Xatolik yuz berdi: {str(e)}', 'error')
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
