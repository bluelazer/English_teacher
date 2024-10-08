import pyaudio
import dashscope
from dashscope.audio.asr import (Recognition, RecognitionCallback,
                                 RecognitionResult)

dashscope.api_key = 'sk-f160f9b3fb444ea390504d34811d6a99'
class Callback(RecognitionCallback):
    def on_complete(self) -> None:
        # 识别完成
        return None
    def on_error(self, result: RecognitionResult) -> None:
        # 错误处理
        return None

    def on_event(self, result: RecognitionResult) -> None:
        # 处理识别结果
        return None
 
callback = Callback()

recognition = Recognition(model='paraformer-realtime-v2',
                          format='wav',
                          sample_rate=16000,
                          callback=callback,
                          language_hints='en-US',)



def v2t(audio):
    result = recognition.call(audio)
    text = ""
    for a in result.get_sentence():

        text += a["text"] + " "
    return text

if __name__ == '__main__':
    path = r"C:\Users\lazer\AppData\Local\Temp\gradio\96e79ac1fc76e43cb55f19cda1085e0028caf092ebd470c6d73f871e5c8dc35d\audio.wav"
    a = v2t(path)
    print(a)