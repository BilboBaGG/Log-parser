def ShowOnlyXIMSS(logs):
	filtered = []
	for log in logs:
		if "XIMSS" in log:
			filtered.append(log)

	return filtered

def ShowOnlyIMAP(logs):
	filtered = []
	for log in logs:
		if "IMAP" in log:
			filtered.append(log)

	return filtered