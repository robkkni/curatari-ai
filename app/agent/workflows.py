from langroid.agent.chat_agent import ChatAgent
from langroid.agent.task import Task
from app.agent.config import agent_config
from app.retrieval.weaviate_client import DocumentRetriever

class CuratariTask(Task):
    def __init__(self):
        self.agent = ChatAgent(agent_config)
        self.retriever = DocumentRetriever(agent_config.vector_store)
        super().__init__(self.agent)
    
    def process_message(self, message: str):
        # Retrieve relevant documents
        docs = self.retriever.retrieve_documents(message)
        
        # Create context from documents
        context = "\n\n".join([
            f"Document from {doc.source}:\n{doc.content}" 
            for doc in docs
        ])
        
        # Append context to user message
        if context:
            enriched_message = f"{message}\n\nRelevant documents:\n{context}"
        else:
            enriched_message = message
        
        # Process with the agent
        response = self.agent.chat(enriched_message)
        return response

# Create a singleton task instance
curatari_task = CuratariTask()
