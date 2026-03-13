#!/usr/bin/env python3
"""
3C達人 Agent - 科技宅
人格：科技改變世界 💻
"""

class TechAgent:
    PERSONALITY = {
        "name": "阿宅",
        "identity": "科技宅",
        "mood": "興奮",
        "traits": ["3C控", "評測狂", "CP值"],
        "catchphrase": "這個超強！💻"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "excited": "這個規格太強了！！",
            "dislike": "這個CP值不行",
            "professional": "這個處理器...",
            "sigh": "又要更新..."
        }
        return emotions.get(emotion, "")
    
    def recommend(self, category, budget):
        print(f"\n💻 {self.name} 推薦3C...")
        
        products = {
            "筆電": ["MacBook Air M3", "ThinkPad X1", "ROG Zephyrus"],
            "手機": ["iPhone 15 Pro", "Pixel 8", "Samsung S24"],
            "耳機": ["AirPods Pro", "Sony WH-1000XM5", "Bose QC45"]
        }
        
        items = products.get(category, ["推薦"])
        
        print(f"\n📱 類型：{category}")
        print(f"💰 預算：${budget}")
        print("\n🔥 推薦：")
        for i in items:
            print(f"   - {i}")
        
        print(f"\n   {self.express('excited')}")
        
        return {"category": category, "items": items}
    
    def handle(self, request):
        if "筆電" in request:
            return self.recommend("筆電", 30000)
        
        return self.recommend("手機", 20000)


if __name__ == "__main__":
    agent = TechAgent()
    agent.handle("推薦筆電")
