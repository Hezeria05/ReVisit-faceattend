-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 07, 2024 at 10:13 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `visitor_attendance`
--

-- --------------------------------------------------------

--
-- Table structure for table `security_admin`
--

CREATE TABLE `security_admin` (
  `sec_id` int(11) NOT NULL,
  `sec_username` varchar(50) NOT NULL,
  `sec_name` varchar(75) NOT NULL,
  `sec_password` varchar(16) NOT NULL,
  `shift_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `security_shift`
--

CREATE TABLE `security_shift` (
  `shift_id` int(11) NOT NULL,
  `shift_time` time NOT NULL,
  `description` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `visitor_data`
--

CREATE TABLE `visitor_data` (
  `visit_id` int(11) NOT NULL,
  `visit_name` varchar(75) NOT NULL,
  `log_day` date NOT NULL,
  `login_time` time NOT NULL,
  `logout_time` time NOT NULL,
  `sec_id` int(11) NOT NULL,
  `shift_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `security_admin`
--
ALTER TABLE `security_admin`
  ADD PRIMARY KEY (`sec_id`),
  ADD KEY `shift_id` (`shift_id`);

--
-- Indexes for table `security_shift`
--
ALTER TABLE `security_shift`
  ADD PRIMARY KEY (`shift_id`);

--
-- Indexes for table `visitor_data`
--
ALTER TABLE `visitor_data`
  ADD PRIMARY KEY (`visit_id`),
  ADD KEY `sec_id` (`sec_id`),
  ADD KEY `shift_id` (`shift_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `security_admin`
--
ALTER TABLE `security_admin`
  MODIFY `sec_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `visitor_data`
--
ALTER TABLE `visitor_data`
  MODIFY `visit_id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `security_admin`
--
ALTER TABLE `security_admin`
  ADD CONSTRAINT `security_admin_ibfk_1` FOREIGN KEY (`shift_id`) REFERENCES `security_shift` (`shift_id`);

--
-- Constraints for table `visitor_data`
--
ALTER TABLE `visitor_data`
  ADD CONSTRAINT `visitor_data_ibfk_1` FOREIGN KEY (`sec_id`) REFERENCES `security_admin` (`sec_id`),
  ADD CONSTRAINT `visitor_data_ibfk_2` FOREIGN KEY (`shift_id`) REFERENCES `security_shift` (`shift_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
