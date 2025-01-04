import io
import pandas as pd
import duckdb

conn = duckdb.connect(database="data/questions.duckdb", read_only=False)

# ------------------------------------------------------------
# QUESTIONS LIST
# ------------------------------------------------------------
questions_dict = {
    "theme": ["SQL"],
    "question_name": ["sql1"],
    "last_reviewed": ["1970-01-01"],
}
questions_df = pd.DataFrame(questions_dict)
conn.execute("CREATE TABLE IF NOT EXISTS questions_df AS SELECT * FROM questions_df")

# ------------------------------------------------------------
# QUESTIONS AND ANSWERS
# ------------------------------------------------------------
questions_answers =  {
    "question_name": ["sql1"],
    "question_title": ["En SQL, quel mot-clé permet d'obtenir de la donnée ?"],
    "answer1": ["SELECT"],
    "answer2": ["GET"],
    "answer3": ["RETRIEVE"],
    "answer4": ["OBTAIN"]
}
questions_answers = pd.DataFrame(questions_answers)
conn.execute("CREATE TABLE IF NOT EXISTS questions_answers AS SELECT * FROM questions_answers")

conn.close()
