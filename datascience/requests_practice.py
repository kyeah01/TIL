import sys
import urllib.request
try:
    with urllib.request.urlopen("https://www.networksciencelab.com") as doc:
        html = doc.read()
except:
    print(f"Could not open", file=sys.stderr)