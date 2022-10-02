from machinetranslation import translator


def test_french_to_english():
    translated_text = translator.french_to_english('Bonjour')
    assert translated_text == 'Hello'
def test_english_to_french():
    translated_text = translator.english_to_french('Hello')
    assert translated_text == 'Bonjour'

def test_french_to_english_null():
    translated_text = translator.french_to_english('')
    assert translated_text == 'Please provide text for translation!'
def test_english_to_french_null():
    translated_text = translator.english_to_french('')
    assert translated_text == 'Please provide text for translation!'
