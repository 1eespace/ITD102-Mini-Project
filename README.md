# ITD102-Mini-Project

# Smart Home System with Raspberry Pi

## 📌 Project Overview

This project implements a **smart home system** using a **Raspberry Pi 3 A+**, integrating IoT sensors and a web-based interface. The system enables **real-time monitoring** of home environments via **CCTV streaming** and **temperature/humidity tracking**.

## 🛠️ Technologies Used

- **Programming:** Python (Flask), HTML, CSS, JavaScript
- **Database:** SQLite3
- **Computer Vision:** OpenCV for real-time image processing
- **IoT Service:** IFTTT for email notifications
- **Web Framework:** Flask for hosting the web application

## 🔧 Key Features

1. **CCTV Monitoring:** Uses a PIR sensor and a USB webcam to detect motion and send email notifications.
2. **Temperature & Humidity Tracking:** Uses a DHT sensor to record environmental data and display graphs.
3. **Real-Time Web Interface:** Developed with Flask, allowing users to access live video and sensor data remotely.
4. **Automated Email Alerts:** Sends notifications when motion is detected.

## 🔍 Challenges & Solutions

- **500 Internal Server Error:** Debugged server-side script errors.
- **TemplateNotFound Error:** Fixed incorrect file directory references.
- **Slow Performance:** Optimised file handling and execution speed.

## 🚀 Future Improvements

- Reduce email spam by limiting frequent notifications.
- Improve response time for PIR motion detection.
- Develop a **mobile-friendly UI** for easier access.
- Implement **real-time updating** temperature/humidity graphs.
