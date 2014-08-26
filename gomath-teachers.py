import csv
from collections import Counter

teacher_list = []
with open('teacherfile.csv', 'rbU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        teacher_dict = {}
        teacher_dict = {
                'action':               row[0],
                'role':                 row[1],
                'school_pid':           row[2], 
                'value':                row[3],
                'username':             row[4],
                'password':             row[5],
                'first_name':           row[6],
                'middle':               row[7],
                'last_name':            row[8],
                'grade':                row[9],
                'student_id':           row[10],
                'gender':               row[11],
                'ethnicity':            row[12],
                'special_services':     row[13],
                'english_proficiency':  row[14],
                'special_conditions':   row[15],
                'economic_status':      row[16],
                'email':                row[17],
                'active/inactive':      row[18],
                'class_name':           row[19],
                'class_grade':          row[20],
                'products':             row[21],
                'period':               row[22],
                'description':          row[23],
                'add_students':         row[24],
                'remove_students':      row[25]
        }
        teacher_list.append(teacher_dict)

usernames = []
username_dup = []
for t in teacher_list:
    if t['username'] in usernames:
        username_dup.append(t['username'])
    usernames.append(t['username'])

username_dup = list(set(username_dup))

updated_teachers = []

for u in username_dup:
    grades = []
    for t in teacher_list:
        if t['username'] == u:
            grades.append(t['grade'])
            teacher_to_update = t
    grades = '|'.join(grades)
    teacher_to_update['grade'] = grades
    updated_teachers.append(teacher_to_update)

remove=[]
for u in updated_teachers:
    for t in teacher_list:
        if u['username'] == t['username']:
            remove.append(t['username'])

final_teachers = []
for t in teacher_list:
    if not t['username'] in remove:
        final_teachers.append(t)

for u in updated_teachers:
    final_teachers.append(u)

keys = ['action', 'role', 'school_pid', 'value', 'username', 'password', 
        'first_name', 'middle', 'last_name', 'grade', 'student_id', 'gender',
        'ethnicity', 'special_services', 'english_proficiency', 
        'special_conditions', 'economic_status', 'email', 'active/inactive', 
        'class_name', 'class_grade', 'products', 'period', 'description',
        'add_students', 'remove_students']

f=open('teacherlistupdated.csv', 'wb')
dict_writer = csv.DictWriter(f, keys, lineterminator='\n')
dict_writer.writer.writerow(keys)
dict_writer.writerows(final_teachers)



