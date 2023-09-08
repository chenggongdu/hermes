from typing import List


class PineconeDB:
    from config.vectorstores import PineconeVS
    pinecone_vs = PineconeVS()

    def __init__(self):
        print('PineconeDB init')
        self.vectorstore = PineconeDB.pinecone_vs.vectorstore

    def insert(self, texts: list, ids: list):
        insert_ids = self.vectorstore.add_texts(texts=texts, ids=ids)
        print("insertIds:", insert_ids)

    def delete(self, ids: List[str]):
        self.vectorstore.delete(ids)


class OtherDB:
    def __init__(self):
        print('OtherDB init')
