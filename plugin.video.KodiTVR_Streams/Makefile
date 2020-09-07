.DEFAULT_GOAL := default
proj = "plugin.video.KodiTVR_Streams"
version = "0.0.1"

default:
	git archive --prefix=$(proj)/ master -o $(proj)-$(version).zip

clean:
	rm *.zip *.pyc
