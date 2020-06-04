import random
import  q

from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.websocket import SynthesizeCallback

authenticator = IAMAuthenticator('r0V3pXuPjLiNnDOVKJzn0UC2nVyPqV4m2OpnG3-wP23k')

voice = TextToSpeechV1(authenticator=authenticator)
voice.set_service_url('https://stream.watsonplatform.net/text-to-speech/api')

file_path = 'test.ogg'
class Say(SynthesizeCallback):
    def __init__(self):
        SynthesizeCallback.__init__(self)
        self.fd = open(file_path, 'ab')

    def on_connected(self):
        print('Connection was successful')

    def on_error(self, error):
        print('Error received: {}'.format(error))

    def on_content_type(self, content_type):
        print('Content type: {}'.format(content_type))

    def on_timing_information(self, timing_information):
        print(timing_information)

    def on_audio_stream(self, audio_stream):
        self.fd.write(audio_stream)

    def on_close(self):
        self.fd.close()
        print('Done synthesizing. Closing the connection')

vocals = Say()

def say(s):
    words = 'There is no data for the session  <break time="300ms"/> have you tried refreshing?'
    voice.synthesize_using_websocket(words, vocals, accept='audio/ogg', voice='en-US_LisaVoice')

def tweak_saml_params(template):
    #for each saml param adjust by +- ~30%
    return template

def interpolate(template, values):
    return sentance + value

def articulate(templates, data):
    random_template = templates[0]
    interpolated = interpolate(random_template, data)
    tweak_saml_params(random_template)

