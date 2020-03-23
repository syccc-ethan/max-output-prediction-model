/*
Navicat MySQL Data Transfer

Source Server         : wqw_1
Source Server Version : 50525
Source Host           : localhost:3306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 50525
File Encoding         : 65001

Date: 2018-07-02 20:08:25
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for dz
-- ----------------------------
DROP TABLE IF EXISTS `dz`;
CREATE TABLE `dz` (
  `SJC` datetime NOT NULL COMMENT '时间戳',
  `GRGH` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `LJGH` varchar(20) COLLATE utf8_bin DEFAULT NULL,
  `DZ` varchar(255) COLLATE utf8_bin DEFAULT NULL,
  `FLAG` varchar(20) COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of dz
-- ----------------------------
INSERT INTO `dz` VALUES ('2018-06-23 07:32:57', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-23 07:42:02', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-23 08:33:06', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-23 08:43:08', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-23 09:33:12', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-23 09:43:14', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-23 10:33:18', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-23 10:43:20', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-23 11:33:53', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-23 11:33:55', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-23 12:33:59', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-23 12:34:01', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-23 13:34:05', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-23 13:34:06', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-23 14:34:10', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-23 14:34:12', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-24 07:32:57', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-24 07:42:02', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-24 08:33:06', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-24 08:43:08', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-24 09:33:12', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-24 09:43:14', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-24 10:33:18', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-24 10:43:20', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-24 11:33:53', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-24 11:33:55', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-24 12:33:59', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-24 12:34:01', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-24 13:34:05', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-24 13:34:06', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-24 14:34:10', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-24 14:34:12', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-25 07:32:57', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-25 07:42:02', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-25 08:33:06', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-25 08:43:08', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-25 09:33:12', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-25 09:43:14', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-25 10:33:18', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-25 10:43:20', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-25 11:33:53', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-25 11:33:55', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-25 12:33:59', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-25 12:34:01', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-25 13:34:05', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-25 13:34:06', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-25 14:34:10', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-25 14:34:12', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-26 07:32:57', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-26 07:42:02', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-26 08:33:06', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-26 08:43:08', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-26 09:33:12', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-26 09:43:14', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-26 10:33:18', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-26 10:43:20', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-26 11:33:53', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-26 11:33:55', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-26 12:33:59', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-26 12:34:01', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-26 13:34:05', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-26 13:34:06', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-26 14:34:10', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-26 14:34:12', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-27 07:32:57', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-27 07:42:02', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-27 08:33:06', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-27 08:43:08', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-27 09:33:12', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-27 09:43:14', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-27 10:33:18', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-27 10:43:20', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-27 11:33:53', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-27 11:33:55', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-27 12:33:59', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-27 12:34:01', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-27 13:34:05', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-27 13:34:06', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-27 14:34:10', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-27 14:34:12', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-28 06:32:57', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-28 07:42:02', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-28 08:33:06', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-28 08:43:08', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-28 09:33:12', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-28 09:43:14', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-28 10:33:18', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-28 10:43:20', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-28 11:33:53', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-28 11:33:55', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-28 12:33:59', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-28 12:34:01', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-28 13:34:05', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-28 13:34:06', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-28 14:34:10', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-28 14:34:12', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-29 07:32:57', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-29 07:42:02', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-29 08:33:06', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-29 08:43:08', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-29 09:33:12', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-29 09:43:14', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-29 10:33:18', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-29 10:43:20', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-29 11:33:53', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-29 11:33:55', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-29 12:33:59', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-29 12:34:01', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-29 13:34:05', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-29 13:34:06', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-29 14:34:10', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-29 14:34:12', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-30 07:32:57', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-30 07:42:02', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-30 08:33:06', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-30 08:43:08', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-30 09:33:12', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-30 09:43:14', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-30 10:33:18', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-30 10:43:20', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-06-30 11:33:53', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-06-30 11:33:55', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-06-30 12:33:59', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-06-30 12:34:01', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-06-30 13:34:05', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-06-30 13:34:06', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-06-30 14:34:10', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-06-30 14:34:12', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-07-01 07:32:57', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-07-01 07:42:02', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-07-01 08:33:06', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-07-01 08:43:08', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-07-01 09:33:12', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-07-01 09:43:14', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-07-01 10:33:18', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-07-01 10:43:20', '1A', '0A', 'action6', 'end');
INSERT INTO `dz` VALUES ('2018-07-01 11:33:53', '1A', '0A', 'action4', 'start');
INSERT INTO `dz` VALUES ('2018-07-01 11:33:55', '1A', '0A', 'action4', 'end');
INSERT INTO `dz` VALUES ('2018-07-01 12:33:59', '1A', '0A', 'action3', 'start');
INSERT INTO `dz` VALUES ('2018-07-01 12:34:01', '1A', '0A', 'action3', 'end');
INSERT INTO `dz` VALUES ('2018-07-01 13:34:05', '1A', '0A', 'action5', 'start');
INSERT INTO `dz` VALUES ('2018-07-01 13:34:06', '1A', '0A', 'action5', 'end');
INSERT INTO `dz` VALUES ('2018-07-01 14:34:10', '1A', '0A', 'action6', 'start');
INSERT INTO `dz` VALUES ('2018-07-01 14:44:12', '1A', '0A', 'action6', 'end');

-- ----------------------------
-- Table structure for loss
-- ----------------------------
DROP TABLE IF EXISTS `loss`;
CREATE TABLE `loss` (
  `SJ` date NOT NULL,
  `ACTION1` int(11) DEFAULT NULL,
  `ACTION2` int(11) DEFAULT NULL,
  `ACTION3` int(11) DEFAULT NULL,
  `ACTION4` int(11) DEFAULT NULL,
  `ACTION5` int(11) DEFAULT NULL,
  `ACTION6` int(11) DEFAULT NULL,
  PRIMARY KEY (`SJ`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of loss
-- ----------------------------
INSERT INTO `loss` VALUES ('2018-06-22', '50', '40', '20', '30', '10', '20');
INSERT INTO `loss` VALUES ('2018-06-23', '49', '47', '10', '15', '25', '20');
INSERT INTO `loss` VALUES ('2018-06-24', '51', '48', '10', '11', '18', '26');
INSERT INTO `loss` VALUES ('2018-06-25', '50', '51', '40', '18', '25', '20');
INSERT INTO `loss` VALUES ('2018-06-26', '41', '43', '26', '18', '14', '26');
INSERT INTO `loss` VALUES ('2018-06-27', '30', '35', '34', '10', '24', '19');
INSERT INTO `loss` VALUES ('2018-06-28', '30', '35', '38', '10', '24', '30');
INSERT INTO `loss` VALUES ('2018-06-29', '45', '45', '39', '40', '40', '17');
INSERT INTO `loss` VALUES ('2018-06-30', '46', '44', '41', '45', '19', '20');
INSERT INTO `loss` VALUES ('2018-07-01', '51', '20', '23', '45', '19', '28');

-- ----------------------------
-- Table structure for oee_date
-- ----------------------------
DROP TABLE IF EXISTS `oee_date`;
CREATE TABLE `oee_date` (
  `SJC` date NOT NULL,
  `O8` float DEFAULT NULL,
  `O9` float DEFAULT NULL,
  `O10` float DEFAULT NULL,
  `O11` float DEFAULT NULL,
  `O12` float DEFAULT NULL,
  `O13` float DEFAULT NULL,
  `O14` float DEFAULT NULL,
  `O15` float DEFAULT NULL,
  `O16` float DEFAULT NULL,
  `O17` float DEFAULT NULL,
  `O18` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ----------------------------
-- Records of oee_date
-- ----------------------------
INSERT INTO `oee_date` VALUES ('2018-06-22', '90', '90', '86', '90', '90', '90', '80', '90', '90', '85', '90');
INSERT INTO `oee_date` VALUES ('2018-06-23', '90', '86', '90', '90', '90', '85', '90', '90', '80', '90', '90');
INSERT INTO `oee_date` VALUES ('2018-06-24', '90', '85', '90', '90', '80', '90', '90', '90', '86', '90', '90');
INSERT INTO `oee_date` VALUES ('2018-06-25', '90', '90', '90', '86', '90', '90', '90', '85', '90', '90', '80');
INSERT INTO `oee_date` VALUES ('2018-06-26', '90', '90', '86', '90', '90', '80', '90', '90', '90', '85', '90');
INSERT INTO `oee_date` VALUES ('2018-06-27', '86', '90', '90', '90', '85', '90', '90', '90', '90', '80', '90');
INSERT INTO `oee_date` VALUES ('2018-06-28', '80', '90', '86', '90', '90', '90', '90', '90', '85', '90', '90');
INSERT INTO `oee_date` VALUES ('2018-06-29', '90', '80', '90', '90', '90', '90', '85', '90', '86', '90', '90');
INSERT INTO `oee_date` VALUES ('2018-06-30', '86', '90', '90', '90', '90', '90', '80', '90', '90', '85', '90');
INSERT INTO `oee_date` VALUES ('2018-07-01', '85', '90', '90', '90', '90', '86', '90', '90', '90', '90', '80');
INSERT INTO `oee_date` VALUES ('2018-07-02', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0');
