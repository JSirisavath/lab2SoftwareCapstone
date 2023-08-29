# Try excepts for an api

import requests


question = input('Enter you question for the magic 8 ball: ')


# Url with users' question
magic_8_ball_url = f'https://magic-8-ball-mctc.uc.r.appspot.com/magic/JSON/{question}'
try:
    # Response back from the url (promise) and parse it into a json format

    response = requests.get(magic_8_ball_url).json()
    print(response)
    # response_text = requests.get(magic_8_ball_url).text

    # print(response_text)

    answer = response['magic']['answer']

    print(f'The magic 8 ball says... {answer} ')

except Exception as e:
    print(e)
    print('Sorry, can not contact magic 8 ball now!')
