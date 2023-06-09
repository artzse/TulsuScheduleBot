from requests import post
from json import loads
from utilities.user_information import user_information

def get_grade_book(id, term):
    grade_book = user_information(id)['grade_book']

    url = 'https://tulsu.ru/progress/queries/GetMarks.php'
    payload = {f'SEARCH':{grade_book}}
    request = post(url, data=payload)
    raw = loads(request.text)['data']

    text = f"`Ваши баллы за {term} семестр:\n\n`"

    for i in raw:
        if i['TERM'] == term:
            text += f"`📚 {i['DISCIPLINE']}\n💯 {i['MARK']} баллов\n\n`".replace('None', '_')

    return text