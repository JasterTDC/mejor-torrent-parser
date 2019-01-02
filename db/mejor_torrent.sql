CREATE TABLE IF NOT EXISTS mt_film (
  film_id     INT(11) NOT NULL,
  film_slug   TEXT NOT NULL,
  film_url    TEXT NOT NULL,
  film_download_url TEXT NOT NULL,
  film_download_torrent TEXT DEFAULT NULL,
  film_download_name TEXT DEFAULT NULL,

  PRIMARY KEY ( film_id )
);
