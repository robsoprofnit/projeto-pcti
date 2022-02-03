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
-- Estrutura da tabela `respostas`
--

CREATE TABLE `respostas` (
  `id` int(11) NOT NULL,
  `resposta` float NOT NULL,
  `data_resposta` datetime DEFAULT NULL,
  `tag` varchar(50) NOT NULL,
  `id_ano_base` int(11) NOT NULL,
  `id_instituicao` int(11) NOT NULL,
  `id_respondido_por` int(11) NOT NULL,
  `id_variavel` int(11) NOT NULL,
  `delete_` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Extraindo dados da tabela `respostas`
--

INSERT INTO `respostas` (`id`, `resposta`, `data_resposta`, `tag`, `id_ano_base`, `id_instituicao`, `id_respondido_por`, `id_variavel`, `delete_`) VALUES
(1, 941.8, '2021-10-17 02:58:51', '#DM01.SBI01.VR01', 1, 1, 2, 1, 0),
(2, 368.1, '2021-10-17 03:00:49', '#DM01.SBI01.VR02', 1, 1, 2, 2, 0),
(3, 1544.4, '2021-10-17 03:01:42', '#DM01.SBI01.VR03', 1, 1, 2, 3, 0),
(4, 0, '2021-10-17 03:02:21', '#DM01.SBI01.VR04', 1, 1, 2, 4, 0);

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `respostas`
--
ALTER TABLE `respostas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `respostas`
--
ALTER TABLE `respostas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
