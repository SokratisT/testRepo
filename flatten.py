import collections
import time


d = {'badv': ['adincmedia.com', 'apple.com', 'a.tribalfusion.com', 'cubepile.com', 'go-text.me/', 'gunggo.com', 'heywire.com/', 'http://drawbrid.ge/', 'http://itunes.apple.com/us/app/text-me!-2-free-texting-voice/id514485964?mt=8', 'http://itunes.apple.com/us/app/text-me!-free-texting-sms/id338088432?mt=8', 'https://itunes.apple.com/app/candy-crush-saga/id553834731?mt=8', 'https://itunes.apple.com/app/jelly-splash/id645949180?mt=8', 'https://itunes.apple.com/app/pet-rescue-saga/id572821456?mt=8', 'https://itunes.apple.com/app/rage-of-heroes/id666856123?mt=8', 'https://itunes.apple.com/us/app/candy-crush-saga/id553834731?mt=8', 'https://itunes.apple.com/us/app/zoosk-1...app/id349160522?mt=8', 'https://itunes.apple.com/us/app/zoosk-1-dating-app/id349160522?mt=8', 'https://play.google.com/store/apps/details?id=com.tap4fun.spartanwar', 'https://play.google.com/store/apps/details?id=com.textmeinc.textme&hl=en', 'https://play.google.com/store/apps/details?id=com.zoosk.zoosk', 'imobitrax.best-mobile-apps-4-u.com', 'info.tikl.mobi', 'itunes.apple.com/us/app/textnfly/id556965247?mt=8', 'jellysplash.com', 'line2.com', 'line.naver.jp/en/', 'messenger.yahoo.com/', 'mobilecasa1.com', 'mpartner.mobi', 'niwali.com', 'parccdn.com', 'petrescuesaga.com', 'rageofheroes.com', 'tap4fun.com', 'textie.me/', 'tvindigital.com', 'web.samsungchaton.com/', 'woamobile.com', 'www.aim.com/', 'www.chaton.com/', 'www.facebook.com/gochat', 'www.facebook.com/mobile/messenger', 'www.gogiigames.com', 'www.hotelscombined.com', 'www.indoona.com/en/', 'www.infinitesmsapp.com/', 'www.jackandjill.com', 'www.mocospace.com/', 'www.oovoo.com', 'www.pinger.com', 'www.skype.com', 'www.talkatone.com/', 'www.talkfree.com', 'www.tango.me', 'www.textplus.com', 'www.viber.com', 'www.vonage.com', 'www.voxer.com', 'www.vtokapp.com/', 'www.wechatapp.com/', 'www.whatsapp.com', 'zoosk.com'], 'app': {'publisher': {'id': 'agltb3B1Yi1pbmNyEAsSB0FjY291bnQYq_imDww', 'name': 'Enflick, Inc.'}, 'ver': '(null)', 'name': 'TextNow MoPub', 'bundle': '314716233', 'cat': ['IAB24', 'IAB3', 'social_networking', 'utilities'], 'id': 'agltb3B1Yi1pbmNyDAsSA0FwcBj6kcoWDA', 'storeurl': 'https://itunes.apple.com/us/app/textnow-+-voice-free-texting/id314716233?mt=8&uo=4'}, 'wseat': ['4de65eb6884511e295fa123138070049'], 'imp': [{'bidfloor': 0.16, 'tagid': '4ddc3076884511e295fa123138070049', 'displaymanagerver': '1.17.0.0', 'displaymanager': 'mopub', 'instl': 0, 'banner': {'h': 250, 'ext': {'mraid': [{'functions': ['storePicture', 'supports', 'playVideo', 'createCalendarEvent'], 'version': '2.0'}], 'nativebrowserclick': 1}, 'pos': 1, 'battr': [1, 3, 9, 10, 14, 6], 'api': [3], 'w': 300, 'btype': [4]}, 'id': '1'}], 'at': 2, 'device': {'os': 'iOS', 'language': 'en', 'ip': '174.73.0.46', 'make': 'Apple', 'connectiontype': 2, 'js': 1, 'dpidsha1': '180e34863285ba4996fb9548dcbacde0558e8c5b', 'dnt': 0, 'ext': {'idfa': 'DB8B7EA1-8A61-4770-9114-C4B65735A317'}, 'ua': 'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) Mobile/11D257', 'devicetype': 1, 'dpidmd5': 'd40572cf227daa2799abb8e111e3a23a', 'osv': '7.1.2', 'geo': {'city': 'Gretna', 'zip': '70056', 'country': 'USA', 'region': 'LA', 'lon': -90.052559, 'lat': 29.899603}, 'model': 'iPad 2 (WiFi)'}, 'bcat': ['IAB7-39', 'IAB8-5', 'IAB8-18', 'IAB9-9', 'IAB13', 'IAB14-1', 'IAB26'], 'id': '6c291e9b-b9e4-4206-be1d-d397b71edeed', 'user': {'keywords': 'cell phones,cell phone plans,smartphones,cell phone accessories,m_area:(null),m_age:59', 'gender': 'f', 'yob': 1955}}

