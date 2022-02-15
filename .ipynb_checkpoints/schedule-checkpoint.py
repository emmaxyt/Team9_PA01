# pylint: disable=no-else-return
'''
schedule maintains a list of courses with features for operating on that list
by filtering, mapping, printing, etc.
'''

import json

class Schedule():
    '''
    Schedule represent a list of Brandeis classes with operations for filtering
    '''
    def __init__(self,courses=()):
        ''' courses is a tuple of the courses being offered '''
        self.courses = courses

    def load_courses(self):
        ''' load_courses reads the course data from the courses.json file'''
        print('getting archived regdata from file')
        with open("courses20-21.json","r",encoding='utf-8') as jsonfile:
            courses = json.load(jsonfile)
        for course in courses:
            course['instructor'] = tuple(course['instructor'])
            course['coinstructors'] = [tuple(f) for f in course['coinstructors']]
        self.courses = tuple(courses)  # making it a tuple means it is immutable

    def lastname(self,names):
        ''' lastname returns the courses by a particular instructor last name'''
        return Schedule([course for course in self.courses if course['instructor'][1] in names])

    def email(self,emails):
        ''' email returns the courses by a particular instructor email'''
        return Schedule([course for course in self.courses if course['instructor'][2] in emails])

    def term(self,terms):
        ''' term returns the courses in a list of term'''
        return Schedule([course for course in self.courses if course['term'] in terms])

    def enrolled(self,vals):
        ''' enrolled filters for enrollment numbers in the list of vals'''
        return Schedule([course for course in self.courses if course['enrolled'] in vals])

    def subject(self,subjects):
        ''' subject filters the courses by subject '''
        return Schedule([course for course in self.courses if course['subject'] in subjects])

    def sort(self,field):
        if field == 'subject':
            return Schedule(sorted(self.courses, key= lambda course: course['subject']))
        elif field == 'term':
            return Schedule(sorted(self.courses, key= lambda course: course['term'], reverse=True))
        else:
            print("can't sort by "+str(field)+" yet")
            return self
    
    # Implemented by Tianjun Cai
    def course(self, courseinfo):
        code = courseinfo.strip().split()
        return Schedule([course for course in self.courses if course['code'] == code])
    def time(self, timeinfo):
        purify_timeinfo = timeinfo.strip().split()
        time = purify_timeinfo[0]
        date = purify_timeinfo[1:]
        # Checks if times is empty, if start time matches with time,and if days is the same
        return Schedule([course for course in self.courses if course['times'] != []
        and course['times'][0]['start'] == int(time)*60
        and set(date) == set(course['times'][0]['days'])])
    
    # Implemented by Siyu Yang
    def sizeAbove(self,num):
        #size filter by the num entered, find the course with size above num
        return Schedule([course for course in self.courses if course['limit']is not None and course['limit']>num])
