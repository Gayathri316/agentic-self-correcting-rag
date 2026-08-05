from services.llm_service import LLMService

llm = LLMService()

for model in llm.client.models.list():
    print(model.name)