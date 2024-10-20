from supabase import Client, create_client
from dotenv import load_dotenv
import os

load_dotenv()


def supabase():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    return supabase
