#!/usr/bin/env python3
"""
AI YouTube Shorts Generator
自動生成 YouTube Shorts 影片
"""

import os
import json
from datetime import datetime

# Shorts 腳本模板
SHORTS_TEMPLATES = [
    {
        "title": "用 AI 10分鐘寫完一篇部落格",
        "script": """你有沒有想過，10 分鐘就能寫完一篇專業部落格？

只要用對 AI Prompt，產出高品質內容超簡單！

今天分享 3 個我常用的 AI 寫作 Prompt：

第一個，部落格大綱 Prompt
第二個，內容生成 Prompt  
第三個，SEO 優化 Prompt

想知道怎麼用嗎？點擊下方連結看看！

#AI #ChatGPT #寫作 #部落格 #教學""",
        "duration": 45
    },
    {
        "title": "5 個 AI 工具讓你準時下班",
        "script": """還在天天加班？

這 5 個 AI 工具，讓我每天準時下班！

1. AI 寫作助手 - 10 分鐘寫完一篇文章
2. AI 郵件生成器 - 自動回覆客戶郵件
3. AI 影片腳本 - YouTuber 必備
4. AI 圖片生成 - 設計師福音
5. AI 自動化腳本 - 搞定重複工作

想要這些工具？連結在描述區！

#AI #工作效率 #自動化 #工具""",
        "duration": 50
    },
    {
        "title": "YouTube 腳本 AI 生成器",
        "script": """YouTuber 們必看！

用這個 AI 工具，10 分鐘生成一支影片腳本！

包含：
- 開場鉤子
- 內容大綱
- 時間戳
- 結束 CTA

#YouTube #AI #腳本 #教學 #創作""",
        "duration": 40
    },
    {
        "title": "Notion AI 工作流教學",
        "script": """Notion 用戶必看！

用 AI 自動化你的 Notion 工作流！

自動：
- 生成每日任務
- 追蹤專案進度
- 整理會議記錄
- 製作每週報告

#Notion #AI #自動化 #生產力""",
        "duration": 55
    },
    {
        "title": "ChatGPT 必備 Prompt 技巧",
        "script": """ChatGPT 輸出不好？那是因為你 Prompt 寫錯！

3 個必學的 Prompt 技巧：

1. 角色設定
2. 結構化輸出
3. Few-shot 學習

學會這三招，AI 輸出品質立刻提升！

#ChatGPT #AI #Prompt #教學""",
        "duration": 48
    },
    {
        "title": "AI 幫我賺了多少錢？",
        "script": """用 AI 數位產品，我一個月賺了多少？

從 0 到有的變現之路...

#AI #變現 #數位產品 #創業""",
        "duration": 45
    },
    {
        "title": "免費 AI Prompt 分享",
        "script": """免費送你好幾個 AI Prompt！

用在部落格、郵件、社群貼文都適用

連結在描述區，快去拿！

#AI #Prompt #免費""",
        "duration": 30
    },
    {
        "title": "AI 時代必備技能",
        "script": """這 3 個 AI 技能，你必須會！

1. Prompt 編寫
2. AI 工具使用
3. 自動化整合

不會的趕快學起來！

#AI #技能 #教學""",
        "duration": 35
    }
]

class YouTubeShortsGenerator:
    def __init__(self, output_dir: str = "/home/terry/ai-products/youtube"):
        self.output_dir = output_dir
        self.templates = SHORTS_TEMPLATES
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(f"{output_dir}/scripts", exist_ok=True)
        os.makedirs(f"{output_dir}/voices", exist_ok=True)
        os.makedirs(f"{output_dir}/images", exist_ok=True)
        os.makedirs(f"{output_dir}/videos", exist_ok=True)
    
    def get_all_templates(self):
        """獲取所有模板"""
        return self.templates
    
    def get_next_script(self):
        """獲取下一個待製作的腳本"""
        log_file = f"{self.output_dir}/production_log.json"
        
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                log = json.load(f)
            completed = log.get("completed", [])
        else:
            completed = []
        
        for i, template in enumerate(self.templates):
            if template["title"] not in completed:
                return template, i
        
        return None, -1
    
    def generate_script_file(self, template_index: int = None):
        """生成腳本文件"""
        if template_index is None:
            template, idx = self.get_next_script()
        else:
            template = self.templates[template_index]
            idx = template_index
        
        if template is None:
            return None
        
        # 保存腳本
        script_file = f"{self.output_dir}/scripts/{idx+1}_{template['title']}.md"
        
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(f"# {template['title']}\n\n")
            f.write(f"## 腳本\n\n{template['script']}\n\n")
            f.write(f"## 預估時長\n\n{template['duration']} 秒\n")
        
        return {
            "index": idx,
            "title": template["title"],
            "script_file": script_file,
            "duration": template["duration"]
        }
    
    def mark_completed(self, title: str):
        """標記為已完成"""
        log_file = f"{self.output_dir}/production_log.json"
        
        if os.path.exists(log_file):
            with open(log_file, 'r') as f:
                log = json.load(f)
        else:
            log = {"completed": [], "in_progress": []}
        
        if title not in log["completed"]:
            log["completed"].append(title)
        
        with open(log_file, 'w') as f:
            json.dump(log, f, indent=2)
    
    def get_status(self):
        """獲取製作狀態"""
        template, idx = self.get_next_script()
        
        return {
            "total": len(self.templates),
            "next_index": idx + 1 if idx >= 0 else None,
            "next_title": template["title"] if template else None,
            "completed": len([t for t in self.templates if self.get_status() and True])  # 简化
        }

if __name__ == "__main__":
    generator = YouTubeShortsGenerator()
    
    print("=" * 60)
    print("🎬 AI YouTube Shorts Generator")
    print("=" * 60)
    
    # 顯示所有腳本
    print("\n📝 可用 Shorts 腳本：")
    print("-" * 40)
    for i, t in enumerate(SHORTS_TEMPLATES, 1):
        print(f"{i}. {t['title']} ({t['duration']}秒)")
    
    # 獲取下一個
    next_script, idx = generator.get_next_script()
    if next_script:
        print(f"\n▶️  下一個待製作：")
        print(f"   標題：{next_script['title']}")
        print(f"   時長：{next_script['duration']}秒")
        
        # 生成腳本文件
        result = generator.generate_script_file()
        print(f"\n✅ 腳本已保存：{result['script_file']}")
