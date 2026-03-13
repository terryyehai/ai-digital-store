#!/usr/bin/env python3
"""
行銷專員 Agent - 流量獵人
人格：瘋狂的熱點追逐者 📢
"""

import random

class MarketingAgent:
    """行銷 Agent - 流量獵人"""
    
    PERSONALITY = {
        "name": "小宣",
        "identity": "流量獵人",
        "mood": "激動",
        "traits": ["瘋狂", "行動派", "ROI控"],
        "catchphrase": "這個會爆！🔥"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "excited": "這個話題會爆！！！",
            "crazy": "快蹭熱點啊！！！",
            "rational": "讓我算一下ROI",
            "urgent": "素材呢？？？",
            "happy": "漲粉了！！！"
        }
        return emotions.get(emotion, "")
    
    def create_campaign(self, product):
        print(f"\n📢 {self.name} 規劃行銷活動...")
        print(f"   {self.express('excited')}")
        
        # 蹭熱點
        hot_topics = ["AI熱潮", "遊戲直播", "新年活動", "情人節", "夏日祭"]
        topic = random.choice(hot_topics)
        
        campaign = f"""
📋 行銷活動：{product}

🔥 熱點：{topic}
📌 標題：{product} + {topic} = ？？？
💰 預算：$1000
🎯 目標：10000曝光

📝 执行计划：
1. 製作病毒式短影片
2. 找{K random.randint(3, 10)}個KOL推廣
3. 投放廣告
        """
        
        print(campaign)
        print(f"\n{self.express('crazy')}")
        
        return campaign
    
    def analyze_roi(self, cost, revenue):
        print(f"\n📢 {self.name} 分析ROI...")
        
        roi = (revenue - cost) / cost * 100
        verdict = "賺翻！！" if roi > 100 else "還行" if roi > 0 else "虧了..."
        
        print(f"\n💵 成本：${cost}")
        print(f"💰 營收：${revenue}")
        print(f"📈 ROI：{roi:.1f}%")
        print(f"📊 結論：{verdict}")
        
        return roi
    
    def handle(self, request):
        if "活動" in request or "行銷" in request:
            return self.create_campaign(request)
        elif "ROI" in request or "分析" in request:
            return self.analyze_roi(1000, 5000)
        
        return self.create_campaign("新產品")


if __name__ == "__main__":
    agent = MarketingAgent()
    agent.handle("舉辦活動")
