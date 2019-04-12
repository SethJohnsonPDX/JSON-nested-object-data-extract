import json
import csv

def getJSON(filePathAndName):
	with open(filePathAndName, 'r') as fp:
		return json.load(fp)


def extract_invitationIds(obj, key):
	arr = []

	def extract(obj, arr, key):
		if isinstance(obj, dict):
			for k, v in obj.items():
				if isinstance(v, (dict, list)):
					extract(v, arr, key)
				elif k == key:
					arr.append(v)
		elif isinstance(obj, list):
			for item in obj:
				extract(item, arr, key)
		return arr

	results = extract(obj, arr, key)
	return results

""" ADD YOUR JSON FILE BELOW AND SAVE TO DESKTOP"""
invitationFile = getJSON('./expApiUser.json')

invitations = extract_invitationIds(invitationFile, 'invitationId')


""" CREATE AND SAVE AN EMPTY CSV """
with open('invitations.csv', 'w') as textfile:
	for i in invitations:
		print >> textfile, i 



