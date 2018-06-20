import urllib;
import urllib2

class TinyPicUrlRequest:
    def __init__(self):
        return

    def Open(self,url):
        return urllib.urlopen(url).read();

    def Post(self, host, url, header, data):
    	encoded_data = urllib.urlencode(data)
    	requestUrl = url
    	conn = urllib2.Request( url = requestUrl, data = encoded_data, headers = header)
    	response = urllib2.urlopen(conn)
    	return response.read()

if __name__ == '__main__':
	requet = TinyPicUrlRequest();
