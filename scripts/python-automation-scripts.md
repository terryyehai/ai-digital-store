# 🐍 Python Automation Scripts Bundle

## 用途
自動化日常任務的 Python 腳本集合

## 腳本列表

### 1. Auto-Email-Sender.py
```python
"""
AI-Powered Email Automation Script
功能：根據名單自動發送個性化郵件
"""

import smtplib
from email.mime.text import MIMEText
import csv

# 配置
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your@email.com"
APP_PASSWORD = "your-app-password"

def send_email(to_email, subject, body):
    """發送郵件"""
    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.send_message(msg)

def send_bulk_emails(csv_file, subject_template, body_template):
    """批量發送個性化郵件"""
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            personalized_body = body_template.format(**row)
            send_email(row['email'], subject_template, personalized_body)
            print(f"已發送至: {row['email']}")

if __name__ == "__main__":
    # 使用示例
    csv_file = "leads.csv"
    subject = "🎉 {name}，您的個人化方案已經準備好！"
    body = """
    <html>
    <body>
        <h2>親愛的 {name}，</h2>
        <p>感謝您對我們的產品感興趣！</p>
        <p>根據您的需求，我們為您準備了個人化方案：</p>
        <ul>
            <li>方案類型：{product_type}</li>
            <li>預算範圍：{budget}</li>
        </ul>
        <p>點擊此處查看詳情：<a href="{link}">立即查看</a></p>
    </body>
    </html>
    """
    send_bulk_emails(csv_file, subject, body)
```

### 2. Social-Media-Poster.py
```python
"""
Social Media Auto-Poster
功能：定時發布到多個社群平台
"""

import schedule
import time
import json
from datetime import datetime

# 支援的平台
PLATFORMS = ['twitter', 'linkedin', 'instagram', 'facebook']

class SocialPoster:
    def __init__(self, config_file):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
    
    def post_to_twitter(self, content, image=None):
        """發布到 Twitter"""
        # Twitter API 整合代碼
        pass
    
    def post_to_linkedin(self, content, image=None):
        """發布到 LinkedIn"""
        # LinkedIn API 整合代碼
        pass
    
    def schedule_post(self, content, platform, post_time):
        """排程發布"""
        schedule.every().day.at(post_time).do(
            getattr(self, f"post_to_{platform}"), content=content
        )
    
    def run(self):
        """運行排程器"""
        while True:
            schedule.run_pending()
            time.sleep(60)

if __name__ == "__main__":
    poster = SocialPoster('config.json')
    poster.schedule_post("Hello World!", "twitter", "09:00")
    poster.run()
```

### 3. Data-Scraper.py
```python
"""
Web Data Scraper
功能：從網站自動抓取數據
"""

import requests
from bs4 import BeautifulSoup
import csv
import time

class WebScraper:
    def __init__(self, headers=None):
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def scrape(self, url, selector):
        """抓取網頁數據"""
        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.select(selector)
    
    def scrape_to_csv(self, url, selectors, output_file):
        """抓取並保存為 CSV"""
        data = []
        elements = self.scrape(url, selectors)
        
        for elem in elements:
            data.append({
                'text': elem.get_text(strip=True),
                'href': elem.get('href', '')
            })
        
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['text', 'href'])
            writer.writeheader()
            writer.writerows(data)
        
        return len(data)

# 使用示例
scraper = WebScraper()
count = scraper.scrape_to_csv(
    'https://example.com/products',
    '.product-item',
    'products.csv'
)
print(f"已抓取 {count} 條數據")
```

---

## 💰 定價：$19.99

版本：1.0 | 更新：2026-03-13
