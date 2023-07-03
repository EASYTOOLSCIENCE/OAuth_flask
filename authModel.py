import psycopg2

# Function to create a user


def create(name, passwd):
    conn = None
    try:
        query = "insert into users(\"name\",\"password\") values(%s,%s)"
        # Connection to the database
        conn = psycopg2.connect(
            user="easytool",
            password="bakeli2023",
            host="localhost",
            database="users_db",
            port="5432"
        )

        # Instance the object allows to interact with database (queries)
        cur = conn.cursor()
        cur.execute(query, (name, passwd))
        conn.commit()

        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print("ERROR: ", error)
        return False
    finally:
        cur.close()
        conn.close()


def login(name, passwd):
    conn = None

    try:
        query = "select * from users where \"name\"=%s and \"password\"=%s"
        # Connection to the database
        conn = psycopg2.connect(
            user="easytool",
            password="bakeli2023",
            host="localhost",
            database="users_db",
            port="5432"
        )

        # Instance the object allows to interact with database (queries)
        cur = conn.cursor()
        cur.execute(query, (name, passwd))

        user = cur.fetchone()
        return user
    except (Exception, psycopg2.DatabaseError) as error:
        print("ERROR: ", error)
        return False
    finally:
        cur.close()
        conn.close()
