"""
Generate OAuth 2.0 Token for DME Equipment Docs

This script helps you authenticate with your Google account and generate
the OAuth credentials needed for Streamlit Cloud deployment.

Run this script locally ONCE to get your OAuth credentials.
"""

import os
import json
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/documents',
    'https://www.googleapis.com/auth/drive'
]

def generate_oauth_credentials():
    """Generate OAuth 2.0 credentials"""

    print("=" * 70)
    print("DME Equipment Docs - OAuth Token Generator")
    print("=" * 70)
    print()

    # Check if credentials.json exists
    if not os.path.exists('credentials.json'):
        print("❌ ERROR: credentials.json not found!")
        print()
        print("Please follow these steps:")
        print()
        print("1. Go to: https://console.cloud.google.com/apis/credentials")
        print("2. Create OAuth 2.0 Client ID (Desktop app)")
        print("3. Download the JSON file")
        print("4. Rename it to 'credentials.json'")
        print("5. Put it in this folder")
        print("6. Run this script again")
        print()
        return

    creds = None

    # Check if we have a token already
    if os.path.exists('token.json'):
        print("📁 Found existing token.json")
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If no valid credentials, let user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            print("🔄 Refreshing expired token...")
            creds.refresh(Request())
        else:
            print("🔐 Starting OAuth authentication flow...")
            print("📌 A browser window will open - please log in with your Google account")
            print()
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials for future use
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
        print("✅ Token saved to token.json")

    # Print credentials for Streamlit secrets
    print()
    print("=" * 70)
    print("✅ SUCCESS! Copy the following to your Streamlit secrets:")
    print("=" * 70)
    print()
    print("[google_oauth]")
    print(f'token = "{creds.token}"')
    print(f'refresh_token = "{creds.refresh_token}"')
    print(f'token_uri = "{creds.token_uri}"')
    print(f'client_id = "{creds.client_id}"')
    print(f'client_secret = "{creds.client_secret}"')
    print()
    print("=" * 70)
    print()
    print("📋 Instructions:")
    print("1. Copy the [google_oauth] section above")
    print("2. Go to your Streamlit Cloud app settings")
    print("3. Paste it in the Secrets section")
    print("4. Replace the existing [gcp_service_account] section")
    print("5. Save and redeploy")
    print()
    print("✅ Your app will now use YOUR Google account!")
    print()

if __name__ == "__main__":
    generate_oauth_credentials()
