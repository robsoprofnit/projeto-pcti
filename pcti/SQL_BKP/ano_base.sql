-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 12-Nov-2021 às 02:43
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
-- Estrutura da tabela `ano_base`
--

DROP TABLE IF EXISTS `ano_base`;
CREATE TABLE `ano_base` (
  `id` int(11) NOT NULL,
  `ano` varchar(4) NOT NULL,
  `delete_` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `ano_base`
--

INSERT INTO `ano_base` (`id`, `ano`, `delete_`) VALUES
(1, '2000', 0),
(2, '2001', 0),
(3, '2002', 0),
(4, '2003', 0),
(5, '2004', 0),
(6, '2005', 0),
(7, '2006', 0),
(8, '2007', 0),
(9, '2008', 0),
(10, '2009', 0),
(11, '2010', 0),
(12, '2011', 0),
(13, '2012', 0),
(14, '2013', 0),
(15, '2014', 0),
(16, '2015', 0),
(17, '2016', 0),
(18, '2017', 0),
(19, '2018', 0),
(20, '2019', 0),
(21, '2020', 0),
(22, '2021', 0),
(23, '2021', 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `ano_base`
--
ALTER TABLE `ano_base`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `ano_base`
--
ALTER TABLE `ano_base`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
