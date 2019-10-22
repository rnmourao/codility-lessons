import requests
from bs4 import BeautifulSoup, NavigableString, Tag
import pandas as pd
import os


main = 'https://app.codility.com'

# get lessons links
url = 'https://app.codility.com/programmers/lessons/'

response = requests.get(url)

page = BeautifulSoup(response.text, 'html5lib')

lessons = page.find_all('a', class_='lesson-item')

ls = []
for lesson in lessons:
    url = main + lesson['href']
    
    names = lesson.find_all('div')
    name = ' - '.join([n.text for n in names])

    ls.append({'url': url, 'lesson': name})

lessons_df = pd.DataFrame(ls)

# get tasks
ls = []
for i, row in lessons_df.iterrows():
    os.mkdir(row['lesson'])
    
    url = row['url']
    response = requests.get(url)

    page = BeautifulSoup(response.text, 'html5lib')

    try:
        with open(row['lesson'] + '/' + row['lesson'].split(' - ')[1] + '.pdf', 'wb') as wb: 
            readings = page.find('a', id ='readings')['href']
            r = requests.get(readings, allow_redirects=True)
            wb.write(r.content)
    except TypeError:
        pass

    tasks = page.find_all('div', class_='task-box')

    for task in tasks:
        title = task.find('h4', class_='title')

        a = title.find('a')
        name = a.text.replace('\n', '').strip()

        view = task.find('a', class_='view-button')
        view_url = main + view['href']

        ls.append({'lesson': row['lesson'], 'task': name, 'url': view_url})

tasks_df = pd.DataFrame(ls)

for i, row in tasks_df.iterrows():
    url = row['url']
    response = requests.get(url)

    page = BeautifulSoup(response.text, 'html5lib')

    description = page.find('div', id='brinza-task-description')

    text = description.get_text()

    with open(row['lesson'] + '/' + row['task'] + '.py', 'w') as w:
        w.write('"""' + text + '"""')
