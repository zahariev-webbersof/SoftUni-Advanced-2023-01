# class Set:
#     MIN_SIZE = 10
#
#     def __init__(self, size=10):
#         self._size = size
#         self.filled = 0
#         self.elements = [[] for _ in range(size)]
#
#     def hash_function(self, value):
#         return hash(value) % self._size
#
#     def _contains(self, value):
#         # 0, 4
#         # 1, 5
#         #
#         for i, e in enumerate(self.elements[self.hash_function(value)]):
#             if value == e: return 1
#         return -1
#
#     def contains(self, value):
#         return self._contains(value) >= 0
#
#     def add(self, value):
#         self.elements[self.hash_function(value)].append(value)
#
#     def delete(self, value):
#         index = self._contains(value)
#         if index >= 0:
#             self.filled -=1
#             self.elements[self.hash_function(value)].pop(index)
#
#     def __str__(self):
#         return f'size: {self._size} elements: {self.elements}'
#
#
# aa = Set()
# aa.add(5)
# aa.add(55)
# aa.add(5555)
# aa.add(14)
# aa.add(0)
# aa.add(9)
# print(aa.__str__())

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import ssl


# --- return soup object of url ---
def getlinks(cUrl):
    html = urlopen(cUrl, context=ctx).read()
    soup = bs(html, "html.parser")
    return soup('a')


# --- writes scraped linked into txt file ---
def writelinks(parent, link):
    f = open("links.txt", "a")
    f.write(parent + link + "\n")
    f.close()


# Ignore ssl certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# search for these file types in ftp server
fileTypes = (
    '.webm', '.mkv', '.flv', '.avi', '.mov', '.wmv', '.mp4', '.mp4p', '.mp4v', '.mpg', '.mpef', '.mpv', '.mpeg', '.flv',
    '.f4v', '.f4p', '.f4a', '.f4b')

seasons = {}
quality = {}
count: int = 0

spidey = """      #######                          ##                          
    /       ###              #          ##                         
   /         ##             ###         ##                         
   ##        #               #          ##                         
    ###                                 ##                         
   ## ###           /###   ###      ### ##    /##   ##   ####      
    ### ###        / ###  / ###    ######### / ###   ##    ###  /  
      ### ###     /   ###/   ##   ##   #### /   ###  ##     ###/   
        ### /##  ##    ##    ##   ##    ## ##    ### ##      ##    
          #/ /## ##    ##    ##   ##    ## ########  ##      ##    
           #/ ## ##    ##    ##   ##    ## #######   ##      ##    
            # /  ##    ##    ##   ##    ## ##        ##      ##    
  /##        /   ##    ##    ##   ##    /# ####    / ##      ##    
 /  ########/    #######     ### / ####/    ######/   #########    
/     #####      ######       ##/   ###      #####      #### ###   
|                ##                                           ###  
 \)              ##                                    #####   ### 
                 ##                                  /#######  /#  
                  ##                                /      ###/    
====================================================================\n"""
print(spidey)

while True:
    # Exception - Invalid URL
    try:
        url = input('Enter target Url: ').strip()
        # get <a> tags from current page
        tags = getlinks(url)
    except Exception:
        print('WARNING!!! Cannnot connect to the url!!!!')
    else:
        print("Available Seasons:\n")
        for tag in tags:
            if tag.get('href', None).lower().endswith(fileTypes):  # if already in file directory
                writelinks(url, tag.get('href', None))
            else:
                link = tag.get('href', None)
                if link == '../':           # skips printing '../'
                    continue
                count += 1
                print('\t({}) - Season {}'.format(count, count))
                seasons[str(count)] = link

        # request seasons from user
        while True:
            # exception value error
            try:
                enteredseasons = list(map(str, input("\nPlease select seasons you want(1,2,3,...): ").split(',')))
            except ValueError:
                print("Invalid input!")
            else:
                if len(seasons) <= count:
                    seasons = {key: val for key, val in seasons.items() if
                               key in enteredseasons}  # keep wanted seasons only
                    break

        for val in seasons.values():  # iterate through the selected seasons
            count = 0
            tmpUrl = url
            tmpUrl += val

            # get <a> in the page
            tags = getlinks(tmpUrl)

            print('\nFor season - {}\n'.format(val.strip('/')))

            tmpQuality = []
            # request quality
            for tag in tags:
                link = tag.get('href', None)
                if link == '../':
                    continue
                count += 1

                tmpQuality.append(link)  # list of available quality
                print('\t({}) - Video Quality - {}'.format(count, link.strip('/')))

            # get input for video quality
            while True:

                try:
                    reqQuality = int(input("\nPlease select Video Quality you want(1 or 2 or...): "))
                except ValueError:
                    print('Invalid Input!')
                else:
                    # correct int value ? is it in range ?
                    if len(tmpQuality) >= reqQuality > 0:
                        quality[val] = tmpQuality[reqQuality - 1]
                        tmpQuality = []
                        break

        for s, q in quality.items():  # s - season, q - quality
            tmpUrl = url + s + q
            tags = getlinks(tmpUrl)

            for tag in tags:
                if tag.get('href', None) == '../':
                    continue
                writelinks(tmpUrl, tag.get('href', None))

        print("All links scraped succesfully!")

        break  # exception - invalid URL



 