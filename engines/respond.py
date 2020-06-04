import q
import adapters.conversationAdapter

def weatherIntentAdapter(intent, instance):
    return('weather')

def sportsIntentAdapter(intent, instance):
    return('sports')

def qLocalIntentAdapter(intent, instance):
    return('local')
    
intent_map = [
    {
        'intent': 'conversate',
        'handler': adapters.conversationAdapter.intentAdapter
    }, {
        'intent': 'weather',
        'handler': weatherIntentAdapter
    }, {
        'intent': 'sports',
        'handler': sportsIntentAdapter
    }, {
        'intent': 'local',
        'handler': qLocalIntentAdapter
    }
]

def create_context(intent):
    print('tada')

def remove_context(intent):
    print('tada')

def transform_context(fromerIntent, newIntent):
    print('tada')

def switch_context(newIntent):
    print('switch')

def response(intent):
    intentInstance = next(filter(lambda i: i['intent'] == intent.split('.')[0], intent_map)) 

    if(q.state.active().get('expecting').get('from') == intent): 
        intent = q.state.active().get('expecting').get('to')

    # if(q.state.active().get('expecting').get('from') == intent and q.state.active().get('expecting').get('type') == 'context'): 
        # transform_context(q.state.active(), q.state.active().get('expecting').get('to'))
        # # state mgmt / clean up
        # return response(intent)

    return intentInstance.get('handler')(intent, intentInstance)
