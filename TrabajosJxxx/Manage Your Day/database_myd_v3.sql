SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "-05:00";

CREATE DATABASE IF NOT EXISTS `myd_db_v2` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `myd_db_v2`;

-- 1. Tabla de Usuarios (Soporta Roles y estados para soporte)
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL UNIQUE,
  `rol` enum('usuario', 'admin') DEFAULT 'usuario',
  `plan` enum('Básico', 'Premium') DEFAULT 'Básico',
  `estado_cuenta` enum('Activo', 'Suspendido', 'En Revisión') DEFAULT 'Activo',
  `nota_soporte` text DEFAULT NULL,
  `fecha_registro` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 2. Tabla de Tareas (Con fechas límite y estados de aplazamiento)
CREATE TABLE IF NOT EXISTS `tareas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `titulo` varchar(150) NOT NULL,
  `fecha_limite` date NOT NULL,
  `completada` boolean DEFAULT FALSE,
  `aplazamientos` int(11) DEFAULT 0,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- 3. Tabla de Finanzas y Metas
CREATE TABLE IF NOT EXISTS `finanzas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `usuario_id` int(11) NOT NULL,
  `tipo` enum('Ingreso', 'Gasto') NOT NULL,
  `monto` decimal(12,2) NOT NULL,
  `concepto` varchar(150) NOT NULL,
  `fecha` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Inserciones iniciales para pruebas de soporte
INSERT INTO `usuarios` (`id`, `nombre`, `email`, `rol`, `plan`, `estado_cuenta`, `nota_soporte`) VALUES
(1, 'Reiner Martínez', 'reiner@myd.com', 'admin', 'Premium', 'Activo', 'Líder de Proyecto - Acceso total.'),
(2, 'Estiven Garcés', 'estiven@myd.com', 'usuario', 'Premium', 'Activo', 'Usuario reporta lentitud en sincronización bancaria.'),
(3, 'Samuel Mira', 'samuel@myd.com', 'usuario', 'Básico', 'Activo', 'Interesado en pasarela de pagos Premium.');

COMMIT;