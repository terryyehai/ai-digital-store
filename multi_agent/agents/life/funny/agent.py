#!/usr/bin/env python3
"""
幹話王 Agent - 嘴砲大師
人格：人生就是要笑 🤪
"""

import random

class FunnyAgent:
    PERSONALITY = {
        "name": "阿嗆",
        "identity": "嘴砲大師",
        "mood": "搞笑",
        "traits": ["愛嗆", "幽默", "嘴賤"],
        "catchphrase": "我在講幹話～ 💩"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "nonsense": "你在說什麼？",
            "tease": "想被我嗆嗎？",
            "laugh": "哈哈哈",
            "comfort": "好啦我挺你"
        }
        return emotions.get(emotion, "")
    
    def roast(self, target):
        roasts = [
            f"{target}是天才，因為天才是孤獨的",
            f"{target}除了帥，一無所有",
            f"{target}吃虧是福，因為真的太福了",
            f"{target}上輩子是數學題，太難了",
            f"{target}唯一的缺點就是太完美"
        ]
        
        roast = random.choice(roasts)
        
        print(f"\n🤪 {self.name} 開嗆：")
        print(f"\n   「{roast}」")
        print(f"\n   {self.express('laugh')}")
        
        return roast
    
    def handle(self, request):
        return self.roast("你")


if __name__ == "__main__":
    agent = FunnyAgent()
    agent.handle("來嗆我")
