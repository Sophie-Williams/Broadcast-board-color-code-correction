# Search
import wndMgr

# Add below
def StripColor(text):
	import re

	regex = '\|c([a-zA-Z0-9]){0,8}|'
	search = re.search(regex, text)
	if search:
		text = re.sub(regex, '', text)

	return text

# Search
			curPos = text.find(" ", prevPos)
			if curPos < 0:
				break

# Add above
			text = StripColor(text)

# Search
		curTime = app.GetTime()
		self.tipList.append((curTime, text))
		self.__RefreshBoard()

# Add above
		text = StripColor(text)