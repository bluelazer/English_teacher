# coding=utf-8

import sys
import datetime
import dashscope
from dashscope.audio.tts import SpeechSynthesizer

dashscope.api_key = 'sk-f160f9b3fb444ea390504d34811d6a99'




def tts_fn(text):
    current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    result = SpeechSynthesizer.call(model='sambert-eva-v1',
                                    text=text,
                                    sample_rate=16000)
    if result.get_audio_data() is not None:
    # 使用当前时间作为文件名的一部分
        file_name = f'output_{current_time}.wav'
        
        with open(file_name, 'wb') as f:
            f.write(result.get_audio_data())
        
        print(f'SUCCESS: get audio data: {sys.getsizeof(result.get_audio_data())} bytes in {file_name}')
    return file_name
