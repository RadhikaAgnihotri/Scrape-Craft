from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    #print(content)
    soup = BeautifulSoup(content,  'lxml')
    # courses_html_tags = soup.find_all('h5')
    # for course in courses_html_tags:
    #     print(course.text) #prints in a much better, readable format
    course_cards = soup.find_all('div', class_='card') #since class is python keyword an underscore helps bs4 to understand that you are relating to the class of html attribute
    for course in course_cards:
        #print(course) #print(course.h5)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        
        print(f'{course_name} costs {course_price}' )    