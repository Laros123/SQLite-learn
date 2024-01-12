import sqlite3

conn = sqlite3.connect('sql.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT
);
''')


cursor.execute('''
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT,
    instructor TEXT
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
)
''')
#"cursor.execute('''''')"
conn.commit()

while True:
    print("\n1. Додати нового студента")
    print("2. Додати новий курс")
    print("3. Показати список студентів")
    print("4. Показати список курсів")
    print("5. Зареєструвати студента на курс")
    print("6. Показати студентів на конкретному курсі")
    print("7. Вийти")

    choice = input("Оберіть опцію (1-7):")

    if choice == "1":
        try:
            name = input('Name\n')
            age = int(input('Age\n'))
            major = input('Major\n')
            cursor.execute(f'INSERT INTO students (name, age, major) VALUES ("{name}", {age}, "{major}")')
        except Exception as error:
            print('Помилка!', str(error))
            continue
        print('Успішно додано!')

    elif choice == "2":
        try:
            course_name = input('Name\n')
            instructor = input('Instructor\n')
            cursor.execute(f'INSERT INTO courses (course_name, instructor) VALUES ("{course_name}", "{instructor}")')
        except Exception as error:
            print('Помилка!', str(error))
            continue
        print('Успішно додано!')

    elif choice == "3":
        try:
            value = cursor.execute('SELECT * FROM students').fetchall()
        except Exception as error:
            print('Помилка!', str(error))
            continue
        print(*value, sep='\n')

    elif choice == "4":
        try:
            value = cursor.execute('SELECT * FROM courses').fetchall()
        except Exception as error:
            print('Помилка!', str(error))
            continue
        print(*value, sep='\n')

    elif choice == "5":
        try:
            student_id = int(input('Student_id\n'))
            course_id = int(input('Course id\n'))
            cursor.execute(f'INSERT INTO enrollments (student_id, course_id) VALUES ({student_id}, {course_id})')
        except Exception as error:
            print('Помилка!', str(error))
            continue
        print('Зареєстровано!')

    elif choice == "6":
        try:
            course_id = int(input('Course id\n'))
            value = cursor.execute(f'''SELECT * FROM students 
                                WHERE id IN (SELECT student_id FROM enrollments 
                                WHERE course_id = {course_id})''').fetchall()
        except Exception as error:
            print('Помилка!', str(error))
            continue
        print(*value, sep='\n')

    elif choice == "7":
        break

    else:
        print("Некоректний вибір. Будь ласка, введіть число від 1 до 7.")

    conn.commit()

conn.close()

