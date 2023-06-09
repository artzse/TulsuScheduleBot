def user_information(id):
    from sqlite3 import connect

    con = connect('./data/db.db')
    cur = con.cursor()

    data = cur.execute('SELECT group_index, grade_book FROM users WHERE id = (?)', (id, )).fetchone()
    con.close()

    if data == None:
        return 0

    return {'group_index':data[0], 'grade_book':data[1]}