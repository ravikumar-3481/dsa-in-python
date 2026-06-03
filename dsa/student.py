import sqlite3 as sq3

class Student:
    def __init__(self):
        pass

    def save_to_db(self, student_record):
        conn = sq3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS students
                          (name TEXT, course TEXT, age INTEGER, grade REAL)''')
        cursor.execute('INSERT INTO students VALUES (?, ?, ?, ?)',
                       (student_record))
        conn.commit()
        conn.close()

student_record = [('Ravi', 'Python', 25, 85.5),
                  ('Anita', 'Data Science', 22, 90.0),
                  ('Suresh', 'Machine Learning', 28, 88.0),
                  ('Priya', 'Web Development', 24, 92.5),
                  ('Amit', 'Cybersecurity', 27, 80.0),
                  ('Neha', 'Cloud Computing', 23, 87.0),
                  ('Vikram', 'AI', 26, 91.0),
                  ('Sneha', 'Big Data', 24, 89.5),
                  ('Rahul', 'DevOps', 29, 84.0),
                  ('Pooja', 'Blockchain', 21, 93.0),
                  ('Karan', 'Data Analysis', 25, 86.0),
                  ('Anjali', 'Software Testing', 22, 88.5),
                  ('Rohit', 'Mobile Development', 27, 90.0),
                  ('Sonal', 'UI/UX Design', 24, 91.5),
                  ('Manish', 'Game Development', 26, 85.0),
                  ('Divya', 'AR/VR', 23, 89.0),
                  ('Aakash', 'IoT', 28, 87.5),
                  ('Meera', 'Data Visualization', 24, 92.0),
                  ('Sanjay', 'Cloud Security', 27, 88.0),
                  ('Riya', 'AI Ethics', 22, 90.5),
                  ('Vivek', 'Quantum Computing', 25, 86.5),
                  ('Ananya', 'Natural Language Processing', 24, 89.0),
                  ('Kavya', 'Computer Vision', 26, 91.0),
                  ('Arjun', 'Reinforcement Learning', 23, 88.5),
                  ('Sanya', 'Data Mining', 27, 90.0),
                  ('Aditya', 'Robotics', 24, 87.0),
                  ('Isha', 'Edge Computing', 22, 89.5),
                  ('Raghav', 'Autonomous Vehicles', 28, 85.0),
                  ('Nisha', 'Cyber Forensics', 25, 91.5),
                  ('Kunal', 'Virtual Reality', 26, 88.0),
                  ('Anika', 'Augmented Reality', 23, 90.0),
                  ('Siddharth', 'Data Engineering', 27, 87.5),
                  ('Maya', 'AI in Healthcare', 24, 89.0),
                  ('Rohini', 'AI in Finance', 22, 91.0),
                  ('Aarav', 'AI in Education', 28, 86.0),
                  ('Suhana', 'AI in Retail', 25, 88.5),
                  ('Devansh', 'AI in Manufacturing', 26, 90.0),
                  ('Anushka', 'AI in Agriculture', 23, 87.0),
                  ('Kartik', 'AI in Transportation', 27, 89.5),
                  ('Nikita', 'AI in Energy', 24, 91.0),
                  ('Rishabh', 'AI in Entertainment', 22, 88.0),
                  ('Sanya', 'AI in Sports', 28, 90.5),
                  ('Amit', 'AI in Marketing', 25, 87.0),
                  ('Isha', 'AI in Law', 26, 89.0),
                  ('Raghav', 'AI in Real Estate', 23, 91.5),
                  ('Nisha', 'AI in Human Resources', 27, 88.0),
                  ('Kunal', 'AI in Supply Chain', 24, 90.0),
                  ('Anika', 'AI in Customer Service', 22, 87.5),
                  ('Siddharth', 'AI in Cybersecurity', 28, 89.0),
                  ('Maya', 'AI in Social Media', 25, 91.0),
                  ('Rohini', 'AI in Advertising', 26, 88.5),
                  ('Aarav', 'AI in Gaming', 23, 90.0),
                  ('Suhana', 'AI in Music', 27, 87.0),
                  ('Devansh', 'AI in Sports', 24, 89.5),
                  ('Anushka', 'AI in Tourism', 22, 91.0),
                  ('Kartik', 'AI in Healthcare', 28, 88.0),
                  ('Nikita', 'AI in Finance', 25, 90.5),
                  ('Rishabh', 'AI in Education', 26, 87.0),
                  ('Sanya', 'AI in Retail', 23, 89.0),
                  ('Amit', 'AI in Manufacturing', 27, 91.0),
                  ('Isha', 'AI in Agriculture', 24, 88.5),
                  ('Raghav', 'AI in Transportation', 22, 90.0),
                  ('Nisha', 'AI in Energy', 28, 87.0),
                  ('Kunal', 'AI in Entertainment', 25, 89.5),
                  ('Anika', 'AI in Sports', 26, 90.0),
                  ('Siddharth', 'AI in Marketing', 23, 88.0),
                  ('Maya', 'AI in Law', 27, 91.5),
                  ('Rohini', 'AI in Real Estate', 24, 89.0),
                  ('Aarav', 'AI in Human Resources', 22, 90.5),
                  ('Suhana', 'AI in Supply Chain', 28, 87.0),
                  ('Devansh', 'AI in Customer Service', 25, 89.0),
                  ('Anushka', 'AI in Cybersecurity', 26, 90.0),
                  ('Kartik', 'AI in Social Media', 23, 88.5),
                  ('Nikita', 'AI in Advertising', 27, 89.0),
                  ('Rishabh', 'AI in Gaming', 24, 91.0),
                  ('Sanya', 'AI in Music', 22, 87.0)]

student = Student()
for record in student_record:
    student.save_to_db(record)

print("Student records have been saved to the database.")
