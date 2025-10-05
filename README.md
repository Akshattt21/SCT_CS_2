# 🔐 Image Encryption and Decryption Project

This project demonstrates a simple yet effective way to perform **image encryption and decryption** using Python.

---

## 📁 Files Included

- `encrypt.py` → Script to encrypt an image  
- `decrypt.py` → Script to decrypt an encrypted image  
- `input.png` → Original input image  
- `encrypted.png` → Encrypted output image  
- `decrypted.png` → Decrypted image after running decryption script  

---

## ⚙️ How It Works

1. The `encrypt.py` script takes an image (`input.png`) and applies a simple **XOR-based encryption algorithm** to produce `encrypted.png`.  
2. The `decrypt.py` script reverses the process, restoring the original image as `decrypted.png`.  

This approach demonstrates how image data can be transformed securely using pixel-level operations.

---

## 🧠 Concept

The idea behind this project is to understand basic **cryptography** concepts using images.  
By manipulating pixel values, we can safely encrypt image data and recover it through the reverse process.

---

## 🏁 Conclusion

This project provides an easy introduction to **cybersecurity** and **cryptography** fundamentals.  
It helps visualize how encryption and decryption algorithms work at a basic level using Python.

---

## 🧩 How to Run

1. Place your image file as `input.png` in the same folder as the scripts.  
2. Run the encryption script:  
   ```bash
   python encrypt.py
