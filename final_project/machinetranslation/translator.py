import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
import urllib3

urllib3.disable_warnings()


load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)




def translate(text, model_id):
    if text == None:
        return 'Please provide text for translation!'
    translation = language_translator.translate(
        text=text,
        model_id=model_id).get_result()
    # print(json.dumps(translation, indent=2, ensure_ascii=False))
    return translation['translations'][0]['translation']

def englishToFrench(englishText):
    return translate(englishText, 'en-fr')


def frenchToEnglish(frenchText):
    return translate(frenchText, 'fr-en')