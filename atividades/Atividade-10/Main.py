import mysql.connector

# Função para calcular status de aprovação
def calcular_status(n1, n2, faltas):
    media = (n1 + n2) / 2
    if faltas > 10:
        return "Reprovado por Faltas"
    elif media >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado por Nota"

# Conectar ao servidor MySQL
conexao = mysql.connector.connect(
    host="localhost",
    user="root",  # Substituir pelo seu usuário MySQL
    password="password"  # Substituir pela sua senha MySQL
)

cursor = conexao.cursor()

# Criar o banco de dados 'db_escola' se ele não existir
cursor.execute("CREATE DATABASE IF NOT EXISTS db_escola;")

# Usar o banco de dados 'db_escola'
cursor.execute("USE db_escola;")

# Criar as tabelas
cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_ALUNO (
        id_aluno INT PRIMARY KEY AUTO_INCREMENT,
        nome_aluno VARCHAR(100) NOT NULL,
        data_nascimento DATE NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_PROFESSOR (
        id_professor INT PRIMARY KEY AUTO_INCREMENT,
        nome_professor VARCHAR(100) NOT NULL,
        especialidade VARCHAR(100)
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_DISCIPLINA (
        id_disciplina INT PRIMARY KEY AUTO_INCREMENT,
        nome_disciplina VARCHAR(100) NOT NULL,
        carga_horaria INT NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS TB_MATRICULA (
        id_matricula INT PRIMARY KEY AUTO_INCREMENT,
        id_aluno INT,
        id_professor INT,
        id_disciplina INT,
        nota_n1 DECIMAL(5, 2),
        nota_n2 DECIMAL(5, 2),
        faltas INT,
        FOREIGN KEY (id_aluno) REFERENCES TB_ALUNO(id_aluno),
        FOREIGN KEY (id_professor) REFERENCES TB_PROFESSOR(id_professor),
        FOREIGN KEY (id_disciplina) REFERENCES TB_DISCIPLINA(id_disciplina)
    );
""")

# Alimentar as tabelas com dados de exemplo
cursor.execute("""
    INSERT INTO TB_ALUNO (nome_aluno, data_nascimento) 
    VALUES ('João Silva', '2000-05-10'),
           ('Maria Oliveira', '1998-12-15'),
           ('Carlos Souza', '1999-07-20')
    ON DUPLICATE KEY UPDATE nome_aluno=VALUES(nome_aluno);
""")

cursor.execute("""
    INSERT INTO TB_PROFESSOR (nome_professor, especialidade) 
    VALUES ('Prof. Ana', 'Matemática'),
           ('Prof. José', 'História'),
           ('Prof. Carla', 'Física')
    ON DUPLICATE KEY UPDATE nome_professor=VALUES(nome_professor);
""")

cursor.execute("""
    INSERT INTO TB_DISCIPLINA (nome_disciplina, carga_horaria) 
    VALUES ('Matemática', 60),
           ('História', 40),
           ('Física', 50)
    ON DUPLICATE KEY UPDATE nome_disciplina=VALUES(nome_disciplina);
""")

cursor.execute("""
    INSERT INTO TB_MATRICULA (id_aluno, id_professor, id_disciplina, nota_n1, nota_n2, faltas) 
    VALUES (1, 1, 1, 7.5, 8.0, 2),
           (2, 2, 2, 6.0, 5.5, 3),
           (3, 3, 3, 5.0, 6.0, 12)
    ON DUPLICATE KEY UPDATE nota_n1=VALUES(nota_n1), nota_n2=VALUES(nota_n2), faltas=VALUES(faltas);
""")

conexao.commit()

# Consulta à tabela de matrículas
cursor.execute("""
    SELECT A.nome_aluno, M.nota_n1, M.nota_n2, M.faltas
    FROM TB_MATRICULA M
    JOIN TB_ALUNO A ON M.id_aluno = A.id_aluno;
""")
matriculas = cursor.fetchall()

# Exibindo o status dos alunos
for matricula in matriculas:
    nome_aluno, nota_n1, nota_n2, faltas = matricula
    status = calcular_status(nota_n1, nota_n2, faltas)
    print(f"Aluno: {nome_aluno}, Status: {status}")

# Fechando a conexão
cursor.close()
conexao.close()

print("Banco de dados e tabelas criadas com sucesso, dados inseridos e status dos alunos exibido.")