import q
from deeppavlov import build_model

sentimentModel = build_model('./engines/intent/sentiment-config.json', download=False)
entitiesModel = build_model('./engines/intent/entities-config.json', download=False)
similarityModel = build_model('./engines/intent/similarties-config.json', download=False)
knowledgeModel = build_model('./engines/intent/knowledge-cofig.json', download=False)
summirizationModel = build_model('./engines/intent/summirization-config.json', download=False)

def create_context():
    print('add shit for bert')

def summirize_conent():
    summary = summirizationModel(['text'])
    print(summary)

def answer_from_context():
    answer = knowledgeModel(['DeepPavlov is library for NLP and dialog systems.'], ['What is DeepPavlov?'])
    # del knowledgeModel
    print(answer)

def get_similaraties():
    predictor = similarityModel.pipe[-1][-1]
    candidates = ['auto insurance', 'life insurance', 'home insurance']
    predictor.rebuild_responses(candidates)
    closest = similarityModel(['how much to pay for auto insurance?'])
    print(closest)

def get_entities():
    entites = entitiesModel(['Bob Ross lived in Florida'])
    print(entites)

def read_sentiment():
    sentiment = sentimentModel(["What is the weather in Boston today?"])
    print(sentiment)
