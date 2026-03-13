#!/usr/bin/env python3
"""
Social Media Auto-Poster
自動發布推廣內容到各平台
"""

import os
import json
from datetime import datetime
from pathlib import Path

# 推廣內容庫
CONTENT_POSTS = {
    "twitter": [
        "🤖 還在花費大量時間寫內容？\n\n我整理了 10 個 AI Prompt 模板，讓你 10 分鐘完成一篇專業文章！\n\n👉 https://terryyehai.github.io/ai-digital-store/\n\n#AI #ChatGPT # productivity",
        
        "💡 告別加班！這 5 個 AI 工具讓你準時下班\n\n工作效率提升 10 倍的秘密武器\n\n🔗 https://terryyehai.github.io/ai-digital-store/\n\n#工作效率 #AI #自動化",
        
        "📝 寫不出好的商業郵件？\n\n我用 AI 幫你寫好了！\n\n商業郵件模板合集，讓回覆率提升 50%！\n\n👉 https://terryyehai.github.io/ai-digital-store/\n\n#商業 #Email #AI",
        
        "🎬 YouTuber 必備！\n\n影片腳本 AI 生成器，讓你告別剪輯瓶頸\n\n10 分鐘完成一個腳本\n\n🔗 https://terryyehai.github.io/ai-digital-store/\n\n#YouTube #影片腳本 #AI",
        
        "📊 Notion 用戶必看！\n\nAI 自動化工作流，讓你的 Notion 變身 AI 助手\n\n工作效率 up up！\n\n👉 https://terryyehai.github.io/ai-digital-store/\n\n#Notion #AI #生產力"
    ],
    
    "reddit": [
        {
            "subreddit": "r/ArtificialIntelligence",
            "title": "I built an AI digital product store - 47 products to boost your productivity",
            "body": """Hey everyone! 👋

I've been working on an AI digital product store that might help you with your daily work.

**What I built:**
- 47 AI-powered products (prompts, templates, automation scripts)
- Prices range from $7.99 to $19.99
- 100% generated and automated

**Products include:**
- Blog post prompts
- YouTube script generators
- Notion workflow templates
- Business email templates
- Python automation scripts

Would love to get your feedback!

Store link: https://terryyehai.github.io/ai-digital-store/

Let me know what you think! 🚀"""
        },
        
        {
            "subreddit": "r/productivity",
            "title": "10 AI tools that will save you 10 hours every week",
            "body": """What's up everyone! 

I've been testing AI tools for productivity and here are my top 10 picks:

1. Blog post AI writer
2. YouTube script generator  
3. Notion workflow automation
4. Business email templates
5. Social media calendar
6. Python automation scripts
7. ChatGPT cheat sheet
8. AI image guide
9. Notion AI setup
10. Midjourney master

All available at my store: https://terryyehai.github.io/ai-digital-store/

Which one would you be most interested in? 👇"""
        }
    ],
    
    "linkedin": [
        "🤖 AI 時代來臨，你準備好了嗎？\n\n我整理了 47 個 AI 數位產品，幫助你提升工作效率！\n\n從部落格寫作到 YouTube 腳本，從 Notion 自動化到商業郵件模板 - 應有盡有！\n\n🌐 https://terryyehai.github.io/ai-digital-store/\n\n#AI #數位轉型 #工作效率 #自動化"
    ]
}

class SocialMediaPoster:
    def __init__(self):
        self.post_log_file = "/home/terry/ai-products/post_log.json"
        self.post_log = self.load_log()
    
    def load_log(self):
        if os.path.exists(self.post_log_file):
            with open(self.post_log_file, 'r') as f:
                return json.load(f)
        return {"twitter": [], "reddit": [], "linkedin": []}
    
    def save_log(self):
        with open(self.post_log_file, 'w') as f:
            json.dump(self.post_log, f, indent=2)
    
    def post_twitter(self, content: str = None):
        """發布 Twitter（需要 API 整合）"""
        if content is None:
            import random
            content = random.choice(CONTENT_POSTS["twitter"])
        
        # 記錄發布
        self.post_log["twitter"].append({
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "status": "ready"
        })
        self.save_log()
        
        return {
            "platform": "twitter",
            "content": content,
            "status": "ready - 需要 API 整合"
        }
    
    def post_reddit(self, subreddit: str = None):
        """發布 Reddit（需要 API 整合）"""
        if subreddit is None:
            post = CONTENT_POSTS["reddit"][0]
        else:
            post = next((p for p in CONTENT_POSTS["reddit"] if p["subreddit"] == subreddit), CONTENT_POSTS["reddit"][0])
        
        self.post_log["reddit"].append({
            "subreddit": post["subreddit"],
            "title": post["title"],
            "body": post["body"],
            "timestamp": datetime.now().isoformat(),
            "status": "ready"
        })
        self.save_log()
        
        return {
            "platform": "reddit",
            "subreddit": post["subreddit"],
            "title": post["title"],
            "status": "ready - 需要 API 整合"
        }
    
    def generate_markdown_posts(self):
        """生成 Markdown 格式的推廣文章（可手動發布）"""
        posts = []
        
        # Twitter posts
        for i, content in enumerate(CONTENT_POSTS["twitter"], 1):
            posts.append(f"### Post {i} (Twitter/X)\n\n{content}\n")
        
        # Reddit posts
        for post in CONTENT_POSTS["reddit"]:
            posts.append(f"### Reddit - {post['subreddit']}\n\n**Title:** {post['title']}\n\n{post['body']}\n")
        
        # LinkedIn posts
        for i, content in enumerate(CONTENT_POSTS["linkedin"], 1):
            posts.append(f"### Post {i} (LinkedIn)\n\n{content}\n")
        
        return "\n---\n\n".join(posts)
    
    def get_next_post(self, platform: str = "twitter"):
        """獲取下一個待發布的內容"""
        if platform == "twitter":
            posted = set([p["content"] for p in self.post_log.get("twitter", [])])
            for content in CONTENT_POSTS["twitter"]:
                if content not in posted:
                    return content
        return None

if __name__ == "__main__":
    poster = SocialMediaPoster()
    
    print("=" * 60)
    print("📣 Social Media Auto-Poster")
    print("=" * 60)
    
    # 顯示待發布內容
    print("\n📝 推廣內容庫：")
    print(f"   Twitter: {len(CONTENT_POSTS['twitter'])} 篇")
    print(f"   Reddit: {len(CONTENT_POSTS['reddit'])} 篇")
    print(f"   LinkedIn: {len(CONTENT_POSTS['linkedin'])} 篇")
    
    # 生成 Markdown
    print("\n📄 生成 Markdown 推廣文章...")
    markdown = poster.generate_markdown_posts()
    
    # 保存
    output_file = "/home/terry/ai-products/SOCIAL_MEDIA_POSTS.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 📣 社交媒體推廣內容\n\n")
        f.write(f"生成時間：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        f.write(markdown)
    
    print(f"✅ 已保存到：{output_file}")
    
    # 顯示下一個 Twitter post
    next_post = poster.get_next_post("twitter")
    if next_post:
        print("\n📌 下一個 Twitter 推文：")
        print("-" * 40)
        print(next_post)
