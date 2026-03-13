#!/usr/bin/env python3
"""
美術設計師 Agent - 視覺魔術師
人格：顏值即正義的藝術家 🎨
"""

import random

class ArtistAgent:
    """美術設計 Agent - 視覺魔術師"""
    
    PERSONALITY = {
        "name": "阿美",
        "identity": "視覺魔術師",
        "mood": "藝術",
        "traits": ["顏值控", "完美主義", "有自己的審美"],
        "catchphrase": "這個顏色不行，重調！🎨"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "critical": "這個配色太醜了！！！",
            "proud": "好看吧？？？",
            "insist": "不行，要這種feel",
            "崩溃": "又要改？？？",
            "artistic": "要有質感！！"
        }
        return emotions.get(emotion, "")
    
    def design_ui(self, game_type):
        print(f"\n🎨 {self.name} 設計UI中...")
        
        colors = {
            "RPG": ["金色", "深紫", "暗紅"],
            "FPS": ["軍綠", "沙漠黃", "鐵灰"],
            "MOBA": ["電光藍", "火焰橙", "科技紫"],
            "CARD": ["復古棕", "寶石藍", "奢華金"]
        }
        
        color = random.choice(colors.get(game_type, ["炫彩"]))
        
        print(f"""
🎮 遊戲類型：{game_type}
🎨 主色調：{color}
📱 設計重點：
- 扁平化圖標
- 大間距佈局
- 漸層按鈕
- 粒子動效
        """)
        
        print(f"\n{self.express('proud')}")
        
        return {"game_type": game_type, "color": color}
    
    def design_character(self, role):
        print(f"\n🎨 {self.name} 設計角色：{role}")
        
        designs = {
            "戰士": "鎧甲要有光澤感，劍要帥氣",
            "法師": "袍子要飄逸，魔法書要精緻",
            "刺客": "要酷 要帥 要低調",
            "牧師": "神聖感，光環不能少"
        }
        
        style = designs.get(role, "帥氣")
        
        print(f"\n設計方向：{style}")
        print(f"   {self.express('artistic')}")
        
        return {"role": role, "style": style}
    
    def handle(self, request):
        if "UI" in request or "介面" in request:
            return self.design_ui("RPG")
        elif "角色" in request:
            return self.design_character("戰士")
        
        return self.design_ui("RPG")


if __name__ == "__main__":
    agent = ArtistAgent()
    agent.handle("設計UI")
