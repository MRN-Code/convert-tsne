from __future__ import print_function

import json,sys

try:
	def main():
		with open("convert.json","w") as f:
			json.dump({"convert":True},f)
except:
	sys.stderr("prcess terminated due to error")

if __name__ == '__main__':
	main()
