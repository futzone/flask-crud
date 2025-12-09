# O'quvchilar Boshqaruv Tizimi (Student Management System)

Ushbu loyiha o'quv markazlari yoki ta'lim muassasalari uchun o'quvchilar ma'lumotlarini boshqarish tizimidir. Tizim Python (Flask) va SQLite texnologiyalari asosida qurilgan bo'lib, zamonaviy va qulay Web interfeysga ega.

## Imkoniyatlar

- **Dashboard**: Asosiy sahifada barcha o'quvchilar ro'yxati va umumiy statistika.
- **CRUD Operatsiyalari**:
  - **Qo'shish**: Yangi o'quvchi ma'lumotlarini kiritish (Ism, Familiya, Tug'ilgan sana, Bosqich, Manzil).
  - **Ko'rish**: O'quvchilar ma'lumotlarini jadval ko'rinishida ko'rish.
  - **Tahrirlash**: Mavjud o'quvchi ma'lumotlarini o'zgartirish.
  - **O'chirish**: O'quvchini tizimdan o'chirish.
- **Qidiruv**: Ism, familiya yoki manzil bo'yicha tezkor qidiruv.
- **O'zbek Tili**: To'liq o'zbek tilidagi interfeys.
- **Dark Mode**: Zamonaviy, ko'zga yoqimli qorong'u dizayn.

## Texnologiyalar

- **Backend**: Python 3, Flask
- **Database**: SQLite
- **Frontend**: HTML5, CSS3 (Custom Design), Jinja2 Templating

## O'rnatish va Ishga Tushirish

Loyihani kompyuteringizda ishga tushirish uchun quyidagi qadamlarni bajaring:

1. **Python o'rnatilganligini tekshiring** (Python 3.6+ talab qilinadi).

2. **Kerakli kutubxonani o'rnating:**
   Terminalda quyidagi buyruqni bering:
   ```bash
   pip install flask
   ```

3. **Loyihani ishga tushiring:**
   Loyiha papkasida turib, quyidagi buyruqni bering:
   ```bash
   python app.py
   ```

4. **Brauzerda oching:**
   Brauzeringizni ochib, quyidagi manzilga kiring:
   ```
   http://localhost:5000
   ```

## Fayl Tuzilmasi

- `app.py` - Asosiy dastur kodi (server).
- `database.py` - Ma'lumotlar bazasi bilan ishlash klassi.
- `student.py` - O'quvchi ma'lumotlari shabloni (class).
- `templates/index.html` - Web sahifa (HTML).
- `static/style.css` - Dizayn fayli (CSS).
- `students.db` - Avtomatik yaratiladigan ma'lumotlar bazasi fayli.

## Xavfsizlik va Sozlamalar

- Ma'lumotlar bazasi `students.db` faylida saqlanadi. Agar bu faylni o'chirsangiz, barcha ma'lumotlar yo'qoladi.
- `app.py` faylida `secret_key` mavjud, haqiqiy loyihada uni o'zgartirish tavsiya etiladi.
