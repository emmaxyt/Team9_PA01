# pylint: disable=trailing-whitespace
'''
course_search is a Python script using a terminal based menu to help
students search for courses they might want to take at Brandeis
'''

from time import time
from schedule import Schedule
import sys

schedule = Schedule()
schedule.load_courses()
schedule = schedule.enrolled(range(5,1000)) # eliminate courses with no students

TOP_LEVEL_MENU = '''
quit
reset
term  (filter by term)
above  (filter by class limit that is above a certain number)
below (filter by class limit that is below a certain number)
course (filter by coursenum, e.g. COSI 103a)
instructor (filter by instructor)
subject (filter by subject, e.g. COSI, or LALS)
title  (filter by phrase in title)
description (filter by phrase in description)
timeofday (filter by day and time, e.g. meets at 11 on Wed)
'''

terms = {c['term'] for c in schedule.courses}
days = ('m', 'tu', 'w', 'th', 'f')

def topmenu():
    '''
    topmenu is the top level loop of the course search app
    '''
    global schedule
    while True:         
        command = input(">> (h for help) ")
        if command=='quit':
            return
        elif command in ['h','help']:
            print(TOP_LEVEL_MENU)
            print('-'*40+'\n\n')
            continue
        elif command in ['r','reset']:
            schedule.load_courses()
            schedule = schedule.enrolled(range(5,1000))
            continue

        elif command in ['t', 'term']:
            term = input("enter a term:"+str(terms)+":")
            schedule = schedule.term([term]).sort('subject')

        # Implemented by Tianjun Cai
        elif command in ['c', 'course']:   
            course = input("enter a couse (i.e. COSI 12B):")
            schedule = schedule.course(course).sort('term')

        elif command in ['s','subject']: 
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])

        # Implemented by Tianjun Cai
        elif command in ['time', 'timeofday']: 
            time_course = input("enter time and day (i.e. 16 m w) (time: 0-23 day: " + str(days) + "): ")
            schedule = schedule.time(time_course).sort('subject')

        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])

        # Implemented by Siyu Yang
        elif command in ['i', 'instructor']:
            instructor = input("enter an instructor:")
            schedule = schedule.lastname([instructor])
         # Implemented by Siyu Yang
        elif command in ['a', 'above']:
            above = int(input("enter a number of class limit:"))
            schedule = schedule.sizeAbove(above)
        elif command in ['b', 'below']:
            below = int(input("enter a number of class limit:"))
            schedule = schedule.sizeBelow(below)
        
        # Implemented by Emma Xu 
        elif command in ['d', 'description']:
            # gives the courses containing the input phrase in their descriptions
            phrase = input("enter a phrase in course description:")
            schedule = schedule.description(phrase)
        # Implemented by Emma Xu
        elif command in ['n', 'name']:
            # gives the courses containing the input phrase in their names
            phrase = input("enter a phrase in course name: ")
            schedule = schedule.phraseInName(phrase)

       # Implemented by Yuxuan Liu
        elif command in ['t', 'title']:
            # filter by title
            phrase = input("enter a phrase in course title: ")
            schedule = schedule.title(phrase)

        else:
            print('command',command,'is not supported')
            continue

        print("courses has",len(schedule.courses),'elements',end="\n\n")
        print('here are the first 10')
        for course in schedule.courses[:10]:
            print_course(course)
        print('\n'*3)

def print_course(course):
    '''
    print_course prints a brief description of the course 
    '''
    print(course['subject'],course['coursenum'],course['section'],
          course['name'],course['term'],course['instructor'])

if __name__ == '__main__':
    topmenu()
