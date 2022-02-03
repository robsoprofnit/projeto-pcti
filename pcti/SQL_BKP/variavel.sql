-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 12-Nov-2021 às 02:45
-- Versão do servidor: 10.4.20-MariaDB
-- versão do PHP: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `our_users`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `variavel`
--

CREATE TABLE `variavel` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `tag` varchar(50) NOT NULL,
  `id_dimensao` int(11) NOT NULL,
  `delete_` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `variavel`
--

INSERT INTO `variavel` (`id`, `nome`, `descricao`, `tag`, `id_dimensao`, `delete_`) VALUES
(1, 'Orçamento Executado P&D', 'Dispêndios dos governos estaduais em pesquisa e desenvolvimento (P&D).', '#DM01.SBI01.VR01', 1, 0),
(2, 'Orçamento Executado ACTC', 'Dispêndios dos governos estaduais em ciência e tecnologia (C&T), por atividades científicas e técnicas correlatas (ACTC).', '#DM01.SBI01.VR02', 1, 0),
(3, 'Pós-graduação P&D', 'Dispêndios de pós-graduação em pesquisa e desenvolvimento (P&D).', '#DM01.SBI01.VR03', 1, 0),
(4, 'Pós-graduação ACTC', 'Dispêndios de pós-graduação em atividades científicas e técnicas correlatas (ACTC).', '#DM01.SBI01.VR04', 1, 0),
(5, 'teste', 'teste', '#TESTE', 1, 0),
(6, 'teste', 'teste', '#TESTE', 1, 0),
(7, 'teste', 'teste', '#TESTE', 1, 0),
(8, 'teste', 'teste', '#TESTE', 1, 0),
(9, 'teste', 'teste', '#TESTE', 1, 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `variavel`
--
ALTER TABLE `variavel`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `variavel`
--
ALTER TABLE `variavel`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
