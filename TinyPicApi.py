from TinyPic import *
from TinyPicEncoder import *
import json

class TinyPicApi:
	tp = None

	def __init__(self):
		self.tp = TinyPic()

	def GetVideosByPage(self, page = 1):
		return json.dumps(self.tp.GetVideosByPage(page), cls = TinyPicVideoEncoder)

	def GetImagesByPage(self, page = 1):
		return json.dumps(self.tp.GetImagesByPage(page), cls = TinyPicImageEncoder)

	def GetTopCategories(self):
		return json.dumps(self.tp.GetTopCategories(), cls = TinyPicCategoryEncoder)

	def GetSubCategories(self, category):
		return json.dumps(self.tp.GetSubCategories(category), cls = TinyPicCategoryEncoder)

	def GetImagsByCategory(self, category):
		return json.dumps(self.tp.GetImagsByCategory(category), cls = TinyPicImageEncoder)

	def SearchImages(self,searchTag):
		return json.dumps(self.tp.SearchImages(searchTag), cls = TinyPicImageEncoder)

if __name__ == '__main__':
	api = TinyPicApi()
	print api.GetSubCategories('animals')