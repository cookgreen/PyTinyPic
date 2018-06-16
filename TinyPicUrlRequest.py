import urllib;

class TinyPicUrlRequest:
    def __init__(self):
        return

    def Open(self,url):
        return urllib.urlopen(url).read();


if __name__ == '__main__':
	requet = TinyPicUrlRequest();
