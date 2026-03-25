# 📰 Fake News Detection (AI/ML Project)

**Author:** Subhranshu

A Machine Learning project that detects whether a news article is **Fake** or **Real** using Natural Language Processing (NLP) and classification algorithms.

---

## 🚀 Overview

This project uses:

* Text preprocessing (NLP)
* TF-IDF Vectorization
* Logistic Regression model
* Streamlit web app for real-time prediction

The system takes a news article or headline as input and predicts whether it is **Fake 🚨** or **Real ✅**.

---

## 📂 Project Structure

```
fake-news-detector/
│── data/
│   ├── Fake.csv
│   ├── True.csv
│   └── news.csv
│── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│── train.py
│── app.py
│── text_utils.py
│── prepare_data.py
│── requirements.txt
│── README.md
```

---

## 📊 Dataset

This project uses the **Fake and Real News Dataset (Kaggle)**.

* Fake news → Label = 1
* Real news → Label = 0

The dataset is preprocessed into a single file:

```
data/news.csv
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/fake-news-detector.git
cd fake-news-detector
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Train the Model

```bash
python train.py
```

This will:

* Clean text data
* Convert text → TF-IDF vectors
* Train Logistic Regression model
* Save model in `/model`

---

## 🌐 Run Web App

```bash
streamlit run app.py
```

Then open in browser:

```
http://localhost:8501
```

---

## 🧪 Example

Input:

```
"Breaking: Government announces new policy"
```

Output:

```
✅ Real News
```

---

## 📈 Features

* NLP text preprocessing
* TF-IDF feature extraction
* Logistic Regression classifier
* Real-time prediction using Streamlit
* Clean and simple UI

---

## 🔥 Future Improvements

* Use **BERT (Transformers)** for higher accuracy
* Add **confidence score**
* Detect fake news from **URLs**
* Multi-language support (Hindi + English)
* Deploy on cloud (Hugging Face / Render)

---

## 🧠 Learning Outcomes

* Natural Language Processing (NLP)
* Machine Learning classification
* Model evaluation
* Web app deployment

---

## 📌 Tech Stack

* Python
* Scikit-learn
* NLTK
* Streamlit

---

## 🙌 Acknowledgment

Dataset inspired by research work:
"Liar, Liar Pants on Fire: A New Benchmark Dataset for Fake News Detection" 

---

## ⭐ Support

If you like this project:

* ⭐ Star the repo
* 🍴 Fork it
* 📢 Share it

---

## 📬 Contact

Created by **Subhranshu**
Feel free to connect and collaborate 🚀
