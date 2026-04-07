import sqlite3

def get_db_connection():
    conn = sqlite3.connect('dados.db', timeout=10)
    conn.execute('PRAGMA journal_mode=WAL')
    conn.execute('PRAGMA busy_timeout=5000')
    conn.row_factory = sqlite3.Row
    return conn
''
def init_db():
    with open('schema.sql') as f:
        conn = get_db_connection()
        conn.executescript(f.read())
        conn.close()

def inserir_leitura(temp, umid, pressao=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO leituras (temperatura, umidade, pressao) VALUES (?, ?, ?)",
        (temp, umid, pressao)
    )
    conn.commit()
    id_novo = cursor.lastrowid
    conn.close()
    return id_novo

def listar_leituras(limite=50):
    conn = get_db_connection()
    dados = conn.execute(
        "SELECT * FROM leituras ORDER BY timestamp DESC LIMIT ?",
        (limite,)
    ).fetchall()
    conn.close()
    return dados