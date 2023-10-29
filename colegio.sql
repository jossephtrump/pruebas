-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 29-10-2023 a las 06:09:07
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `colegio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `alumno`
--

CREATE TABLE `alumno` (
  `cedula` int(11) NOT NULL,
  `cedula_representante` int(11) DEFAULT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `pago` float(10,2) NOT NULL,
  `curso` varchar(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `alumno`
--

INSERT INTO `alumno` (`cedula`, `cedula_representante`, `nombre`, `direccion`, `telefono`, `pago`, `curso`) VALUES
(2, 0, 't', 'rf', '3', 0.00, ''),
(3, 2, 'victor', 'calle43', '04246281612', 80.00, ''),
(4, 2, 'andre', 'calle42', '04246281612', 60.00, ''),
(6, 2, 'VIC', 'ER', '434', 60.00, ''),
(1010, 0, 'victor', 'calle31', '0424', 60.00, 'S3');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_pagos`
--

CREATE TABLE `registro_pagos` (
  `id` int(11) NOT NULL,
  `fecha` date DEFAULT NULL,
  `hora` time DEFAULT NULL,
  `cedula_estudiante` int(11) DEFAULT NULL,
  `cedula_representante` int(11) DEFAULT NULL,
  `pago` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registro_pagos`
--

INSERT INTO `registro_pagos` (`id`, `fecha`, `hora`, `cedula_estudiante`, `cedula_representante`, `pago`) VALUES
(4, '2023-10-26', '03:33:00', 3, 2, 20),
(6, '2023-10-28', '22:57:00', 1010, 0, 60);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `representante`
--

CREATE TABLE `representante` (
  `cedula` int(11) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  `direccion` varchar(255) DEFAULT NULL,
  `telefono` varchar(15) DEFAULT NULL,
  `numero_alumnos` int(11) DEFAULT NULL,
  `correo` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `representante`
--

INSERT INTO `representante` (`cedula`, `nombre`, `direccion`, `telefono`, `numero_alumnos`, `correo`) VALUES
(0, 'coño', 'njd', 'la', 2, 'madre'),
(2, '2', '2', '2', 2, '2');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `alumno`
--
ALTER TABLE `alumno`
  ADD PRIMARY KEY (`cedula`),
  ADD KEY `cedula_representante` (`cedula_representante`);

--
-- Indices de la tabla `registro_pagos`
--
ALTER TABLE `registro_pagos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cedula_estudiante` (`cedula_estudiante`),
  ADD KEY `cedula_representante` (`cedula_representante`);

--
-- Indices de la tabla `representante`
--
ALTER TABLE `representante`
  ADD PRIMARY KEY (`cedula`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `registro_pagos`
--
ALTER TABLE `registro_pagos`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `alumno`
--
ALTER TABLE `alumno`
  ADD CONSTRAINT `alumno_ibfk_1` FOREIGN KEY (`cedula_representante`) REFERENCES `representante` (`cedula`);

--
-- Filtros para la tabla `registro_pagos`
--
ALTER TABLE `registro_pagos`
  ADD CONSTRAINT `registro_pagos_ibfk_1` FOREIGN KEY (`cedula_estudiante`) REFERENCES `alumno` (`cedula`),
  ADD CONSTRAINT `registro_pagos_ibfk_2` FOREIGN KEY (`cedula_representante`) REFERENCES `representante` (`cedula`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
