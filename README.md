# 🎯 Object Tracker using OpenCV

This project is a simple but powerful **object tracking system** using **Python** and **OpenCV**.  
You can track any colored object (like a purple ball, red cup, or blue pen) live through your webcam!

> Built fully in an **object-oriented** way for clean and scalable code.

---

## 📚 Features
- Real-time object detection and tracking
- Adjustable color range (track any color: purple, green, red, etc.)
- Object-oriented design for scalability
- Easy to extend with more features (like multiple color tracking)

---

## 🛠️ How It Works
- Captures live video frames from your webcam
- Converts frames from BGR to HSV color space
- Creates a mask using defined color boundaries
- Finds contours and tracks the largest one detected
- Draws a bounding circle and center point on the object

---

## 🖥️ Technologies Used
- Python 3
- OpenCV

---

## 🛠️ Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/object-tracker.git
   cd object-tracker
