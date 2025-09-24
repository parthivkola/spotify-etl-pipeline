
# 🎵 Spotify Data ETL Pipeline

## 📖 *Overview*
A simple **ETL pipeline** in Python:
- **Extract** → Read raw Kaggle CSV dataset  
- **Transform** → Clean, handle missing values, add new columns  
- **Load** → Save into PostgreSQL + local CSV  

This project demonstrates:
* Data cleaning with **pandas**  
* Secure credential handling with **dotenv**  
* Database integration with **SQLAlchemy + PostgreSQL**  

---

## 🛠 *Tech Stack*
* **Language** → Python 3.11+  
* **Database** → PostgreSQL  
* **Libraries** → pandas, SQLAlchemy, psycopg2-binary, python-dotenv  

---

## ⚙️ *Setup*

### 1. Clone Repo
```bash
git clone https://github.com/parthivkola/spotify-etl-pipeline.git
cd spotify-etl-pipeline
```

### 2. Create Virtual Environment
```bash
conda create --name spotify_etl python=3.11
conda activate spotify_etl
pip install -r requirements.txt
```

### 3. Configure PostgreSQL
* Create DB → `spotify_db`  
* Create user with permissions  

### 4. Configure Environment Variables
```bash
cp .env.example .env
```

Fill in:
```
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=spotify_db
```

---

## ▶️ *Run the Pipeline*
```bash
python main.py
```

Steps:
* Extract → from `dataset.csv`  
* Transform → clean + add `duration_min`  
* Load → into Postgres (`popular_tracks`)  

Query data:
```sql
SELECT * FROM popular_tracks LIMIT 10;
```

---

## 📊 *Example Output*

| track_name | artist_name | duration_min | popularity |
|------------|-------------|--------------|-------------|
| Song A     | Artist 1    | 3.5          | 85          |
| Song B     | Artist 2    | 4.1          | 90          |

---
