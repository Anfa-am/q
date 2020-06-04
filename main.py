import q
import engines.listen
import engines.classify
import engines.respond
# import engines.speak
# import engines.abilities
# import engines.feelings

def talk(response):
    print(response)
    # engines.speak.say(response)

def think():
    if(len(q.state.get('heard')) > 0):
        perdiction = engines.classify.understand(q.state.get('heard').popleft())
        intent = perdiction[0][0]
        confidence = perdiction[0][1]
        print(intent, confidence)
        if(confidence > 0.8):
            talk(engines.respond.response(intent))

def hear(said):
    q.state.get('heard').append(said)
    think()
