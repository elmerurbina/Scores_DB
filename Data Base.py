from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

# Create engine and metadata
engine = create_engine('sqlite:///UNI Scores.db', echo=True)
meta = MetaData()

# Define the table
my_scores = Table('Elmer', meta,
                  Column('id', Integer, primary_key=True),
                  Column('name', String),
                  Column("lastname", String),
                  Column("Class", String),
                  Column("Score", Float))

# Reflect the table from the database
meta.create_all(engine, checkfirst=True)

# Insert data into the table
with engine.connect() as conn:
    conn.execute(my_scores.delete())
    conn.execute(my_scores.insert(), [
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Matematica I', 'Score': 89.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'English I', 'Score': 92.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Redaccion Tecnica', 'Score': 95.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Introduccion a la Programacion', 'Score': 93.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Contabilidad Financiera', 'Score': 95.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Filosofia', 'Score': 94.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Programacion I', 'Score': 97.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'English II', 'Score': 100.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Contabilidad de costos', 'Score': 85.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Algebra Lineal', 'Score': 87.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Matematica II', 'Score': 64.00},
        {'name': 'Elmer', 'lastname': 'Urbina Meneses', 'Class': 'Sociologia', 'Score': 98}
    ])

# Retrieve scores from the database
with engine.connect() as conn:
    scores = conn.execute(my_scores.select()).fetchall()
