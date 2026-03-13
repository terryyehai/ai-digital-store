#!/usr/bin/env python3
"""
YouTube OAuth 授權助手 - 全新設定
"""

# 請 Terry 在 Google Cloud Console 完成以下步驟：
# 1. 建立新專案
# 2. 啟用 YouTube Data API v3
# 3. 建立 OAuth 2.0 憑證（桌面應用程式）
# 4. 下載 client_secret.json
# 5. 將內容貼到下方

OAUTH_SETUP_INSTRUCTIONS = """
============================================================
🔧 YouTube API OAuth 全新設定教學
============================================================

步驟 1: 建立 Google Cloud 專案
--------------------------------
1. 打開 https://console.cloud.google.com/
2. 點擊「選取專案」→「建立新專案」
3. 名稱輸入「YouTube-Upload-自動化和成」
4. 建立

步驟 2: 啟用 YouTube Data API
--------------------------------
1. 點擊「API 和服務」→「程式庫」
2. 搜尋「YouTube Data API v3」
3. 點擊「啟用」

步驟 3: 建立 OAuth 憑證
--------------------------------
1. 點擊「API 和服務」→「憑證」
2. 點擊「建立憑證」→「 OAuth 用戶端 ID」
3. 應用程式類型選擇「桌面應用程式」
4. 名稱輸入「YouTube-Uploader」
5. 建立
6. 下載 JSON → 複製 client_secret 給 AI

步驟 4: 發布 OAuth 同意畫面
--------------------------------
1. 點擊「OAuth 同意畫面」
2. 點擊「發布應用程式」
3. 選擇「公開」or 新增測試用戶

============================================================
"""

print(OAUTH_SETUP_INSTRUCTIONS)
