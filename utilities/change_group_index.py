def change_group_index(id, new_group_index):
    from sqlite3 import connect

    con = connect('./data/db.db')
    cur = con.cursor()

    cur.execute(f"UPDATE users SET group_index = ? WHERE id = ?", (new_group_index, id))

    con.commit()
    con.close()