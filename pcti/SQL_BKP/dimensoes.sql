-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 12-Nov-2021 às 02:44
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
-- Estrutura da tabela `dimensoes`
--

CREATE TABLE `dimensoes` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `descricao` varchar(1028) NOT NULL,
  `delete_` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `dimensoes`
--

INSERT INTO `dimensoes` (`id`, `nome`, `descricao`, `delete_`) VALUES
(1, 'Recursos Aplicados', 'São os principais indicadores na área de ciência e tecnologia (C&T), incluindo investimentos em pesquisa e desenvolvimento (P&D), públicos e privados e em atividades científicas e técnicas correlatas (ACTC) públicas. Produzidos no MCTIC, estes indicadores são apresentados segundo diferentes domínios e perspectivas.', 0),
(2, 'Recursos Humanos', 'descricao', 0),
(3, 'Bolsas de Formação', 'descricao', 0),
(4, 'Produção Científica', 'descricao', 0),
(5, 'Patentes', 'descricao', 0),
(6, 'Inovação', 'descricao', 0),
(7, 'teste', 'reste', 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `dimensoes`
--
ALTER TABLE `dimensoes`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `dimensoes`
--
ALTER TABLE `dimensoes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
