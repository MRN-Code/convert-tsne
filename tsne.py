from __future__ import print_function

import json,sys

sys.stderr("running...")

try:
	def main():
		with open("tsne.json","w") as f:
			json.dump({"complete":True},f)
		with open("tsne.txt","w") as fp:
			fp.write("tsne done")
except:
	sys.stderr("Process terminated due to error")

if __name__ == '__main__':
	main()
