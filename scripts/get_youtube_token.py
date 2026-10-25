"""
Run this ONCE on your own laptop to get your YouTube refresh token.

  pip install google-auth-oauthlib
  python scripts/get_youtube_token.py client_secret.json

A browser opens -> sign in with the channel's Google account -> allow.
Copy the 3 values it prints into GitHub Secrets. Never commit client_secret.json.
"""
import json
import sys

from google_auth_oauthlib.flow import InstalledAppFlow

if len(sys.argv) != 2:
    sys.exit("Usage: python scripts/get_youtube_token.py client_secret.json")

flow = InstalledAppFlow.from_client_secrets_file(
    sys.argv[1], scopes=["https://www.googleapis.com/auth/youtube.upload"])
creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")
client = json.load(open(sys.argv[1]))
client = client.get("installed") or client.get("web")

print("\nAdd these as GitHub Secrets:\n")
print("YT_CLIENT_ID      =", client["client_id"])
print("YT_CLIENT_SECRET  =", client["client_secret"])
print("YT_REFRESH_TOKEN  =", creds.refresh_token)
