Face Recognition Attendance System

An automated Face Recognition–based Attendance System built using OpenCV and the face_recognition library. The system detects and recognizes faces in real time through a webcam and logs attendance automatically into a CSV file.

This project is ideal for learning computer vision, real-time systems, and practical AI integration in Python.


---

✨ Features

Real-time face detection and recognition via webcam

Automatic attendance logging

Prevents duplicate attendance entries for the same person on the same day

Simple CSV-based storage (easy to extend to databases later)

Clean, beginner-friendly project structure



---

📁 Project Structure

Face-Recognition-Attendance-System/
│
├── Images/                 # Authorized face images (training data)
├── Attendance.csv          # Attendance log file
├── main.py                 # Main execution script
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation


---

🛠️ Installation & Setup

1️⃣ Prerequisites

Make sure you have the following installed:

Python 3.7 or higher

CMake

Visual Studio Build Tools (C++ Desktop Development)

Required for compiling the dlib dependency



> ⚠️ Windows users must install Visual Studio Build Tools before installing dependencies.




---

2️⃣ Install Dependencies

Clone the repository and install all required libraries:

pip install -r requirements.txt


---

3️⃣ Add Authorized Faces

1. Add clear, front-facing images of authorized people to the Images/ folder


2. Name each image using the person’s name



Example:

Images/
├── elon_musk.jpg
├── steve_jobs.png

> 📌 The filename is used as the identity name in the attendance CSV file.




---

📊 How It Works

🔍 Face Recognition Pipeline

The system operates in three main phases:

1. Encoding

Reads images from the Images/ folder

Converts each face into a 128-dimension facial encoding

Stores these encodings in memory


2. Detection & Comparison

Captures frames from the webcam

Detects faces in real time

Generates encodings for detected faces


3. Matching

Compares real-time encodings with stored encodings

Uses face distance to determine the closest match

Applies a confidence threshold to ensure accuracy



---

🧾 Attendance Logging Logic

When a face match is confirmed:

1. Read the existing Attendance.csv


2. Check if the person has already been marked present for the current date


3. Write a new record only if they are not already logged



Each attendance entry includes:

Name – Derived from image filename

Time – First recognition timestamp

Date – Current calendar date


> ✅ This ensures one entry per person per day, even if the face appears multiple times.




---

🚀 Usage

Start the face recognition system by running:

python main.py

The webcam will open automatically

Press q to stop the program and close the camera window



---

📦 Sample Attendance.csv Format

Name,Time,Date
Elon Musk,09:42:15,2026-01-29
Steve Jobs,09:45:02,2026-01-29


---

🔮 Future Enhancements

Replace CSV with MongoDB / PostgreSQL

Add GUI dashboard for attendance visualization

Export reports (PDF / Excel)

Multi-camera support

Face mask detection

Cloud-based deployment



---

🧠 Tech Stack

Python

OpenCV

face_recognition (dlib)

NumPy

CSV file handling



---

🤝 Contributing

Pull requests are welcome. Feel free to fork this repository and improve it.


---

📜 License

This project is open-source and available under the MIT License.


---

🔥 Built with curiosity, vision, and the grind mindset.
