from Film import Film

class FilmDAO :

    def __init__ (self, conn) :
        self.conn = conn;
        self.cursor = conn.cursor()

    def create (self, film) :
        flm = self.getByFilmId(film.getFilmId())

        if ( flm == None ) :
            self.cursor.execute(
            "INSERT INTO mt_film (film_id, film_slug, film_url, film_download_url) VALUES (?, ?, ?, ?)",
            (film.getFilmId(), film.getFilmSlug(), film.getFilmUrl(), film.getFilmDownloadUrl())
            )
            self.conn.commit()

    def updateDownloadTorrent(self, film) :
        flm = self.getByFilmId(film.getFilmId())

        if ( flm == None ) :
            return None

        self.cursor.execute(
        "UPDATE mt_film SET film_download_torrent = ? WHERE film_id = ?",
        (film.getFilmDonwloadTorrent(), film.getFilmId())
        )
        self.conn.commit()

    def updateDownloadNameTorrent(self, film) :
        flm = self.getByFilmId(film.getFilmId())

        if ( flm == None ) :
            return None

        self.cursor.execute(
        "UPDATE mt_film SET film_download_torrent = ?, film_download_name = ? WHERE film_id = ?",
        (film.getFilmDonwloadTorrent(), film.getFilmDownloadName(), film.getFilmId())
        )
        self.conn.commit()

    def getByFilmId(self, film_id) :
        self.cursor.execute(
        "SELECT film_id, film_slug, film_url, film_download_url, film_download_torrent, film_download_name FROM mt_film WHERE film_id = ?", (film_id, )
        )
        result = self.cursor.fetchone()

        if ( result != None ) :
            flm = Film()
            flm.setFilmId(result[0])
            flm.setFilmSlug(result[1])
            flm.setFilmUrl(result[2])
            flm.setFilmDownloadUrl(result[3])
            flm.setFilmDownloadTorrent(result[4])
            flm.setFilmDownloadName(result[5])

            return flm

        return None

    def getAll(self) :
        self.cursor.execute(
        "SELECT film_id, film_slug, film_url, film_download_url, film_download_torrent, film_download_name FROM mt_film"
        )
        result = self.cursor.fetchall()
        ret = []

        if ( result != None ) :
            for film_id, film_slug, film_url, film_download_url, film_download_torrent, film_download_name in result :
                flm = Film()
                flm.setFilmId(film_id)
                flm.setFilmSlug(film_slug)
                flm.setFilmUrl(film_url)
                flm.setFilmDownloadUrl(film_download_url)
                flm.setFilmDownloadTorrent(film_download_torrent)
                flm.setFilmDownloadName(film_download_name)

                ret.append(flm)

            return ret

        return None
