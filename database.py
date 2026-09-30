from flask import Flask, render_template, request, jsonify
import sqlite3

DB_NAME = "college.db"

def create_database():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    # FAQ table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        category TEXT,
        message TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

    # Courses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    # Departments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL
        )
    """)

    # Helplines table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS helplines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    """)

    # Add FAQ data
    cursor.execute("""
        INSERT INTO faqs (keyword, answer)
        VALUES (?, ?)
    """, (
        "courses",
        "MRDU offers a wide range of engineering and medical courses."
    ))

    cursor.execute("""
        INSERT INTO faqs (keyword, answer)
        VALUES (?, ?)
    """, (
        "fees",
        "Engineering fees start from approximately ₹1.5 lakh and vary by course and scholarships."
    ))

    cursor.execute("""
        INSERT INTO faqs (keyword, answer)
        VALUES (?, ?)
    """, (
        "exam",
        "Examinations are scheduled to begin on November 6."
    ))

    cursor.execute("""
        INSERT INTO faqs (keyword, answer)
        VALUES (?, ?)
    """, (
        "location",
        "MRDU is located in Maisammaguda."
    ))

    # Add courses
    courses = [
        ("CSE", "Computer Science and Engineering"),
        ("ECE", "Electronics and Communication Engineering"),
        ("EEE", "Electrical and Electronics Engineering"),
        ("Mechanical", "Mechanical Engineering"),
        ("Civil", "Civil Engineering"),
        ("AI & ML", "Artificial Intelligence and Machine Learning"),
        ("Data Science", "Data Science"),
        ("MBBS", "Bachelor of Medicine and Bachelor of Surgery"),
        ("BDS", "Bachelor of Dental Surgery"),
        ("B.Pharm", "Bachelor of Pharmacy"),
        ("Nursing", "Nursing"),
        ("Physiotherapy", "Physiotherapy")
    ]

    cursor.executemany("""
        INSERT INTO courses (name, description)
        VALUES (?, ?)
    """, courses)

    # Add helpline
    cursor.execute("""
        INSERT INTO helplines (category, phone, email)
        VALUES (?, ?, ?)
    """, (
        "General",
        "+91 1234567890",
        "MRDUcampus@mrduc.ac.in"
    ))

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
    print("MRDU SQLite database created and populated successfully!")