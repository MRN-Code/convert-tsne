from __future__ import print_function
import json
import sys

sys.stderr.write("running...")

try:
    def main():
        sys.stdout.write(json.dumps({"tsne": True}))
except:
    sys.stderr.write("Process terminated due to error")

if __name__ == '__main__':
    main()
