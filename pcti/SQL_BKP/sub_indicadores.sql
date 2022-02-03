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
-- Estrutura da tabela `sub_indicadores`
--

CREATE TABLE `sub_indicadores` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `descricao` varchar(255) NOT NULL,
  `id_dimensao` int(11) NOT NULL,
  `delete_` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `sub_indicadores`
--

INSERT INTO `sub_indicadores` (`id`, `nome`, `descricao`, `id_dimensao`, `delete_`) VALUES
(1, 'teste', 'teste', 1, 0),
(2, 'teste', 'teste', 2, 0),
(3, 'rrrr', 'rrrr', 4, 0),
(4, 'teste', 'rrrr', 6, 0),
(5, 'teste', 'teste', 7, 0),
(6, 'rrrr', 'rrrr', 8, 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `sub_indicadores`
--
ALTER TABLE `sub_indicadores`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `sub_indicadores`
--
ALTER TABLE `sub_indicadores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
