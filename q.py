from collections import deque

state = {
    'active': False,
    'heard': deque( [] ),
    'responses': deque( [ ] ),

    'contexts': deque( [
        # {'id': '0', 'active': False,'entities': [], 'artifacts': [], 'last_updated': 'date', 'created_date': 'date'}, 
        # {'id': '1', 'active': True, 'entities': [{'class': 'PER', 'value': 'Anfa Abukar'}], 'artifacts': [{'ui': 'browser', 'payload': {'page': 'https://google.com'}, 'device': 'phone'}] 'expecting': {'from': 'common.affirm.positive', 'to': 'conversate.awknoldge'}, 'last_updated': 'date', 'created_date': 'date'}, 
    ] ),

    'devices': [
        {'name': 'phone', 'active': False}, 
        {'name': 'tablet', 'active': False}, 
        {'name': 'terminal1', 'active': False}, 
        {'name': 'terminal2', 'active': False}, 
        {'name': 'base', 'active': True}
    ],

    'profile': {
        'firstName': 'Anfa',
        'lastName': 'Abukar',
        'address': '3441 E43rd Ave',
        'city': 'Vancouver',
        'country': 'Canada',
        'phoneNumber': '416-875-4792'
    }
}

def active():
    return next((x for x in state.get('contexts') if x.value.get('active') == True), None)

