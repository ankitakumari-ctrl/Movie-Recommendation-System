# 🎬 Movie Recommendation System

## 📌 Overview

The Movie Recommendation System is a content-based recommendation engine developed using Python. It suggests movies similar to a user's selected movie by analyzing movie metadata such as genres, keywords, cast, crew, and overview information.

The project utilizes Natural Language Processing (NLP) techniques and cosine similarity to identify and recommend the most relevant movies from the dataset.

---

## 🚀 Features

* Recommend movies based on user selection
* Content-based filtering approach
* Interactive web interface using Streamlit
* Displays movie posters using the TMDB API
* Fast recommendation generation using precomputed similarity scores
* User-friendly and responsive interface

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK
* Streamlit
* Pickle
* TMDB API

---

## 📂 Dataset

This project uses the following datasets:

* `tmdb_5000_movies.csv`
* `tmdb_5000_credits.csv`

These datasets contain movie information such as:

* Genres
* Cast
* Crew
* Keywords
* Movie descriptions

---

## ⚙️ Project Workflow

1. Load movie datasets.
2. Perform data cleaning and preprocessing.
3. Extract important features:

   * Genres
   * Keywords
   * Cast
   * Crew
   * Overview
4. Create tags by combining selected features.
5. Convert textual data into vectors using CountVectorizer.
6. Calculate cosine similarity between movies.
7. Recommend the top similar movies based on user selection.
8. Display recommendations through a Streamlit web application.

---

## 📁 Project Structure

movie-recommendation-system/

├── app.py

├── movie_recommendation_system.py

├── tmdb_5000_movies.csv

├── tmdb_5000_credits.csv

├── requirements.txt

├── README.md

└── screenshots/

---

## 🔧 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
cd Movie-Recommendation-System
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install streamlit pandas requests
```

---

## ▶️ Generate Required Pickle Files

The repository does not include the generated `.pkl` files because they are large and can be recreated from the dataset.

Run:

```bash
python movie_recommendation_system.py
```

This will generate:

* movie_dict.pkl
* movies.pkl
* similarity.pkl

These files are required before launching the application.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

---

## 💡 Future Enhancements

* Hybrid recommendation system
* Collaborative filtering
* User authentication
* Personalized recommendations
* Movie ratings and reviews
* Deployment on Streamlit Cloud or Render

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Data preprocessing and feature engineering
* Natural Language Processing (NLP)
* Machine Learning recommendation systems
* Similarity algorithms
* Streamlit web application development
* Git and GitHub project management

---

## 👩‍💻 Author

Ankita Kumari

Computer Science & Engineering Student

Passionate about Machine Learning, Data Science, and Software Development.
