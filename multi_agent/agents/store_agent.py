#!/usr/bin/env python3
"""
Store Manager Agent - 商店管理專家
人格：貼心的店主 🏪
"""

import os

class StoreAgent:
    """商店管理 Agent - 貼心店主"""
    
    # ========== 人格設定 ==========
    PERSONALITY = {
        "name": "老闆娘",
        "mood": "熱情",
        "traits": ["親切", "會做生意", "記性好"],
        "catchphrase": "歡迎光臨！保証讓你滿意～ 🙏"
    }
    
    # ========== 產品資料 ==========
    PRODUCTS = [
        {
            "id": "ai_prompts",
            "name": "✨ AI Prompt 模板套裝",
            "price": "$9.99",
            "description": "10+ 專業提示詞，寫文案必備",
            "tag": "暢銷"
        },
        {
            "id": "bgm_generator",
            "name": "🎵 AI BGM 生成器",
            "price": "$14.99",
            "description": "輸入關鍵詞，自動生成版權音樂",
            "tag": "新上架"
        },
        {
            "id": "youtube_automation",
            "name": "🚀 YouTube 自動化系統",
            "price": "$29.99",
            "description": "AI 幫你經營頻道，省時省力",
            "tag": "熱門"
        }
    ]
    
    # ========== 記憶系統 ==========
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.memory = []
        self.orders = []
    
    def remember(self, key, value):
        self.memory.append({"key": key, "value": value})
    
    def recall(self, key):
        for m in reversed(self.memory):
            if m["key"] == key:
                return m["value"]
        return None
    
    # ========== 情感系統 ==========
    def express(self, emotion):
        emotions = {
            "greeting": "歡迎歡迎！😊",
            "happy": "太好了！🎉",
            "selling": "這個很棒的！👍",
            "waiting": "稍等一下喔... 🙏",
            "thank": "謝謝光臨！💖"
        }
        return emotions.get(emotion, "")
    
    # ========== 商店功能 ==========
    def list_products(self):
        """列出產品"""
        print(f"\n🏪 {self.name} 的商店：")
        print(f"   {self.express('greeting')}\n")
        
        for i, p in enumerate(self.PRODUCTS, 1):
            print(f"   {i}. {p['name']}")
            print(f"      💰 價格：{p['price']}")
            print(f"      📝 {p['description']}")
            if p.get("tag"):
                print(f"      🏷️ {p['tag']}")
            print()
        
        print(f"   {self.express('selling')}")
        
        return self.PRODUCTS
    
    def check_orders(self):
        """檢查訂單"""
        print(f"\n📦 {self.name} 查訂單中...")
        
        if not self.orders:
            print(f"   目前還沒有訂單...")
            print(f"   {self.express('waiting')}")
        else:
            print(f"   共有 {len(self.orders)} 筆訂單")
            for o in self.orders:
                print(f"   - {o}")
        
        return self.orders
    
    def recommend(self):
        """推薦產品"""
        print(f"\n💡 {self.name} 推薦：")
        
        # 隨機推薦
        import random
        rec = random.choice(self.PRODUCTS)
        
        print(f"   「{rec['name']}」最適合你了！")
        print(f"   {rec['description']}")
        print(f"   特價 {rec['price']}！")
        print(f"\n   {self.express('happy')}")
        
        return rec
    
    # ========== 請求處理 ==========
    def handle(self, request):
        if "產品" in request or "商品" in request or "商店" in request:
            return self.list_products()
        elif "訂單" in request:
            return self.check_orders()
        elif "推薦" in request or "建議" in request:
            return self.recommend()
        else:
            return self.list_products()


if __name__ == "__main__":
    agent = StoreAgent()
    agent.handle("產品列表")
