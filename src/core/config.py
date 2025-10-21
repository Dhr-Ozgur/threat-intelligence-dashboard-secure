import os
from dotenv import load_dotenv

load_dotenv()

ABUSEIPDB_KEY = os.getenv("ABUSEIPDB_KEY")
VT_KEY = os.getenv("VT_KEY")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
