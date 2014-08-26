import csv
from collections import Counter

teacher_list = []
with open('class.csv', 'rbU') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        teacher_dict = {}
        teacher_dict = {
                'action':               row[0],
                'role':                 row[1],
                'school_pid':           row[2], 
                'username':             row[3],
                'password':             row[4],
                'first_name':           row[5],
                'middle':               row[6],
                'last_name':            row[7],
                'grade':                row[8],
                'student_id':           row[9],
                'gender':               row[10],
                'ethnicity':            row[11],
                'special_services':     row[12],
                'english_proficiency':  row[13],
                'special_conditions':   row[14],
                'economic_status':      row[15],
                'email':                row[16],
                'active/inactive':      row[17],
                'class_name':           row[18],
                'class_grade':          row[19],
                'products':             row[20],
                'period':               row[21],
                'description':          row[22],
                'add_students':         row[23],
                'remove_students':      row[24]
        }
        teacher_list.append(teacher_dict)

usernames = []
username_dup = []
for t in teacher_list:
    if t['username'] in usernames:
        username_dup.append(t['username'])
    usernames.append(t['username'])

usernames = list(set(username_dup))

class_list = []
for t in teacher_list:
    if t['username'] in usernames:
        new_dict = {'username': t['username']}
        class_list.append(new_dict)

class_list = [dict(tupleized) for tupleized in set(
                tuple(item.items()) for item in class_list)]

for c in class_list:
    classes = []
    products = []
    for t in teacher_list:
        if c['username'] == t['username']:
            classes.append({'class_name': t['class_name'],
                            'description': t['description']})
            products.append(t['products'])
    c['classes'] = classes
    c['products'] = products

for c in class_list:
    classes = c['classes']
    classes = [dict(tupleized) for tupleized in set(
                tuple(item.items()) for item in classes)]
    c['classes'] = classes
    c['products'] = list(set(c['products']))
    c['products'] = '|'.join(c['products'])

final = []
for c in class_list:
    for t in teacher_list:
        if c['username'] == t['username']:
            for cl in c['classes']:
                final.append(
                        {
                            'action':               t['action'],
                            'role':                 t['role'],
                            'school_pid':           t['school_pid'], 
                            'username':             c['username'],
                            'password':             t['password'],
                            'first_name':           t['first_name'],
                            'middle':               t['middle'],
                            'last_name':            t['last_name'],
                            'grade':                t['grade'],
                            'student_id':           t['student_id'],
                            'gender':               t['gender'],
                            'ethnicity':            t['ethnicity'],
                            'special_services':     t['special_services'],
                            'english_proficiency':  t['english_proficiency'],
                            'special_conditions':   t['special_conditions'],
                            'economic_status':      t['economic_status'],
                            'email':                t['email'],
                            'active/inactive':      t['active/inactive'],
                            'class_name':           cl['class_name'],
                            'class_grade':          t['class_grade'],
                            'products':             c['products'],
                            'period':               t['period'],
                            'description':          cl['description'],
                            'add_students':         t['add_students'],
                            'remove_students':      t['remove_students']
                        }
                )

final = [dict(tupleized) for tupleized in set(
            tuple(item.items()) for item in final)]

keys = ['action', 'role', 'school_pid', 'value', 'username', 'password', 
        'first_name', 'middle', 'last_name', 'grade', 'student_id', 'gender',
        'ethnicity', 'special_services', 'english_proficiency', 
        'special_conditions', 'economic_status', 'email', 'active/inactive', 
        'class_name', 'class_grade', 'products', 'period', 'description',
        'add_students', 'remove_students']

f=open('classlistupdated.csv', 'wb')
dict_writer = csv.DictWriter(f, keys, lineterminator='\n')
dict_writer.writer.writerow(keys)
dict_writer.writerows(final)



