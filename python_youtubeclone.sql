-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Gegenereerd op: 15 jan 2021 om 10:58
-- Serverversie: 5.7.31
-- PHP-versie: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python_youtubeclone`
--

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `channels`
--

DROP TABLE IF EXISTS `channels`;
CREATE TABLE IF NOT EXISTS `channels` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `channel_name` varchar(255) NOT NULL,
  `channel_pass` varchar(255) NOT NULL,
  `channel_subs` int(11) NOT NULL,
  `channel_imgurl` varchar(255) NOT NULL,
  `created_at` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `channels`
--

INSERT INTO `channels` (`id`, `channel_name`, `channel_pass`, `channel_subs`, `channel_imgurl`, `created_at`) VALUES
(1, 'spookyjelle', '$5$rounds=535000$j6KVOD.TNx4Z/XJe$9PpDyhPCQjQEunvvDQawn5KNMHQW4LOMgWIwJynwshC', 180, 'https://yt3.ggpht.com/ytc/AAUvwnijOGGvsN2Ga1lDPYtW1ozP2NAn774Xi0QNyTWbIrc=s176-c-k-c0x00ffffff-no-rj-mo', '2020-12-01'),
(2, 'Pewdiepie', '', 20000, 'https://yt3.ggpht.com/ytc/AAUvwng76cTETu1glc_8o4UBUiFL2v-m3818ACnK0JLFPA=s176-c-k-c0x00ffffff-no-rj-mo', '2020-12-06');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `comments`
--

DROP TABLE IF EXISTS `comments`;
CREATE TABLE IF NOT EXISTS `comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `video_id` int(11) NOT NULL,
  `channel_id` int(11) NOT NULL,
  `comment_text` varchar(255) NOT NULL,
  `created_at` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `comments`
--

INSERT INTO `comments` (`id`, `video_id`, `channel_id`, `comment_text`, `created_at`) VALUES
(1, 5, 1, 'haha wat een mooie maat', '2020-12-17'),
(2, 5, 2, 'Hallo dit is pewdiepie', '2020-12-02');

-- --------------------------------------------------------

--
-- Tabelstructuur voor tabel `videos`
--

DROP TABLE IF EXISTS `videos`;
CREATE TABLE IF NOT EXISTS `videos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `channel_id` int(11) NOT NULL,
  `video_title` varchar(255) NOT NULL,
  `video_desc` text NOT NULL,
  `video_views` int(11) NOT NULL,
  `video_url` varchar(255) NOT NULL,
  `created_at` date NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Gegevens worden geëxporteerd voor tabel `videos`
--

INSERT INTO `videos` (`id`, `channel_id`, `video_title`, `video_desc`, `video_views`, `video_url`, `created_at`) VALUES
(3, 1, 'Jeboitest', 'sdfkjaskdfhjkasdf', 251, 'http://192.168.48.78/videos/volkswagen.mp4', '2020-12-04'),
(4, 1, 'Nogeenwejo', 'kjdfalskdfjklasdjf', 31, 'http://192.168.48.76:5000/static/videos', '2020-12-12'),
(5, 2, 'I wrote a Song\r\n\r\n', 'Check Out My New Clothing Based: https://www.based.gg\r\nLAST CHANCE TO ORDER BEFORE FRIDAY!\r\nSubscribe to become a FLOOR GANG Member here: https://www.youtube.com/channel/UC-lH...\r\nGet exclusive epic pewdiepie inside epic access and large !\r\n\r\nPewDiePie Gfuel:(affiliate link): https://gfuel.ly/31Kargr\r\n#CodePewdiepie\r\n\r\nMy Stores\r\n Merch: https://represent.com/store/pewdiepie\r\n Tsuki clothing: https://tsuki.market/\r\nigurine: https://pewdiepie.store/\r\nCustomized Devices: https://bit.ly/rspewdiepie\r\n\r\nMy Setup (affiliate link)\r\n Chair: https://clutchchairz.com/pewdiepie/\r\nKeyboard: https://ghostkeyboards.com/pages/pewd...\r\nMouse: https://ghostkeyboards.com/pages/pewd...\r\n\r\n Pewdiepie\'s Pixelings\r\niOS: https://buff.ly/2pNG0aT\r\nAndroid: https://buff.ly/34C68nZ\r\n#pewdiepie #pixelings\r\n\r\n', 2331, 'http://192.168.48.76:5000/static/videos', '2020-11-06'),
(6, 1, 'HOW TO MAKE MONEY', 'Totally legit', 2100010, 'http://192.168.48.76:5000/static/videos', '2017-09-22');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
