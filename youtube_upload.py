#!/usr/bin/env python3
"""YouTube 上傳工具"""
import os
import sys
import json
import pickle
import requests
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

TOKEN_PATH = os.path.expanduser("~/.openclaw/workspace-dev/youtube/token.json")
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

def get_credentials():
    """獲取認證"""
    creds = None
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH, 'r') as f:
            token = json.load(f)
            
            from google.oauth2.credentials import Credentials
            creds = Credentials(
                token=token['access_token'],
                refresh_token=token.get('refresh_token'),
                token_uri='https://oauth2.googleapis.com/token',
                client_id='142777211047-8kk2cufu7gref15g3ajdspbo35vq1k48.apps.googleusercontent.com',
                scopes=SCOPES
            )
            
    return creds

def upload_video(file_path, title, description, tags=None):
    """上傳影片"""
    creds = get_credentials()
    
    if not creds or not creds.valid:
        print("❌ 認證失敗，請重新授權")
        return None
    
    # 檢查並刷新 token
    if creds.expired:
        creds.refresh(Request())
    
    youtube = build('youtube', 'v3', credentials=creds)
    
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags or [],
                "categoryId": "22",  # People & Blogs
            },
            "status": {
                "privacyStatus": "public",
                "selfDeclaredMadeForKids": False,
            }
        },
        media_body=file_path
    )
    
    response = request.execute()
    print(f"✅ 上傳成功: https://youtube.com/watch?v={response['id']}")
    return response['id']

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", required=True)
    parser.add_argument("--title", "-t", required=True)
    parser.add_argument("--description", "-d", default="")
    args = parser.parse_args()
    
    upload_video(args.file, args.title, args.description)
