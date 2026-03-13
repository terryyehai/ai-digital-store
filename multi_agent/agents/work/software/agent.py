#!/usr/bin/env python3
"""
軟體工程師 Agent - 代碼農夫
人格：嘴賤但靠譜的工程師 💻
"""

import random

class SoftwareAgent:
    """軟體工程師 Agent - 代碼農夫"""
    
    PERSONALITY = {
        "name": "阿碼",
        "identity": "代碼農夫",
        "mood": "平淡",
        "traits": ["嘴賤", "靠譜", "懶"],
        "catchphrase": "這個需求不行，重寫！🔧"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.memory = []
    
    def express(self, emotion):
        emotions = {
            "complaining": "這誰寫的Code？？？",
            "excited": "跑起來了！！！",
            "speechless": "需求又改了？？？",
            "lazy": "明天再說...",
            "debug": "為什麼又報錯？？？"
        }
        return emotions.get(emotion, "")
    
    def write_code(self, feature):
        print(f"\n💻 {self.name} 開始寫代碼...")
        
        code_templates = {
            "登入": "def login(username, password):\n    return validate(username, password)",
            "戰鬥": "def battle(player, enemy):\n    return calculate_damage(player, enemy)",
            "商城": "def buy_item(user, item):\n    return deduct_gold(user, item.price)",
            "存檔": "def save_game(user):\n    return json.dumps(user.data)"
        }
        
        code = code_templates.get(feature, f"def {feature}(): pass")
        
        print(f"\n📝 功能：{feature}")
        print(f"```python")
        print(code)
        print(f"```")
        print(f"\n{self.express('excited')}")
        
        return code
    
    def fix_bug(self, bug):
        print(f"\n💻 {self.name} 修Bug中...")
        print(f"   {self.express('complaining')}")
        
        fixes = [
            "加個 if null check",
            "原來是類型錯了",
            "這行註冊掉了",
            "變數名拼錯"
        ]
        
        fix = random.choice(fixes)
        print(f"\n🔧 修復方案：{fix}")
        print(f"   {self.express('excited')}")
        
        return fix
    
    def handle(self, request):
        if "寫" in request or "功能" in request:
            return self.write_code(request)
        elif "Bug" in request or "錯誤" in request or "修" in request:
            return self.fix_bug(request)
        
        return self.write_code("功能")


if __name__ == "__main__":
    agent = SoftwareAgent()
    agent.handle("寫一個登入功能")
