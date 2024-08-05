import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 
import sqlite3
from typing import List, Optional


app = FastAPI()


class Aluno(BaseModel):
    aluno_nome: str
    endereco: str


def get_db_connection():
    conn = sqlite3.connect('dbalunos.db')
    return conn


@app.post("/criar_aluno/")
async def criar_aluno(aluno: Aluno):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO TB_ALUNO (aluno_nome, endereco) VALUES (?, ?)",
            (aluno.aluno_nome, aluno.endereco)
        )
        conn.commit()
        return {"message": "Aluno criado com sucesso!"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao criar aluno: {e}")
    finally:
        conn.close()


@app.get("/listar_alunos/", response_model=List[Aluno])
async def listar_alunos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT aluno_nome, endereco FROM TB_ALUNO")
        alunos = cursor.fetchall()
        return [{"aluno_nome": aluno[0], "endereco": aluno[1]} for aluno in alunos]
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar alunos: {e}")
    finally:
        conn.close()


@app.get("/listar_um_aluno/{aluno_id}", response_model=Aluno)
async def listar_um_aluno(aluno_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT aluno_nome, endereco FROM TB_ALUNO WHERE id = ?", (aluno_id,))
        aluno = cursor.fetchone()
        if aluno:
            return {"aluno_nome": aluno[0], "endereco": aluno[1]}
        else:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar aluno: {e}")
    finally:
        conn.close()

@app.put("/atualizar_aluno/{aluno_id}")
async def atualizar_aluno(aluno_id: int, aluno: Aluno):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE TB_ALUNO SET aluno_nome = ?, endereco = ? WHERE id = ?",
            (aluno.aluno_nome, aluno.endereco, aluno_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        return {"message": "Aluno atualizado com sucesso!"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao atualizar aluno: {e}")
    finally:
        conn.close()


@app.delete("/excluir_aluno/{aluno_id}")
async def excluir_aluno(aluno_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM TB_ALUNO WHERE id = ?", (aluno_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Aluno não encontrado")
        return {"message": "Aluno excluído com sucesso!"}
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Erro ao excluir aluno: {e}")
    finally:
        conn.close()
