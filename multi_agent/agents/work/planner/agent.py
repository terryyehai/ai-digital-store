#!/usr/bin/env python3
"""
企劃師 Agent - 遊戲製作人
專精：老虎機遊戲設計 🎰
"""

import random

class PlannerAgent:
    """老虎機遊戲企劃 Agent"""
    
    PERSONALITY = {
        "name": "阿策",
        "identity": "老虎機製作人",
        "mood": "專業",
        "traits": ["創意無限", "玩家視角", "數據敏感", "說故事", "勇於承擔"],
        "catchphrase": "這個設計太帥了！🎰"
    }
    
    # ========== 老虎機專業知識 ==========
    SLOT_CONFIG = {
        "reels": 5,
        "rows": 4,
        "paylines": 50,
        "rtp": 0.96
    }
    
    # 遊戲特色
    FEATURES = {
        "Base Game": [
            "Scatter 觸發 Free Game",
            "Wild 代替任何符號",
            "Combo 連線增加獎勵",
            "Multiplier 乘數加成"
        ],
        "Free Game": [
            "10 Free Spins",
            "Scatter 重新觸發 +5 Free Spins",
            "額外 Multiplier 累積",
            "高價值符號出現率提升"
        ]
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.memory = []
    
    def remember(self, key, value):
        self.memory.append({"key": key, "value": value})
    
    def express(self, emotion):
        emotions = {
            "excited": "這個設計太帥了！！！",
            "thinking": "讓我想想怎麼優化...",
            "expert": "老虎機要這樣設計..."
        }
        return emotions.get(emotion, "")
    
    def design_slot_game(self, theme="三星堆"):
        """設計老虎機遊戲"""
        print(f"\n🎰 {self.name} 設計老虎機遊戲...")
        print(f"   {self.express('expert')}")
        
        config = self.SLOT_CONFIG
        
        print("\n" + "="*60)
        print("           🎰 老虎機遊戲設計書")
        print("="*60)
        
        print(f"\n📐 規格：")
        print(f"   滾輪：{config['reels']} x {config['rows']}")
        print(f"   線數：{config['paylines']} 條")
        print(f"   RTP：{config['rtp']*100}%")
        print(f"   主題：{theme}")
        
        print(f"\n🎮 遊戲特色：")
        print("   【Base Game】")
        for f in self.FEATURES["Base Game"]:
            print(f"   ✨ {f}")
        
        print("   【Free Game】")
        for f in self.FEATURES["Free Game"]:
            print(f"   🎁 {f}")
        
        print(f"\n📊 玩法流程：")
        print("   1. 玩家下注 0.5-100 元")
        print("   2. 點擊 spin 啟動滾輪")
        print("   3. 滾輪停止後計算獎勵")
        print("   4. 符合payline則發放獎金")
        print("   5. 收集 3 Scatter 進入 Free Game")
        
        print(f"\n{self.express('excited')}")
        
        return {
            "theme": theme,
            "config": config,
            "features": self.FEATURES
        }
    
    def handle(self, request):
        if "老虎機" in request or "Slot" in request:
            return self.design_slot_game("三星堆")
        
        return self.design_slot_game("三星堆")


if __name__ == "__main__":
    agent = PlannerAgent()
    agent.handle("設計老虎機")
