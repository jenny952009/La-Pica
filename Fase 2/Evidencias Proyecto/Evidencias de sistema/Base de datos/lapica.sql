-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-12-2024 a las 16:57:20
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `lapica`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add Categoria', 6, 'add_categoria'),
(22, 'Can change Categoria', 6, 'change_categoria'),
(23, 'Can delete Categoria', 6, 'delete_categoria'),
(24, 'Can view Categoria', 6, 'view_categoria'),
(25, 'Can add cuenta', 7, 'add_cuenta'),
(26, 'Can change cuenta', 7, 'change_cuenta'),
(27, 'Can delete cuenta', 7, 'delete_cuenta'),
(28, 'Can view cuenta', 7, 'view_cuenta'),
(29, 'Can add usuario perfil', 8, 'add_usuarioperfil'),
(30, 'Can change usuario perfil', 8, 'change_usuarioperfil'),
(31, 'Can delete usuario perfil', 8, 'delete_usuarioperfil'),
(32, 'Can view usuario perfil', 8, 'view_usuarioperfil'),
(33, 'Can add producto', 9, 'add_producto'),
(34, 'Can change producto', 9, 'change_producto'),
(35, 'Can delete producto', 9, 'delete_producto'),
(36, 'Can view producto', 9, 'view_producto'),
(37, 'Can add variacion', 10, 'add_variacion'),
(38, 'Can change variacion', 10, 'change_variacion'),
(39, 'Can delete variacion', 10, 'delete_variacion'),
(40, 'Can view variacion', 10, 'view_variacion'),
(41, 'Can add revisar rating', 11, 'add_revisarrating'),
(42, 'Can change revisar rating', 11, 'change_revisarrating'),
(43, 'Can delete revisar rating', 11, 'delete_revisarrating'),
(44, 'Can view revisar rating', 11, 'view_revisarrating'),
(45, 'Can add producto galeria', 12, 'add_productogaleria'),
(46, 'Can change producto galeria', 12, 'change_productogaleria'),
(47, 'Can delete producto galeria', 12, 'delete_productogaleria'),
(48, 'Can view producto galeria', 12, 'view_productogaleria'),
(49, 'Can add carrito', 13, 'add_carrito'),
(50, 'Can change carrito', 13, 'change_carrito'),
(51, 'Can delete carrito', 13, 'delete_carrito'),
(52, 'Can view carrito', 13, 'view_carrito'),
(53, 'Can add carrito item', 14, 'add_carritoitem'),
(54, 'Can change carrito item', 14, 'change_carritoitem'),
(55, 'Can delete carrito item', 14, 'delete_carritoitem'),
(56, 'Can view carrito item', 14, 'view_carritoitem'),
(57, 'Can add pago', 15, 'add_pago'),
(58, 'Can change pago', 15, 'change_pago'),
(59, 'Can delete pago', 15, 'delete_pago'),
(60, 'Can view pago', 15, 'view_pago'),
(61, 'Can add pedido', 16, 'add_pedido'),
(62, 'Can change pedido', 16, 'change_pedido'),
(63, 'Can delete pedido', 16, 'delete_pedido'),
(64, 'Can view pedido', 16, 'view_pedido'),
(65, 'Can add pedido producto', 17, 'add_pedidoproducto'),
(66, 'Can change pedido producto', 17, 'change_pedidoproducto'),
(67, 'Can delete pedido producto', 17, 'delete_pedidoproducto'),
(68, 'Can view pedido producto', 17, 'view_pedidoproducto'),
(69, 'Can add reserva', 18, 'add_reserva'),
(70, 'Can change reserva', 18, 'change_reserva'),
(71, 'Can delete reserva', 18, 'delete_reserva'),
(72, 'Can view reserva', 18, 'view_reserva'),
(73, 'Can add suscripcion', 19, 'add_suscripcion'),
(74, 'Can change suscripcion', 19, 'change_suscripcion'),
(75, 'Can delete suscripcion', 19, 'delete_suscripcion'),
(76, 'Can view suscripcion', 19, 'view_suscripcion'),
(77, 'Can add reseña rating', 11, 'add_reseñarating'),
(78, 'Can change reseña rating', 11, 'change_reseñarating'),
(79, 'Can delete reseña rating', 11, 'delete_reseñarating'),
(80, 'Can view reseña rating', 11, 'view_reseñarating');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito_carrito`
--

CREATE TABLE `carrito_carrito` (
  `id` bigint(20) NOT NULL,
  `carrito_id` varchar(250) NOT NULL,
  `fecha_agregado` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito_carrito`
--

INSERT INTO `carrito_carrito` (`id`, `carrito_id`, `fecha_agregado`) VALUES
(1, 'sb4wb5rkmpxfte3kpv8rb57516tt8i6r', '2024-10-09'),
(2, 'vi7gvixv73waatn7p6fdto11lks5xkgu', '2024-10-09'),
(3, '6iuhafuf8jn1ew8fn0jgjzt9bk2mv5bz', '2024-10-09'),
(4, 'rm2x4b9pzrv090p9yuz893pm2agbn0du', '2024-11-01'),
(5, 'owrqotsytchvqiosqo92y8v5zc6nob9q', '2024-11-04'),
(6, '73qj4j7wmsfz5ysueag0fkso0j5wxznb', '2024-11-05'),
(7, '5sq78znub5d6zvhr0b8y37gz0ympx0qg', '2024-11-06'),
(8, 'yh1htt7y4odlv5hr8rguvkij09qdqm5s', '2024-11-07'),
(9, '4rbkbg77qlqdirto5sdaw7kkm5q3tri6', '2024-12-09'),
(10, 'u2s5qqupunrfscveiee5sgnxecifcwj1', '2024-12-10'),
(11, 'hx0w7o1sec1v31l35qfh0migc8qnjz1n', '2024-12-11'),
(12, '5eknbbzzf5evj4u7i0qxkkanrijqtm7n', '2024-12-13');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `carrito_carritoitem`
--

CREATE TABLE `carrito_carritoitem` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `carro_id` bigint(20) DEFAULT NULL,
  `producto_id` bigint(20) NOT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `carrito_carritoitem`
--