log = {}

"""
@profile
def flatten3(root, prefix_keys=True):
	dicts = [([], root)]
	ret = {}
	seen = set()
	for path, d in dicts:
		if id(d) in seen:
			continue
		seen.add(id(d))
		for k, v in d.items():
			new_path = path + [k]
			prefix = '_'.join(new_path) if prefix_keys else k
			if hasattr(v, 'items'):
				dicts.append((new_path, v))
			else:
				ret[prefix] = v
	return ret
"""

"""
@profile
def flatten2(d, parent_key='', sep='_'):
	items = []
	for k, v in d.items():
		new_key = parent_key + sep + k if parent_key else k
		if isinstance(v, collections.MutableMapping) :
			items.extend(flatten2(v, new_key).items())
	elif k == 'imp' or k == 'mraid':
		items.extend(flatten2(v[0], new_key).items())
		else:
			items.append((new_key, v))
	return dict(items)
"""

#---------------currently used---------------------
def flatten1(obj, log, parent ):
		for key, val in obj.iteritems():
				if isinstance(val, dict): # type( val ) == type( dict() ):
						flatten1( val, log, parent + key + "_" )
				elif isinstance(val, list): #type( val ) == type( list() ):
						if len( val ) == 1: # and len( val ) < 2:
								if isinstance(val[0], dict): #type( val[0] ) == type( dict() ):
										for v in val:
												flatten1( v, log, parent + key + "_" )

								else:
										log[ parent + key ] = val

						elif len( val ) > 1:
								log[ parent + key ] = val
						else:
								log[ parent + key ] = val
				else:
						log[ parent + key ] = val

#---------------my ver-----------------------------
def flatten4(init, lkey=''):
	logme = {}
	for rkey,val in init.iteritems():
		key = lkey+rkey
		if isinstance(val, dict):
			logme.update(flatten4(val, key+'_'))
		elif isinstance(val, list) and len(val) == 1 and isinstance(val[0], dict): #elif rkey in 'imp' or rkey == 'mraid' :
			logme.update(flatten4(val[0], key+'_'))
		else:
			logme[key] = val
	return logme

#--------------best performing--------------------
def flatten5(d, separator='_'):
	final = {}
	def _flatten_dict(obj, parent_keys=[]):
		for k, v in obj.iteritems():
			if isinstance(v, dict):
				_flatten_dict(v, parent_keys + [k])
			elif k == 'imp' or k == 'mraid':
						_flatten_dict(v[0], parent_keys + [k])
			else:
				key = separator.join(parent_keys + [k])
				final[key] = v
	_flatten_dict(d)
	return final

#--------------flatten6------------------------
def flatten6(dd, separator='_', prefix=''):
	return { prefix + separator + k if prefix else k : v
			 for kk, vv in dd.items()
			 for k, v in flatten6(vv, separator, kk).items()
			 } if isinstance(dd, dict) else { prefix : dd }


#---------------flatten7----------------------
def flat_dic_helper(prepand,d):
	if len(prepand) > 0:
		prepand = prepand + "_"
	for k in d:
		i=d[k]
		if type(i) is dict:
			r = flat_dic_helper(prepand+k,i)
			for j in r:
				yield j
		else:
			yield (prepand+k,i)

#calls------------


start = time.time()
for i in xrange(0, 100000):
	flatten1(d, log, "")
end = time.time()
print "1: " + str(end - start)


start = time.time()
for i in xrange(0, 100000):
	f4 = flatten4(d, "")
end = time.time()
print "4: " + str(end - start)

"""
start = time.time()
for i in xrange(0, 100000):
	f5 = flatten5(d)
end = time.time()
print "5: " + str(end - start)


def flat_dic(d): return dict(flat_dic_helper("",d))

start = time.time()
for i in xrange(0, 100000):
		f7 = flat_dic(d)
end = time.time()
print "7: " + str(end - start)
"""

"""
print "Current: "
print  log

print "\n--------\nNew 4: "
print f4

print "\n--------\nNew 5: "
print f5

print "\n--------\nNew 7: "
print f7
"""
