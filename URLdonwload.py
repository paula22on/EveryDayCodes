###################################################################################
###################################### URL Downloader #############################
###################################################################################

url = "https://instagram.com/favicon.ico"

# ____________Method 1_______________
# pip install requests
import requests
r = requests.get(url)
with open("favicon.ico", "wb") as f:
    f.write(r.content)



# ____________Method 2_______________
# pip install wget
import wget
r = wget.download(url, "favicon.ico")
# Method 3
# pip install urllib3
import urllib.request
urllib.request.urlretrieve(url, "favicon.ico")