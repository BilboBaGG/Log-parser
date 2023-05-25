from statistic import *
from validate import *

logs = open("./logs/server.log").read().split("\n")

def PrintHeader():
	output = ""
	output += "-"*50 + "\n"
	output += f'|{" "*int((50-22)/2)}Here is a log parser{" "*int((50-22)/2)}|\n'
	print(output,end="")

def PrintHelp():
	output = "-"*50 + "\n"
	output += '  Flags:\n'
	output += '\t-h, --help : prints this help window\n'
	output += '\t-a, --all : prints statistic for all log file\n'
	output += '\t--ximss : prints statostic only for XIMSS logs\n'
	output += '\t--imap : prints statostic only for IMAP logs\n'
	print(output,end = "")
	PrintPoweredBy()

def PrintUnknownArgs():
	output = ""
	output += "-"*50 + "\n"
	output += f'|{" "*int((50-22)/2)}Unknown arguments!!{" "*int((50-22)/2)}|\n'
	output += "-"*50 + "\n"
	output += '\nPowered by B9I1bl3 Gof3pbl'
	print(output)

def PrintXIMSSLogsStat():
	allLogs = ShowOnlyXIMSS(logs)
	maxTimeFrom, maxTimeTo, maxConnections = GetXIMSSLogsStat(allLogs)
	output = ""
	output += "-"*50 + "\n"
	output += "  Statistic for XIMSS the logs:" + "\n\n"
	output += "  Max connection number was :\n"
	output += f"\tFrom {maxTimeFrom} to {maxTimeTo}\n"
	output += f"\tConnection number: {maxConnections}\n"
	output += ""
	print(output, end = "")

def PrintIMAPLogsStat():
	allLogs = ShowOnlyIMAP(logs)
	maxTimeFrom, maxTimeTo, maxConnections = GetIMAPLogsStat(allLogs)
	output = ""
	output += "-"*50 + "\n"
	output += "  Statistic for IMAP the logs:" + "\n\n"
	output += "  Max connection number was :\n"
	output += f"\tFrom {maxTimeFrom} to {maxTimeTo}\n"
	output += f"\tConnection number: {maxConnections}\n"
	output += ""
	print(output,end = "")

def PrintAllLogsStat():
	allLogs = logs
	maxTimeFrom, maxTimeTo, maxConnections = GetAllLogsStat(allLogs)
	output = ""
	output += "-"*50 + "\n"
	output += "  Statistic for all the logs:" + "\n\n"
	output += "  Max connection number was :\n"
	output += f"\tFrom {maxTimeFrom} to {maxTimeTo}\n"
	output += f"\tConnection number: {maxConnections}\n"
	output += ""
	print(output,end = "")

def PrintPoweredBy():
	print("-" * 50)
	print('  Powered by B9I1bl3 Gof3pbl')