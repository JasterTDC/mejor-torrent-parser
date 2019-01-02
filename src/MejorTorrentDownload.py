from html.parser import HTMLParser
import re

class MejorTorrentDownload(HTMLParser) :

    def __init__(self):
        HTMLParser.__init__(self)

        self.torrent = ''
        self.name = ''

    def handle_starttag (self, tag, attrs):
        if ( tag == 'a' ) :
            for name, value in attrs:
                if ( name == 'href' ) :
                    uploadMatch = re.findall(r'(.+)\/uploads\/torrents\/', value)
                    nameMatch = re.findall(r'.+name\=(.+)', value)

                    if len(uploadMatch) > 0 and len(nameMatch) > 0:
                        self.torrent = value
                        self.name = nameMatch[0]
