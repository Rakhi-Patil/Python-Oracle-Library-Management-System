import oracledb

def get_connection():
    try:
        conne = oracledb.connect(
            user="sys",
            password="1234",
            host="localhost",
            port=1521,
            service_name="xe",
            mode=oracledb.AUTH_MODE_SYSDBA
        )

        print("Connected!")
        return conne

    except Exception as e:
        print("Connection Error:", e)
        return None