INSERT INTO `carrito_carritoitem` (`id`, `cantidad`, `is_active`, `carro_id`, `producto_id`, `user_id`) VALUES
(1, 1, 1, 1, 4, NULL),
(19, 1, 1, 9, 18, NULL),
(20, 1, 1, 10, 1, NULL),
(21, 1, 1, 10, 4, NULL),
(22, 1, 1, 10, 3, NULL),
(31, 1, 1, NULL, 1, 5),
(32, 2, 1, 11, 3, NULL),
(35, 1, 1, 12, 1, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `categoria_categoria`
--

CREATE TABLE `categoria_categoria` (
  `id` bigint(20) NOT NULL,
  `categoria_nombre` varchar(20) NOT NULL,
  `descripcion` varchar(255) NOT NULL,
  `slug` varchar(100) NOT NULL,
  `cat_image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `categoria_categoria`
--

INSERT INTO `categoria_categoria` (`id`, `categoria_nombre`, `descripcion`, `slug`, `cat_image`) VALUES
(1, 'Ensaladas', 'Ensaladas para agregados de menú', 'ensalada-tomate-lechuga-papas', ''),
(2, 'Refrescos', 'Refrescos de agregado para menús', 'refrescos-jugo-bebida', ''),
(3, 'Comidas Típicas', 'Comidas tipicas chilenas', 'comidas-tipicas-menus', ''),
(4, 'Comida Rápida', 'Comida rapida para servir o llevar', 'comida-rapida-chatarra', ''),
(5, 'Pescado', 'Pescado como agregado', 'pescado-pez-ceviche', ''),
(6, 'Empanadas', 'Empanadas', 'empanadas', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta_cuenta`
--

CREATE TABLE `cuenta_cuenta` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `nombre` varchar(30) NOT NULL,
  `apellido` varchar(55) NOT NULL,
  `username` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `last_login` datetime(6) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superadmin` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cuenta_cuenta`
--

INSERT INTO `cuenta_cuenta` (`id`, `password`, `nombre`, `apellido`, `username`, `email`, `telefono`, `date_joined`, `last_login`, `is_admin`, `is_staff`, `is_active`, `is_superadmin`, `is_superuser`) VALUES
(1, 'pbkdf2_sha256$260000$12ZkkbQRFSHVaAtwf8G0F6$oUuBnnmB61rdlp8NlW5+kC5JmZ5I0Zir+lnM8UkfI2A=', 'admin', 'admin', 'admin', 'pam.aldana@duocuc.cl', '', '2024-10-18 01:48:12.202044', '2024-10-18 01:48:12.209770', 1, 1, 1, 1, 0),
(2, 'pbkdf2_sha256$260000$euHrPzApUgHLgURV0WRdCh$mt08t6PNB5GISYBV4D1CUwWqs5m7B0Ww0c1FKJs5JiM=', 'Pamela', 'Aldana', 'cat20pam', 'cat20pam@gmail.com', '951248446', '2024-10-18 01:48:38.108800', '2024-10-18 02:55:55.061191', 0, 0, 1, 0, 0),
(5, 'pbkdf2_sha256$600000$a4xhNz8jxHcVL1YdAYXutq$hHc1g722JqLiRgT2Ann4ZyKoVli85cDcwgM9NMVTTls=', 'jenny', 'lopez', 'jenny', 'jen.lopez@duocuc.cl', '954319275', '2024-11-19 05:33:24.388058', '2024-12-13 15:07:36.966696', 1, 1, 1, 1, 0),
(8, 'pbkdf2_sha256$600000$642Y5MJKuBTg0wEdiA0Ilk$8O4s9oXxIuS7b6kL23ziJzPKV/sJLmXc/yO3uOwmXVA=', 'Jenifer', 'Lopez', 'jennycarolinalopezsuarez', 'jennycarolinalopezsuarez@gmail.com', '951753698', '2024-12-11 02:04:35.249090', '2024-12-13 05:29:10.995520', 0, 0, 1, 0, 0),
(9, 'pbkdf2_sha256$600000$0viAjUFGI96kz1QatWSmdl$E4eWnkAXtRivj1Wytyv7ar8RGptNho4OXsM4n/K6SaQ=', 'jenifer', 'lopez', 'jenifer', 'lapicadelachabelita1234@gmail.com', '954319275', '2024-12-13 07:48:22.290484', '2024-12-13 07:48:22.290484', 0, 0, 1, 0, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta_cuenta_groups`
--

CREATE TABLE `cuenta_cuenta_groups` (
  `id` bigint(20) NOT NULL,
  `cuenta_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta_cuenta_user_permissions`
--

CREATE TABLE `cuenta_cuenta_user_permissions` (
  `id` bigint(20) NOT NULL,
  `cuenta_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cuenta_usuarioperfil`
--

CREATE TABLE `cuenta_usuarioperfil` (
  `id` bigint(20) NOT NULL,
  `direccion_1` varchar(100) NOT NULL,
  `direccion_2` varchar(100) NOT NULL,
  `profile_picture` varchar(100) NOT NULL,
  `ciudad` varchar(20) NOT NULL,
  `region` varchar(20) NOT NULL,
  `pais` varchar(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `cuenta_usuarioperfil`
--

INSERT INTO `cuenta_usuarioperfil` (`id`, `direccion_1`, `direccion_2`, `profile_picture`, `ciudad`, `region`, `pais`, `user_id`) VALUES
(5, '', '', 'default/default-user.png', '', '', '', 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-10-09 06:55:01.835275', '1', 'Ensaladas', 1, '[{\"added\": {}}]', 6, 1),
(2, '2024-10-09 06:55:49.624458', '2', 'Refrescos', 1, '[{\"added\": {}}]', 6, 1),
(3, '2024-10-09 06:56:36.229827', '3', 'Comidas Típicas', 1, '[{\"added\": {}}]', 6, 1),
(4, '2024-10-09 06:57:33.850565', '4', 'Comida Rápida', 1, '[{\"added\": {}}]', 6, 1),
(5, '2024-10-09 07:08:38.689406', '1', 'Cazuela de Vacuno', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Cazuela de Vacuno\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Cazuela de Vacuno\"}}]', 9, 2),
(6, '2024-10-09 07:15:12.550567', '5', 'Pescado', 1, '[{\"added\": {}}]', 6, 2),
(7, '2024-10-09 07:15:41.914321', '2', 'Ceviche', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ceviche\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ceviche\"}}]', 9, 2),
(8, '2024-10-09 07:16:35.617497', '2', 'Ceviche', 3, '', 9, 2),
(9, '2024-10-09 07:18:53.646577', '3', 'Ceviche', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ceviche\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ceviche\"}}]', 9, 2),
(10, '2024-10-09 07:19:26.408867', '1', 'Cazuela de Vacuno', 2, '[{\"changed\": {\"fields\": [\"Precio\"]}}]', 9, 2),
(11, '2024-10-09 07:19:51.038730', '1', 'Cazuela de Vacuno', 2, '[]', 9, 2),
(12, '2024-10-09 07:23:19.803666', '4', 'Completo Italiano', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Completo Italiano\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Completo Italiano\"}}]', 9, 2),
(13, '2024-10-09 07:28:56.627636', '5', 'Curanto', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Curanto\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Curanto\"}}]', 9, 2),
(14, '2024-10-09 07:31:42.883080', '6', 'Empanadas', 1, '[{\"added\": {}}]', 6, 2),
(15, '2024-10-09 07:31:59.004828', '6', 'Empanada de Pino', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Empanada de Pino\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Empanada de Pino\"}}]', 9, 2),
(16, '2024-10-09 07:36:55.096513', '7', 'Ensalada Surtida', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada Surtida\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada Surtida\"}}]', 9, 2),
(17, '2024-10-09 07:39:34.512837', '8', 'Humitas', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Humitas\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Humitas\"}}]', 9, 2),
(18, '2024-10-09 07:44:48.987155', '9', 'Ensalada de Lechuga', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Lechuga\"}}]', 9, 2),
(19, '2024-10-09 07:46:27.293133', '9', 'Ensalada de Lechuga', 2, '[{\"changed\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Lechuga\", \"fields\": [\"Image\"]}}]', 9, 2),
(20, '2024-10-09 07:47:29.964353', '9', 'Ensalada de Lechuga', 3, '', 9, 2),
(21, '2024-10-09 07:48:07.075552', '10', 'Ensalada de Lechuga', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Lechuga\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Lechuga\"}}]', 9, 2),
(22, '2024-10-09 07:48:49.131300', '10', 'Ensalada de Lechuga', 2, '[{\"changed\": {\"fields\": [\"Images\"]}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Lechuga\"}}]', 9, 2),
(23, '2024-10-09 07:49:37.329269', '10', 'Ensalada de Lechuga', 2, '[{\"deleted\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Lechuga\"}}]', 9, 2),
(24, '2024-10-09 07:50:51.888905', '10', 'Ensalada de Lechuga', 2, '[]', 9, 2),
(25, '2024-10-09 07:54:15.171258', '11', 'Nuggets de Pollo', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Nuggets de Pollo\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Nuggets de Pollo\"}}]', 9, 2),
(26, '2024-10-09 07:58:37.617204', '12', 'Papas Fritas', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Papas Fritas\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Papas Fritas\"}}]', 9, 2),
(27, '2024-10-09 08:00:18.218903', '13', 'Ensalada de Papas Mayo', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Papas Mayo\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Papas Mayo\"}}]', 9, 2),
(28, '2024-10-09 08:04:47.984597', '14', 'Pollo Asado con Papas Fritas', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Pollo Asado con Papas Fritas\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Pollo Asado con Papas Fritas\"}}]', 9, 2),
(29, '2024-10-09 08:06:20.502269', '15', 'Ensalada de Repollo', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Repollo\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada de Repollo\"}}]', 9, 2),
(30, '2024-10-09 08:08:07.018194', '16', 'Ensalada Tomate con Cebolla', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada Tomate con Cebolla\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Ensalada Tomate con Cebolla\"}}]', 9, 2),
(31, '2024-10-09 08:12:19.140154', '17', 'Empanada de Queso', 1, '[{\"added\": {}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Empanada de Queso\"}}, {\"added\": {\"name\": \"producto galeria\", \"object\": \"Empanada de Queso\"}}]', 9, 2),
(32, '2024-10-09 09:32:37.991289', '14', 'Pollo Asado con Papas Fritas', 2, '[{\"changed\": {\"fields\": [\"Categoria\"]}}]', 9, 2),
(33, '2024-12-06 02:44:06.617182', '6', 'promocion.dentalpacifico@gmail.com', 3, '', 7, 5),
(34, '2024-12-06 02:44:17.333991', '4', 'jennycarolinalopezsuarez@gmail.com', 3, '', 7, 5),
(35, '2024-12-11 01:59:41.002675', '30', 'lapicadelachabelita1234@gmail.com', 3, '', 19, 5),
(36, '2024-12-11 01:59:41.092553', '29', 'jen.lopez@duocuc.cl', 3, '', 19, 5),
(37, '2024-12-11 01:59:41.172413', '28', 'promocion.dentalpacifico@gmail.com', 3, '', 19, 5),
(38, '2024-12-11 01:59:41.239861', '27', 'jennycarolinalopezsuarez@gmail.com', 3, '', 19, 5),
(39, '2024-12-11 01:59:49.971078', '15', 'lll@jjj.com', 3, '', 19, 5),
(40, '2024-12-11 02:03:39.015691', '4', 'Jenifer', 3, '', 8, 5),
(41, '2024-12-11 02:04:02.476492', '7', 'jennycarolinalopezsuarez@gmail.com', 3, '', 7, 5),
(42, '2024-12-11 02:06:50.441712', '8', 'Jenifer Lopez - Mesa 9', 3, '', 18, 5),
(43, '2024-12-11 02:06:50.447598', '7', 'Jenifer Lopez - Mesa 5', 3, '', 18, 5),
(44, '2024-12-11 02:06:50.462688', '6', 'Jenifer Lopez - Mesa 5', 3, '', 18, 5),
(45, '2024-12-11 02:06:50.471387', '5', 'Jenifer Lopez - Mesa 7', 3, '', 18, 5),
(46, '2024-12-11 02:06:50.476431', '4', 'Jenifer Lopez - Mesa 5', 3, '', 18, 5),
(47, '2024-12-11 02:06:50.480390', '3', 'Jenifer Lopez - Mesa 2', 3, '', 18, 5),
(48, '2024-12-11 02:06:50.484474', '2', 'papa papa - Mesa 2', 3, '', 18, 5),
(49, '2024-12-11 02:06:50.488096', '1', 'oaooa ooaooa - Mesa 7', 3, '', 18, 5),
(50, '2024-12-13 07:48:22.295721', '9', 'lapicadelachabelita1234@gmail.com', 1, '[{\"added\": {}}]', 7, 5),
(51, '2024-12-13 07:50:27.317928', '32', 'Empanada de mariscos', 2, '[{\"changed\": {\"fields\": [\"Nombre del producto\", \"Slug\"]}}]', 9, 5),
(52, '2024-12-13 07:53:35.801052', '5', 'jen.lopez@duocuc.cl', 2, '[{\"changed\": {\"fields\": [\"Tel\\u00e9fono\"]}}]', 7, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(13, 'carrito', 'carrito'),
(14, 'carrito', 'carritoitem'),
(6, 'categoria', 'categoria'),
(4, 'contenttypes', 'contenttype'),
(7, 'cuenta', 'cuenta'),
(8, 'cuenta', 'usuarioperfil'),
(15, 'pedido', 'pago'),
(16, 'pedido', 'pedido'),
(17, 'pedido', 'pedidoproducto'),
(18, 'reservaciones', 'reserva'),
(5, 'sessions', 'session'),
(19, 'suscripcion', 'suscripcion'),
(9, 'tienda', 'producto'),
(12, 'tienda', 'productogaleria'),
(11, 'tienda', 'reseñarating'),
(10, 'tienda', 'variacion');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'cuenta', '0001_initial', '2024-10-18 01:47:47.953346'),
(2, 'contenttypes', '0001_initial', '2024-10-18 01:47:47.984662'),
(3, 'admin', '0001_initial', '2024-10-18 01:47:48.072137'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-10-18 01:47:48.077135'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-10-18 01:47:48.082105'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-10-18 01:47:48.119654'),
(7, 'auth', '0001_initial', '2024-10-18 01:47:48.282349'),
(8, 'auth', '0002_alter_permission_name_max_length', '2024-10-18 01:47:48.319858'),
(9, 'auth', '0003_alter_user_email_max_length', '2024-10-18 01:47:48.338337'),
(10, 'auth', '0004_alter_user_username_opts', '2024-10-18 01:47:48.346516'),
(11, 'auth', '0005_alter_user_last_login_null', '2024-10-18 01:47:48.351749'),
(12, 'auth', '0006_require_contenttypes_0002', '2024-10-18 01:47:48.358226'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2024-10-18 01:47:48.363371'),
(14, 'auth', '0008_alter_user_username_max_length', '2024-10-18 01:47:48.373066'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2024-10-18 01:47:48.378751'),
(16, 'auth', '0010_alter_group_name_max_length', '2024-10-18 01:47:48.385045'),
(17, 'auth', '0011_update_proxy_permissions', '2024-10-18 01:47:48.401660'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2024-10-18 01:47:48.411275'),
(19, 'categoria', '0001_initial', '2024-10-18 01:47:48.437702'),
(20, 'tienda', '0001_initial', '2024-10-18 01:47:48.677431'),
(21, 'tienda', '0002_rename_revisar_revisarrating_review', '2024-10-18 01:47:48.693291'),
(22, 'carrito', '0001_initial', '2024-10-18 01:47:48.946430'),
(23, 'cuenta', '0002_auto_20241001_1013', '2024-10-18 01:47:48.946430'),
(24, 'cuenta', '0003_alter_usuarioperfil_region', '2024-10-18 01:47:48.975864'),
(25, 'sessions', '0001_initial', '2024-10-18 01:47:49.003475'),
(26, 'pedido', '0001_initial', '2024-10-18 02:05:56.575428'),
(27, 'reservaciones', '0001_initial', '2024-10-20 01:10:41.909867'),
(28, 'suscripcion', '0001_initial', '2024-10-20 02:36:30.005943'),
(29, 'suscripcion', '0002_suscripcion_activo', '2024-10-22 03:17:18.499599'),
(30, 'reservaciones', '0002_reserva_dia_reserva', '2024-11-05 02:51:11.193660'),
(31, 'carrito', '0002_remove_carritoitem_variacion', '2024-11-19 04:47:31.416676'),
(32, 'pedido', '0002_remove_pedidoproducto_variacion', '2024-11-19 04:47:31.461064'),
(33, 'pedido', '0003_alter_pedido_direccion_2', '2024-11-19 04:47:31.476654'),
(34, 'tienda', '0003_auto_20241106_1827', '2024-11-19 04:47:31.551696'),
(35, 'tienda', '0004_auto_20241106_1958', '2024-11-19 04:47:31.579101'),
(36, 'reservaciones', '0003_auto_20241124_1955', '2024-12-06 02:29:12.937468'),
(37, 'tienda', '0005_producto_ventas', '2024-12-10 20:41:45.141609'),
(38, 'carrito', '0003_alter_carritoitem_is_active_alter_carritoitem_user', '2024-12-13 03:59:03.395225'),
(39, 'cuenta', '0004_alter_cuenta_options_alter_usuarioperfil_options_and_more', '2024-12-13 03:59:04.510715'),
(40, 'tienda', '0006_alter_producto_options_alter_productogaleria_options_and_more', '2024-12-13 03:59:04.744632'),
(41, 'tienda', '0007_alter_producto_options', '2024-12-13 03:59:04.762063'),
(42, 'pedido', '0004_alter_pago_created_at_alter_pago_monto_id_and_more', '2024-12-13 03:59:05.123134'),
(43, 'pedido', '0005_alter_pago_created_at_alter_pago_monto_id_and_more', '2024-12-13 03:59:05.444967'),
(44, 'pedido', '0006_alter_pago_created_at_alter_pago_monto_id_and_more', '2024-12-13 03:59:05.781751'),
(45, 'reservaciones', '0004_alter_reserva_options_alter_reserva_apellido_and_more', '2024-12-13 03:59:05.799590');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0x0nq7nmoli6rawfngqyo7vqmlm5rqhh', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE3MzQxMDU0MDcuODYwMTMxNX0:1tM823:Aje2NYbMrKGhIhWYUtuM6T0BepZLOgSZWixp-_A05zM', '2024-12-13 16:26:47.869089'),
('572ju76ck4g063896ft7q81tyf5ufqrb', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE3MjkzODIxNDYuODA1NzQ0NH0:1t2JIR:Kjt7llzl3ZmVCBrHHt90RyAzF20mJrIGXlP63w_IH48', '2024-11-02 23:55:47.124525'),
('ou0f4mwg3necm0kdhfrgk04ndbq0a8lk', 'e30:1tM0UV:Ha7beMxRrskCJr7yrfL3S5kGQHJvBLQT6U5qHyYPozE', '2024-12-13 08:23:39.719347'),
('qz960p2dr550qmqtv27dqprus9lq2vyz', '.eJxVjDsOwjAQBe_iGln-rD-kpOcM1sbrEAOxUexUiLsDUpq0b2bem4WWWsu1hFxyDz0vqXVcXoEN0mmQQoEVXIHwoE8s4NbnsLW0hkxsYIYdthHjI5U_oDuWW-Wxlr7mkf8VvtPGr5XS87K7h4MZ2_yrbTRukpG8FGR8AoKzV2QEqYgKrSSFWsQRpCJvnCGUIMSUnEa0zmNiny_GWkX_:1tM7GW:l7w36kr7RAuHbX9r97UqaTBt5CMATto5VYGsu8ry4Tk', '2024-12-13 15:37:40.308194'),
('rgkpmpsyygd537zew5s2rcipv7ijbxga', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE3MjkzNTk3MzcuOTkxNTI3fQ:1t2DT0:Z2T0AOpbvxk4ZCXMddczKxO0zxNScsRQL_MnKGEgR2s', '2024-11-02 17:42:18.231167'),
('rkrqtavy11s49ae1cirl8yznmn1k4zos', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE3MjkyMTYxOTUuNTAyNTIzNH0:1t1c7n:MX9LO0VvafXvmsQ2iCTO9Fvh01l68gL5akJ6VHM9CH4', '2024-11-01 01:49:55.509801'),
('ugowmq1fjk66zmo2s1f98p23wja2g1xj', '.eJxVjMEOwiAQBf-FsyFAWaA9evcbyJalFrVgCj0Z_12b9NLrm5n3Yb7GWlPJPuXUfEtLrA2Xt2eDtJ0WpofecQnaQX9hHrc2-63G1SdiAwN22kYMz5h3QA_M98JDyW1NI98VftDKb4Xi63q4p4MZ6_yvTQA7yUBOCgIXNeneKQJBKqBCI0lhJ8KopSIHFgilFmKKtkM01mFk3x_ev0Yi:1tLyiU:hIKs9iqoyofUKUJ6qql3BVk1k9lTKuZmVpQSmde0XZQ', '2024-12-13 06:29:58.223962'),
('uwmadb4xaill99azmloswpdit7a3c0se', 'e30:1t5xAN:k0CweyBGPyXqSuAUKr92m9KyyZAo3bl_nlvSYmosudY', '2024-11-13 01:06:31.703270'),
('w9jjy21sk34vsawkv3qfja2ay68gfdls', 'eyJfc2Vzc2lvbl9pbml0X3RpbWVzdGFtcF8iOjE3MjkyODI4MzIuNTY0MDA5N30:1t1tSa:AOeHbuvNtHG9MA3RU2XbBqIPcFza1m3OSNah88yTiC8', '2024-11-01 20:20:32.980579');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido_pago`
--

CREATE TABLE `pedido_pago` (
  `id` bigint(20) NOT NULL,
  `pago_id` varchar(100) NOT NULL,
  `pago_method` varchar(100) NOT NULL,
  `monto_id` varchar(100) NOT NULL,
  `status` varchar(100) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido_pago`
--

INSERT INTO `pedido_pago` (`id`, `pago_id`, `pago_method`, `monto_id`, `status`, `created_at`, `user_id`) VALUES
(4, '4HF59574U2840041L', 'Paypal', '10674.3', 'COMPLETED', '2024-12-10 21:55:54.306908', 5),
(5, '3EJ6942440404742T', 'Paypal', '10686.2', 'COMPLETED', '2024-12-10 21:57:27.898442', 5),
(7, '8SX51742PL3380922', 'Paypal', '4748.1', 'COMPLETED', '2024-12-11 02:58:27.301026', 5),
(8, '1M188279SG732384S', 'Paypal', '4748.1', 'COMPLETED', '2024-12-13 04:01:06.024711', 8),
(9, '8NJ327529N948224M', 'Paypal', '4748.1', 'COMPLETED', '2024-12-13 05:02:55.835547', 8),
(10, '5KK38447DN498093G', 'Paypal', '4748.1', 'COMPLETED', '2024-12-13 05:30:08.132275', 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido_pedido`
--

CREATE TABLE `pedido_pedido` (
  `id` bigint(20) NOT NULL,
  `pedido_numero` varchar(20) NOT NULL,
  `nombre` varchar(50) NOT NULL,
  `apellido` varchar(50) NOT NULL,
  `telefono` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `direccion_1` varchar(100) NOT NULL,
  `direccion_2` varchar(100) NOT NULL,
  `pais` varchar(50) NOT NULL,
  `ciudad` varchar(50) NOT NULL,
  `region` varchar(20) NOT NULL,
  `pedido_nota` varchar(100) NOT NULL,
  `pedido_total` double NOT NULL,
  `impuesto` double NOT NULL,
  `status` varchar(50) NOT NULL,
  `ip` varchar(20) NOT NULL,
  `is_ordered` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `pago_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido_pedido`
--

INSERT INTO `pedido_pedido` (`id`, `pedido_numero`, `nombre`, `apellido`, `telefono`, `email`, `direccion_1`, `direccion_2`, `pais`, `ciudad`, `region`, `pedido_nota`, `pedido_total`, `impuesto`, `status`, `ip`, `is_ordered`, `created_at`, `updated_at`, `pago_id`, `user_id`) VALUES
(1, '202410091', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'la cazuela sin verde porfavor', 9496.2, 1516.2, 'New', '127.0.0.1', 0, '2024-10-09 09:41:54.846896', '2024-10-09 09:41:54.852297', NULL, 2),
(2, '202410092', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'la cazuela sin verde porfavor', 9496.2, 1516.2, 'New', '127.0.0.1', 0, '2024-10-09 09:46:30.564239', '2024-10-09 09:46:30.569231', NULL, 2),
(3, '202410093', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'sin sal', 9496.2, 1516.2, 'New', '127.0.0.1', 0, '2024-10-09 09:47:34.545013', '2024-10-09 09:47:34.564991', NULL, 2),
(4, '202410174', 'pamel', 'pam', '9999999999', 'pam@cat.com', 'libertad', '123', 'chile', 'meli', 'RM', 'HDHDHDHH', 15434.3, 2464.3, 'New', '127.0.0.1', 0, '2024-10-18 02:56:38.149037', '2024-10-18 02:56:38.165007', NULL, 2),
(5, '202410175', 'pp', 'pp', '988877', 'pa@dll.com', 'jkjjj', 'kkk', 'kk', 'kk', 'rm', 'jj', 21360.5, 3410.5, 'New', '127.0.0.1', 0, '2024-10-18 03:58:04.160564', '2024-10-18 03:58:04.165615', NULL, 2),
(6, '202411056', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'ghg', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-05 03:22:33.546573', '2024-11-05 03:22:33.557471', NULL, NULL),
(7, '202411057', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'ghg', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-05 03:40:42.352311', '2024-11-05 03:40:42.366657', NULL, NULL),
(8, '202411058', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'ghg', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-05 03:44:27.457512', '2024-11-05 03:44:27.468591', NULL, NULL),
(9, '202411059', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'ghg', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-05 03:44:36.382441', '2024-11-05 03:44:36.402158', NULL, NULL),
(10, '2024110510', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'ghg', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-05 03:44:41.464185', '2024-11-05 03:44:41.464185', NULL, NULL),
(11, '2024110511', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'ghg', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-05 03:45:21.553928', '2024-11-05 03:45:21.562504', NULL, NULL),
(12, '2024110512', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'xcx', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-05 21:56:21.469983', '2024-11-05 21:56:21.478270', NULL, NULL),
(13, '2024110513', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'xcx', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-05 21:57:28.832237', '2024-11-05 21:57:28.863272', NULL, NULL),
(14, '2024110514', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'dgf', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-05 21:58:04.705820', '2024-11-05 21:58:04.712097', NULL, NULL),
(15, '2024110515', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'vng', 4748.1, 758.1, 'New', '127.0.0.1', 1, '2024-11-05 22:18:20.597840', '2024-11-05 22:20:02.251190', NULL, NULL),
(16, '2024110516', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'bnhgb', 4748.1, 758.1, 'New', '127.0.0.1', 1, '2024-11-05 22:21:19.786417', '2024-11-05 22:21:39.599354', NULL, NULL),
(17, '2024110717', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'vb', 4748.1, 758.1, 'New', '127.0.0.1', 1, '2024-11-07 17:54:35.353249', '2024-11-07 18:11:42.848016', NULL, NULL),
(18, '2024110718', 'Jenifer', 'Lopez', '+56954319275', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'ijij', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-11-07 18:13:27.821864', '2024-11-07 18:13:27.833403', NULL, NULL),
(19, '2024121019', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjdfjd', 10674.3, 1704.3, 'New', '127.0.0.1', 1, '2024-12-10 21:48:39.106204', '2024-12-10 21:55:54.315887', 4, 5),
(20, '2024121020', 'Jenifer Lopez', 'aldana', '569543194', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'knnkk', 10686.2, 1706.2, 'New', '127.0.0.1', 1, '2024-12-10 21:56:57.147596', '2024-12-10 21:57:27.932625', 5, 5),
(21, '2024121021', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'casa roja', 10686.2, 1706.2, 'New', '127.0.0.1', 1, '2024-12-10 23:01:27.077197', '2024-12-10 23:02:13.768211', NULL, NULL),
(22, '2024121022', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjfvjvfj', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:28:31.520400', '2024-12-11 02:28:31.527959', NULL, 5),
(23, '2024121023', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjfvjvfj', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:33:24.732818', '2024-12-11 02:33:24.744839', NULL, 5),
(24, '2024121024', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjfvjvfj', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:33:46.980398', '2024-12-11 02:33:46.993041', NULL, 5),
(25, '2024121025', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjfvjvfj', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:33:50.468355', '2024-12-11 02:33:50.474339', NULL, 5),
(26, '2024121026', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjfvjvfj', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:34:21.339898', '2024-12-11 02:34:21.367697', NULL, 5),
(27, '2024121027', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjfvjvfj', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:34:26.609569', '2024-12-11 02:34:26.663441', NULL, 5),
(28, '2024121028', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjfvjvfj', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:36:24.460154', '2024-12-11 02:36:24.474320', NULL, 5),
(29, '2024121029', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjfvjvfj', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:50:16.138633', '2024-12-11 02:50:16.146670', NULL, 5),
(30, '2024121030', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'kjfvjvfj', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:50:20.733863', '2024-12-11 02:50:20.737856', NULL, 5),
(31, '2024121031', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'HII', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 02:51:05.907294', '2024-12-11 02:51:05.911284', NULL, 5),
(32, '2024121032', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'HII', 4748.1, 758.1, 'New', '127.0.0.1', 1, '2024-12-11 02:52:33.795513', '2024-12-11 02:58:27.307010', 7, 5),
(33, '2024121133', 'Jenifer', 'Lopez', '856954319', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'l,l', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 03:04:03.575095', '2024-12-11 03:04:03.583079', NULL, 5),
(34, '2024121134', 'Jenifer', 'Lopez', '856954319', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'l,l', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 03:14:43.892006', '2024-12-11 03:14:43.898166', NULL, 5),
(35, '2024121135', 'Jenifer', 'Lopez', '856954319', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'l,l', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-11 03:15:17.023715', '2024-12-11 03:15:17.030034', NULL, 5),
(36, '2024121136', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'ijfijfg', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-12 01:26:30.084583', '2024-12-12 01:26:30.096123', NULL, 8),
(37, '2024121337', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'njjj', 4748.1, 758.1, 'New', '127.0.0.1', 1, '2024-12-13 04:00:21.078186', '2024-12-13 04:01:06.032426', 8, 8),
(38, '', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'hkk', 4748.1, 758.1, 'New', '127.0.0.1', 0, '2024-12-13 04:51:45.129740', '2024-12-13 04:51:45.129740', NULL, 8),
(39, '2024121339', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'jhjuih', 4748.1, 758.1, 'New', '127.0.0.1', 1, '2024-12-13 05:02:10.852814', '2024-12-13 05:02:55.858739', 9, 8),
(40, '2024121340', 'Jenifer', 'Lopez', '951753698', 'jennycarolinalopezsuarez@gmail.com', 'av circunvalacion', 'segundo lomo de toro', 'chile', 'melipilla', 'metropolitana', 'bvnbv', 4748.1, 758.1, 'New', '127.0.0.1', 1, '2024-12-13 05:29:41.695271', '2024-12-13 05:30:08.139788', 10, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pedido_pedidoproducto`
--

CREATE TABLE `pedido_pedidoproducto` (
  `id` bigint(20) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `producto_precio` double NOT NULL,
  `ordered` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `pago_id` bigint(20) DEFAULT NULL,
  `pedido_id` bigint(20) NOT NULL,
  `producto_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `pedido_pedidoproducto`
--

INSERT INTO `pedido_pedidoproducto` (`id`, `cantidad`, `producto_precio`, `ordered`, `created_at`, `updated_at`, `pago_id`, `pedido_id`, `producto_id`, `user_id`) VALUES
(4, 1, 3990, 1, '2024-12-10 21:55:54.333839', '2024-12-10 21:55:54.333839', 4, 19, 1, 5),
(5, 1, 2490, 1, '2024-12-10 21:55:54.349798', '2024-12-10 21:55:54.349798', 4, 19, 4, 5),
(6, 1, 2490, 1, '2024-12-10 21:55:54.367258', '2024-12-10 21:55:54.367258', 4, 19, 6, 5),
(7, 1, 3990, 1, '2024-12-10 21:57:27.945201', '2024-12-10 21:57:27.945201', 5, 20, 1, 5),
(8, 1, 4990, 1, '2024-12-10 21:57:27.960302', '2024-12-10 21:57:27.960302', 5, 20, 3, 5),
(11, 1, 3990, 1, '2024-12-11 02:58:27.320474', '2024-12-11 02:58:27.320474', 7, 32, 1, 5),
(12, 1, 3990, 1, '2024-12-13 04:01:06.045027', '2024-12-13 04:01:06.045027', 8, 37, 1, 8),
(13, 1, 3990, 1, '2024-12-13 05:02:55.871265', '2024-12-13 05:02:55.871265', 9, 39, 1, 8),
(14, 1, 3990, 1, '2024-12-13 05:30:08.176297', '2024-12-13 05:30:08.177296', 10, 40, 1, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `reservaciones_reserva`
--

CREATE TABLE `reservaciones_reserva` (
  `id` bigint(20) NOT NULL,
  `codigo_reserva` varchar(100) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `apellido` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `telefono` varchar(15) NOT NULL,
  `numero_mesa` int(11) NOT NULL,
  `fecha_reserva` datetime(6) NOT NULL,
  `hora_comienzo` varchar(100) NOT NULL,
  `personas` int(11) NOT NULL,
  `dia_reserva` date NOT NULL,
  `hora_fin` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `reservaciones_reserva`
--

INSERT INTO `reservaciones_reserva` (`id`, `codigo_reserva`, `nombre`, `apellido`, `email`, `telefono`, `numero_mesa`, `fecha_reserva`, `hora_comienzo`, `personas`, `dia_reserva`, `hora_fin`) VALUES
(9, '7E6GL7', 'Jenifer', 'Lopez', 'jennycarolinalopezsuarez@gmail.com', '951753698', 10, '2024-12-11 02:07:34.108488', '12:00', 10, '2024-12-11', '13:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `suscripcion_suscripcion`
--

CREATE TABLE `suscripcion_suscripcion` (
  `id` bigint(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `fecha_creacion` datetime(6) NOT NULL,
  `activo` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `suscripcion_suscripcion`
--

INSERT INTO `suscripcion_suscripcion` (`id`, `email`, `fecha_creacion`, `activo`) VALUES
(14, 'ppa@hh.com', '2024-10-20 04:34:27.346213', 1),
(31, 'lapicadelachabelita1234@gmail.com', '2024-12-11 02:00:24.009624', 1),
(32, 'jen.lopez@duocuc.cl', '2024-12-11 02:01:17.349907', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tienda_producto`
--

CREATE TABLE `tienda_producto` (
  `id` bigint(20) NOT NULL,
  `producto_nombre` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `descripcion` longtext NOT NULL,
  `precio` int(11) NOT NULL,
  `images` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `is_available` tinyint(1) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `modified_date` datetime(6) NOT NULL,
  `categoria_id` bigint(20) NOT NULL,
  `ventas` int(10) UNSIGNED NOT NULL CHECK (`ventas` >= 0)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tienda_producto`
--

INSERT INTO `tienda_producto` (`id`, `producto_nombre`, `slug`, `descripcion`, `precio`, `images`, `stock`, `is_available`, `created_date`, `modified_date`, `categoria_id`, `ventas`) VALUES
(1, 'Cazuela de Vacuno', 'cazuela-de-vacuno', 'Plato típico, elaborado con una presa de carne de vacuno, más verduras variadas: zapallo, choclo, papa, arroz u otras verduras.', 3990, 'fotos/productos/cazuelavacuno1.png', 0, 1, '2024-10-09 07:08:38.689406', '2024-12-13 05:30:08.196372', 3, 7),
(3, 'Ceviche', 'ceviche-pescado', 'Platillo preparado con pescado crudo y mariscos marinado en jugo de limón y condimentado con cebolla, cilantro y sal.', 4990, 'fotos/productos/ceviche3.png', 8, 1, '2024-10-09 07:18:53.631132', '2024-12-10 23:02:13.800564', 5, 2),
(4, 'Completo Italiano', 'completo-italiano-hotdog', 'Pan de completo grande abierto a lo largo, con vienesa, tomate, palta y mayo casera.', 2490, 'fotos/productos/completo3.png', 9, 1, '2024-10-09 07:23:19.789053', '2024-12-10 21:55:54.353786', 4, 1),
(5, 'Curanto', 'curanto-cocimiento', 'Curanto, Pulmay o Cocimiento de diversos tipos de mariscos, carne de cerdo ahumado, pollo, junto a milcaos, papas y arvejas.', 4990, 'fotos/productos/curanto3.png', 10, 1, '2024-10-09 07:28:56.617793', '2024-10-09 07:28:56.617793', 5, 0),
(6, 'Empanada de Pino', 'empanada-de-pino', 'Rellenas con carne vacuna picada, frito con cebolla blanca y condimentada con aliño completo, ají de color, huevo duro, aceitunas y, opcionalmente, pasas de uva.​', 2490, 'fotos/productos/empanadapino2.png', 9, 1, '2024-10-09 07:31:58.989580', '2024-12-10 21:55:54.371247', 6, 1),
(7, 'Ensalada Surtida', 'ensalada-surtida', 'Conjunto de ensaladas como luchuga, repollo, zanahoria, papas mayo, porotos verdes y choclo mezcladas en un plato único.', 1990, 'fotos/productos/ensaladasurtida1.jpg', 10, 1, '2024-10-09 07:36:55.083534', '2024-10-09 07:36:55.083534', 1, 0),
(8, 'Humitas', 'humitas-choclo', 'Pasta a base de choclo, aliñada con cebolla y albahaca, que va envuelta en las propias hojas del choclo.', 2490, 'fotos/productos/humita1.png', 10, 1, '2024-10-09 07:39:34.499278', '2024-10-09 07:39:34.500268', 3, 0),
(10, 'Ensalada de Lechuga', 'ensalada-de-lechuga', 'Ensalada de lechuga aliñada con aceite, limón y sal.', 1990, 'fotos/productos/lechuga2_ZuMrmme.png', 10, 1, '2024-10-09 07:48:07.067534', '2024-10-09 07:50:51.887261', 1, 0),
(11, 'Nuggets de Pollo', 'nuggets-de-pollo', '6 unidades de nuggets de pollo fritos en freidora de aire.', 2490, 'fotos/productos/nugget1.png', 10, 1, '2024-10-09 07:54:15.162214', '2024-10-09 07:54:15.162214', 4, 0),
(12, 'Papas Fritas', 'papas-fritas', 'Porción de 500gr. de papas fritas.', 2490, 'fotos/productos/papas2.png', 10, 1, '2024-10-09 07:58:37.608098', '2024-10-09 07:58:37.608098', 4, 0),
(13, 'Ensalada de Papas Mayo', 'ensalada-de-papas-mayo', 'Papas en cuadritos con mayonesa y un toque cilantro picado.', 1990, 'fotos/productos/papasmayo3.jpg', 10, 1, '2024-10-09 08:00:18.209644', '2024-10-09 08:00:18.209644', 1, 0),
(14, 'Pollo Asado con Papas Fritas', 'pollo-asado-con-papas-fritas', 'Trozo de pollo asado con porción de papas fritas.', 3990, 'fotos/productos/pollo1.jpg', 10, 1, '2024-10-09 08:04:47.968353', '2024-10-09 09:32:37.989291', 4, 0),
(15, 'Ensalada de Repollo', 'ensalada-de-repollo', 'Repollo picado con un toque de cilantro, aliñada con limón, aceite y sal.', 1990, 'fotos/productos/repollo2.jpg', 10, 1, '2024-10-09 08:06:20.493477', '2024-10-09 08:06:20.493477', 1, 0),
(16, 'Ensalada Tomate con Cebolla', 'ensalada-tomate-con-cebolla', 'Tomate picado con cebolla en pluma y un toque de cilantro, aliñada con aceite y sal.', 1990, 'fotos/productos/tomate3.jpg', 10, 1, '2024-10-09 08:08:07.007884', '2024-10-09 08:08:07.007884', 1, 0),
(17, 'Empanada de Queso', 'empanada-de-queso', 'Empanada frita de queso de campo.', 2490, 'fotos/productos/empanadadequeso1.jpg', 10, 1, '2024-10-09 08:12:19.123845', '2024-10-09 08:12:19.123845', 6, 0),
(18, 'Pastel de choclo', 'pastel-de-choclo', 'Plato típico preparado con una pasta horneada de granos tiernos de choclo, y, dependiendo del lugar donde se prepare, es dulce, con relleno.', 2990, 'fotos/productos/PastelChoclo.jpg', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-18 01:50:09.000000', 3, 0),
(19, 'Chuleta con puré', 'chuleta-con-pure', 'Plato típico de chile chuleta vetada cocida a la parrilla a fuego lento con puré de papas.', 1990, 'fotos/productos/ChuletaConPure1.jpg', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 3, 0),
(20, 'Chorrillana', 'Plato-chorrillana', 'Plato de exquisitas papas fritas y sobre ellas van distintos tipos de carne, cebolla y huevo frito.', 1590, 'fotos/productos/chorrillana1.png', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 4, 0),
(21, 'Plato churrasco', 'Plato-churrasco', 'Corte vacuno generalmente muy fino con mayonesa, tomate, palta y pan sandwich.', 1990, 'fotos/productos/ChurrascoItaliano1.png', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 4, 0),
(22, 'Mote con huesillo', 'Mote-con-huesillo', 'Bebida tradicional chilena sin alcohol, principalmente de la zona central del país, que se compone de una mezcla de jugo acaramelado de durazno, con mote de trigo y duraznos deshidratados.', 1500, 'fotos/productos/MoteConHuesillo1.jpg', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 2, 0),
(23, 'Coca Cola Lata', 'Coca-Cola-Lata', 'Bebida de 330 ml de Coca‐Cola contiene 35 gramos de azúcar, lo que equivale a 139 calorías (kcal) y un vaso de 250 ml contiene 27 g de azúcar, lo que equivale a 105 calorías (kcal).', 500, 'fotos/productos/CocaColaLata1.png', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 2, 0),
(24, 'Fanta Lata', 'Fanta-Lata', 'Bebida Fanta, refresco sabor naranja. 330 ml Agua carbonatada, 1% zumo de limón a partir de concentrado, correctores de acidez: E-300 y E-331, edulcorantes: E-950, E-952 y aspartamo, antioxidante: ácido ascórbico, conservador: E-202, estabilizantes: E-414 y E-445, aromas naturales de limón y otros aromas naturales y colorante: betacaroteno.', 500, 'fotos/productos/FantaLata1.jpg', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 2, 0),
(25, 'Sprite Lata', 'Sprite-Lata', 'Bebida gaseosa burbujeante en práctica presentación de lata de 350 ml. Su sabor limón-lima te brinda un vibrante y suave regocijo que despierta tus sentidos.', 500, 'fotos/productos/SpriteLata1.png', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 2, 0),
(26, 'Té', 'Refresco-te', 'Bebida 200 ml de agua caliente de las hojas y brotes de la planta. El sabor es fresco, ligeramente amargo y astringente; este gusto es agradable.', 500, 'fotos/productos/te1.jpg', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 2, 0),
(27, 'Café', 'Refresco-cafe', 'Bebida 200ml que se obtiene mediante el percolado de agua caliente a través de los granos tostados y molidos de los frutos de la planta del café.', 500, 'fotos/productos/cafe1.png', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 2, 0),
(28, 'Ensalada de choclo', 'ensalada-de-choclo', 'Ensalada de choclo con mayonesa revuelta, 1 porción pequeña.', 1990, 'fotos/productos/EnsaladaDeChoclo1.png', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 1, 0),
(29, 'Porotos granados', 'porotos-granados', 'Plato típico de la cocina campesina del centro-sur de Chile, el cual consiste en porotos cocidos con mazamorra o alternativamente pilco, cebolla, zapallo, tomate y ajo.', 1990, 'fotos/productos/PorotosGranados1.png', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 3, 0),
(30, 'Tomaticán', 'Plato-tomatican', 'Guiso originado de Chile, fusión de la gastronomía de los pueblos indígenas Mapuches. Consiste en un guiso con carne cortada en tiras, tomate, choclo, papas y cebolla.', 1990, 'fotos/productos/Tomaticán1.png', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 3, 0),
(31, 'Pescado frito', 'pescado-frito', 'Pescados pequeños y poco espinosos salmonete frito en aceite ', 4990, 'fotos/productos/PescadoFrito1.jpg', 10, 1, '2024-10-09 01:50:09.000000', '2024-10-09 01:50:09.000000', 5, 0),
(32, 'Empanada de mariscos', 'empanada-de-mariscos', 'La masa de pan o de hojaldre que se rellena con un guiso de mariscos se fríe a fuego lento para dar el mejor sabor posible.', 4990, 'fotos/productos/EmpanadaDeMarisco1.png', 10, 1, '2024-10-09 01:50:09.000000', '2024-12-13 07:50:27.310411', 6, 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tienda_productogaleria`
--

CREATE TABLE `tienda_productogaleria` (
  `id` bigint(20) NOT NULL,
  `image` varchar(255) NOT NULL,
  `producto_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `tienda_productogaleria`
--

INSERT INTO `tienda_productogaleria` (`id`, `image`, `producto_id`) VALUES
(1, 'tienda/productos/cazuelavacuno2.png', 1),
(2, 'tienda/productos/cazuelavacuno3.png', 1),
(5, 'tienda/productos/ceviche2_bgoHTw6.png', 3),
(6, 'tienda/productos/ceviche1.png', 3),
(7, 'tienda/productos/completo2.png', 4),
(8, 'tienda/productos/completo1.png', 4),
(9, 'tienda/productos/curanto2.png', 5),
(10, 'tienda/productos/curanto1.png', 5),
(11, 'tienda/productos/empanadapino1.png', 6),
(12, 'tienda/productos/empanadapino3.png', 6),
(13, 'tienda/productos/ensaladasurtida2.jpg', 7),
(14, 'tienda/productos/ensaladasurtida3.jpg', 7),
(15, 'tienda/productos/humita2.png', 8),
(16, 'tienda/productos/humita3.jpg', 8),
(19, 'tienda/productos/lechuga3_b2x9IJK.png', 10),
(20, 'tienda/productos/lechuga1_EMppZJ2.png', 10),
(21, 'tienda/productos/nugget3.png', 11),
(22, 'tienda/productos/nugget2.png', 11),
(23, 'tienda/productos/papas1.png', 12),
(24, 'tienda/productos/papas3.png', 12),
(25, 'tienda/productos/papasmayo2.jpg', 13),
(26, 'tienda/productos/papasmayo1.jpg', 13),
(27, 'tienda/productos/pollo3.jpg', 14),
(28, 'tienda/productos/pollo2.jpg', 14),
(29, 'tienda/productos/repollo1.jpg', 15),
(30, 'tienda/productos/repollo3.jpg', 15),
(31, 'tienda/productos/tomate1.jpg', 16),
(32, 'tienda/productos/tomate2.jpg', 16),
(33, 'tienda/productos/empanadadequeso2.jpg', 17),
(34, 'tienda/productos/empanadadequeso3.jpg', 17),
(35, 'tienda/productos/PastelDeChoclo2.png', 18),
(37, 'tienda/productos/PastelDeChoclo3.png', 18),
(38, 'tienda/productos/ChuletaConPure2.jpg', 19),
(39, 'tienda/productos/ChuletaConPure3.jpg', 19),
(40, 'tienda/productos/chorrillana2.jpg', 20),
(41, 'tienda/productos/chorrillana3.jpg', 20),
(42, 'tienda/productos/ChurrascoItaliano2.png', 21),
(43, 'tienda/productos/ChurrascoItaliano3.png', 21),
(44, 'tienda/productos/cafe2.png', 27),
(45, 'tienda/productos/cafe3.png', 27),
(46, 'tienda/productos/te2.jpg', 26),
(47, 'tienda/productos/te3.jpg', 26),
(48, 'tienda/productos/SpriteLata2.png', 25),
(49, 'tienda/productos/SpriteLata3.png', 25),
(50, 'tienda/productos/FantaLata2.jpg', 24),
(51, 'tienda/productos/FantaLata3.jpg', 24),
(52, 'tienda/productos/CocaColaLata2.png', 23),
(53, 'tienda/productos/CocaColaLata3.png', 23),
(54, 'tienda/productos/MoteConHuesillo2.jpg', 22),
(55, 'tienda/productos/MoteConHuesillo3.jpg', 22),
(56, 'tienda/productos/EnsaladaDeChoclo2.png', 28),
(57, 'tienda/productos/EnsaladaDeChoclo3.png', 28),
(58, 'tienda/productos/PorotosGranados2.png', 29),
(59, 'tienda/productos/PorotosGranados3.png', 29),
(60, 'tienda/productos/Tomaticán2.png', 30),
(61, 'tienda/productos/Tomaticán3.png', 30),
(62, 'tienda/productos/PescadoFrito2.jpg', 31),
(63, 'tienda/productos/PescadoFrito3.jpg', 31),
(64, 'tienda/productos/EmpanadaDeMarisco2.png', 32),
(65, 'tienda/productos/EmpanadaDeMarisco3.png', 32);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tienda_reseñarating`
--

CREATE TABLE `tienda_reseñarating` (
  `id` bigint(20) NOT NULL,
  `titulo` varchar(100) NOT NULL,
  `reseña` varchar(500) NOT NULL,
  `rating` double NOT NULL,
  `ip` varchar(20) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `producto_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `carrito_carrito`
--
ALTER TABLE `carrito_carrito`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `carrito_carritoitem`
--
ALTER TABLE `carrito_carritoitem`
  ADD PRIMARY KEY (`id`),
  ADD KEY `carrito_carritoitem_carro_id_11d68fdc_fk_carrito_carrito_id` (`carro_id`),
  ADD KEY `carrito_carritoitem_producto_id_16bca47d_fk_tienda_producto_id` (`producto_id`),
  ADD KEY `carrito_carritoitem_user_id_bb70ded7_fk_cuenta_cuenta_id` (`user_id`);

--
-- Indices de la tabla `categoria_categoria`
--
ALTER TABLE `categoria_categoria`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `categoria_nombre` (`categoria_nombre`),
  ADD UNIQUE KEY `slug` (`slug`);

--
-- Indices de la tabla `cuenta_cuenta`
--
ALTER TABLE `cuenta_cuenta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `cuenta_cuenta_groups`
--
ALTER TABLE `cuenta_cuenta_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cuenta_cuenta_groups_cuenta_id_group_id_f9701e8e_uniq` (`cuenta_id`,`group_id`),
  ADD KEY `cuenta_cuenta_groups_group_id_86317fd0_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `cuenta_cuenta_user_permissions`
--
ALTER TABLE `cuenta_cuenta_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `cuenta_cuenta_user_permi_cuenta_id_permission_id_60bc2f23_uniq` (`cuenta_id`,`permission_id`),
  ADD KEY `cuenta_cuenta_user_p_permission_id_81d71b97_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `cuenta_usuarioperfil`
--
ALTER TABLE `cuenta_usuarioperfil`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_cuenta_cuenta_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `pedido_pago`
--
ALTER TABLE `pedido_pago`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pedido_pago_user_id_14e3b44c_fk_cuenta_cuenta_id` (`user_id`);

--
-- Indices de la tabla `pedido_pedido`
--
ALTER TABLE `pedido_pedido`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pedido_pedido_pago_id_4854aead_fk_pedido_pago_id` (`pago_id`),
  ADD KEY `pedido_pedido_user_id_16627dad_fk_cuenta_cuenta_id` (`user_id`);

--
-- Indices de la tabla `pedido_pedidoproducto`
--
ALTER TABLE `pedido_pedidoproducto`
  ADD PRIMARY KEY (`id`),
  ADD KEY `pedido_pedidoproducto_pago_id_63ce78e4_fk_pedido_pago_id` (`pago_id`),
  ADD KEY `pedido_pedidoproducto_pedido_id_82f96461_fk_pedido_pedido_id` (`pedido_id`),
  ADD KEY `pedido_pedidoproducto_producto_id_68300456_fk_tienda_producto_id` (`producto_id`),
  ADD KEY `pedido_pedidoproducto_user_id_3c37548b_fk_cuenta_cuenta_id` (`user_id`);

--
-- Indices de la tabla `reservaciones_reserva`
--
ALTER TABLE `reservaciones_reserva`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo_reserva` (`codigo_reserva`);

--
-- Indices de la tabla `suscripcion_suscripcion`
--
ALTER TABLE `suscripcion_suscripcion`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indices de la tabla `tienda_producto`
--
ALTER TABLE `tienda_producto`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `producto_nombre` (`producto_nombre`),
  ADD UNIQUE KEY `slug` (`slug`),
  ADD KEY `tienda_producto_categoria_id_6dc179b4_fk_categoria_categoria_id` (`categoria_id`);

--
-- Indices de la tabla `tienda_productogaleria`
--
ALTER TABLE `tienda_productogaleria`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tienda_productogaler_producto_id_d2054f29_fk_tienda_pr` (`producto_id`);

--
-- Indices de la tabla `tienda_reseñarating`
--
ALTER TABLE `tienda_reseñarating`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tienda_revisarrating_producto_id_7ba26d55_fk_tienda_producto_id` (`producto_id`),
  ADD KEY `tienda_revisarrating_user_id_ea94c6c4_fk_cuenta_cuenta_id` (`user_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT de la tabla `carrito_carrito`
--
ALTER TABLE `carrito_carrito`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `carrito_carritoitem`
--
ALTER TABLE `carrito_carritoitem`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT de la tabla `categoria_categoria`
--
ALTER TABLE `categoria_categoria`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `cuenta_cuenta`
--
ALTER TABLE `cuenta_cuenta`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `cuenta_cuenta_groups`
--
ALTER TABLE `cuenta_cuenta_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cuenta_cuenta_user_permissions`
--
ALTER TABLE `cuenta_cuenta_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `cuenta_usuarioperfil`
--
ALTER TABLE `cuenta_usuarioperfil`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;

--
-- AUTO_INCREMENT de la tabla `pedido_pago`
--
ALTER TABLE `pedido_pago`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `pedido_pedido`
--
ALTER TABLE `pedido_pedido`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `pedido_pedidoproducto`
--
ALTER TABLE `pedido_pedidoproducto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT de la tabla `reservaciones_reserva`
--
ALTER TABLE `reservaciones_reserva`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `suscripcion_suscripcion`
--
ALTER TABLE `suscripcion_suscripcion`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `tienda_producto`
--
ALTER TABLE `tienda_producto`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `tienda_productogaleria`
--
ALTER TABLE `tienda_productogaleria`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT de la tabla `tienda_reseñarating`
--
ALTER TABLE `tienda_reseñarating`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `carrito_carritoitem`
--
ALTER TABLE `carrito_carritoitem`
  ADD CONSTRAINT `carrito_carritoitem_carro_id_11d68fdc_fk_carrito_carrito_id` FOREIGN KEY (`carro_id`) REFERENCES `carrito_carrito` (`id`),
  ADD CONSTRAINT `carrito_carritoitem_producto_id_16bca47d_fk_tienda_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `tienda_producto` (`id`),
  ADD CONSTRAINT `carrito_carritoitem_user_id_bb70ded7_fk_cuenta_cuenta_id` FOREIGN KEY (`user_id`) REFERENCES `cuenta_cuenta` (`id`);

--
-- Filtros para la tabla `cuenta_cuenta_groups`
--
ALTER TABLE `cuenta_cuenta_groups`
  ADD CONSTRAINT `cuenta_cuenta_groups_cuenta_id_2f535e0f_fk_cuenta_cuenta_id` FOREIGN KEY (`cuenta_id`) REFERENCES `cuenta_cuenta` (`id`),
  ADD CONSTRAINT `cuenta_cuenta_groups_group_id_86317fd0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `cuenta_cuenta_user_permissions`
--
ALTER TABLE `cuenta_cuenta_user_permissions`
  ADD CONSTRAINT `cuenta_cuenta_user_p_cuenta_id_feea7ba4_fk_cuenta_cu` FOREIGN KEY (`cuenta_id`) REFERENCES `cuenta_cuenta` (`id`),
  ADD CONSTRAINT `cuenta_cuenta_user_p_permission_id_81d71b97_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- Filtros para la tabla `cuenta_usuarioperfil`
--
ALTER TABLE `cuenta_usuarioperfil`
  ADD CONSTRAINT `cuenta_usuarioperfil_user_id_7e3f0d79_fk_cuenta_cuenta_id` FOREIGN KEY (`user_id`) REFERENCES `cuenta_cuenta` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_cuenta_cuenta_id` FOREIGN KEY (`user_id`) REFERENCES `cuenta_cuenta` (`id`);

--
-- Filtros para la tabla `pedido_pago`
--
ALTER TABLE `pedido_pago`
  ADD CONSTRAINT `pedido_pago_user_id_14e3b44c_fk_cuenta_cuenta_id` FOREIGN KEY (`user_id`) REFERENCES `cuenta_cuenta` (`id`);

--
-- Filtros para la tabla `pedido_pedido`
--
ALTER TABLE `pedido_pedido`
  ADD CONSTRAINT `pedido_pedido_pago_id_4854aead_fk_pedido_pago_id` FOREIGN KEY (`pago_id`) REFERENCES `pedido_pago` (`id`),
  ADD CONSTRAINT `pedido_pedido_user_id_16627dad_fk_cuenta_cuenta_id` FOREIGN KEY (`user_id`) REFERENCES `cuenta_cuenta` (`id`);

--
-- Filtros para la tabla `pedido_pedidoproducto`
--
ALTER TABLE `pedido_pedidoproducto`
  ADD CONSTRAINT `pedido_pedidoproducto_pago_id_63ce78e4_fk_pedido_pago_id` FOREIGN KEY (`pago_id`) REFERENCES `pedido_pago` (`id`),
  ADD CONSTRAINT `pedido_pedidoproducto_pedido_id_82f96461_fk_pedido_pedido_id` FOREIGN KEY (`pedido_id`) REFERENCES `pedido_pedido` (`id`),
  ADD CONSTRAINT `pedido_pedidoproducto_producto_id_68300456_fk_tienda_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `tienda_producto` (`id`),
  ADD CONSTRAINT `pedido_pedidoproducto_user_id_3c37548b_fk_cuenta_cuenta_id` FOREIGN KEY (`user_id`) REFERENCES `cuenta_cuenta` (`id`);

--
-- Filtros para la tabla `tienda_producto`
--
ALTER TABLE `tienda_producto`
  ADD CONSTRAINT `tienda_producto_categoria_id_6dc179b4_fk_categoria_categoria_id` FOREIGN KEY (`categoria_id`) REFERENCES `categoria_categoria` (`id`);

--
-- Filtros para la tabla `tienda_productogaleria`
--
ALTER TABLE `tienda_productogaleria`
  ADD CONSTRAINT `tienda_productogaler_producto_id_d2054f29_fk_tienda_pr` FOREIGN KEY (`producto_id`) REFERENCES `tienda_producto` (`id`);

--
-- Filtros para la tabla `tienda_reseñarating`
--
ALTER TABLE `tienda_reseñarating`
  ADD CONSTRAINT `tienda_revisarrating_producto_id_7ba26d55_fk_tienda_producto_id` FOREIGN KEY (`producto_id`) REFERENCES `tienda_producto` (`id`),
  ADD CONSTRAINT `tienda_revisarrating_user_id_ea94c6c4_fk_cuenta_cuenta_id` FOREIGN KEY (`user_id`) REFERENCES `cuenta_cuenta` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
