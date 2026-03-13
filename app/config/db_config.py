import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="db.rfvzywmfpysnjinykmdr.supabase.co",
        port="5432",
        user="postgres",
        password="post@Pry2026",
        dbname="postgres"
    )