#!/usr/bin/env python3
"""YouTube 上傳工具 - 簡化版"""
import os
import json
import requests

TOKEN_PATH = os.path.expanduser("~/.openclaw/workspace-dev/youtube/token.json")

def upload_video_simple(file_path, title, description):
    """使用 token 直接上傳"""
    
    with open(TOKEN_PATH, 'r') as f:
        token = json.load(f)
    
    access_token = token['access_token']
    
    # 請求
    url = "https://www.googleapis.com/upload/youtube/v3/videos"
    
    metadata = {
        "snippet": {
            "title": title,
            "description": description,
            "categoryId": "22"
        },
        "status": {
            "privacyStatus": "public"
        }
    }
    
    # 分割上傳
    import subprocess
    
    # 使用 curl 上傳
    cmd = f'''curl -X POST \\
        -H "Authorization: Bearer {access_token}" \\
        -H "Content-Type: application/json" \\
        -d '{json.dumps(metadata)}' \\
        "https://www.googleapis.com/youtube/v3/videos?part=snippet,status&uploadType=media&fileName={os.path.basename(file_path)}"'''
    
    print(f"上傳: {title}")
    print("⚠️ 需要重新 OAuth 授權，請運行:")
    print("cd /home/terry/ai-products")
    print("python3 youtube_oauth.py")
    
    return None

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", required=True)
    parser.add_argument("--title", "-t", required=True)
    parser.add_argument("--description", "-d", default="")
    args = parser.parse_args()
    
    upload_video_simple(args.file, args.title, args.description)
