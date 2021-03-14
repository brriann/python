from lxml import html, etree
import requests
siteLink = 'http://users.cis.fiu.edu/~weiss/dsaa_c++4/code/'
page = requests.get(siteLink)
extractedHtml = html.fromstring(page.content)
cppSrc = extractedHtml.xpath("//a/@href")

for cppSrcFile in cppSrc:
    if not (cppSrcFile.startswith('http') or cppSrcFile.startswith('../')):
        fileLink = str(siteLink) + str(cppSrcFile)
        rawFile = requests.get(fileLink, stream=True)
        with open('scrapefiles/' + str(cppSrcFile), 'wb') as fd:
            for chunk in rawFile.iter_content(chunk_size=1024):
                fd.write(chunk)
    