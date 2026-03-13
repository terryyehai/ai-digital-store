#!/usr/bin/env python3
"""YouTube OAuth 授權"""
import os
import json

CLIENT_ID = '142777211047-8kk2cufu7gref15g3ajdspbo35vq1k48.apps.googleusercontent.com'
CLIENT_SECRET = 'GOCSPX-AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'  # 需要替換
REDIRECT_URI = 'http://localhost:8080'
TOKEN_PATH = os.path.expanduser("~/.openclaw/workspace-dev/youtube/token.json")

# 設備碼流程
def device_flow():
    """設備碼授權"""
    import requests
    
    # 獲取設備碼
    resp = requests.post(
        "https://oauth2.googleapis.com/device/code",
        data={
            "client_id": CLIENT_ID,
            "scope": "https://www.googleapis.com/auth/youtube.upload"
        }
    )
    
    device_code = resp.json()
    print(f"\n請在瀏覽器打開: {device_code['verification_url']}")
    print(f"輸入代碼: {device_code['user_code']}")
    print("\n等待授權...")
    
    # 輪詢 token
    import time
    while True:
        time.sleep(5)
        token_resp = requests.post(
            "https://oauth2.googleapis.com/token",
            data={
                "client_id": CLIENT_ID,
                "client_secret": CLIENT_SECRET,
                "code": device_code['device_code'],
                "grant_type": "http://oauth.net/grant_type/device/1.0"
            }
        )
        
        if token_resp.status_code == 200:
            token = token_resp.json()
            
            # 保存 token
            os.makedirs(os.path.dirname(TOKEN_PATH), exist_ok=True)
            with open(TOKEN_PATH, 'w') as f:
                json.dump(token, f)
            
            print("✅ 授權成功!")
            return token
        elif token_resp.status_code == 400:
            error = token_resp.json()
            if error.get('error') == 'slow_down':
                time.sleep(5)
                continue
            elif error.get('error') == 'expired':
                print("❌ 授權超時，請重新運行")
                return None
        else:
            print(f"錯誤: {token_resp.text}")

if __name__ == "__main__":
    print("開始 OAuth 設備碼授權...")
    result = device_flow()
    if result:
        print(f"\nToken 已保存到: {TOKEN_PATH}")
