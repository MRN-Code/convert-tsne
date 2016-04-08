from __future__ import print_function

import json

def main():
	with open("convert.json","w") as f:
		json.dump({"convert":True},f)

if __name__ == '__main__':
	main()
