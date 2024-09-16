-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql:3306
-- Tempo de geração: 16/09/2024 às 17:42
-- Versão do servidor: 8.0.39
-- Versão do PHP: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `Escola`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `TB_ALUNO`
--

CREATE TABLE `TB_ALUNO` (
  `aluno_id` int NOT NULL,
  `nome` varchar(100) NOT NULL,
  `data_nascimento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `TB_ALUNO`
--

INSERT INTO `TB_ALUNO` (`aluno_id`, `nome`, `data_nascimento`) VALUES
(1, 'João Silva', '2000-05-15'),
(2, 'Mario', '2008-06-15');

-- --------------------------------------------------------

--
-- Estrutura para tabela `TB_DISCIPLINA`
--

CREATE TABLE `TB_DISCIPLINA` (
  `disciplina_id` int NOT NULL,
  `nome` varchar(100) NOT NULL,
  `carga_horaria` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `TB_DISCIPLINA`
--

INSERT INTO `TB_DISCIPLINA` (`disciplina_id`, `nome`, `carga_horaria`) VALUES
(1, 'Matemática', 60);

-- --------------------------------------------------------

--
-- Estrutura para tabela `TB_MATRICULA`
--

CREATE TABLE `TB_MATRICULA` (
  `matricula_id` int NOT NULL,
  `aluno_id` int DEFAULT NULL,
  `disciplina_id` int DEFAULT NULL,
  `professor_id` int DEFAULT NULL,
  `n1` decimal(5,2) DEFAULT NULL,
  `n2` decimal(5,2) DEFAULT NULL,
  `faltas` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `TB_MATRICULA`
--

INSERT INTO `TB_MATRICULA` (`matricula_id`, `aluno_id`, `disciplina_id`, `professor_id`, `n1`, `n2`, `faltas`) VALUES
(1, 1, 1, 1, 7.50, 8.00, 3);

-- --------------------------------------------------------

--
-- Estrutura para tabela `TB_PROFESSOR`
--

CREATE TABLE `TB_PROFESSOR` (
  `professor_id` int NOT NULL,
  `nome` varchar(100) NOT NULL,
  `especialidade` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Despejando dados para a tabela `TB_PROFESSOR`
--

INSERT INTO `TB_PROFESSOR` (`professor_id`, `nome`, `especialidade`) VALUES
(1, 'Maria Oliveira', 'Matemática');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `TB_ALUNO`
--
ALTER TABLE `TB_ALUNO`
  ADD PRIMARY KEY (`aluno_id`);

--
-- Índices de tabela `TB_DISCIPLINA`
--
ALTER TABLE `TB_DISCIPLINA`
  ADD PRIMARY KEY (`disciplina_id`);

--
-- Índices de tabela `TB_MATRICULA`
--
ALTER TABLE `TB_MATRICULA`
  ADD PRIMARY KEY (`matricula_id`),
  ADD KEY `aluno_id` (`aluno_id`),
  ADD KEY `disciplina_id` (`disciplina_id`),
  ADD KEY `professor_id` (`professor_id`);

--
-- Índices de tabela `TB_PROFESSOR`
--
ALTER TABLE `TB_PROFESSOR`
  ADD PRIMARY KEY (`professor_id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `TB_ALUNO`
--
ALTER TABLE `TB_ALUNO`
  MODIFY `aluno_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de tabela `TB_DISCIPLINA`
--
ALTER TABLE `TB_DISCIPLINA`
  MODIFY `disciplina_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `TB_MATRICULA`
--
ALTER TABLE `TB_MATRICULA`
  MODIFY `matricula_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de tabela `TB_PROFESSOR`
--
ALTER TABLE `TB_PROFESSOR`
  MODIFY `professor_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restrições para tabelas despejadas
--

--
-- Restrições para tabelas `TB_MATRICULA`
--
ALTER TABLE `TB_MATRICULA`
  ADD CONSTRAINT `TB_MATRICULA_ibfk_1` FOREIGN KEY (`aluno_id`) REFERENCES `TB_ALUNO` (`aluno_id`),
  ADD CONSTRAINT `TB_MATRICULA_ibfk_2` FOREIGN KEY (`disciplina_id`) REFERENCES `TB_DISCIPLINA` (`disciplina_id`),
  ADD CONSTRAINT `TB_MATRICULA_ibfk_3` FOREIGN KEY (`professor_id`) REFERENCES `TB_PROFESSOR` (`professor_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
