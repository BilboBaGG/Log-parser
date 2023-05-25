# String parsers
def GetIMAPSrc(string):
	return string[string.find("[") + 1:string.find("]")] + string[string.index("]") + 1 :string.find(')')]

def IsIMAPConnected(string):
	return not("disconnect" in string) 

def GetXIMSSSrcCon(string):
	return string[string.find("[") + 1:string.find("]")] + string[string.index("]") + 1:]

def GetXIMSSSrcDiscon(string):
	return string[string.find("[") + 1:string.find("]")] + string[string.index("]") + 1:-1]

def IsXIMSSConnected(string):
	return ("logged" in string)