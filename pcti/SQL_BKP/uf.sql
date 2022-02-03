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
-- Estrutura da tabela `uf`
--

CREATE TABLE `uf` (
  `id` int(11) NOT NULL,
  `nome` varchar(50) NOT NULL,
  `sigla` varchar(2) NOT NULL,
  `id_regiao` int(11) NOT NULL,
  `delete_` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `uf`
--

INSERT INTO `uf` (`id`, `nome`, `sigla`, `id_regiao`, `delete_`) VALUES
(1, 'Acre', 'AC', 3, 0),
(2, 'Alagoas', 'AL', 2, 0),
(3, 'Amapá', 'AP', 3, 0),
(4, 'Amazonas', 'AM', 3, 0),
(5, 'Bahia', 'BA', 3, 0),
(6, 'Ceará', 'CE', 2, 0),
(7, 'Distrito Federal', 'DF', 1, 0),
(8, 'Espirito Santo', 'ES', 3, 0),
(9, 'Goiás', 'GO', 1, 0),
(10, 'Maranhão', 'MA', 3, 0),
(11, 'Mato Grosso', 'MT', 1, 0),
(12, 'Mato Grosso do Sul', 'MS', 3, 0),
(13, 'Minas Gerais', 'MG', 3, 0),
(14, 'Pará', 'PA', 3, 0),
(15, 'Paraíba', 'PB', 3, 0),
(16, 'Paraná', 'PR', 3, 0),
(17, 'Pernambuco', 'PE', 3, 0),
(18, 'Piauí', 'PI', 3, 0),
(19, 'Rio de Janeiro', 'RJ', 3, 0),
(20, 'Rio Grande do Norte', 'RN', 3, 0),
(21, 'Rio Grande do Sul', 'RS', 3, 0),
(22, 'Rondônia', 'RO', 3, 0),
(23, 'Roraima', 'RR', 3, 0),
(24, 'Santa Catarina', 'SC', 3, 0),
(25, 'São Paulo', 'SP', 3, 0),
(26, 'Sergipe', 'SE', 3, 0),
(27, 'Tocantins', 'TO', 3, 0),
(28, 'teste', 'TS', 2, 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `uf`
--
ALTER TABLE `uf`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `sigla` (`sigla`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `uf`
--
ALTER TABLE `uf`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
