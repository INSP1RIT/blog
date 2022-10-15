import requests as r
from flask_babel import _
from flask import current_app


def get_translation(text,source_language,dest_language):
    response = r.get("https://translate.yandex.net/api/v1.5/tr.json/translate" ,
                     params={"key": current_app.config['YA_TRANSLATOR_KEY'],
                     "text":text,"lang" : f"{source_language}-{dest_language}"}
    )
    return response


def translate(text,source_language,dest_language):
    if 'YA_TRANSLATOR_KEY' not in current_app.config or \
            not current_app.config['YA_TRANSLATOR_KEY']:
        return _("Error: the translation service is not configured")
    r = get_translation(text,source_language,dest_language)
    if r.status_code != 200:
        return _("Error: the translation service failed")

    return r.json()['text'][0]