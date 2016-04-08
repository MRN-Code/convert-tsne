from __future__ import print_function

import json

def main():
	with open("tsne.json","w") as f:
		json.dump({"complete":True},f)

if __name__ == '__main__':
	main()
