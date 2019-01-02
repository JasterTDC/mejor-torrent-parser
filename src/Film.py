class Film:
    def __init__(self):
        self.film_slug = ''
        self.film_url = ''
        self.film_download_url = ''
        self.film_download_torrent = ''
        self.film_download_name = ''

    def setFilmId (self, film_id) :
        self.film_id = film_id

    def setFilmSlug (self, film_slug) :
        self.film_slug = film_slug

    def setFilmUrl (self, film_url) :
        self.film_url = film_url

    def setFilmDownloadUrl (self, film_download_url) :
        self.film_download_url = film_download_url

    def setFilmDownloadTorrent (self, film_download_torrent) :
        self.film_download_torrent = film_download_torrent

    def setFilmDownloadName ( self, film_download_name ) :
        self.film_download_name = film_download_name

    def getFilmId (self) :
        return self.film_id

    def getFilmSlug (self) :
        return self.film_slug

    def getFilmUrl (self) :
        return self.film_url

    def getFilmDownloadUrl (self) :
        return self.film_download_url

    def getFilmDonwloadTorrent (self) :
        return self.film_download_torrent

    def getFilmDownloadName (self) :
        return self.film_download_name
