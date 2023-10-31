"""Init for the main module"""
from os import path
from dotenv import load_dotenv

load_dotenv(path.join(path.dirname(__file__), "..", ".env"))
