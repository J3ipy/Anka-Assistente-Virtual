import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import pywhatkit


audio = sr.Recognizer()
maquina = pyttsx3.init()


def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo...')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'anka' in comando:
                comando = comando.replace('anka', '')
                maquina.say(comando)
                maquina.runAndWait()
    except:
        print('Microfone não estar ok!')
    return comando


def comando_voz_user():
    comando = executa_comando()

    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H : %M')
        maquina.say('Agora são: ' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, 2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
    elif 'me conte uma piada' in comando:
        maquina.say(pyjokes.get_joke())
        maquina.runAndWait()

    elif 'toque' in comando:
        musica = comando.replace('toque', '')
        resultado = pywhatkit.playonyt(musica)
        maquina.say('Tocando música:')
        maquina.runAndWait()
    else:
        maquina.say('Por favor repita o comando!')


while True:
    comando_voz_user()
