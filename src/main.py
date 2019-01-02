from Film import Film
from FilmDAO import FilmDAO
from MejorTorrent import MejorTorrent
from MejorTorrentDownload import MejorTorrentDownload
import sqlite3 as db
import requests

conn = db.connect( '../db/mejor_torrent.db' )

filmDAO = FilmDAO(conn)
filmUrl = 'http://www.mejortorrent.org/secciones.php?sec=descargas&ap=peliculas&p={page}'

for ind in range(1, 20) :
    print('[IND] ' + str(ind))
    print('[URL] ' + filmUrl.format(page = ind))

    htmlStr = requests.get( filmUrl.format(page = ind) )

    mejorTorrentParser = MejorTorrent()
    mejorTorrentParser.feed(htmlStr.text)

    if len(mejorTorrentParser.films) > 0 :
        for film in mejorTorrentParser.films :
            filmDAO.create(film)

    mejorTorrentParser.reset_films()

films = filmDAO.getAll()

if ( films != None ):
    downloadParser = MejorTorrentDownload()

    for film in films :
        print('[DOWNLOAD][URL] ' + film.getFilmDownloadUrl())

        htmlStr = requests.get( film.getFilmDownloadUrl() )
        downloadParser.feed(htmlStr.text)

        film.setFilmDownloadTorrent(downloadParser.torrent)
        film.setFilmDownloadName(downloadParser.name)

        filmDAO.updateDownloadNameTorrent(film)

films = filmDAO.getAll()

if ( films != None ) :
    for film in films :
        print('[DOWNLOAD][TORRENT] ' + film.getFilmDonwloadTorrent())

        torrent = requests.get(film.getFilmDonwloadTorrent())

        with (open('../torrents/' + film.getFilmDownloadName(), 'wb')) as f :
            f.write(torrent.content)

conn.close()
