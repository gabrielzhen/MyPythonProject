import speech_recognition as sr

def recognize_speech(recognizer,microphone):
    print('请开始你的表演：')
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)

    try:
        text=recognizer.recognize_bing(audio)
    except Exception as e:
        text=e
    return text 
        
if __name__=='__mian__':
    text=input('input a english centanc')

    recognizer=sr.Recognizer()
    microphone=sr.Microphone()

    speech_text=recognize_speech(recognizer,microphone)

    while speech_text!=None and text.lower()!=speech_text.lower():
        print(speech_text)
        speech_text=recognize_speech(recognizer,microphone)
    if speech_text:
        print(speech_text,'correct')
         