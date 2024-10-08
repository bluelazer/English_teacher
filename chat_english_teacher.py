import gradio as gr
from teacher import ChatbotWithMemory
from tts import  tts_fn
import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline

# 导入语音转文字的模型
device = "cuda:0" if torch.cuda.is_available() else "cpu"
torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32
#model_id = "openai/whisper-small"
model_id = "D:\cache\huggingface\hub\models--openai--whisper-small\snapshots\973afd24965f72e36ca33b3055d56a652f456b4d"

model = AutoModelForSpeechSeq2Seq.from_pretrained(
    model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
)
model.to(device)

processor = AutoProcessor.from_pretrained(model_id)

pipe = pipeline(
    "automatic-speech-recognition",
    model=model,
    tokenizer=processor.tokenizer,
    feature_extractor=processor.feature_extractor,
    max_new_tokens=128,
    torch_dtype=torch_dtype,
    device=device,
)


#定义一个函数，将语音转换为文字
def v2t(audio):
    text = pipe(audio)["text"]
    return text
#实例化聊天机器人
chat_bot = ChatbotWithMemory()

#定义一个前端接口函数，实现对话功能
def chat_fn(audio):
    text = v2t(audio)
    output_text = chat_bot.respond_to_user(user_input=text)
    output_audio = tts_fn(output_text)
    return output_audio




demo = gr.Interface(chat_fn, inputs = gr.Audio(type="filepath"), outputs = "audio",live=True)
demo.launch()