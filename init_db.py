import pandas as pd
import duckdb

conn = duckdb.connect(database="data/questions.duckdb", read_only=False)

# ------------------------------------------------------------
# QUESTIONS LIST
# ------------------------------------------------------------
questions_dict = {
    "theme": ["SQL", "SQL"],
    "question_name": ["sql1", "sql2"],
    "last_reviewed": ["1970-01-01", "1970-01-01"],
}
questions_df = pd.DataFrame(questions_dict)
conn.execute("CREATE TABLE IF NOT EXISTS questions_df AS SELECT * FROM questions_df")

# ------------------------------------------------------------
# QUESTIONS AND ANSWERS
# ------------------------------------------------------------
questions_answers =  {
    "question_name": ["sql1", "sql2"],
    "question_title": ["En SQL, quel mot-clé permet d'obtenir de la donnée ?",
                       "Quelle requête SQL est correcte ?"],
    "answer1": ["SELECT", "SELECT * FROM character WHERE name = 'Shrek'"],
    "answer2": ["GET", "SELECT id OR name FROM character"],
    "answer3": ["RETRIEVE", "DELETE TABLE WHERE character=id"],
    "answer4": ["OBTAIN", "CREATE TABLE WITH id=4 AND character='Shrek'"]
}
questions_answers = pd.DataFrame(questions_answers)
conn.execute("CREATE TABLE IF NOT EXISTS questions_answers AS SELECT * FROM questions_answers")

conn.close()
