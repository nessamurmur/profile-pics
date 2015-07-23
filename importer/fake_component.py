import random


def _fetch_from_fake_service():
    n = random.randint(0, 100)
    if n < 40:
        return random.choice(images)
    elif n < 80:
        return None
    else:
        raise NameError


def fetch_user(user_id):
    try:
        return _fetch_from_fake_service()
    except:
        return None


images = [u'http://giphy.com/gifs/cat-voF1Droc9eISs', u'http://giphy.com/gifs/cat-fail-cartoon-vdSCURsOBxZmM', u'http://giphy.com/gifs/cat-funny-cute-qGkAAgZMJzRhm', u'http://giphy.com/gifs/cat-love-QK88ua7gxmyT6', u'http://giphy.com/gifs/cat-funny-cute-8faOrJIiNGRd6', u'http://giphy.com/gifs/cat-kitten-10pSeSHjy0OMV2', u'http://giphy.com/gifs/high-five-cat-vnnoqBjIrJ73y', u'http://giphy.com/gifs/cat-cute-adorable-O3GJk0JA3dDsk', u'http://giphy.com/gifs/kitten-cat-black-and-white-bYdol5sZWOBqM', u'http://giphy.com/gifs/cat-reaction-D0AO75Kn7Biq4', u'http://giphy.com/gifs/cat-day-office-5r5J4JD9miis', u'http://giphy.com/gifs/cat-animated-sukitte-iinayo-Q5B2NZm2Vj5lu', u'http://giphy.com/gifs/cat-cute-L2djWse2JlucU', u'http://giphy.com/gifs/cat-flcl-tid0uMdWMTBh6', u'http://giphy.com/gifs/cats-gatos-nl5wVNRJSWcO4', u'http://giphy.com/gifs/cat-cats-KHUrQZ1xouiv6', u'http://giphy.com/gifs/illustration-2d-animation-fA5fRLP2rMtP2', u'http://giphy.com/gifs/confused-cats-lovers-h1QtppV27igCI', u'http://giphy.com/gifs/china-cats-catgifs-a4WCILDLxigww', u'http://giphy.com/gifs/cat-cats-B6odR0DhsStfW', u'http://giphy.com/gifs/office-boots-uUsyXxEgM5TnW', u'http://giphy.com/gifs/cats-JQRKxN6GuhGhy', u'http://giphy.com/gifs/lol-fight-come-at-me-bro-Rt3xpiV6KfibC', u'http://giphy.com/gifs/cats-synchronized-BOaEM3TkP1uUg', u'http://giphy.com/gifs/lol-cats-squirrel-LVAFReXII8Qec']
