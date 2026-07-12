# knowledge_base.py
# Complete offline knowledge base containing institute, courses, and student FAQ details.

knowledge = {
    # ==================================================================
    # 1. GREETINGS & SOCIALS
    # ==================================================================
    "greeting_hi": {
        "keywords": ["hi"],
        "answer": "Hello! 👋 Welcome to Easy Learn Academy. I'm your virtual assistant. How can I help you today?"
    },
    "greeting_hello": {
        "keywords": ["hello", "hey"],
        "answer": "Hi! It's great to see you. How may I assist you with our courses or institute information?"
    },
    "goodmorning": {
        "keywords": ["morning"],
        "answer": "Good Morning! 🌞 Welcome to Easy Learn Academy. I hope you're having a wonderful day. How can I assist you today?"
    },
    "goodevening": {
        "keywords": ["evening"],
        "answer": "Good Evening! 🌆 Welcome to Easy Learn Academy. I hope you're having a wonderful evening. How can I assist you today?"
    },
    "howareyou": {
        "keywords": [["how", "you"], ["how", "are", "you"]],
        "answer": "I'm doing great, thank you for asking! 😊 I'm here to help you with information about Easy Learn Academy and our courses."
    },
    "bye": {
        "keywords": ["bye", "goodbye", "exit", "quit"],
        "answer": "Thank you for visiting Easy Learn Academy. 👋 Have a wonderful day, and I hope to assist you again soon!"
    },
    "thankyou": {
        "keywords": ["thank", "thanks", "thankyou"],
        "answer": "You're most welcome! 😊 If you have any more questions, feel free to ask. Have a great day!"
    },
    "identity": {
        "keywords": [["who", "you"], ["your", "name"], ["what", "you", "do"]],
        "answer": "I am the EasyLearn AI Student Assistant. I can help you with details about our IT courses, fees, duration, lab timings, placements, and academy policies."
    },

    # ==================================================================
    # 2. INSTITUTE OVERVIEW & INFO
    # ==================================================================
    "vision_mission": {
        "keywords": ["vision", "mission", "goal", "aim"],
        "answer": "Our Vision is to bridge the gap between academic education and industry requirements. Our Mission is to provide 100% practical, hands-on coding training to make every student job-ready."
    },
    "founder_director": {
        "keywords": ["founder", "director", "owner", "started", "head", "management"],
        "answer": "EasyLearn Academy was founded and is directed by senior software developers with over 10+ years of active industry experience in full-stack programming."
    },
    "experience_history": {
        "keywords": ["experience", "history", "established", "years", "old"],
        "answer": "Established in Bhavnagar, EasyLearn Academy has successfully trained hundreds of BCA, MCA, Diploma, and engineering students, helping them transition into professional software developers."
    },
    "achievements_awards": {
        "keywords": ["achievements", "awards", "achievement", "ranking", "rank"],
        "answer": "We are proud to be an ISO 9001:2015 Certified IT Institute. Our biggest achievement is our high placement success rate in local and national IT firms."
    },
    "why_choose_us": {
        "keywords": ["why", "choose", "benefits", "features", "special", "difference"],
        "answer": "Choose us for: (1) 100% practical lab training (No theory rote learning), (2) Individual desktop PC for practice, (3) ISO Certification, (4) Experienced developer trainers, (5) Monthly EMI options, (6) 100% job placement support."
    },

    # ==================================================================
    # 3. CONTACT & LOCATION INFO
    # ==================================================================
    "location": {
        "keywords": ["location", "address", "situated", "office", "directions", "mall"],
        "answer": "EasyLearn Academy is located at Shop No. 105, Eva Surbhi Mall, Waghawadi Road, opposite Aksharwadi Mandir, Bhavnagar, Gujarat - 364002."
    },
    "landmark": {
        "keywords": ["landmark", "opposite", "crossroad"],
        "answer": "Our academy is located on the 1st floor of Eva Surbhi Mall, situated right opposite the Aksharwadi Temple on Waghawadi Road, Bhavnagar."
    },
    "map": {
        "keywords": ["map", "location link", "directions link"],
        "answer": "You can search 'EasyLearn Academy Bhavnagar' on Google Maps or visit this location link: [Eva Surbhi Mall Location](https://maps.google.com/?q=EasyLearn+Academy+Bhavnagar) (Internet required for map)."
    },
    "contact": {
        "keywords": ["contact", "phone", "mobile", "number", "call", "inquire"],
        "answer": "You can call us directly on our mobile helpline: +91-9662512857 for admissions and queries."
    },
    "whatsapp": {
        "keywords": ["whatsapp", "wa", "message"],
        "answer": "Send us a WhatsApp message on our support number: +91-9662512857 for instant course details."
    },
    "email": {
        "keywords": ["email", "mail"],
        "answer": "Our official support email address is: theeasylearn@gmail.com. Feel free to write to us."
    },
    "website": {
        "keywords": ["website", "site", "url", "link"],
        "answer": "Visit our official website at: www.theeasylearnacademy.com for course details and announcements."
    },
    "working_hours": {
        "keywords": ["hours", "timings", "timing", "open", "close", "working", "schedule"],
        "answer": "The academy is open Monday to Saturday from 8:00 AM to 8:00 PM. Lab coordinates run throughout these hours."
    },
    "holidays": {
        "keywords": ["holiday", "holidays", "sunday", "sunday open", "closed"],
        "answer": "The academy remains closed on Sundays and major public holidays (like Diwali, Uttarayan, Independence Day)."
    },

    # ==================================================================
    # 4. ADMISSIONS & FINANCE
    # ==================================================================
    "admission_process": {
        "keywords": ["admission", "process", "enroll", "how to join"],
        "answer": "Admission is direct: (1) Visit our office at Eva Surbhi Mall, (2) Get counseling and choose your course, (3) Take 3 days free demo classes, (4) Fill the admission form, pay the registration fee, and start."
    },
    "registration": {
        "keywords": ["registration", "register", "admission form"],
        "answer": "Registration can be completed offline at our office by filling the student registration form and paying a nominal booking fee of Rs. 1,000 (which is adjusted in your course fees)."
    },
    "documents": {
        "keywords": ["documents", "document", "marksheet", "required"],
        "answer": "Required documents for admission: (1) Copy of Aadhaar Card, (2) Passport size photograph, (3) Copy of last academic marksheet (10th/12th/College result)."
    },
    "payment_methods": {
        "keywords": ["payment", "methods", "gpay", "upi", "card", "cash"],
        "answer": "We accept various payment methods: Cash, Google Pay, PhonePe, Paytm, BHIM UPI, Net Banking, and Bank Account transfers."
    },
    "installments": {
        "keywords": ["installments", "installment", "part payment", "fee installment"],
        "answer": "Yes! All course fees can be paid in comfortable monthly installments (EMIs) over the duration of the course."
    },
    "scholarship": {
        "keywords": ["scholarship", "scholarships", "concession", "discount", "discounts"],
        "answer": "We offer discounts for: (1) Single payment (lump-sum discount), (2) Meritorious college students, (3) Group admissions (2 or more students joining together)."
    },
    "refund_policy": {
        "keywords": ["refund", "cancel", "fee return"],
        "answer": "Fees once paid after the 3-day demo period are non-refundable. However, students can freeze their batch and resume the course later."
    },
    "seat_availability": {
        "keywords": ["seat", "seats", "seats left", "availability"],
        "answer": "To ensure individual attention, we keep batch sizes limited (maximum 10-12 students per batch). Contact us on +91-9662512857 to verify seat availability."
    },

    # ==================================================================
    # 5. PYTHON COURSE DETAILS
    # ==================================================================
    "python_fees": {
        "keywords": [["python", "fee"], ["python", "fees"], ["python", "cost"]],
        "answer": "The fee for the Python Full Stack development course is Rs. 15,000 (inclusive of project guidance). Paid in installments of Rs. 3,750 per month."
    },
    "python_duration": {
        "keywords": [["python", "duration"], ["python", "months"], ["python", "long"]],
        "answer": "The Python Full Stack course takes 4 months, featuring 2 hours of daily sessions (1 hour lecture + 1 hour lab practice)."
    },
    "python_syllabus": {
        "keywords": [["python", "syllabus"], ["python", "subjects"], ["python", "learn"]],
        "answer": "Python Syllabus: Core Python concepts, OOPs, File handling, SQL (SQLite/MySQL), HTML5, CSS3, JavaScript, Flask framework, Django framework, and API integration."
    },
    "python_eligibility": {
        "keywords": [["python", "eligibility"], ["python", "qualification"], ["python", "eligible"]],
        "answer": "BCA, MCA, B.Tech, Diploma, BSC-IT, and non-IT students who wish to build a career in software development are eligible to join."
    },
    "python_projects": {
        "keywords": [["python", "project"], ["python", "projects"]],
        "answer": "Python Projects: (1) E-Commerce Web Portal, (2) Student Admission Management System, (3) Offline AI/NLP Chatbot application."
    },
    "python_overview": {
        "keywords": ["python"],
        "answer": "Our Python Full Stack course covers complete frontend and backend development using Python, a popular high-level programming language, along with Django and Flask frameworks."
    },

    # ==================================================================
    # 6. MERN STACK COURSE DETAILS
    # ==================================================================
    "mern_fees": {
        "keywords": [["mern", "fee"], ["mern", "fees"], ["react", "fee"], ["react", "fees"]],
        "answer": "MERN Stack Web Developer course fee is Rs. 18,000. It can be paid in 4 monthly installments of Rs. 4,500."
    },
    "mern_duration": {
        "keywords": [["mern", "duration"], ["mern", "months"], ["react", "duration"]],
        "answer": "MERN Stack takes 5 months of daily training, combining intensive frontend and backend modules."
    },
    "mern_syllabus": {
        "keywords": [["mern", "syllabus"], ["mern", "subjects"], ["react", "syllabus"]],
        "answer": "MERN Syllabus: Advanced JavaScript (ES6+), React.js frontend library, Node.js runtime, Express.js server, and MongoDB database management."
    },
    "mern_overview": {
        "keywords": ["mern", "react"],
        "answer": "MERN Stack is a premier full-stack JavaScript web course that covers MongoDB, Express, React, and Node.js to make you a job-ready web engineer."
    },

    # ==================================================================
    # 7. JAVA COURSE DETAILS
    # ==================================================================
    "java_fees": {
        "keywords": [["java", "fee"], ["java", "fees"]],
        "answer": "The Core & Advanced Java programming course fee is Rs. 12,000."
    },
    "java_duration": {
        "keywords": [["java", "duration"], ["java", "months"]],
        "answer": "The Java training program takes 3 months."
    },
    "java_overview": {
        "keywords": ["java"],
        "answer": "Java course covers Object-Oriented Programming (OOPs), Multithreading, Exception Handling, Collections, JDBC database connectivity, and Desktop Swing GUI development."
    },

    # ==================================================================
    # 8. C / C++ COURSE DETAILS
    # ==================================================================
    "cpp_fees": {
        "keywords": [["cpp", "fee"], ["cpp", "fees"], ["c++", "fee"], ["c++", "fees"]],
        "answer": "The combined C & C++ programming foundations course fee is Rs. 6,000."
    },
    "cpp_duration": {
        "keywords": [["cpp", "duration"], ["c++", "duration"], ["cpp", "months"], ["c++", "months"]],
        "answer": "C & C++ training takes 2 to 3 months to complete, focusing on logical concepts."
    },
    "cpp_overview": {
        "keywords": ["cpp", "c++", "programming language"],
        "answer": "Our C & C++ course covers variables, loops, conditional statements, arrays, functions, pointers, structure, union, classes, objects, inheritance, and file operations. Best foundations for BCA freshers."
    },

    # ==================================================================
    # 9. PHP & LARAVEL COURSE DETAILS
    # ==================================================================
    "php_fees": {
        "keywords": [["php", "fee"], ["php", "fees"], ["laravel", "fee"], ["laravel", "fees"]],
        "answer": "The PHP Full Stack with Laravel course fee is Rs. 14,000."
    },
    "php_duration": {
        "keywords": [["php", "duration"], ["laravel", "duration"]],
        "answer": "The course takes 4 months, covering basic web design, core PHP, MySQL, and Laravel framework."
    },
    "php_overview": {
        "keywords": ["php", "laravel"],
        "answer": "Covers frontend HTML/CSS/Bootstrap, core PHP, object-oriented PHP, MySQL databases, and MVC web development using the Laravel framework."
    },

    # ==================================================================
    # 10. FLUTTER & ANDROID APP COURSES
    # ==================================================================
    "flutter_fees": {
        "keywords": [["flutter", "fee"], ["flutter", "fees"]],
        "answer": "The Flutter cross-platform mobile app course fee is Rs. 16,000."
    },
    "flutter_duration": {
        "keywords": [["flutter", "duration"], ["flutter", "months"]],
        "answer": "Flutter app development training takes 4 months."
    },
    "flutter_overview": {
        "keywords": ["flutter", "dart"],
        "answer": "Flutter covers Dart programming, widgets, layout designs, local databases (SQFlite), state management, Firebase integration, and compiling Android/iOS applications."
    },
    "android_fees": {
        "keywords": [["android", "fee"], ["android", "fees"]],
        "answer": "The Native Android App course fee is Rs. 15,000."
    },
    "android_duration": {
        "keywords": [["android", "duration"], ["android", "months"]],
        "answer": "The native Android app course duration is 4 months."
    },
    "android_overview": {
        "keywords": ["android", "kotlin", "app"],
        "answer": "Native Android covers Java/Kotlin concepts, Android Studio components, Activity Lifecycles, UI widgets, SQLite, Retrofit APIs, and releasing apps to Play Store."
    },

    # ==================================================================
    # 11. AI / ML & DATA SCIENCE COURSES
    # ==================================================================
    "ai_fees": {
        "keywords": [["ai", "fee"], ["ml", "fee"], ["data", "fee"], ["science", "fee"]],
        "answer": "The AI/ML and Data Science course fee is Rs. 20,000."
    },
    "ai_duration": {
        "keywords": [["ai", "duration"], ["data", "duration"]],
        "answer": "Data Science & AI/ML training is a 6 months comprehensive program."
    },
    "ai_overview": {
        "keywords": ["ai", "ml", "data science", "machine learning"],
        "answer": "Covers python libraries (NumPy, Pandas, Matplotlib, Scikit-learn), Data Cleaning, supervised learning algorithms (Regression, Decision Trees, SVM, KNN), and basic Neural Networks."
    },

    # ==================================================================
    # 12. CYBER SECURITY & HACKING
    # ==================================================================
    "cyber_fees": {
        "keywords": [["cyber", "fee"], ["cyber", "fees"], ["security", "fee"], ["security", "fees"]],
        "answer": "The Cyber Security and Ethical Hacking course fee is Rs. 16,000."
    },
    "cyber_duration": {
        "keywords": [["cyber", "duration"], ["security", "duration"]],
        "answer": "Cyber Security course takes 4 months."
    },
    "cyber_overview": {
        "keywords": ["cyber", "security", "hacking", "ethical"],
        "answer": "Covers Networking basics, Linux server configuration, Ethical Hacking techniques, Metasploit, Cryptography, SQL Injection, WiFi security, and Cyber forensics."
    },

    # ==================================================================
    # 13. UI / UX DESIGN
    # ==================================================================
    "uiux_fees": {
        "keywords": [["uiux", "fee"], ["uiux", "fees"], ["design", "fee"], ["design", "fees"]],
        "answer": "The UI/UX design course fee is Rs. 12,000."
    },
    "uiux_duration": {
        "keywords": [["uiux", "duration"], ["design", "duration"]],
        "answer": "UI/UX design course duration is 3 months."
    },
    "uiux_overview": {
        "keywords": ["uiux", "ui", "ux", "figma"],
        "answer": "UI/UX design covers Wireframing, User Research, Prototyping, Mobile App Layout designs, Desktop UI dashboards, and Figma tool practice."
    },

    # ==================================================================
    # 14. DIGITAL MARKETING, EXCEL, SQL, POWER BI
    # ==================================================================
    "digital_marketing_fees": {
        "keywords": [["digital", "marketing", "fee"], ["digital", "marketing", "fees"]],
        "answer": "Digital Marketing training course fee is Rs. 10,000."
    },
    "digital_marketing_overview": {
        "keywords": ["digital marketing", "seo", "social media"],
        "answer": "Covers Search Engine Optimization (SEO), Social Media Marketing (Facebook, Instagram, LinkedIn ads), Google Ads, Email Marketing, and Google Analytics."
    },
    "datascience_overview": {
        "keywords": ["data analytics", "excel", "sql", "power bi"],
        "answer": "Covers Advanced Excel (VLookup, Pivot Tables, Macros), SQL database queries, data cleaning, and building interactive business intelligence reports in Power BI."
    },
    "datascience_fees": {
        "keywords": [["data", "analytics", "fee"], ["excel", "fee"], ["sql", "fee"], ["power", "bi", "fee"]],
        "answer": "The Data Analytics course (Excel + SQL + Power BI) fee is Rs. 12,000 for 3 months."
    },

    # ==================================================================
    # 15. TALLY & CCC
    # ==================================================================
    "tally_fees": {
        "keywords": [["tally", "fee"], ["tally", "fees"]],
        "answer": "Tally Prime ERP with GST course fee is Rs. 5,000."
    },
    "tally_overview": {
        "keywords": ["tally", "accounting", "gst"],
        "answer": "Covers basic financial accounting, journal vouchers, ledgers, inventory management, tax computations (GST, TDS), and invoice printings."
    },
    "ccc_fees": {
        "keywords": [["ccc", "fee"], ["ccc", "fees"]],
        "answer": "CCC (Course on Computer Concepts) fee is Rs. 3,500."
    },
    "ccc_overview": {
        "keywords": ["ccc", "computer concept"],
        "answer": "CCC covers MS Word, MS Excel, MS PowerPoint, basic computer networks, emailing, and Windows OS configuration. Recommended for government exam requirements."
    },

    # ==================================================================
    # 16. PLACEMENT & RESUME SUPPORT
    # ==================================================================
    "placement_support": {
        "keywords": ["placement", "placements", "job", "jobs", "career", "hire", "interview"],
        "answer": "We offer 100% placement support. Our trainers prepare you with mock interviews, resume writing guidance, and schedule direct interviews with local and regional IT companies."
    },
    "resume_support": {
        "keywords": ["resume", "cv", "resume support", "cv building"],
        "answer": "Yes, we help students build a professional, project-based resume. We highlight your live training projects and key programming languages to stand out to HR recruiters."
    },
    "mock_interview": {
        "keywords": ["mock", "interview practice", "preps", "interview questions"],
        "answer": "We hold weekly mock interviews (technical round + HR round) to boost students' confidence and prepare them for standard coding interview challenges."
    },
    "placement_companies": {
        "keywords": ["companies", "recruiters", "hiring partners", "employer"],
        "answer": "Our placed students work at prominent local and state-wide IT companies in Bhavnagar and Ahmedabad, including software houses and digital agencies."
    },
    "success_stories": {
        "keywords": ["success", "placed students", "placed list", "placed"],
        "answer": "Many of our former BCA and engineering students have successfully secured positions as junior Python developers, React engineers, and graphic designers."
    },

    # ==================================================================
    # 17. STUDENT SUPPORT & SERVICES
    # ==================================================================
    "doubt_solving": {
        "keywords": ["doubt", "doubts", "solving", "extra class", "help"],
        "answer": "We have dedicated doubt-solving time daily. If you face any issues while debugging your code, our trainers sit with you individually to explain the solutions."
    },
    "notes_material": {
        "keywords": ["notes", "material", "study", "books", "pdf"],
        "answer": "Yes, we provide printed study materials, custom laboratory manual PDFs, list of viva questions, and practice codes for all subjects."
    },
    "recorded_lectures": {
        "keywords": ["recorded", "videos", "lectures", "absent", "missed"],
        "answer": "If you miss a class, you can access our reference recorded code sessions or schedule an extra class session with the trainer."
    },
    "lab_facility": {
        "keywords": ["lab", "labs", "pc", "computer", "practice", "wifi"],
        "answer": "Our lab is fully air-conditioned and equipped with individual high-speed desktop PCs and free WiFi. Students can sit and practice extra hours daily."
    },

    # ==================================================================
    # 18. INFRASTRUCTURE & SAFETY
    # ==================================================================
    "infrastructure": {
        "keywords": ["infrastructure", "classrooms", "ac", "parking", "smart class"],
        "answer": "We provide air-conditioned classrooms, a modern individual computer lab, high-speed internet, smart presentation screens, and clean drinking water."
    },
    "safety_environment": {
        "keywords": ["safety", "security", "cctv", "environment", "safe"],
        "answer": "Our premises are secured with 24/7 CCTV surveillance, a safe campus environment, and separate parking spaces for students' two-wheelers."
    },

    # ==================================================================
    # 19. ACADEMY POLICIES
    # ==================================================================
    "attendance_policy": {
        "keywords": ["attendance", "leaves", "regular", "presence"],
        "answer": "We recommend maintaining at least 80% attendance so you do not miss any sequential coding logic, which is crucial for building logic."
    },
    "leave_policy": {
        "keywords": ["leave", "absent", "inform", "holiday request"],
        "answer": "If you need leave, please inform your batch trainer beforehand via phone or WhatsApp so we can adjust the coding schedule accordingly."
    },
    "certificate_rules": {
        "keywords": ["certificate rules", "get certificate", "project submit"],
        "answer": "To get your ISO training certificate, students must maintain 80% attendance and submit their final practical projects for trainer evaluation."
    },
    "batch_change": {
        "keywords": ["batch change", "transfer batch", "time change"],
        "answer": "Yes, students can request a batch change if they have college lecture conflicts. Change requests depend on slot availability in the desired hour."
    },

    # ==================================================================
    # 20. GENERAL/FALLBACK TOPICS
    # ==================================================================
    "courses": {
        "keywords": ["courses", "course", "subjects", "learn", "study", "list", "teach", "classes"],
        "answer": "We offer Python Full Stack, MERN Stack, Java, PHP, Android Web/App development, AI/ML, Cyber Security, UI/UX, and Tally."
    },
    "about": {
        "keywords": ["about", "easylearn", "academy", "institute"],
        "answer": "EasyLearn Academy is a leading computer training institute in Bhavnagar, Gujarat, offering 100% practical, project-based education."
    }
}
