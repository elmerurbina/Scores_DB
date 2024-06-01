from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
import tkinter as tk
from tkinter import ttk, messagebox

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

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a Session
session = Session()


# Define the function to insert data into the database
def insert_data():
    name = entry_name.get()
    lastname = entry_lastname.get()
    class_name = entry_class.get()
    try:
        score = float(entry_score.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Score must be a number")
        return

    new_record = {'name': name, 'lastname': lastname, 'Class': class_name, 'Score': score}

    # Insert data into the table
    with engine.connect() as conn:
        trans = conn.begin()
        try:
            conn.execute(my_scores.insert(), [new_record])
            trans.commit()
            messagebox.showinfo("Success", "Data inserted successfully")
        except Exception as e:
            trans.rollback()
            messagebox.showerror("Error", f"Failed to insert data: {e}")


# Define the function to delete data from the database
def delete_data():
    name = entry_name.get()
    lastname = entry_lastname.get()
    class_name = entry_class.get()

    with engine.connect() as conn:
        trans = conn.begin()
        try:
            delete_query = my_scores.delete().where(
                my_scores.c.name == name,
                my_scores.c.lastname == lastname,
                my_scores.c.Class == class_name
            )
            result = conn.execute(delete_query)
            trans.commit()
            if result.rowcount > 0:
                messagebox.showinfo("Success", "Data deleted successfully")
            else:
                messagebox.showinfo("No match", "No matching record found")
        except Exception as e:
            trans.rollback()
            messagebox.showerror("Error", f"Failed to delete data: {e}")


# Create the Tkinter interface
root = tk.Tk()
root.title("UNI Scores Management")

# Create a style
style = ttk.Style()
style.configure("TButton", font=('Helvetica', 12), padding=10)
style.configure("TLabel", font=('Helvetica', 12))
style.configure("TEntry", font=('Helvetica', 12))

# Labels and entries for each field
ttk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
entry_name = ttk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=5)

ttk.Label(root, text="Last Name").grid(row=1, column=0, padx=10, pady=5)
entry_lastname = ttk.Entry(root)
entry_lastname.grid(row=1, column=1, padx=10, pady=5)

ttk.Label(root, text="Class").grid(row=2, column=0, padx=10, pady=5)
entry_class = ttk.Entry(root)
entry_class.grid(row=2, column=1, padx=10, pady=5)

ttk.Label(root, text="Score").grid(row=3, column=0, padx=10, pady=5)
entry_score = ttk.Entry(root)
entry_score.grid(row=3, column=1, padx=10, pady=5)

# Insert button
insert_button = ttk.Button(root, text="Insert", command=insert_data)
insert_button.grid(row=4, column=0, padx=10, pady=20, columnspan=2)

# Delete button
delete_button = ttk.Button(root, text="Delete", command=delete_data)
delete_button.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

# Run the Tkinter event loop
root.mainloop()
