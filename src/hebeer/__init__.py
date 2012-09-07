from flask import Flask

class _DefaultSettings(object):
    USERNAME = 'hebeer'

app = Flask(__name__)
app.config.from_object(_DefaultSettings)
del _DefaultSettings

def init():
    """ TODO: Setup """
    pass

import hebeer.ui
