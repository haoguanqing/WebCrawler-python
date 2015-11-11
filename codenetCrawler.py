import urllib
import urllib2

content = urllib.urlopen('http://codecloud.net').read()
f = open("website.txt", 'w')
s1=0
i=0
while s1 >= 0 and i<1000:
    begin = content.find(r'<a',s1)
    m1 = content.find(r'href=',begin)
    m2 = content.find(r'>',m1)
    if(content[m1:m2].find(r'.html')!=-1):
        m2 = content.find(r'.html',m1)
        url = content[m1+6:m2+5]
        f.write(url+"\n")
        print url
    s1 = m2
    i+=1
f.close()
print "\nWebsites crawled and saved in website.txt"



print "\n\n\n===========GET MP3============="
url = "http://mp3light.net/assets/songs/393000-393999/393608-locked-away-ft-adam-levine--1446015599.mp3"

file_name = url.split('/')[-1]
u = urllib2.urlopen(url)
f = open(file_name, 'wb')
meta = u.info()
file_size = int(meta.getheaders("Content-Length")[0])
print "Downloading: %s Bytes: %s" % (file_name, file_size)

file_size_dl = 0
block_sz = 65536
while True:
    buffer = u.read(block_sz)
    if not buffer:
        break

    file_size_dl += len(buffer)
    f.write(buffer)
    status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    status = status + chr(8)*(len(status)+1)
    print status

f.close()
print "Download complete"
