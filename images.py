import urllib

start = 3000
end = 3820

errors = open('fails.txt', 'wa')

current = start
while(current <= end):
	curAsStr = str(current)
	try:
		f = open(curAsStr + '.jpg','wb')
		f.write(urllib.urlopen('http://hao.newtabplus.com/cloudWallpaper/Scenery/' + curAsStr + '.jpg').read())
		f.close()
	except:
		errors.write(curAsStr + ', ')
	current = current + 1

errors.close()



#urllib.urlretrieve('http://hao.newtabplus.com/cloudWallpaper/Scenery/3000.jpg')
