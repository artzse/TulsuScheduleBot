def registration(id, username, first_name, group_index, grade_book):
    from sqlite3 import connect

    con = connect('./data/db.db')
    cur = con.cursor()

    cur.execute('INSERT OR REPLACE INTO users VALUES(?, ?, ?, ?, ?)', (id, username, first_name, group_index, grade_book))

    con.commit()
    con.close()