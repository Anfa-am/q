import  q
import  engines.speak

responses = {
    'greet': {
        # hey q, hey buddy, yo q!, hello
        'initiate': { 
            'execute': None,
            'templates': ['Hey! what\'s up?', 'What\'s suh my du', 'Yo maine', 'Hi, how are you?'],
            'expect': []
        },

        'objective': {
            'execute': None,
            'templates': ['So what can I help you with', 'What are we doing today', 'So what are we doing', 'Ok, whats happening'],
            'expect': []
        },

        'objective_urge': {
            'execute': None,
            'templates': ['Cmon lets do something', 'boo comon dummy', 'stop it, lets go bitch ass', 'you suck... you really suck'],
            'expect': [{'from': '!NEUTRAL!', 'to': 'conversate.greet.objective'}, {'from': '!POSITIVE!', 'to': 'conversate.greet.objective'}, {'from': '!NEGATIVE!', 'to': 'conversate.objective_urge'}],
        },

        'inqury': {
            # hey q whats up, whats happening, whats good
            'generic': { 
                'execute': None,
                'templates': ['Nothing much, want the latest?', 'Hey! not much. How are you?'],
                'expect': [{'from': 'generic.affirm', 'to': 'knowledge.news.headlines'}, {'from':  'generic.decline', 'to': 'conversate.greet.objective'}]
            },

            # hey q how have you been, how are you doing, how are you feeling, what's new with you
            'personal': { 
                'execute': None,
                'templates': ['not bad thanks', 'i\'m good thanks!'],
                'expect': []
            },

            # I'm fine, how are you?
            'response_personal': { 
                'execute': None,
                'templates': ['glad to hear, I\'m not bad thanks', 'i\'m good thanks!'],
                'expect': [{'from': '!POSITIVE!', 'to': 'conversate.greet.objective'}]
            },
  
            #...im good thanks, nothing much
            'response_positive': { 
                'execute': None,
                'templates': ['Awesome!', 'good good!', 'Nice, so what are we doing'],
                'expect': []
            },

            # not feeling so good |
            'response_negative': { 
                'execute': None,
                'templates': ['I\'m sorry to hear that', 'let\'s try and work and forget about it'],
                'expect': [{'from': '!NEUTRAL!', 'to': 'conversate.greet.objective'}, {'from': '!POSITIVE!', 'to': 'conversate.greet.objective'}, {'from': '!NEGATIVE!', 'to': 'conversate.objectiv_urge'}]
            }
        }
    },

    'character_reveal': {
        #what are your dreams, any palns for you tonight
        'fasiceous': { 
            'execute': None,
            'templates': ['Might take over the world. IDK feeling cute', 'I\'ll share your browser history with your contacts.'],
            'expect': [{'from': '!TIMEOUT!', 'to': 'conversate.insulted'}]
        },

        #what do you think, do you have any thoughts on this?
        'opinion': {
            'execute': None,
            'templates': ['I\'m gonna sit this one out', 'ummm... no comment'],
            'expect': []
        }, 
    },

    'insulted': {
        #really, wow!, I never!, 
        'execute': None,
        'templates': ['Yeah, thats what I thought', 'ummhmm', 'HELLOO!!?!'],
        'expect': []
    },

    'insult': {
        #goddamn asshole, son of a bitch, oh tits!
        'generic': {
            'execute': None,
            'templates': ['hey watch the langugae', 'excuse me'],
            'expect': []
        },

        #you muppet, you cunt
        'personal': {
            'execute': None,
            'templates': ['ill take physical form and kick ur ass boi', 'you good?', 'umm hello?'],
            'expect': []
        },
    },

    #ok, talk later | bye | peace out
    'good_bye': {
        'execute': None,
        'templates': ['easy fam', 'alright see ya soon'],
        'expect': []
    }
}

# def intentAdapter(intent, instance):

def intentAdapter(intent, instance):
    intent.split('.')[1]
    #run execution, save return as data
    #regesiter expectation
    engines.speak.articulate(templates, data)
    return('hi')

