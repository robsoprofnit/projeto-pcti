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
-- Estrutura da tabela `pessoa`
--

CREATE TABLE `pessoa` (
  `id` int(11) NOT NULL,
  `nome` varchar(255) NOT NULL,
  `cpf_cnpj` varchar(50) NOT NULL,
  `razao_social` varchar(255) DEFAULT NULL,
  `nome_social` varchar(255) DEFAULT NULL,
  `id_email` int(11) NOT NULL,
  `id_tipo_pessoa` int(11) NOT NULL,
  `id_uf` int(11) NOT NULL,
  `delete_` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `pessoa`
--

INSERT INTO `pessoa` (`id`, `nome`, `cpf_cnpj`, `razao_social`, `nome_social`, `id_email`, `id_tipo_pessoa`, `id_uf`, `delete_`) VALUES
(1, 'Robson Rodrigues Neves Aguiar', '11111111111', 'Robson Rodrigues Neves Aguiar', 'Robson Rodrigues Neves Aguiar', 1, 1, 1, 0),
(2, 'Rafael Pontes Lima', '22222222222', 'Rafael Pontes Lima', 'Rafael Pontes Lima', 2, 1, 1, 0),
(3, 'SETEC', '00.394.577/0001-25', 'SETEC', 'SETEC', 3, 2, 3, 0),
(4, 'teste', '12434545', '', '', 3, 1, 0, 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `pessoa`
--
ALTER TABLE `pessoa`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `pessoa`
--
ALTER TABLE `pessoa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
