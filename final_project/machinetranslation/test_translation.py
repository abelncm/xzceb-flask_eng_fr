import translator



def testFrenchToEnglish():
    translatedText = translator.frenchToEnglish('Bonjour')
    assert translatedText == 'Hello'
def testEnglishToFrench():
    translatedText = translator.englishToFrench('Hello')
    assert translatedText == 'Bonjour'

def testFrenchToEnglishNull():
    translatedText = translator.frenchToEnglish(None)
    assert translatedText == 'Please provide text for translation!'
def testEnglishToFrenchNull():
    translatedText = translator.englishToFrench(None)
    assert translatedText == 'Please provide text for translation!'