import urllib.request
import bs4 as BeautifulSoup4

# load in teacher ids
teacher_ids = open("teacher_ids", 'r').read().split('\n')
headers = {'User-Agent': 'Mozilla/5.0'}

for tid in teacher_ids:
    url = 'https://www.ratemyprofessors.com/ShowRatings.jsp?tid=' + tid

    # grab and parse the html
    req = urllib.request.Request(url, None, headers)

    with urllib.request.urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup4.BeautifulSoup(html, 'html.parser')

    # extract data
    fname     = soup.find('h1',  attrs={'class': 'profname'}).contents[1].text.strip()
    lname     = soup.find('h1',  attrs={'class': 'profname'}).contents[5].text.strip()
    faculty   = soup.find('div', attrs={'class': 'result-title'}).contents[0].strip().replace('Professor in the ','').replace(' department','')
    grade     = soup.find('div', attrs={'class': 'grade'}).text.strip()
    takeAgain = soup.find('div', attrs={'class': 'breakdown-section'}).contents[3].text.strip().replace('%','')
    diff      = soup.find('div', attrs={'class': 'breakdown-section difficulty'}).contents[1].text.strip()
    reviews   = soup.find('div', attrs={'class': 'table-toggle', 'data-table': 'rating-filter'}).text.strip().replace(' Student Ratings','')

    # write to file
    with open('data', 'a') as the_file:
        the_file.write(lname + ',' + fname + ',' + faculty + ',' + grade + ',' + takeAgain + ',' + diff + ',' + reviews + '\n')
