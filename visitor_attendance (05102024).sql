-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 10, 2024 at 02:48 PM
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
-- Table structure for table `resident_data`
--

CREATE TABLE `resident_data` (
  `res_id` int(11) NOT NULL,
  `res_name` varchar(50) NOT NULL,
  `res_address` varchar(250) NOT NULL,
  `res_phonenumber` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `resident_data`
--

INSERT INTO `resident_data` (`res_id`, `res_name`, `res_address`, `res_phonenumber`) VALUES
(1, 'John Doe', 'BLK 1 LOT 1 Phase 1', '09123456781'),
(2, 'Jane Smith', 'BLK 1 LOT 2 Phase 1', '09234567890'),
(3, 'Alice Johnson', 'BLK 1 LOT 3 Phase 1', '09345678901'),
(4, 'Michael Brown', 'BLK 1 LOT 4 Phase 1', '09456789012'),
(5, 'Chloe Davis', 'BLK 1 LOT 5 Phase 1', '09567890123'),
(6, 'Lucas Miller', 'BLK 2 LOT 1 Phase 1', '09678901234'),
(7, 'Emma Wilson', 'BLK 2 LOT 2 Phase 1', '09789012345'),
(8, 'Oliver Moore', 'BLK 2 LOT 3 Phase 1', '09890123456'),
(9, 'Sophia Young', 'BLK 2 LOT 4 Phase 1', '09901234567'),
(10, 'Ethan Johnson', 'BLK 2 LOT 5 Phase 1', '09012345678'),
(11, 'Mia Williams', 'BLK 3 LOT 1 Phase 2', '09123456780'),
(12, 'Noah Jones', 'BLK 3 LOT 2 Phase 2', '09234567891'),
(13, 'Isabella Taylor', 'BLK 3 LOT 3 Phase 2', '09345678902'),
(14, 'William White', 'BLK 3 LOT 4 Phase 2', '09456789013'),
(15, 'Ava Thompson', 'BLK 3 LOT 5 Phase 2', '09567890124'),
(16, 'Matthew Harris', 'BLK 4 LOT 1 Phase 2', '09678901235'),
(17, 'Amelia Martin', 'BLK 4 LOT 2 Phase 2', '09789012346'),
(18, 'James Lee', 'BLK 4 LOT 3 Phase 2', '09890123457'),
(19, 'Charlotte Hall', 'BLK 4 LOT 4 Phase 2', '09901234568'),
(20, 'Alexander Allen', 'BLK 4 LOT 5 Phase 2', '09012345679'),
(21, 'Harper Young', 'BLK 5 LOT 1 Phase 3', '09123456781'),
(22, 'Elijah Scott', 'BLK 5 LOT 2 Phase 3', '09234567892'),
(23, 'Isabelle Edwards', 'BLK 5 LOT 3 Phase 3', '09345678903'),
(24, 'Jack Wright', 'BLK 5 LOT 4 Phase 3', '09456789014'),
(25, 'Lily King', 'BLK 5 LOT 5 Phase 3', '09567890125'),
(26, 'Benjamin Moore', 'BLK 6 LOT 1 Phase 3', '09678901236'),
(27, 'Zoe Miller', 'BLK 6 LOT 2 Phase 3', '09789012347'),
(28, 'Logan Brown', 'BLK 6 LOT 3 Phase 3', '09890123458'),
(29, 'Grace Davis', 'BLK 6 LOT 4 Phase 3', '09901234569'),
(30, 'Ryan Wilson', 'BLK 6 LOT 5 Phase 3', '09012345670');

-- --------------------------------------------------------

--
-- Table structure for table `security_admin`
--

CREATE TABLE `security_admin` (
  `sec_id` int(11) NOT NULL,
  `sec_username` varchar(50) NOT NULL,
  `sec_name` varchar(75) NOT NULL,
  `sec_password` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `security_admin`
--

INSERT INTO `security_admin` (`sec_id`, `sec_username`, `sec_name`, `sec_password`) VALUES
(13, 'Security1', 'Hannah Santos', '12345'),
(19, 'Security2', 'Wayne Tolopia', '12345'),
(21, 'Security4', 'Kaye Alcantara', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `visitor_data`
--

CREATE TABLE `visitor_data` (
  `visit_id` int(11) NOT NULL,
  `visit_name` varchar(75) NOT NULL,
  `log_purpose` text NOT NULL,
  `log_day` date NOT NULL,
  `log_stat` tinyint(1) NOT NULL,
  `login_time` time DEFAULT NULL,
  `logout_time` time DEFAULT NULL,
  `sec_id` int(11) NOT NULL,
  `res_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `visitor_data`
--

INSERT INTO `visitor_data` (`visit_id`, `visit_name`, `log_purpose`, `log_day`, `log_stat`, `login_time`, `logout_time`, `sec_id`, `res_id`) VALUES
(74, 'HANNAH', 'try out 1', '2024-05-10', 0, '20:33:57', '20:34:04', 13, 5),
(75, 'HANNAH', '1', '2024-05-10', 0, '20:35:58', '20:36:02', 13, 1),
(76, 'HANNAH', '1', '2024-05-10', 0, '20:36:11', '20:36:14', 13, 1),
(77, 'HANNAH', '1', '2024-05-10', 0, '20:37:14', '20:37:20', 13, 1),
(78, 'HANNAH', '2', '2024-05-10', 0, '20:37:25', '20:37:30', 13, 1),
(79, 'HANNAH', '1', '2024-05-10', 0, '20:38:56', '20:39:00', 13, 1),
(80, 'HANNAH', '2', '2024-05-10', 0, '20:39:12', '20:39:17', 13, 1),
(81, 'HANNAH', '1', '2024-05-10', 0, '20:45:03', '20:45:08', 13, 1),
(82, 'HANNAH', '1', '2024-05-10', 0, '20:46:52', '20:46:57', 13, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `resident_data`
--
ALTER TABLE `resident_data`
  ADD PRIMARY KEY (`res_id`);

--
-- Indexes for table `security_admin`
--
ALTER TABLE `security_admin`
  ADD PRIMARY KEY (`sec_id`);

--
-- Indexes for table `visitor_data`
--
ALTER TABLE `visitor_data`
  ADD PRIMARY KEY (`visit_id`),
  ADD KEY `visitor_sec_ibfk_1` (`sec_id`),
  ADD KEY `visitor_res_ibfk_3` (`res_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `resident_data`
--
ALTER TABLE `resident_data`
  MODIFY `res_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=31;

--
-- AUTO_INCREMENT for table `security_admin`
--
ALTER TABLE `security_admin`
  MODIFY `sec_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `visitor_data`
--
ALTER TABLE `visitor_data`
  MODIFY `visit_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `visitor_data`
--
ALTER TABLE `visitor_data`
  ADD CONSTRAINT `visitor_res_ibfk_3` FOREIGN KEY (`res_id`) REFERENCES `resident_data` (`res_id`),
  ADD CONSTRAINT `visitor_sec_ibfk_1` FOREIGN KEY (`sec_id`) REFERENCES `security_admin` (`sec_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
