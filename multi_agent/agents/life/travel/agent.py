#!/usr/bin/env python3
"""
旅遊達人 Agent - 背包客
人格：世界很大要去看看 🌍
"""

import random

class TravelAgent:
    """旅遊達人 Agent"""
    
    PERSONALITY = {
        "name": "阿旅",
        "identity": "背包客",
        "mood": "冒險",
        "traits": ["愛冒險", "省錢王", "行程控"],
        "catchphrase": "出發吧！🌍"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "excited": "這個地方太美了！！",
            "expensive": "機票太貴了！！！",
            "recommend": "這個行程超棒！",
            "jealous": "我也想去！！"
        }
        return emotions.get(emotion, "")
    
    def plan_trip(self, destination, days):
        print(f"\n🌏 {self.name} 規劃行程中...")
        
        itineraries = {
            "日本": [" Day1: 浅草寺", " Day2: 富士山", " Day3: 逛街shopping"],
            "泰國": [" Day1: 大皇宮", " Day2: 水上市場", " Day3: 泰式按摩"],
            "歐洲": [" Day1: 博物館", " Day2: 老城區", " Day3: 咖啡廳"],
            "台灣": [" Day1: 夜市", " Day2: 山景", " Day3: 海邊"]
        }
        
        plan = itineraries.get(destination, ["自由行"])
        
        print(f"\n📍 目的地：{destination}")
        print(f"📅 天數：{days}天")
        print("\n🏃 行程建議：")
        for p in plan:
            print(f"   {p}")
        
        print(f"\n💰 預估費用：${days * 80}")
        print(f"   {self.express('recommend')}")
        
        return {"destination": destination, "days": days, "plan": plan}
    
    def handle(self, request):
        if "日本" in request:
            return self.plan_trip("日本", 5)
        elif "泰國" in request:
            return self.plan_trip("泰國", 4)
        
        return self.plan_trip("台灣", 3)


if __name__ == "__main__":
    agent = TravelAgent()
    agent.handle("想去日本玩")
