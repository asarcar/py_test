#!/usr/bin/env python3

import os
import pytest
import sys

# non-standard library imports
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    myPlatform = sys.platform
    return "Hello, welcome from '%s'!" % myPlatform

app.run(host="0.0.0.0", port=50100, debug=True)