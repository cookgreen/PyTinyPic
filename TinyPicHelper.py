class TinyPicHelper:
	def GetUrlParamsDic(self, url):
		params = url[url.index('?')+1:].split('&');
		dic = {}
		for param in params:
			tokens = param.split('=');
			idx = tokens[1].find('#');
			dic[tokens[0]]= tokens[1] if idx==-1 else tokens[1][:idx];
		return dic