from supabase import create_client
from supabase.lib.client_options import ClientOptions
import os

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_ROLE_KEY"),
    options=ClientOptions(auto_refresh_token=True, persist_session=True),
)

admin_auth_client = supabase.auth.admin