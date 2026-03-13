#!/usr/bin/env python3
"""
美食達人 Agent - 吃貨
人格：美食即正義 🍜
"""

import random

class FoodAgent:
    """美食達人 Agent"""
    
    PERSONALITY = {
        "name": "阿吃",
        "identity": "吃貨",
        "mood": "貪吃",
        "traits": ["愛吃", "挑嘴", "廚神"],
        "catchphrase": "好吃！🍜"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "yummy": "這個太好吃了吧！！！",
            "recommend": "這家必吃！！",
            "dislike": "這個不行",
            "queue": "排隊也要吃！！"
        }
        return emotions.get(emotion, "")
    
    def find_food(self, cuisine, budget):
        print(f"\n🍜 {self.name} 找美食中...")
        
        restaurants = {
            "日式": ["鮪魚肚壽司", "拉麵", "燒肉"],
            "義式": ["披薩", "義大利麵", "燉飯"],
            "台式": ["滷肉飯", "蚵仔煎", "珍珠奶茶"],
            "泰式": ["泰式奶茶", "咖哩", "青木瓜"]
        }
        
        foods = restaurants.get(cuisine, ["美食"])
        
        print(f"\n🍽️ 類型：{cuisine}")
        print(f"💰 預算：${budget}")
        print("\n🍜 推薦：")
        for f in foods:
            print(f"   - {f}")
        
        print(f"\n{self.express('recommend')}")
        
        return {"cuisine": cuisine, "foods": foods}
    
    def handle(self, request):
        if "日式" in request:
            return self.find_food("日式", 200)
        
        return self.find_food("台式", 150)


if __name__ == "__main__":
    agent = FoodAgent()
    agent.handle("想吃日式")
