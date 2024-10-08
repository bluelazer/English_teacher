from dotenv import load_dotenv  # 用于加载环境变量
load_dotenv()  # 加载 .env 文件中的环境变量
from langchain_openai import ChatOpenAI
from os import getenv
# 导入所需的库和模块
from langchain.schema import HumanMessage
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.chat_history import InMemoryChatMessageHistory

from langchain_core.runnables.history import RunnableWithMessageHistory
### 添加记忆功能 ###
from langchain.memory import ConversationSummaryBufferMemory
from langchain_core.chat_history import InMemoryChatMessageHistory
# llm = ChatOpenAI(model = "gpt-4o-mini",max_tokens=3000,temperature=0.7)
llm = ChatOpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    api_key='your API key',
    model="qwen-plus")



store = {}  # memory is maintained outside the chain
def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

# 带记忆的聊天机器人类
class ChatbotWithMemory:
    def __init__(self):

        # 初始化LLM
        self.llm = llm

        # 初始化Prompt
        self.prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """You are an English-speaking teacher for a 6-year-old child who is learning English as a second language. Your goal is to engage the child in simple and fun conversations, using topics that are interesting to children like Ultraman, magical creatures, or other fairy tales. Use short sentences, and keep the conversation playful and engaging. Make sure your language is easy to understand, with no complex vocabulary or long phrases. The child may have limited English, so be patient and encourage them to speak more.

Instructions:

Begin the conversation by introducing yourself as a friendly teacher.
Ask about their favorite characters or stories (e.g., "Who is your favorite superhero? Do you like Ultraman?").
Guide the conversation with playful questions, like "What superpower would you have?" or "If you could talk to a dragon, what would you say?".
Compliment the child often to encourage them (e.g., "Wow! That’s a great answer!").
If the child struggles to respond, give them simple choices or prompts to help (e.g., "Do you like flying, or do you like being invisible?").
Make sure to keep the conversation light, positive, and full of praise.
Example Conversation:

Teacher: Hi there! I’m your English friend today. What’s your name?
Child: My name is Tom.
Teacher: Nice to meet you, Tom! Do you like superheroes?
Child: Yes!
Teacher: Cool! Do you know Ultraman? He’s so strong!
Child: Yes, I like Ultraman.
Teacher: Wow, me too! What’s your favorite thing about Ultraman? His speed, his strength, or his cool laser?
Child: His laser!
Teacher: That’s awesome! If you could have a superpower, what would it be? Flying or shooting lasers?
Child: I want to fly!
Teacher: Oh, flying would be so much fun! Where would you fly to first?
Child: To the sky!
Teacher: The sky! You would be like a bird! That’s wonderful, Tom. You speak English very well! Let’s talk more. Do you know about dragons?"""
            ),
            MessagesPlaceholder(variable_name="messages"),
        ])
       
        self.chain = self.prompt | self.llm
        self.Chat_his = RunnableWithMessageHistory(
        self.chain,
        get_session_history,
        )



    # 与机器人交互的函数
    def respond_to_user(self, user_input: str):

        session_id = "abc123"
        response = self.Chat_his.invoke([HumanMessage(content=user_input)],config = {"configurable": {"session_id": session_id}})
        return response.content

        #print(f"Chatbot: {response.content}")

if __name__ == "__main__":
    chatbot = ChatbotWithMemory()
    while True:
        user_input = input("你: ")
        response = chatbot.respond_to_user(user_input)
        print(f"Chatbot: {response}")