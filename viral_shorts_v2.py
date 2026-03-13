#!/usr/bin/env python3
"""
爆款 Shorts 生成器 V2.0
符合爆款廣告要素
"""

import os
from datetime import datetime

# 爆款 Shorts 腳本
VIRALS = [
    {
        "id": "viral_001",
        "type": "痛點型",
        "title": "又熬夜了？",
        "script": """又熬夜寫部落格了？凌晨兩點還在對著電腦，結果閱讀量還不到100？

我以前也這樣...

後來用 AI 輔助寫作，10 分鐘搞定一篇專業文章

這是我上週的收入截圖：單篇文章賺了 3000 多塊

想要的私信我，送你一個免費體驗
記得按讚訂閱！

#AI #部落格 #賺錢 #創業 #shorts""",
        "duration": 35,
        "scenes": [
            {"time": "0-3", "type": "痛點", "content": "深夜熬夜場景"},
            {"time": "3-10", "type": "問題", "content": "閱讀量低"},
            {"time": "10-20", "type": "解決", "content": "AI 10分鐘寫文"},
            {"time": "20-30", "type": "成果", "content": "收入截圖"},
            {"time": "30-35", "type": "CTA", "content": "免費體驗"}
        ]
    },
    {
        "id": "viral_002", 
        "type": "成果型",
        "title": "被動收入 527 美元",
        "script": """單日被動收入 527 美元！

我就靠這套 AI 數位產品模板

不用直播帶貨，不用拍影片
就是把模板上架到網店

已經有 47 個人購買了
名額有限，優惠碼只剩 3 個

#被動收入 #AI #賺錢 #數位產品 #創業 #shorts""",
        "duration": 30,
        "scenes": [
            {"time": "0-3", "type": "成果", "content": "收入截圖"},
            {"time": "3-12", "type": "產品", "content": "AI 模板展示"},
            {"time": "12-22", "type": "場景", "content": "上架網店"},
            {"time": "22-28", "type": "證明", "content": "47人購買"},
            {"time": "28-30", "type": "緊迫", "content": "只剩3個名額"}
        ]
    },
    {
        "id": "viral_003",
        "type": "教學型", 
        "title": "3個ChatGPT技巧",
        "script": """3 個讓 ChatGPT 輸出質量提升 10 倍的技巧

第一個：角色設定
告诉 AI 你是谁，它才能帮你

第二個：結構化輸出
指定格式，结果更精准

第三個：Few-shot 學習
给例子学习，效果更好

想要完整版？連結在描述區

#ChatGPT #AI #教學 #技巧 #shorts""",
        "duration": 35,
        "scenes": [
            {"time": "0-5", "type": "開頭", "content": "3個技巧"},
            {"time": "5-15", "type": "技巧1", "content": "角色設定"},
            {"time": "15-22", "type": "技巧2", "content": "結構輸出"},
            {"time": "22-30", "type": "技巧3", "content": "Few-shot"},
            {"time": "30-35", "type": "CTA", "content": "連結"}
        ]
    }
]

class ViralShortsGenerator:
    def __init__(self, output_dir: str = "/home/terry/ai-products/youtube_v2"):
        self.output_dir = output_dir
        self.virals = VIRALS
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(f"{output_dir}/scripts", exist_ok=True)
        os.makedirs(f"{output_dir}/scenes", exist_ok=True)
    
    def get_all_scripts(self):
        return self.virals
    
    def generate_script(self, viral_id: str = None):
        if viral_id is None:
            viral = self.virals[0]
        else:
            viral = next((v for v in self.virals if v["id"] == viral_id), self.virals[0])
        
        # 保存腳本
        script_file = f"{self.output_dir}/scripts/{viral['id']}_script.md"
        
        with open(script_file, 'w', encoding='utf-8') as f:
            f.write(f"# {viral['title']}\n\n")
            f.write(f"**類型**: {viral['type']}\n\n")
            f.write(f"## 腳本\n\n{viral['script']}\n\n")
            f.write(f"## 場景設計\n\n")
            for scene in viral["scenes"]:
                f.write(f"- {scene['time']} | {scene['type']} | {scene['content']}\n")
        
        return viral, script_file

if __name__ == "__main__":
    generator = ViralShortsGenerator()
    
    print("=" * 60)
    print("🎬 爆款 Shorts 生成器 V2.0")
    print("=" * 60)
    
    print("\n📝 可用腳本：")
    for v in VIRALS:
        print(f"  - {v['id']}: {v['title']} ({v['type']}, {v['duration']}秒)")
    
    # 生成第一個
    viral, script_file = generator.generate_script()
    print(f"\n✅ 已生成：{script_file}")
    print(f"\n📝 腳本內容：")
    print("-" * 40)
    print(viral["script"])
