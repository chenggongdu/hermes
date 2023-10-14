import pinecone

# youlu
api_key = 'XX'
environment = 'us-west4-gcp-free'
index_name = 'hermes-pd'


class PineconeSetting:
    def __init__(self):
        """initialize pinecone"""
        pinecone.init(
            api_key=api_key,  # find at app.pinecone.io
            environment=environment,  # next to api key in console
        )
