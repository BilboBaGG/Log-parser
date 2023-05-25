import sys
from printers import *

flags = ["--help", "--all", "--ximss", "-h", "-a","--imap"]

notOpenedLogs = []

def main():
	PrintHeader()
	if len(sys.argv) == 1 or sys.argv[1] == "--help" or sys.argv[1] == "-h": 
		PrintHelp()
		return
	for argument in sys.argv[1:]:
		if argument not in flags:
			PrintUnknownArgs()
			return
	if "--ximss" in sys.argv:
		PrintXIMSSLogsStat()
	if "--imap" in sys.argv:
		PrintIMAPLogsStat()
	if "-a" in sys.argv or "--all" in sys.argv:
		PrintAllLogsStat()
	PrintPoweredBy()

main()