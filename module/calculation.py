import json


#def get_courses(s):

def get_length(s, course_id, chapter_id):
    response = s.get(f'https://api.nnn.ed.nico/v2/material/courses/{course_id}/chapters/{chapter_id}')
    response_info = json.loads(response.content)
    lengths = []
    for response in response_info['chapter']['sections']:
        if response['resource_type'] == 'movie':
            lengths.append(response['length'])

    total_seconds = sum(lengths)
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    return f'{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}'