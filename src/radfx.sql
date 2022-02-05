-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 05, 2022 at 02:37 AM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `radfx`
--

-- --------------------------------------------------------

--
-- Stand-in structure for view `1`
-- (See below for the actual view)
--
CREATE TABLE `1` (
`permission_id` varchar(4)
,`name` varchar(50)
,`description` varchar(150)
);

-- --------------------------------------------------------

--
-- Table structure for table `affiliation`
--

CREATE TABLE `affiliation` (
  `affiliation_id` varchar(4) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(150) DEFAULT NULL,
  `primary_email` varchar(100) DEFAULT NULL,
  `primary_phone` varchar(15) DEFAULT NULL,
  `secondary_email` varchar(100) DEFAULT NULL,
  `secondary_phone` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auto_email`
--

CREATE TABLE `auto_email` (
  `auto_email_id` int(4) NOT NULL,
  `headder` varchar(100) NOT NULL,
  `content` varchar(2500) DEFAULT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `request_id` int(10) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `facility`
--

CREATE TABLE `facility` (
  `facility_id` varchar(4) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `affiliation_id` varchar(4) DEFAULT NULL,
  `operation_hours` varchar(100) DEFAULT NULL,
  `switching_times` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `permission`
--

CREATE TABLE `permission` (
  `permission_id` varchar(4) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `description` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `permission`
--

INSERT INTO `permission` (`permission_id`, `name`, `description`) VALUES
('0', 'unathuroized', 'A user who has not been authorized as a tester by admin'),
('1', 'tester', 'A user who has authorized as a tester by admin');

-- --------------------------------------------------------

--
-- Table structure for table `purpose`
--

CREATE TABLE `purpose` (
  `purpose_id` varchar(4) NOT NULL,
  `purpose_of_test` varchar(500) DEFAULT NULL,
  `description` varchar(2500) DEFAULT NULL,
  `energy_level` varchar(25) DEFAULT NULL,
  `requested_ions` varchar(50) DEFAULT NULL,
  `vacume` tinyint(1) DEFAULT 0,
  `public` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `request`
--

CREATE TABLE `request` (
  `request_id` int(10) NOT NULL,
  `total_hours` int(5) DEFAULT NULL,
  `facility_id` varchar(4) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  `earliest_date` datetime DEFAULT NULL,
  `purpose_id` varchar(4) DEFAULT NULL,
  `approved` tinyint(1) DEFAULT NULL,
  `retracted` tinyint(1) DEFAULT 0,
  `time_used` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `role`
--

CREATE TABLE `role` (
  `role_id` varchar(4) NOT NULL,
  `name` varchar(50) DEFAULT NULL,
  `permission_id` varchar(4) NOT NULL DEFAULT '1',
  `description` varchar(150) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `disabled_at` datetime DEFAULT NULL,
  `disabled` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `role`
--

INSERT INTO `role` (`role_id`, `name`, `permission_id`, `description`, `created_at`, `updated_at`, `disabled_at`, `disabled`) VALUES
('0', 'tester', '1', 'A user who has been authorized as a tester by admin', NULL, NULL, NULL, 0);

-- --------------------------------------------------------

--
-- Table structure for table `scheduled`
--

CREATE TABLE `scheduled` (
  `scheduled_id` int(5) NOT NULL,
  `request_id` int(10) DEFAULT NULL,
  `time_scheduled` int(5) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `public` tinyint(1) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

CREATE TABLE `user` (
  `user_id` int(11) NOT NULL,
  `affiliation_id` varchar(4) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `phone` varchar(15) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `created_at` datetime DEFAULT current_timestamp(),
  `disabled_at` datetime DEFAULT NULL,
  `role_id` varchar(4) NOT NULL DEFAULT '1',
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`user_id`, `affiliation_id`, `first_name`, `last_name`, `phone`, `email`, `created_at`, `disabled_at`, `role_id`, `password`) VALUES
(30, NULL, 'eeee', 'eeee', NULL, 'Radfxproject@hotmaail.com', '2022-02-04 19:34:39', NULL, '0', '$2b$12$WeaxhWva7UYgWly3wzD.rOh0ylqLcDqtncauBAqDSOlxnkZ6ey/N2'),
(31, NULL, 'eeee', 'eeee', NULL, 'Radfxproject@hotmail.com', '2022-02-04 19:59:29', NULL, '0', '$2b$12$XTp9i.tB4vWwp2ZnginCW.nbmIKxvkCNEfkZgl51ebpu4Hp57ZUSK');

-- --------------------------------------------------------

--
-- Structure for view `1`
--
DROP TABLE IF EXISTS `1`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `1`  AS SELECT `permission`.`permission_id` AS `permission_id`, `permission`.`name` AS `name`, `permission`.`description` AS `description` FROM `permission` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `affiliation`
--
ALTER TABLE `affiliation`
  ADD PRIMARY KEY (`affiliation_id`);

--
-- Indexes for table `auto_email`
--
ALTER TABLE `auto_email`
  ADD PRIMARY KEY (`auto_email_id`),
  ADD KEY `auto_email_FK` (`request_id`),
  ADD KEY `auto_email_FK_1` (`user_id`);

--
-- Indexes for table `facility`
--
ALTER TABLE `facility`
  ADD PRIMARY KEY (`facility_id`),
  ADD KEY `facility_FK` (`affiliation_id`);

--
-- Indexes for table `permission`
--
ALTER TABLE `permission`
  ADD PRIMARY KEY (`permission_id`);

--
-- Indexes for table `purpose`
--
ALTER TABLE `purpose`
  ADD PRIMARY KEY (`purpose_id`);

--
-- Indexes for table `request`
--
ALTER TABLE `request`
  ADD PRIMARY KEY (`request_id`),
  ADD KEY `request_FK` (`user_id`),
  ADD KEY `request_FK_1` (`facility_id`),
  ADD KEY `request_FK_2` (`purpose_id`);

--
-- Indexes for table `role`
--
ALTER TABLE `role`
  ADD PRIMARY KEY (`role_id`),
  ADD KEY `role_FK` (`permission_id`);

--
-- Indexes for table `scheduled`
--
ALTER TABLE `scheduled`
  ADD PRIMARY KEY (`scheduled_id`),
  ADD KEY `scheduled_FK` (`request_id`);

--
-- Indexes for table `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `user_FK` (`role_id`),
  ADD KEY `user_FK_1` (`affiliation_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auto_email`
--
ALTER TABLE `auto_email`
  MODIFY `auto_email_id` int(4) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `request`
--
ALTER TABLE `request`
  MODIFY `request_id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `scheduled`
--
ALTER TABLE `scheduled`
  MODIFY `scheduled_id` int(5) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user`
--
ALTER TABLE `user`
  MODIFY `user_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auto_email`
--
ALTER TABLE `auto_email`
  ADD CONSTRAINT `auto_email_FK` FOREIGN KEY (`request_id`) REFERENCES `request` (`request_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `auto_email_FK_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `facility`
--
ALTER TABLE `facility`
  ADD CONSTRAINT `facility_FK` FOREIGN KEY (`affiliation_id`) REFERENCES `affiliation` (`affiliation_id`) ON UPDATE CASCADE;

--
-- Constraints for table `request`
--
ALTER TABLE `request`
  ADD CONSTRAINT `request_FK` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `request_FK_1` FOREIGN KEY (`facility_id`) REFERENCES `facility` (`facility_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `request_FK_2` FOREIGN KEY (`purpose_id`) REFERENCES `purpose` (`purpose_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `role`
--
ALTER TABLE `role`
  ADD CONSTRAINT `role_FK` FOREIGN KEY (`permission_id`) REFERENCES `permission` (`permission_id`) ON UPDATE CASCADE;

--
-- Constraints for table `scheduled`
--
ALTER TABLE `scheduled`
  ADD CONSTRAINT `scheduled_FK` FOREIGN KEY (`request_id`) REFERENCES `request` (`request_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user`
--
ALTER TABLE `user`
  ADD CONSTRAINT `user_FK` FOREIGN KEY (`role_id`) REFERENCES `role` (`role_id`) ON UPDATE CASCADE,
  ADD CONSTRAINT `user_FK_1` FOREIGN KEY (`affiliation_id`) REFERENCES `affiliation` (`affiliation_id`) ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
