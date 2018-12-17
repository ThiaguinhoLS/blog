# -*- coding: utf-8 -*-

from app import app
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
load_dotenv(dotenv_path)

