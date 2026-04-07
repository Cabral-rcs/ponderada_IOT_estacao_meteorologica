from flask import Flask, request, jsonify, render_template, redirect
from database import (
    init_db,
    inserir_leitura,
    listar_leituras,
    get_db_connection
)

app = Flask(__name__)

# 🔹 HOME (Dashboard)
@app.route('/')
def index():
    dados = listar_leituras(10)
    dados = [dict(row) for row in dados]
    return render_template('index.html', leituras=dados)


# 🔹 HISTÓRICO
@app.route('/leituras')
def historico():
    dados = listar_leituras(50)
    dados = [dict(row) for row in dados]
    return render_template('historico.html', leituras=dados)


# 🔹 CRIAR LEITURA (POST)
@app.route('/leituras', methods=['POST'])
def criar():
    dados = request.get_json()

    if not dados:
        return jsonify({'erro': 'JSON inválido'}), 400

    id_novo = inserir_leitura(
        dados['temperatura'],
        dados['umidade'],
        dados.get('pressao')
    )

    return jsonify({'id': id_novo, 'status': 'criado'}), 201


# 🔹 BUSCAR POR ID
@app.route('/leituras/<int:id>')
def detalhe(id):
    conn = get_db_connection()
    leitura = conn.execute(
        "SELECT * FROM leituras WHERE id = ?",
        (id,)
    ).fetchone()
    conn.close()

    if not leitura:
        return "Leitura não encontrada", 404

    return render_template('editar.html', leitura=leitura)


# 🔹 ATUALIZAR (PUT)
@app.route('/leituras/<int:id>', methods=['PUT'])
def atualizar(id):
    dados = request.get_json()

    conn = get_db_connection()
    conn.execute(
        """
        UPDATE leituras
        SET temperatura = ?, umidade = ?
        WHERE id = ?
        """,
        (dados['temperatura'], dados['umidade'], id)
    )
    conn.commit()
    conn.close()

    return jsonify({'status': 'atualizado'})


# 🔹 DELETAR
@app.route('/leituras/<int:id>', methods=['DELETE'])
def deletar(id):
    conn = get_db_connection()
    conn.execute("DELETE FROM leituras WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return jsonify({'status': 'deletado'})


# 🔹 API JSON (listar)
@app.route('/api/leituras')
def api_leituras():
    dados = listar_leituras(50)
    return jsonify([dict(row) for row in dados])


# 🔹 ESTATÍSTICAS
@app.route('/api/estatisticas')
def estatisticas():
    conn = get_db_connection()

    stats = conn.execute("""
        SELECT 
            AVG(temperatura) as media_temp,
            MIN(temperatura) as min_temp,
            MAX(temperatura) as max_temp,
            AVG(umidade) as media_umid
        FROM leituras
    """).fetchone()

    conn.close()

    return jsonify(dict(stats))


# 🔹 START
if __name__ == '__main__':
    init_db()
    app.run(debug=True)