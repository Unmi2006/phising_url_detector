🔐 Phishing URL Detector
📌 Project Overview

Phishing URL Detector is a Machine Learning-based web security project that identifies whether a given URL is Safe or Phishing (Malicious).

The system extracts important features from URLs and uses trained ML models to classify them.

🚀 Features

Detects phishing URLs

Extracts URL-based features automatically

Uses Machine Learning models

Beginner-friendly Python implementation

Can be extended to real-time web applications

🧠 Machine Learning Models Used

Logistic Regression

Random Forest

Decision Tree

Support Vector Machine (Optional)

📊 Features Extracted from URL

Examples:

Length of URL

Number of dots (.)

Presence of @ symbol

Presence of IP address

Use of HTTPS

Suspicious keywords (login, verify, update, etc.)

🛠️ Technologies Used

Python

NumPy

Pandas

Scikit-learn

Regex (re module)

📂 Project Structure
phishing_url_detector/
│
├── dataset.csv
├── feature_extraction.py
├── train_model.py
├── predict.py
├── model.pkl
└── README.md
⚙️ Installation
git clone https://github.com/yourusername/phishing_url_detector.git
cd phishing_url_detector
pip install -r requirements.txt
▶️ How to Run
1️⃣ Train the Model
python train_model.py
2️⃣ Predict URL
python predict.py

Example:

Enter URL: http://verify-paypal-login.com

Output: ⚠️ Phishing URL
📈 Example Feature Extraction Code
def extract_features(url):
    features = []

    # Length of URL
    features.append(len(url))

    # Has @ symbol
    features.append(1 if "@" in url else 0)

    # Number of dots
    features.append(url.count("."))

    return features
🔒 Example Unsafe URLs

http://secure-login-paypal.com

http://192.168.0.1/login

http://bankofindia.verify-account.ru

🎯 Future Improvements

Deep Learning model (LSTM for URL sequence)

Real-time browser extension

Deployment using Flask

Integration with cybersecurity APIs

👨‍💻 Author

Unmilan Das

⭐ If You Like This Project

Give it a star on GitHub ⭐
