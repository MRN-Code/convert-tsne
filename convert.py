from __future__ import print_function
import json
import sys

sys.stderr.write("running...")

try:
    def main():
        sys.stdout.write(json.dumps({"convert": True}))
except:
    sys.stderr.write("prcess terminated due to error")

if __name__ == '__main__':
    main()
