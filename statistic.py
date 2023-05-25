from parse_func import *

# Statistic functions
def GetAllLogsStat(logs):
	openedConnections = []
	statistic = []
	for log in logs:
		if "IMAP" in log:
			isConnected = IsIMAPConnected(log)
			ip = GetIMAPSrc(log)
		elif "XIMSS" in log:
			isConnected = IsXIMSSConnected(log)
			if isConnected:
				ip = GetXIMSSSrcCon(log)
			else:
				ip = GetXIMSSSrcDiscon(log)
		time = log.split(" ")[0]
		statistic.append((ip,isConnected, time))

		if isConnected:
			openedConnections.append(ip)
		else:
			if ip in openedConnections:
				del openedConnections[openedConnections.index(ip)]
			else:
				# Для коннектов, не попавших в лог
				statistic.insert(0,(ip,True,"00:00:00.000"))
	statistic.append((None, False, "23:59:59.999"))
	countConnections = 0

	maxConnetcionCounter = 0
	maxConnectionIndex = 0

	for index in range(len(statistic)):
		if statistic[index][1]:
			countConnections += 1 			
			if countConnections > maxConnetcionCounter:
				maxConnetcionCounter = countConnections
				maxConnectionIndex = index
		else:
			countConnections -= 1

	maxTimeFrom = statistic[maxConnectionIndex][2]
	maxTimeTo = statistic[maxConnectionIndex + 1][2]
	maxConnections = maxConnetcionCounter

	return (maxTimeFrom, maxTimeTo, maxConnections)

def GetXIMSSLogsStat(logs):
	openedConnections = []
	statistic = []
	for log in logs:
		isConnected = IsXIMSSConnected(log)
		if isConnected:
			ip = GetXIMSSSrcCon(log)
		else:
			ip = GetXIMSSSrcDiscon(log)
		time = log.split(" ")[0]
		statistic.append((ip,isConnected, time))

		if isConnected:
			openedConnections.append(ip)
		else:
			if ip in openedConnections:
				del openedConnections[openedConnections.index(ip)]
			else:
				# Для коннектов, не попавших в лог
				statistic.insert(0,(ip,True,"00:00:00.000"))
	statistic.append((None, False, "23:59:59.999"))

	countConnections = 0

	maxConnetcionCounter = 0
	maxConnectionIndex = 0

	for index in range(len(statistic)):
		if statistic[index][1]:
			countConnections += 1 			
			if countConnections > maxConnetcionCounter:
				maxConnetcionCounter = countConnections
				maxConnectionIndex = index
		else:
			countConnections -= 1

	maxTimeFrom = statistic[maxConnectionIndex][2]
	maxTimeTo = statistic[maxConnectionIndex + 1][2]
	maxConnections = maxConnetcionCounter

	return (maxTimeFrom, maxTimeTo, maxConnections)


def GetIMAPLogsStat(logs):
	openedConnections = []
	statistic = []
	for log in logs:
		isConnected = IsIMAPConnected(log)
		ip = GetIMAPSrc(log)
		time = log.split(" ")[0]
		statistic.append((ip,isConnected, time))

		if isConnected:
			openedConnections.append(ip)
		else:
			if ip in openedConnections:
				del openedConnections[openedConnections.index(ip)]
			else:
				# Для коннектов, не попавших в лог
				statistic.insert(0,(ip,True,"00:00:00.000"))
	statistic.append((None, False, "23:59:59.999"))
	countConnections = 0

	maxConnetcionCounter = 0
	maxConnectionIndex = 0

	for index in range(len(statistic)):
		if statistic[index][1]:
			countConnections += 1 			
			if countConnections > maxConnetcionCounter:
				maxConnetcionCounter = countConnections
				maxConnectionIndex = index
		else:
			countConnections -= 1

	maxTimeFrom = statistic[maxConnectionIndex][2]
	maxTimeTo = statistic[maxConnectionIndex + 1][2]
	maxConnections = maxConnetcionCounter

	return (maxTimeFrom, maxTimeTo, maxConnections)
