import psycopg2

# Function to create a user


def create(name, passwd):
    conn = None
    try:
        query = ""
        # Connection to the database
        conn = psycopg2.connect(
            user="",
            password="",
            host="",
            database="",
            port=""
        )

        # Instance the object allows to interact with database (queries)
        cur = conn.cursor()

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
        query = ""
        # Connection to the database
        conn = psycopg2.connect(
            user="",
            password="",
            host="",
            database="",
            port=""
        )

        # Instance the object allows to interact with database (queries)
        cur = conn.cursor()
        return True
    except (Exception, psycopg2.DatabaseError) as error:
        print("ERROR: ", error)
        return False
    finally:
        cur.close()
        conn.close()
