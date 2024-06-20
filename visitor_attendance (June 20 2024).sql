-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 20, 2024 at 03:19 PM
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
(32, 'John Doe', 'Block 1 Lot 1 Phase 1 Hydrogen', '09123456780'),
(33, 'Jane Smith', 'Block 1 Lot 2 Phase 1 Helium', '09123456781'),
(34, 'Alice Johnson', 'Block 1 Lot 3 Phase 1 Lithium', '09123456782'),
(35, 'Michael Brown', 'Block 1 Lot 4 Phase 1 Beryllium', '09123456783'),
(36, 'Chloe Davis', 'Block 1 Lot 5 Phase 1 Boron', '09123456784'),
(37, 'Lucas Miller', 'Block 1 Lot 6 Phase 1 Carbon', '09123456785'),
(38, 'Emma Wilson', 'Block 1 Lot 7 Phase 1 Nitrogen', '09123456786'),
(39, 'Oliver Moore', 'Block 1 Lot 8 Phase 1 Oxygen', '09123456787'),
(40, 'Sophia Young', 'Block 1 Lot 9 Phase 1 Fluorine', '09123456788'),
(41, 'Ethan Johnson', 'Block 1 Lot 10 Phase 1 Neon', '09123456789'),
(42, 'Mia Williams', 'Block 1 Lot 11 Phase 1 Hydrogen', '09123456790'),
(43, 'Noah Jones', 'Block 1 Lot 12 Phase 1 Helium', '09123456791'),
(44, 'Isabella Taylor', 'Block 1 Lot 13 Phase 1 Lithium', '09123456792'),
(45, 'William White', 'Block 1 Lot 14 Phase 1 Beryllium', '09123456793'),
(46, 'Ava Thompson', 'Block 1 Lot 15 Phase 1 Boron', '09123456794'),
(47, 'Matthew Harris', 'Block 1 Lot 16 Phase 1 Carbon', '09123456795'),
(48, 'Amelia Martin', 'Block 1 Lot 17 Phase 1 Nitrogen', '09123456796'),
(49, 'James Lee', 'Block 1 Lot 18 Phase 1 Oxygen', '09123456797'),
(50, 'Charlotte Hall', 'Block 2 Lot 1 Phase 2 Fluorine', '09123456798'),
(51, 'Alexander Allen', 'Block 2 Lot 2 Phase 2 Neon', '09123456799'),
(52, 'Harper Young', 'Block 2 Lot 3 Phase 2 Hydrogen', '09123456800'),
(53, 'Elijah Scott', 'Block 2 Lot 4 Phase 2 Helium', '09123456801'),
(54, 'Isabelle Edwards', 'Block 2 Lot 5 Phase 2 Lithium', '09123456802'),
(55, 'Jack Wright', 'Block 2 Lot 6 Phase 2 Beryllium', '09123456803'),
(56, 'Lily King', 'Block 2 Lot 7 Phase 2 Boron', '09123456804'),
(57, 'Benjamin Moore', 'Block 2 Lot 8 Phase 2 Carbon', '09123456805'),
(58, 'Zoe Miller', 'Block 2 Lot 9 Phase 2 Nitrogen', '09123456806'),
(59, 'Logan Brown', 'Block 2 Lot 10 Phase 2 Oxygen', '09123456807'),
(60, 'Grace Davis', 'Block 3 Lot 1 Phase 1 Fluorine', '09123456808'),
(61, 'Ryan Wilson', 'Block 3 Lot 2 Phase 1 Neon', '09123456809'),
(62, 'Jackson Wong', 'Block 3 Lot 3 Phase 1 Hydrogen', '09123456810'),
(63, 'Ella Thompson', 'Block 3 Lot 4 Phase 1 Helium', '09123456811'),
(64, 'Henry Anderson', 'Block 3 Lot 5 Phase 1 Lithium', '09123456812'),
(65, 'Scarlett Lee', 'Block 3 Lot 6 Phase 1 Beryllium', '09123456813'),
(66, 'David Martin', 'Block 3 Lot 7 Phase 1 Boron', '09123456814'),
(67, 'Victoria Clark', 'Block 3 Lot 8 Phase 1 Carbon', '09123456815'),
(68, 'Daniel Lewis', 'Block 3 Lot 9 Phase 1 Nitrogen', '09123456816'),
(69, 'Abigail Walker', 'Block 3 Lot 10 Phase 1 Oxygen', '09123456817'),
(70, 'Mason Young', 'Block 3 Lot 11 Phase 1 Fluorine', '09123456818'),
(71, 'Hannah Hill', 'Block 3 Lot 12 Phase 1 Neon', '09123456819'),
(72, 'Jacob Martinez', 'Block 3 Lot 13 Phase 1 Hydrogen', '09123456820'),
(73, 'Sofia Wright', 'Block 3 Lot 14 Phase 1 Helium', '09123456821'),
(74, 'William Robinson', 'Block 3 Lot 15 Phase 1 Lithium', '09123456822'),
(75, 'Grace Mitchell', 'Block 3 Lot 16 Phase 1 Beryllium', '09123456823'),
(76, 'James Harris', 'Block 3 Lot 17 Phase 1 Boron', '09123456824'),
(77, 'Olivia Carter', 'Block 3 Lot 18 Phase 1 Carbon', '09123456825');

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
(24, 'Security1', 'Juan Dela Cruz', '12345678'),
(26, 'Security2', 'Mike Reyes', '12345678'),
(31, 'Security3', 'Hannah Grace', '12345678');

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
  MODIFY `res_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=78;

--
-- AUTO_INCREMENT for table `security_admin`
--
ALTER TABLE `security_admin`
  MODIFY `sec_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `visitor_data`
--
ALTER TABLE `visitor_data`
  MODIFY `visit_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=140;

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
