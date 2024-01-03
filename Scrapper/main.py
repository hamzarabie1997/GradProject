import re
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Lists
urls = []
regenerated_links = []
used_urls = []
final_info = []

# Parsing URL
url = 'https://www.indeed.com/worldwide'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')


# Retrieve all anchor tags from worldwide page
tags = soup('a')
for tag in tags:
    url = tag.get('href', None)
    if url not in urls:
        if re.match(r'https://[\w]{2}\.indeed\.com/', url):
            urls.append(url)
        elif re.match(r'https://www.indeed.co.[\w]{2}', url):
            urls.append(url)
        elif re.match(r'https://www.indeed.com[.\w]{2}', url):
            urls.append(url)
        else:
            continue
    else:
        continue






# Splitting job title into individual words
try:
    job_pick = int(input('Choose a job title:\n 1- Data scientist\n 2- Software engineer\n'
                         '3- Machine Learning engineer\n 4- Front-End Developer\n'
                         '5- Back-End Developer\n 6- Other\n'))
    if job_pick == 1:
        job_title = "data scientist"
        job_title_splitted = job_title.split()
    elif job_pick == 2:
        job_title = "software engineer"
        job_title_splitted = job_title.split()
    elif job_pick == 3:
        job_title = "machine learning engineer"
        job_title_splitted = job_title.split()
    elif job_pick == 4:
        job_title = "front end developer"
        job_title_splitted = job_title.split()
    elif job_pick == 5:
        job_title = "back end developer"
        job_title_splitted = job_title.split()
    elif job_pick == 6:
        other_picked = input('Enter the job title you want to search for: ')
        job_title_splitted = other_picked.split()
    else:
        print('Wrong pick !')

    while True:
        try:
            print("Select 99 to end the process")
            country_pick = int(input('Choose a country to search in:\n 1- Argentina\n'
                                     '2- Australia\n 3- Austria\n 4- Bahrain\n'
                                     '5- Belgium\n 6- Brazil\n 7- Canada\n 8- Chile\n'
                                     '9- China\n 10- Colombia\n 11- Costa Rica\n'
                                     '12- Czech\n 13- Denmark\n 14- Ecuador\n'
                                     '15- Egypt\n 16- Finland\n 17- France\n'
                                     '18- Germany\n 19- Greece\n 20- Hong Kong\n'
                                     '21- Hungary\n 22- India\n 23- Indonesia\n'
                                     '24- Ireland\n 25- Israel\n 26- Italy\n 27- Japan\n'
                                     '28- Kuwait\n 29- Luxembourg\n 30- Mexico\n'
                                     '31- Morocco\n 32- Netherlands\n 33- New Zealand\n'
                                     '34- Nigeria\n 35- Norway\n 36- Oman\n 37- Pakistan\n '
                                     '38- Panama\n 39- Peru\n 40- Philippines\n 41- Poland\n '
                                     '42- Portugal\n 43- Qatar\n 44- Romania\n 45- Russia\n'
                                     '46- Saudi Arabia\n 47- Singapore\n'
                                     '48- South Africa\n 49- South Korea\n 50- Spain\n'
                                     '51- Sweden\n 52- Switzerland\n 53- Taiwan\n 54- Thailand\n'
                                     '55- Turkey\n 56- Ukraine\n 57- United Arab Emirates\n'
                                     '58- United Kingdom\n 59- Uruguay\n 60- Venezuela\n 61- Vietnam\n'))
            if country_pick == 1:
                used_urls.append(urls[0])
            if country_pick == 2:
                used_urls.append(urls[1])
            if country_pick == 3:
                used_urls.append(urls[2])
            if country_pick == 4:
                used_urls.append(urls[3])
            if country_pick == 5:
                used_urls.append(urls[4])
            if country_pick == 6:
                used_urls.append(urls[5])
            if country_pick == 7:
                used_urls.append(urls[6])
            if country_pick == 8:
                used_urls.append(urls[7])
            if country_pick == 9:
                used_urls.append(urls[8])
            if country_pick == 10:
                used_urls.append(urls[9])
            if country_pick == 11:
                used_urls.append(urls[10])
            if country_pick == 12:
                used_urls.append(urls[11])
            if country_pick == 13:
                used_urls.append(urls[12])
            if country_pick == 14:
                used_urls.append(urls[13])
            if country_pick == 15:
                used_urls.append(urls[14])
            if country_pick == 16:
                used_urls.append(urls[15])
            if country_pick == 17:
                used_urls.append(urls[16])
            if country_pick == 18:
                used_urls.append(urls[17])
            if country_pick == 19:
                used_urls.append(urls[18])
            if country_pick == 20:
                used_urls.append(urls[19])
            if country_pick == 21:
                used_urls.append(urls[20])
            if country_pick == 22:
                used_urls.append(urls[21])
            if country_pick == 23:
                used_urls.append(urls[22])
            if country_pick == 24:
                used_urls.append(urls[23])
            if country_pick == 25:
                used_urls.append(urls[24])
            if country_pick == 26:
                used_urls.append(urls[25])
            if country_pick == 27:
                used_urls.append(urls[26])
            if country_pick == 28:
                used_urls.append(urls[27])
            if country_pick == 29:
                used_urls.append(urls[28])
            if country_pick == 30:
                used_urls.append(urls[29])
            if country_pick == 31:
                used_urls.append(urls[30])
            if country_pick == 32:
                used_urls.append(urls[31])
            if country_pick == 33:
                used_urls.append(urls[32])
            if country_pick == 34:
                used_urls.append(urls[33])
            if country_pick == 35:
                used_urls.append(urls[34])
            if country_pick == 36:
                used_urls.append(urls[35])
            if country_pick == 37:
                used_urls.append(urls[36])
            if country_pick == 38:
                used_urls.append(urls[37])
            if country_pick == 39:
                used_urls.append(urls[38])
            if country_pick == 40:
                used_urls.append(urls[39])
            if country_pick == 41:
                used_urls.append(urls[40])
            if country_pick == 42:
                used_urls.append(urls[41])
            if country_pick == 43:
                used_urls.append(urls[42])
            if country_pick == 44:
                used_urls.append(urls[43])
            if country_pick == 45:
                used_urls.append(urls[44])
            if country_pick == 46:
                used_urls.append(urls[45])
            if country_pick == 47:
                used_urls.append(urls[46])
            if country_pick == 48:
                used_urls.append(urls[47])
            if country_pick == 49:
                used_urls.append(urls[48])
            if country_pick == 50:
                used_urls.append(urls[49])
            if country_pick == 51:
                used_urls.append(urls[50])
            if country_pick == 52:
                used_urls.append(urls[51])
            if country_pick == 53:
                used_urls.append(urls[52])
            if country_pick == 54:
                used_urls.append(urls[53])
            if country_pick == 55:
                used_urls.append(urls[54])
            if country_pick == 56:
                used_urls.append(urls[55])
            if country_pick == 57:
                used_urls.append(urls[56])
            if country_pick == 58:
                used_urls.append(urls[57])
            if country_pick == 59:
                used_urls.append(urls[58])
            if country_pick == 60:
                used_urls.append(urls[59])
            if country_pick == 61:
                used_urls.append(urls[60])
            if country_pick == 62:
                used_urls.append(urls[61])


            if country_pick == 99:
                break
        except:
            print('Entered value is not a number !!!')
            exit()

