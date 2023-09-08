import pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone

from config.setting import Setting

Setting()


class PineconeVS:

    def __init__(self):
        self.index_name = 'hermes-pd'
        self.embeddings = OpenAIEmbeddings()
        self.index = pinecone.Index(self.index_name)
        self.vectorstore = Pinecone(
            self.index, self.embeddings.embed_query, 'text')
