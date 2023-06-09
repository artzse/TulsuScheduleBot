def change_grade_book(id, new_grade_book):
    from sqlite3 import connect

    con = connect('./data/db.db')
    cur = con.cursor()

    cur.execute(f"UPDATE users SET grade_book = ? WHERE id = ?", (new_grade_book, id))

    con.commit()
    con.close()