from html.parser import HTMLParser
from Film import Film
import requests
import re

class MejorTorrent (HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.films = []
        self.base_url = 'http://www.mejortorrent.org'
        self.download_url = 'http://www.mejortorrent.org/secciones.php?sec=descargas&ap=contar&tabla=peliculas&id={film_id}&link_bajar=1'

    def handle_starttag (self, tag, attrs):
        if ( tag == 'a' ):
            for name, value in attrs:
                if ( name == 'href' ):
                    filmMatch = re.findall(r'\/peli\-(.+)\-(\d+)\-(.+[^\.html])', value)
                    if ( len(filmMatch) > 0 ):
                        for trash, film_id, slug in filmMatch :
                            film = Film()
                            film.setFilmId(film_id)
                            film.setFilmSlug(slug)
                            film.setFilmUrl(self.base_url + value)
                            film.setFilmDownloadUrl(self.download_url.format(film_id = film_id))

                            self.films.append(film)

    def reset_films (self) :
        self.films = []
