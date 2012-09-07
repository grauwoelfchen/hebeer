#!/usr/bin/env python

import os
from hebeer import app

if __name__ == '__main__':
    port  = int(os.environ.get('PORT', 5000))
    debug = int(os.environ.get('DEBUG', True))
    app.run(host='0.0.0.0', port=port, debug=debug)

