import streamlit as st
import pickle
import re
import numpy as np

# Load trained model
model = pickle.load(open("model (1).pkl", "rb"))

# Feature extraction function
def extract_features(url):
    features = []
    
    # URL Length
    features.append(len(url))
    
    # Has @ symbol
    features.append(1 if "@" in url else 0)
    
    # Number of dots
    features.append(url.count("."))
    
    # Contains IP address
    ip_pattern = r"\d+\.\d+\.\d+\.\d+"
    features.append(1 if re.search(ip_pattern, url) else 0)
    
    # Suspicious words
    suspicious_words = ["login", "verify", "update", "secure", "bank", "free", "bonus"]
    features.append(1 if any(word in url.lower() for word in suspicious_words) else 0)
    
    return np.array(features).reshape(1, -1)

# Streamlit UI
st.set_page_config(page_title="Phishing URL Detector", page_icon="🔐")

st.title("🔐 Phishing URL Detector")
st.write("Enter a URL below to check whether it is Safe or Phishing.")

url = st.text_input("Enter URL")

if st.button("Check URL"):
    
    if url == "":
        st.warning("Please enter a URL")
    else:
        features = extract_features(url)
        prediction = model.predict(features)
        
        if prediction[0] == 1:
            st.error("⚠️ Phishing Website Detected!")
        else:
            st.success("✅ This Website Looks Safe")