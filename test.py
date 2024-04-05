import detectlanguage
import deepl
from openai import OpenAI


client = OpenAI(api_key="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")
# detectlanguage.configuration.api_key = '194f8dc31ce4bf0b1460ece885aad7ba'
text = '''
1.
Короткий опис:
Нелогічне розміщення логотипу та занадто великий розмір
Кроки відтворення:
* перейдіть на головну сторінку сайту
* зверніть увагу на розміщення логотипу в хедері
        Очікуваний результат:
                Логотип має гармонійно вписуватись в загальну композицію хедера
        Фактичний результат:
                Логотип завеликий і не вписується в композицію 
'''
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text,
)

response.write_to_file("output.mp3")
# lang = single_detection(text=text, api_key='9c4b0dc9-8236-414b-8ce6-450f06d9622c:fx')
# lang = detectlanguage.simple_detect(text)
# print(lang)
#
# translator = deepl.Translator('9c4b0dc9-8236-414b-8ce6-450f06d9622c:fx')

# for language in translator.get_source_languages():
#     if str.upper(lang) in language.code:
#         print('detected')

# print("Target languages:")
# for language in translator.get_target_languages():
#     print(language)
#
# print('--------')
# for lang in detectlanguage.languages():
#     print(lang['code'] + ' ' + lang['name'])

