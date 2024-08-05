from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('dbalunos.db')

# Criando um cursor para interagir com o banco
cursor = conn.cursor()

# Criando a tabela TB_ALUNO
cursor.execute('''
CREATE TABLE IF NOT EXISTS TB_ALUNO (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_nome TEXT NOT NULL,
    endereco TEXT NOT NULL
)
''')

# Salvando as alterações e fechando a conexão
conn.commit()
conn.close()

# Criação da aplicação FastAPI
app = FastAPI()

# Modelo Pydantic para o Aluno
class Aluno(BaseModel):
    aluno_nome: str
    endereco: str

# Função para conectar ao banco de dados
def get_db_connection():
    conn = sqlite3.connect('dbalunos.db')
    return conn

# a) Criar Aluno
@app.post("/criar_aluno/")
async def criar_aluno(aluno: Aluno):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO TB_ALUNO (aluno_nome, endereco) VALUES (?, ?)",
        (aluno.aluno_nome, aluno.endereco)
    )
    conn.commit()
    conn.close()
    return {"message": "Aluno criado com sucesso!"}

# b) Listar Alunos
@app.get("/listar_alunos/")
async def listar_alunos():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TB_ALUNO")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

# c) Listar um Aluno
@app.get("/listar_um_aluno/{aluno_id}")
async def listar_um_aluno(aluno_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM TB_ALUNO WHERE id = ?", (aluno_id,))
    aluno = cursor.fetchone()
    conn.close()
    if aluno:
        return aluno
    else:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

# d) Atualizar Aluno
@app.put("/atualizar_aluno/{aluno_id}")
async def atualizar_aluno(aluno_id: int, aluno: Aluno):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE TB_ALUNO SET aluno_nome = ?, endereco = ? WHERE id = ?",
        (aluno.aluno_nome, aluno.endereco, aluno_id)
    )
    conn.commit()
    conn.close()
    return {"message": "Aluno atualizado com sucesso!"}

# e) Excluir Aluno
@app.delete("/excluir_aluno/{aluno_id}")
async def excluir_aluno(aluno_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM TB_ALUNO WHERE id = ?", (aluno_id,))
    conn.commit()
    conn.close()
    return {"message": "Aluno excluído com sucesso!"}
