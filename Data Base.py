from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

engine = create_engine('sqlite:///UNI Scores.db', echo=True)

meta = MetaData()
my_scores = Table('Elmer', meta, Column('id', Integer, primary_key=True),
                  Column('name', String), Column("lastname", String), Column("Class", String), Column("Score", Float))

meta.create_all(engine)

ins = my_scores.insert().values()

conn = engine.connect()
conn.execute(my_scores.delete())
conn.execute(my_scores.insert(),  [
    {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Matematica I', 'Score': 89.00},
    {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'English I', 'Score': 92.00},
    {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Redaccion Tecnica', 'Score': 95.00},
    {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Introduccion a la Programacion', 'Score': 93.00},
    {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Contabilidad Financiera', 'Score': 95.00},
    {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Filosofia', 'Score': 94.00},
    {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Programacion I', 'Score': 97.00},
    {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'English II', 'Score': 100.00},
    {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Contabilidad de costos', 'Score': 85.00}
])

result = conn.execute(ins)
conn.commit()
conn.close()


def get_score_color(score):
    if score is None:
        return 'gray'
    elif score >= 90:
        return 'green'
    elif 80 <= score < 90:
        return 'yellow'
    else:
        return 'red'


# Retrieve scores from the database
conn = engine.connect()
scores = conn.execute(my_scores.select()).fetchall()
conn.close()

# Display scores with color-coding
for score in scores:
    name, lastname, course, score_value = score[1], score[2], score[3], score[4]
    color = get_score_color(score_value)
    print(f'{name} {lastname} - {course}: {score_value} ({color} color)')
