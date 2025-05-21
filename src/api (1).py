from dotenv import load_dotenv
from os import getenv
from openai import OpenAI
from openai import Client
load_dotenv()



global file
class AI_Api:

    def __init__(self, desctiption: str, max_tokens: int):
        self.client = OpenAI(api_key=getenv("API_KEY"))
        self.description: str = desctiption
        self.max_tokens: int = max_tokens


    def search(self, query: str) -> str:
        file = self.client.files.create(
            file=open('data.txt', 'rb'),
            purpose='assistants'
        )
        assistant = self.client.beta.assistants.create(
            name='Катя',
            description=self.description,
            model="gpt-3.5-turbo-1106",
            tools=[{'type':'retrieval'}],
            file_ids=[file.id])
        thread=self.client.beta.threads.create(
            messages=[
                {
                    'role': 'user',
                    'content':'Посмотри информацию из файла',
                    'file_ids':[file.id]
                }
            ]
        )
        assistant_id=assistant.id
        self.thread_id=thread.id
        message_create=self.client.beta.threads.messages.create(
            role='user',
            thread_id=self.thread_id,
            content=query
        )

        return message_create.data[0].content[0].text.value
