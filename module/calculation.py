import json
import configparser

configparser = configparser.ConfigParser()
configparser.read('config/config.ini')
material_type = configparser['config']['material_type']

def get_course_list(s):
    response = s.get('https://api.nnn.ed.nico/v2/my_courses?service=n_school')
    response_info = json.loads(response.content)
    course_list = []
    for course in response_info['services'][0]['courses']:
        course_info = [course['id'], course['title']]
        course_list.append(course_info)

    #print(course_list)#! debug
    return course_list

def get_chapter_list(s, course_id):
    response = s.get(f'https://api.nnn.ed.nico/v2/material/courses/{course_id}')
    response_info = json.loads(response.content)
    chapter_list = []
    for chapter in response_info['course']['chapters']:
        chapter_info = [chapter['id'], chapter['title']]
        chapter_list.append(chapter_info)

    #print(chapter_list)#! debug
    return chapter_list

def get_length(s, course_id, chapter_id):
    response = s.get(f'https://api.nnn.ed.nico/v2/material/courses/{course_id}/chapters/{chapter_id}')
    response_info = json.loads(response.content)
    lengths = []
    for response in response_info['chapter']['sections']:
        if response['resource_type'] == 'movie' and response['material_type'] == material_type:
            lengths.append(response['length'])
        elif material_type == 'all':
            lengths.append(response['length'])

    total_seconds = sum(lengths)
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return f'{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}'

def get_all_chapter_length(s):
    course_list = get_course_list(s)
    result = []  # 結果を保存するリスト

    for course in course_list:
        chapter_list = get_chapter_list(s, course[0])
        for chapter in chapter_list:
            length = get_length(s, course[0], chapter[0])
            result.append((course[1], chapter[1], length))
        result.append(('','',''))

    return result