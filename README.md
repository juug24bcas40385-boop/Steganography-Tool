# 🖼️ Steganography Tool

## 📌 Project Overview

The *Steganography Tool* is a Python-based application that hides and extracts secret text messages within PNG images using the *Least Significant Bit (LSB)* steganography technique. The hidden message does not noticeably change the appearance of the image, making it a simple and effective way to demonstrate secure communication.

---

## ✨ Features

- Hide secret messages inside PNG images
- Extract hidden messages from encoded images
- Simple menu-driven interface
- Supports RGB and RGBA images
- Easy to use and understand
- Built using Python and the Pillow library

---

## 🛠️ Technologies Used

- Python 3
- Pillow (PIL)

---

## 📁 Project Structure


Steganography-Tool/
│
├── steganography.py
├── README.md
├── requirements.txt
├── Images/
│   ├── IMG.png
│   └── encoded_image.png
├── Outputs/
└── Screenshots/


---

## ▶️ Installation

Install the required library:

bash
pip install pillow


---

## 🚀 How to Run

1. Open the project in Python IDLE.
2. Run steganography.py.
3. Choose:
   - *1* to encode a message.
   - *2* to decode a message.
4. Enter the image path and follow the on-screen instructions.

---

## 📸 Sample Output

*Encode*

Enter image path:
Enter secret message:
Message hidden successfully!
Encoded image saved as: encoded_image.png


*Decode*

Enter encoded image path:
Hidden Message:
Hello Varsha


---

## 🎯 Applications

- Secure communication
- Cybersecurity education
- Digital forensics
- Data hiding techniques
- Academic projects

---

## 🔮 Future Enhancements

- Graphical User Interface (GUI)
- Password-protected message encryption
- Support for multiple image formats
- Audio and video steganography
- Improved security algorithms

---

## 👩‍💻 Author

*Varsha KN*

BCA Student

---

## 📄 License

This project is created for educational and learning purposes
