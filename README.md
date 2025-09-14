# Spotify Data ETL Pipeline

## 📄 Description

This project is a complete Extract, Transform, and Load (ETL) pipeline built with Python. It extracts song data from a Kaggle CSV file, performs data cleaning and transformation using Pandas, and loads the processed data into a PostgreSQL database for analysis.

This project demonstrates core data engineering skills, including data processing with Pandas, database management with PostgreSQL, and secure credential handling using environment variables.

---

## 🛠️ Tech Stack

- **Language:** Python 3.13
- **Database:** PostgreSQL
- **Key Libraries:**
    - Pandas
    - SQLAlchemy
    - psycopg2-binary
    - python-dotenv

---

## ⚙️ Setup and Installation

To run this project locally, please follow these steps:

**1. Clone the Repository**
```bash
git clone [https://github.com/parthivkola/spotify-etl-pipeline.git](https://github.com/parthivkola/spotify-etl-pipeline.git)
cd spotify-etl-pipeline
```

**2. Manual Setup:**
```bash
conda create --name ml_project python=3.13
conda activate ml_project
pip install -r requirements.txt
```

**3. Set Up PostgreSQL Database**

  - Ensure you have a PostgreSQL server running.
  - Create a new database and a user with permissions to access it.

**4. Configure Environment Variables**

  - This project uses a `.env` file to manage database credentials.
  - Create your own `.env` file by copying the template:
    ```bash
    cp .env.example .env
    ```
  - Open the newly created `.env` file and fill in your actual database credentials.

-----

## ▶️ Usage

Once the setup is complete, you can run the entire ETL pipeline with a single command from your terminal:

```bash
python pipeline.py
```

The script will connect to the database, process the `dataset.csv` file, and load the cleaned data into the `popular_tracks` table. You can then connect to your PostgreSQL database to view and query the final table.

```
```