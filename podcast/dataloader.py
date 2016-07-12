from bs4 import BeautifulSoup
import requests
import unidecode
from podcast.models import Episode

url = 'http://www.travandlos.com/'
podcast_list = range(1, 79)
for count in podcast_list:
    response = requests.get(url+str(count))
    soup = BeautifulSoup(response.content, 'html.parser')
    podcast_details = soup.article.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in podcast_details.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    podcast_episode = str(count)
    podcast_desc = ''
    i = 0
    for link in soup.section.find_all('img'):
        if unidecode.unidecode(link.get('src'))[-3:] == 'jpg':
            i_link = link.get('src')
    for link in soup.article.footer.find_all('a'):
        down = link.get('href')
    for line in text.splitlines():
        if i == 0:
            podcast_timestamp = unidecode.unidecode(line)
        if i == 1:
            podcast_title = unidecode.unidecode(line)
        if i >= 2:
            podcast_desc += unidecode.unidecode(line)+'\n'
        i += 1
    temp = Episode(number=count, date=podcast_timestamp, title=podcast_title, desc=podcast_desc, pod_link=down, img_link=i_link)
    temp.save()
    print str(count)+'done'
print 'Finally done'






