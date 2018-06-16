from TinyPicImage import *
from TinyPicVideo import *
from TinyPicCategory import *
from TinyPicUrlRequest import *
from TinyPicHelper import *
import bs4

class TinyPic:
	request = None
	helper = None
	soup = None
	def __init__(self):
		self.request = TinyPicUrlRequest()
		self.helper = TinyPicHelper()

	def GetVideosByPage(self, page = 1):
		videos=[]
		url = "http://tinypic.com/videos.php?page=" + str(page)
		soup = bs4.BeautifulSoup(self.request.Open(url))
		divElement = soup.find('div', {'class' : 'browse'});
		ulElement = divElement.ul
		for child in ulElement.children:
			if type(child) == bs4.element.Tag and (not child.has_attr('class')):
				url = child.a['href']
				dic = self.helper.GetUrlParamsDic(url)
				video = TinyPicVideo()
				video.VId = dic['v'];
				video.VUrl = url
				video.VFileUrl = "http://v" + dic['s'] + ".tinypic.com/" + dic['v'] +".flv";
				videos.append(video)
		return videos

	def GetImagesByPage(self, page = 1):
		images=[]
		url = "http://tinypic.com/images.php?page=" + str(page)
		soup = bs4.BeautifulSoup(self.request.Open(url))
		divElement = soup.find('div', {'class' : 'browse'})
		ulElement = divElement.ul
		for child in ulElement.children:
			if type(child) == bs4.element.Tag and (not child.has_attr('class')):
				url = child.a['href']
				image = TinyPicImage()
				image.PId = self.helper.GetUrlParamsDic(url)['id']
				image.PUrl = url
				image.PFileUrl = "http://oi43.tinypic.com/" + self.helper.GetUrlParamsDic(url)['pic'] + ".jpg";
				images.append(image)
		return images

	def GetTopCategories(self):
		categories=[]
		url = "http://tinypic.com/categories/"
		soup = bs4.BeautifulSoup(self.request.Open(url))
		divElement = soup.find('div', {'class' : 'browse'})
		ulElement = divElement.ul
		for child in ulElement.children:
			if type(child) == bs4.element.Tag and child.has_attr('class'):
				category = TinyPicCategory()
				category.CName = child.h3.a.string;
				category.CUrl = child.h3.a['href'];
				categories.append(category)
		return categories

	def GetSubCategories(self, category):
		subCategories=[]
		url = "http://tinypic.com/categories/" + category.lower();
		soup = bs4.BeautifulSoup(self.request.Open(url))
		divElement = soup.find('div', {'class' : 'browse'})
		ulElement = divElement.ul
		for child in ulElement.children:
			if type(child) == bs4.element.Tag and child.has_attr('class'):
				category = TinyPicCategory()
				category.CName = child.h3.a.string;
				category.CUrl = child.h3.a['href'];
				subCategories.append(category)

		ulEle = soup.find('ul', {'class' : "secondary-categories"})
		for child in ulEle.children:
			if type(child) == bs4.element.Tag and child.has_attr('class'):
				temp_ul_ele = child.ul
				for ch in temp_ul_ele.children:
					if type(ch) == bs4.element.Tag:
						category = TinyPicCategory()
						category.CName = ch.a.string
						category.CUrl = ch.a['href']
						subCategories.append(category)
		return subCategories

	def GetImagsByCategory(self, category):
		images=[]
		url = "http://tinypic.com/search.php?tag="+category.lower()+"&type=images"
		soup = bs4.BeautifulSoup(self.request.Open(url))
		divElement = soup.find('div', {'class' : 'browse'})
		ulElement = divElement.ul
		for child in ulElement.children:
			if type(child) == bs4.element.Tag and child.has_attr('class'):
				image = TinyPicImage()
				image.PId = child.a.img['src'];
				image.PUrl = child.a.img['src'];
				image.PFileUrl = "http://oi43.tinypic.com/" + self.helper.GetUrlParamsDic(child.a.img['src'])['pic'] + ".jpg";
				images.append(image)
		return images

	def SearchImages(self,searchTag):
		return GetImagsByCategory(searchTag)

	def Login(self, email, password, confirmcode):
		return

	def Register(self, email, password, birthday, confirmcode, isRemeber):
		return

	def Logout(self):
		return

	def GetMyVideos():
		return

	def GetMyCategories():
		return

	def GetMyImages():
		return
