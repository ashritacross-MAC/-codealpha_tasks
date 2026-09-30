from flask import Flask, render_template, request, jsonify
import sqlite3

def get_db_connection():
    connection = sqlite3.connect("college.db")
    connection.row_factory = sqlite3.Row
    return connection
def get_faq(keyword):
    connection = get_db_connection()

    faq = connection.execute(
        "SELECT answer FROM faqs WHERE keyword = ?",
        (keyword,)
    ).fetchone()

    connection.close()

    if faq:
        return faq["answer"]

    return None

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json()
    user_message = data.get("message", "")
    language = data.get("language", "en")
    faq = {
        "courses": "MRDU offers a wide range of engineering and medical courses.",
        "fees": "Engineering course fees at MRDU start from approximately ₹1.5 lakh. The final fee may vary depending on the course and applicable scholarships. Scholarships may include NCC and sports-based benefits.",
        "exam": "The examinations are scheduled to begin from November 6.",
        "results": "Results will be announced after the examination process is completed. Please check the official college notifications for updates.",
        "location": "MRDU is located in Maisammaguda.",
        "library": "The college library provides textbooks, reference materials, journals, and study spaces for students.",
        "events": "College events, workshops, seminars, and holidays are announced through official college notifications.",
        "certificate": "Students can contact the administration office to request certificates and other official documents."
    }

    message = user_message.lower()

    # ---------------- HELPLINES ----------------

    if "admission" in message:
        reply = "📞 Admissions: +91 1234567890"

    elif "examination" in message:
        reply = "📞 Examination Cell: +91 1234567890"

    elif "exam" in message:
        reply = "📞 Examination Cell: +91 1234567890"

    elif "fee"  "account" in message:
        reply = "📞 Accounts/Fees: +91 1234567890"

    elif "hostel" in message:
        reply = "📞 Hostel: +91 1234567890"

    elif "transport" in message:
        reply = "📞 Transport: +91 1234567890"

    elif "technical" in message or "it help" in message:
        reply = "📞 IT/Technical: +91 1234567890"

    elif "security" in message:
        reply = "📞 Security: +91 1234567890"

    elif "medical" in message:
        reply = "📞 Medical: +91 1234567890"

    elif "emergency" in message:
        reply = "🚨 Emergency: +91 1234567890"

    elif "email" in message or "mail" in message:
        reply = "📧 MRDU Email: MRDUcampus@mrduc.ac.in"

    elif "helpline" in message or "contact" in message or "phone" in message:
        reply = (
            "📞 MRDU Helplines:\n\n"
            "College Office: +91 1234567890\n"
            "Admissions: +91 1234567890\n"
            "Examination Cell: +91 1234567890\n"
            "Accounts/Fees: +91 1234567890\n"
            "CSE/Academic: +91 1234567890\n"
            "Hostel: +91 1234567890\n"
            "Transport: +91 1234567890\n"
            "IT/Technical: +91 1234567890\n"
            "Security: +91 1234567890\n"
            "Medical: +91 1234567890\n"
            "Emergency: +91 1234567890\n\n"
            "📧 Email: MRDUcampus@mrduc.ac.in"
        )

    # ---------------- COURSES ----------------

    elif "cse" in message or "computer science" in message:
        reply = (
            "💻 CSE — Computer Science & Engineering\n\n"
            "📖 About:\n"
            "CSE focuses on programming, software development, "
            "algorithms, databases, computer networks, AI and "
            "modern computing technologies.\n\n"
            "🧠 Major Subjects:\n"
            "• Programming & Data Structures\n"
            "• Database Management Systems\n"
            "• Operating Systems\n"
            "• Computer Networks\n"
            "• Artificial Intelligence\n"
            "• Web Development\n\n"
            "💼 Career Areas:\n"
            "Software Development, AI/ML, Data Science, "
            "Cybersecurity, Cloud Computing and Web Development.\n\n"
            "📚 Recommended Books:\n"
            "• Python Crash Course — Eric Matthes\n"
            "• Introduction to Algorithms — Cormen et al.\n"
            "• Operating System Concepts — Silberschatz et al.\n"
            "• Computer Networking — Kurose & Ross\n\n"
            "📞 CSE/Academic Contact: +91 1234567890"
        )

    elif "ece" in message or "electronics" in message:
        reply = (
            "📡 ECE — Electronics & Communication Engineering\n\n"
            "📖 About:\n"
            "ECE focuses on electronic circuits, communication "
            "systems, digital electronics, signal processing and "
            "embedded technologies.\n\n"
            "🧠 Major Subjects:\n"
            "• Electronic Devices & Circuits\n"
            "• Digital Electronics\n"
            "• Signals & Systems\n"
            "• Communication Systems\n"
            "• Microprocessors\n"
            "• Embedded Systems\n\n"
            "💼 Career Areas:\n"
            "Embedded Systems, Electronics Design, Telecommunications, "
            "VLSI, Networking and Signal Processing.\n\n"
            "📚 Recommended Books:\n"
            "• Microelectronic Circuits — Sedra & Smith\n"
            "• Digital Design — Morris Mano\n"
            "• Electronic Communication Systems — Kennedy\n"
            "• Signals and Systems — Oppenheim\n\n"
            "📞 ECE Academic Contact: +91 1234567890"
        )

    elif "eee" in message or "electrical" in message:
        reply = (
            "⚡ EEE — Electrical & Electronics Engineering\n\n"
            "📖 About:\n"
            "EEE deals with electrical power systems, machines, "
            "control systems, electronics and renewable energy.\n\n"
            "🧠 Major Subjects:\n"
            "• Electrical Machines\n"
            "• Power Systems\n"
            "• Control Systems\n"
            "• Power Electronics\n"
            "• Electrical Measurements\n"
            "• Renewable Energy\n\n"
            "💼 Career Areas:\n"
            "Power Engineering, Electrical Design, Automation, "
            "Renewable Energy and Industrial Systems.\n\n"
            "📚 Recommended Books:\n"
            "• Electrical Machinery — P.S. Bimbhra\n"
            "• Power System Engineering — Nagrath & Kothari\n"
            "• Power Electronics — P.S. Bimbhra\n"
            "• Control Systems Engineering — Nise\n\n"
            "📞 EEE Academic Contact: +91 1234567890"
        )

    elif "mechanical" in message:
        reply = (
            "⚙️ Mechanical Engineering\n\n"
            "📖 About:\n"
            "Mechanical Engineering focuses on machines, manufacturing, "
            "thermodynamics, mechanics, materials and industrial systems.\n\n"
            "🧠 Major Subjects:\n"
            "• Engineering Mechanics\n"
            "• Thermodynamics\n"
            "• Manufacturing Processes\n"
            "• Machine Design\n"
            "• Fluid Mechanics\n"
            "• Heat Transfer\n\n"
            "💼 Career Areas:\n"
            "Automotive, Manufacturing, Design, Robotics, Production "
            "and Industrial Engineering.\n\n"
            "📚 Recommended Books:\n"
            "• Engineering Mechanics — R.S. Khurmi\n"
            "• Thermodynamics — Cengel\n"
            "• Manufacturing Engineering — Kalpakjian\n"
            "• Theory of Machines — Rattan\n\n"
            "📞 Mechanical Academic Contact: +91 1234567890"
        )

    elif "civil" in message:
        reply = (
            "🏗️ Civil Engineering\n\n"
            "📖 About:\n"
            "Civil Engineering deals with construction, structures, "
            "transportation, environmental systems and infrastructure.\n\n"
            "🧠 Major Subjects:\n"
            "• Structural Engineering\n"
            "• Surveying\n"
            "• Geotechnical Engineering\n"
            "• Transportation Engineering\n"
            "• Environmental Engineering\n"
            "• Construction Management\n\n"
            "💼 Career Areas:\n"
            "Construction, Structural Design, Infrastructure, "
            "Transportation, Surveying and Project Management.\n\n"
            "📚 Recommended Books:\n"
            "• Strength of Materials — R.K. Rajput\n"
            "• Soil Mechanics — Gopal Ranjan\n"
            "• Surveying — B.C. Punmia\n"
            "• Structural Analysis — R.C. Hibbeler\n\n"
            "📞 Civil Academic Contact: +91 1234567890"
        )

    elif "ai" in message or "artificial intelligence" in message or "machine learning" in message:
        reply = (
            "🤖 AI & ML — Artificial Intelligence & Machine Learning\n\n"
            "📖 About:\n"
            "AI & ML focuses on intelligent systems, machine learning, "
            "data-driven models, computer vision and natural language processing.\n\n"
            "🧠 Major Subjects:\n"
            "• Python Programming\n"
            "• Machine Learning\n"
            "• Deep Learning\n"
            "• Computer Vision\n"
            "• Natural Language Processing\n"
            "• Data Mining\n\n"
            "💼 Career Areas:\n"
            "AI Engineer, ML Engineer, Data Scientist, AI Researcher "
            "and Computer Vision Engineer.\n\n"
            "📚 Recommended Books:\n"
            "• Hands-On Machine Learning — Aurélien Géron\n"
            "• Deep Learning — Goodfellow, Bengio & Courville\n"
            "• Artificial Intelligence: A Modern Approach — Russell & Norvig\n"
            "• Python for Data Analysis — Wes McKinney\n\n"
            "📞 AI & ML Academic Contact: +91 1234567890"
        )

    elif "data science" in message or "data analytics" in message:
        reply = (
            "📊 Data Science\n\n"
            "📖 About:\n"
            "Data Science combines programming, statistics and machine "
            "learning to extract useful insights from data.\n\n"
            "🧠 Major Subjects:\n"
            "• Python Programming\n"
            "• Statistics\n"
            "• Data Analysis\n"
            "• Machine Learning\n"
            "• Data Visualization\n"
            "• Database Systems\n\n"
            "💼 Career Areas:\n"
            "Data Scientist, Data Analyst, Business Analyst, "
            "ML Engineer and Data Engineer.\n\n"
            "📚 Recommended Books:\n"
            "• Python for Data Analysis — Wes McKinney\n"
            "• Hands-On Machine Learning — Aurélien Géron\n"
            "• Practical Statistics for Data Scientists — Bruce & Bruce\n"
            "• Data Science from Scratch — Joel Grus\n\n"
            "📞 Data Science Academic Contact: +91 1234567890"
        )

    # ---------------- MEDICAL COURSES ----------------

    elif "mbbs" in message:
        reply = (
            "🩺 MBBS — Bachelor of Medicine and Bachelor of Surgery\n\n"
            "📖 About:\n"
            "MBBS is a medical education program covering human anatomy, "
            "physiology, pathology, pharmacology and clinical medicine.\n\n"
            "🧠 Major Areas:\n"
            "• Anatomy\n"
            "• Physiology\n"
            "• Biochemistry\n"
            "• Pathology\n"
            "• Pharmacology\n"
            "• Clinical Medicine\n\n"
            "💼 Career Areas:\n"
            "Medical practice, hospitals, clinical specialties, "
            "public health and medical research.\n\n"
            "📚 Recommended Books:\n"
            "• Gray's Anatomy for Students\n"
            "• Guyton and Hall Textbook of Medical Physiology\n"
            "• Robbins Basic Pathology\n"
            "• Katzung's Basic & Clinical Pharmacology\n\n"
            "📞 Medical Contact: +91 1234567890"
        )

    elif "bds" in message or "dental" in message:
        reply = (
            "🦷 BDS — Bachelor of Dental Surgery\n\n"
            "📖 About:\n"
            "BDS focuses on oral health, dental sciences, diagnosis, "
            "prevention and treatment of dental conditions.\n\n"
            "🧠 Major Areas:\n"
            "• Oral Anatomy\n"
            "• Dental Materials\n"
            "• Oral Pathology\n"
            "• Periodontics\n"
            "• Prosthodontics\n"
            "• Oral Surgery\n\n"
            "💼 Career Areas:\n"
            "Dental Practice, Hospitals, Dental Clinics, Research "
            "and Public Health Dentistry.\n\n"
            "📚 Recommended Books:\n"
            "• Textbook of Oral Pathology — Shafer\n"
            "• Dental Materials — Anusavice\n"
            "• Clinical Periodontology — Carranza\n"
            "• Prosthodontic Treatment — Zarb\n\n"
            "📞 Dental/Medical Contact: +91 1234567890"
        )

    elif "b.pharm" in message or "b pharm" in message or "pharmacy" in message:
        reply = (
            "💊 B.Pharm — Bachelor of Pharmacy\n\n"
            "📖 About:\n"
            "B.Pharm focuses on medicines, pharmaceutical sciences, "
            "drug development, formulation and patient care.\n\n"
            "🧠 Major Subjects:\n"
            "• Pharmaceutics\n"
            "• Pharmacology\n"
            "• Pharmaceutical Chemistry\n"
            "• Pharmacognosy\n"
            "• Biochemistry\n"
            "• Drug Analysis\n\n"
            "💼 Career Areas:\n"
            "Pharmaceutical Industry, Drug Research, Quality Control, "
            "Hospital Pharmacy and Regulatory Affairs.\n\n"
            "📚 Recommended Books:\n"
            "• Remington: The Science and Practice of Pharmacy\n"
            "• Essentials of Medical Pharmacology — K.D. Tripathi\n"
            "• Wilson and Gisvold's Textbook of Organic Medicinal Chemistry\n"
            "• Aulton’s Pharmaceutics\n\n"
            "📞 Pharmacy Contact: +91 1234567890"
        )

    elif "nursing" in message:
        reply = (
            "👩‍⚕️ Nursing\n\n"
            "📖 About:\n"
            "Nursing education focuses on patient care, health assessment, "
            "clinical practice, healthcare procedures and community health.\n\n"
            "🧠 Major Areas:\n"
            "• Fundamentals of Nursing\n"
            "• Anatomy & Physiology\n"
            "• Medical-Surgical Nursing\n"
            "• Community Health Nursing\n"
            "• Child Health Nursing\n"
            "• Mental Health Nursing\n\n"
            "💼 Career Areas:\n"
            "Hospitals, Clinics, Community Health, Public Health, "
            "Specialized Nursing and Healthcare Administration.\n\n"
            "📚 Recommended Books:\n"
            "• Fundamentals of Nursing — Potter & Perry\n"
            "• Medical-Surgical Nursing — Brunner & Suddarth\n"
            "• Community Health Nursing — K. Park\n"
            "• Anatomy & Physiology — Ross & Wilson\n\n"
            "📞 Nursing Contact: +91 1234567890"
        )

    elif "physiotherapy" in message or "physio" in message:
        reply = (
            "🏃 Physiotherapy\n\n"
            "📖 About:\n"
            "Physiotherapy focuses on movement, rehabilitation, pain "
            "management and improving physical function.\n\n"
            "🧠 Major Areas:\n"
            "• Human Anatomy\n"
            "• Exercise Therapy\n"
            "• Electrotherapy\n"
            "• Orthopaedic Physiotherapy\n"
            "• Neurological Physiotherapy\n"
            "• Sports Physiotherapy\n\n"
            "💼 Career Areas:\n"
            "Hospitals, Rehabilitation Centres, Sports Clinics, "
            "Private Practice and Fitness & Wellness.\n\n"
            "📚 Recommended Books:\n"
            "• Therapeutic Exercise — Kisner & Colby\n"
            "• Textbook of Orthopaedics — Maheshwari\n"
            "• Electrotherapy — Clayton's\n"
            "• Gray's Anatomy for Students\n\n"
            "📞 Physiotherapy Contact: +91 1234567890"
        )

    # ---------------- GENERAL COLLEGE INFORMATION ----------------

    if "course" in message:
        if language == "te":
            reply = "MRDUలో వివిధ ఇంజినీరింగ్ మరియు మెడికల్ కోర్సులు అందుబాటులో ఉన్నాయి."
        elif language == "hi":
            reply = "MRDU में विभिन्न इंजीनियरिंग और मेडिकल पाठ्यक्रम उपलब्ध हैं।"
        else:
            reply = get_faq("courses")
    elif "fee" in message:
        if language == "te":
            reply = "ఇంజినీరింగ్ కోర్సుల ఫీజు సుమారు ₹1.5 లక్షల నుండి ప్రారంభమవుతుంది."
        elif language == "hi":
            reply = "इंजीनियरिंग पाठ्यक्रमों की फीस लगभग ₹1.5 लाख से शुरू होती है।"
        else:
            reply = get_faq("fees")

    elif "result" in message:
        reply = get_faq("results")

    elif "location" in message or "where" in message or "campus" in message:
        reply = get_faq("location")

    elif "library" in message:
        reply = get_faq("library")

    elif "event" in message or "holiday" in message:
        reply = get_faq("events")

    elif "certificate" in message or "document" in message:
        reply = get_faq("certificate")
    elif "exam" in message:
        reply = get_faq("exam")

    else:
        reply = (
            "I'm sorry, I don't have information about that yet. "
            "Please contact the college administration for assistance."
        )

    return jsonify({
        "reply": reply
    })


if __name__ == "__main__":
    app.run(debug=True)