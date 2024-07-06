from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY')
    MONGODB_URI = os.getenv('MONGODB_URI')