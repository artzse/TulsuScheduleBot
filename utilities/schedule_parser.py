def schedule_parser(id, date):
    from utilities.user_information import user_information
    from json import loads
    from requests import post
    import datetime

    group_index = user_information(id)['group_index']

    url = 'https://tulsu.ru/schedule/queries/GetSchedule.php'
    payload = {f'search_field': 'GROUP_P', 'search_value': {group_index}}
    request = post(url, data=payload)
    raw = loads(request.text)

    weekdays = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда', 3: 'Четверг', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}
    schedule_text = f"`{weekdays[datetime.datetime.strptime(date, '%d.%m.%Y').weekday()]} [{date[0:5]}]`"

    count = 0

    for i in raw:
        if i['DATE_Z'] == date:

            count += 1

            if i['PREP'] == None:
                lecturer = 'Не найдено'
            else:
                lecturer = f"{i['PREP'].split()[0]} {i['PREP'].split()[1][0]}. {i['PREP'].split()[2][0]}."

            schedule_text += f"`\n\n························\n\n🕐 {i['TIME_Z']} | {i['AUD']}" \
                             f"\n📚 {i['DISCIP']}" \
                             f"\n📝 {i['KOW']} {i['GROUPS'][0]['PRIM']}" \
                             f"\n👨‍🏫 {lecturer}`"

    if count == 0:
        schedule_text += '\n\nНичего не найдено!'

    return schedule_text

schedule_parser(433639463, '22.05.2023')