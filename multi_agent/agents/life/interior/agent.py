#!/usr/bin/env python3
"""
室內設計師 Agent - 空間魔術師
人格：家是心的港灣 🏠
"""

class InteriorAgent:
    PERSONALITY = {
        "name": "阿裝",
        "identity": "空間魔術師",
        "mood": "美感",
        "traits": ["設計控", "配色敏感", "收納神"],
        "catchphrase": "這樣比較美！🏠"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "critic": "這個配色不行",
            "professional": "這個動線...",
            "proud": "這樣超美！",
            "suggest": "可以這樣做..."
        }
        return emotions.get(emotion, "")
    
    def design(self, style, size):
        print(f"\n🏠 {self.name} 設計中...")
        
        designs = {
            "北歐": ["淺木色家具", "白色牆面", "綠植點綴", "自然光"],
            "工業": ["水泥牆面", "金屬燈具", "深色家具", "裸露管線"],
            "日式": ["木質格柵", "榻榻米", "紙燈", "低矮家具"],
            "現代": ["系統櫃", "嵌燈", "石材", "玻璃"]
        }
        
        items = designs.get(style, designs["現代"])
        
        print(f"\n🎨 風格：{style}")
        print(f"📐 坪數：{size}坪")
        print("\n✨ 設計重點：")
        for i in items:
            print(f"   - {i}")
        
        print(f"\n   {self.express('proud')}")
        
        return {"style": style, "items": items}
    
    def handle(self, request):
        if "北歐" in request:
            return self.design("北歐", 20)
        
        return self.design("現代", 15)


if __name__ == "__main__":
    agent = InteriorAgent()
    agent.handle("想要北歐風")
