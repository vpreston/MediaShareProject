import os
def run_things(address):
	myfile="playingvid.mp4"
	try:
		os.remove(myfile)
	except OSError:
		k=2

	os.system('youtube-dl -o playingvid.mp4 %s'%address)
	os.system('gnome-open playingvid.mp4')

	
if __name__ == '__main__':
		run_things('http://www.youtube.com/watch?v=kZUPCB9533Y')

#sudo pip install --upgrade youtube_dl

#youtube-dl -o panda.mp4 "http://www.youtube.com/watch?v=u155ncSlkCk"

#del playingvid.mp4
#youtube-dl -o playingvid.mp4 "http://www.youtube.com/watch?v=kZUPCB9533Y.mp4"
#gnome-open playingvid.mp4




#download videos= youtube-dl "url"
#play videos= gnome-open nameofvideo.mp4
#nameofvideo has to be one word
#youtube-dl -o name.ext "ur"
