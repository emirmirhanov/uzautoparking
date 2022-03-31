import psycopg2


def connect_db():
    base = psycopg2.connect(host='db', dbname='postgres', user='postgres', password='postgres')
    return base


def search_password(password):
	cur = connect_db().cursor()
	cur.execute(f'SELECT id FROM ugc_security WHERE password = \'{password}\'')
	result = cur.fetchone()
	cur.close()
	if result:
		return result[0]
	return None


def search_tg_user_id(id):
	cur = connect_db().cursor()
	cur.execute(f'SELECT name, lastname, blocked, block_comment FROM ugc_security WHERE tg_account_id = {id}')
	result = cur.fetchone()
	cur.close()
	return result


def add_user_id(security_tg_id, security_phone, security_id):
	con = connect_db()
	query = f"UPDATE ugc_security SET tg_account_id='{security_tg_id}',phone='{security_phone}' WHERE id='{security_id}'"
	con.cursor().execute(query)
	con.commit()
	con.close()


def search_employee(mess):
	cur = connect_db().cursor()
	cur.execute(f"""SELECT ugc_employees.name, ugc_employees.surname,
	 			ugc_cars.model, ugc_cars.num_car, ugc_cars.color
	 			FROM ugc_employees, ugc_cars WHERE ugc_employees.id = ugc_cars.driver_id
	 			AND (ugc_employees.name iLIKE '%{mess}%' OR ugc_cars.num_car
	 			iLIKE '%{mess}%' OR ugc_employees.surname iLIKE '%{mess}%')""")
	result = cur.fetchall()
	cur.close()
	return result


def plus():
	con = connect_db()
	cur = con.cursor()
	query = f'UPDATE ugc_parkingspaces SET busy_spaces = busy_spaces + 1 WHERE busy_spaces < all_spaces'
	cur.execute(query)
	con.commit()
	con.close()
	return cur.rowcount


def minus():
	con = connect_db()
	cur = con.cursor()
	query = f'UPDATE ugc_parkingspaces SET busy_spaces = busy_spaces - 1 WHERE busy_spaces > 0'
	cur.execute(query)
	con.commit()
	con.close()
	return cur.rowcount


def all_spaces():
	con = connect_db()
	cur = con.cursor()
	query = 'SELECT all_spaces, busy_spaces, all_spaces - busy_spaces FROM ugc_parkingspaces'
	cur.execute(query)
	result = cur.fetchone()
	return result
