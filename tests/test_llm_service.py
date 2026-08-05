from services.llm_service import LLMService

llm = LLMService()

models = llm.client.models.list()

for model in models:
    print(model.name)