except:
    print('Entered value is not a number !!!')
    exit()






# Loop to regenerate the URLs with the job title to search for it
for url in used_urls:
    if len(job_title_splitted) == 1:
        x = url + 'jobs?q=' + job_title_splitted[0]
        regenerated_links.append(x)
    elif len(job_title_splitted) == 2:
        x = url + 'jobs?q=' + job_title_splitted[0] + '+' + job_title_splitted[1]
        regenerated_links.append(x)
    elif len(job_title_splitted) == 3:
        x = url + 'jobs?q=' + job_title_splitted[0] + '+' + job_title_splitted[1] + '+' + job_title_splitted[2]
        regenerated_links.append(x)

print(urls)

print(regenerated_links)

######################### All together ##################################
#scraping code:
for link in regenerated_links:
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'html.parser')
    for div in soup.find_all(name="div", attrs={"class":"row"}):
        job_post = []
        #grabbing job title
        for a in div.find_all(name="a", attrs={"data-tn-element":"jobTitle"}):
            job_post.append(a["title"])
        #grabbing company name
        company = div.find_all(name="span", attrs={"class":"company"})
        if len(company) > 0:
            for b in company:
                job_post.append(b.text.strip())
        else:
          sec_try = div.find_all(name="span", attrs={"class":"result-link-source"})
          for span in sec_try:
            job_post.append(span.text)


        #grabbing location name
        c = div.findAll('span', attrs={'class': 'location'})
        for span in c:
            job_post.append(span.text)

        #grabbing summary text
        for a in div.find_all(name="a", attrs={"data-tn-element": "jobTitle"}):
            # Recreating the links that we will use to get the job description
            s = a["href"]
            des_ref = s[1:]
            re_link = str(link)
            at_pos = re_link.find('h')
            end_pos = re_link.find('j')
            host = re_link[at_pos : end_pos]
            des_link = host + des_ref

            # Calling and Parsing the recreated links
            des_page = requests.get(des_link)
            des_soup = BeautifulSoup(des_page.text, 'html.parser')

            # Getting the job description
            f = des_soup.find_all(name="div", attrs={"class": "jobsearch-jobDescriptionText"})
            for div in f:
                description = div.text
                job_post.append(description)
        final_info.append(job_post)
df = pd.DataFrame(final_info)
df.to_csv('data.csv')