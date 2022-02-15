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
limit  (filter by class limit)
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
            time = input("enter time and day (i.e. 16 m w) (time: 0-23 day: " + str(days) + "): ")
            schedule = schedule.time(time).sort('subject')

        elif command in ['s','subject']:
            subject = input("enter a subject:")
            schedule = schedule.subject([subject])

        #implemented by Siyu
        elif command in ['i', 'instructor']:
            instructor = input("enter an instructor:")
            schedule = schedule.lastname([instructor])
         #implemented by Siyu
        elif command in ['l', 'limit']:
            limit = int(input("enter a number of class limit:"))
            schedule = schedule.sizeAbove(limit)
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