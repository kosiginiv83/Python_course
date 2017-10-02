import os
import requests


def translate_it(text):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/\
                translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    
    params = {
        'key': key,
        'lang': 'ru-en',
        'text': text,
    }
    response = requests.get(url, params=params).json()
    return ' '.join(response.get('text', []))



def files():
   
    
    # file_original =
    # file_translate =
    language_need = 'ru'
    a = translate_it(file_original, result_dir, language_need)
    print(a)


if __name__ == '__main__':
    files()
