import random
import cowsay

questions = [
    {
        'question': 'What part of Africa is Kenya in?',
        'answer': ('b', 'East'),
        'choices': [('a', 'North'), ('b', 'East'), ('c', 'South'), ('d',
                                                                    'West')]
    },
    {
        'question':
        'How many people live in Kenya?',
        'answer': ('a', '49.7 million'),
        'choices': [('a', '49.7 million'), ('b', '22.5 million'),
                    ('c', '65.1 million'), ('d', '10.3 million')]
    },
    {
        'question':
        'What is the capital of Kenya?',
        'answer': ('c', 'Nairobi'),
        'choices': [('a', 'Lagos'), ('b', 'Mombasa'), ('c', 'Nairobi'),
                    ('d', 'Dakar')]
    },
    {
        'question':
        'Aside from English, what\'s the national language?',
        'answer': ('b', 'Swahili'),
        'choices': [('a', 'kinyarwanda'), ('b', 'Swahili'), ('c', 'Igbo'),
                    ('d', 'Setswana')]
    },
]

glow_ups = ['Good job', 'Well played', 'Flyin colors']

correct_answers = 0
total_asked = 0


def game_mistress():
    while questions:
        prompt = questions.pop()
        ask_question(prompt)
        new = raw_input('Want another one? y/n ')
        if new == 'n':
            print '\n' * 3
            print 'Asante (thanks) for playing %s ' % name
            get_results()
            quit()
        else:
            continue
    print '\n' * 3
    print 'Ouf looks like that\'s all she wrote bruh - good job getting your learning on!'
    get_results()


def ask_question(prompt):
    global correct_answers, total_asked
    question, answer, choices = [
        prompt[k] for k in ('question', 'answer', 'choices')
    ]

    cowsay.cow(question)
    for choice, description in choices:
        print choice, description
    guess = raw_input('whatcha think? ')

    if guess.lower() == answer[0]:
        print cowsay.tux('Yaaasss! %s, you right, you right it\'s %s' %
                         (random.choice(glow_ups), answer[1]))
        correct_answers += 1
    else:
        print cowsay.tux('Oops! Nice try but it\'s %s' % answer[1])
    total_asked += 1


def get_results():
    print 'You got %s out of %s' % (correct_answers, total_asked)


if __name__ == '__main__':
    print '*' * 65
    print '**'
    print '**'
    print '**   Welcome to this round of Jeopardy: Kenya edition'
    print '**'
    print '**'
    print '*' * 65
    print ''
    print('please Enter your name to get started... ')
    name = raw_input('> ')
    print ''
    print 'Sawa! Twende %s' % (name or 'knowledge seeker')
    print '\n' * 5
    game_mistress()
