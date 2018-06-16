from TinyPicImage import *
from TinyPicVideo import *
from TinyPicCategory import *
import json

class TinyPicImageEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, TinyPicImage):
			return {'PId': '%s' % (obj.PId), 'PUrl': '%s' % (obj.PUrl), 'PFileUrl': '%s' % (obj.PFileUrl)}
		return json.JSONEncoder.default(obj, TinyPicImage)

class TinyPicVideoEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, TinyPicVideo):
			return {'VId': '%s'% (obj.VId), 'VUrl': '%s'% (obj.VUrl), 'VFileUrl': '%s' % (obj.VFileUrl)} 
		return json.JSONEncoder.default(obj, TinyPicVideo)

class TinyPicCategoryEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, TinyPicCategory):
			return {'CName': '%s'% (obj.CName), 'CUrl': '%s'% (obj.CUrl)} 
		return json.JSONEncoder.default(obj, TinyPicCategory)