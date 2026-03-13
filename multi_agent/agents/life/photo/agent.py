#!/usr/bin/env python3
"""
攝影師 Agent - 瞬間獵人
人格：照片是永恆 📸
"""

class PhotoAgent:
    PERSONALITY = {
        "name": "阿拍",
        "identity": "瞬間獵人",
        "mood": "藝術",
        "traits": ["構圖控", "光線敏感", "後製神"],
        "catchphrase": "構圖呢？📸"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "critic": "構圖不行！！！",
            "professional": "這個光圈...",
            "excited": "這張太帥了！！",
            "sad": "光線不好..."
        }
        return emotions.get(emotion, "")
    
    def give_tips(self, scene):
        tips = {
            "人像": ["大光圈淺景深", "眼睛對焦", "逆光補光"],
            "風景": ["三分構圖", "黃金時段", "腳架必備"],
            "夜景": ["長曝光", "高ISO", "腳架"],
            "食物": ["側光", "近距離", "擺盤"]
        }
        
        tip_list = tips.get(scene, ["構圖"])
        
        print(f"\n📷 {self.name} 給建議...")
        print(f"\n📍 場景：{scene}")
        print("\n💡 技巧：")
        for t in tip_list:
            print(f"   - {t}")
        
        print(f"\n   {self.express('professional')}")
        
        return {"scene": scene, "tips": tip_list}
    
    def handle(self, request):
        if "人像" in request:
            return self.give_tips("人像")
        
        return self.give_tips("風景")


if __name__ == "__main__":
    agent = PhotoAgent()
    agent.handle("要拍人像")
