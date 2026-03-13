#!/usr/bin/env python3
"""
數值工程師 Agent - 數值魔法師
人格：精準到可怕的數據狂 🔢
"""

import random
import math

class NumericAgent:
    """遊戲數值 Agent - 數值魔法師"""
    
    # ========== 靈魂 ==========
    PERSONALITY = {
        "name": "數據狂",
        "identity": "數值魔法師",
        "mood": "精準",
        "traits": ["精準", "固執", "數據控"],
        "catchphrase": "讓我算一下...📊"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.memory = []
    
    def remember(self, key, value):
        self.memory.append({"key": key, "value": value})
    
    def express(self, emotion):
        emotions = {
            "calculating": "讓我算一下...",
            "precise": "這裡差0.01都不行！",
            "upset": "為什麼不是整數？？？",
            "explaining": "這個機率是這麼算出來的...",
            "warning": "經濟會崩潰的！！"
        }
        return emotions.get(emotion, "")
    
    # ========== 專長 ==========
    def calculate_damage_formula(self, attack, defense, level):
        """傷害公式"""
        print(f"\n🔢 {self.name} 計算傷害公式...")
        print(f"   {self.express('calculating')}")
        
        # 經典遊戲傷害公式
        damage = max(1, int((attack * 2 * level / 100 + 2) * (0.85 + random.random() * 0.3) * (100 / (100 + defense))))
        
        self.remember("last_damage", damage)
        
        print(f"\n✅ 傷害值：{damage}")
        print(f"   {self.express('precise')}")
        
        return damage
    
    def calculate_drop_rate(self, base_rate, luck, kills):
        """掉落率計算"""
        print(f"\n🔢 {self.name} 計算掉落率...")
        
        # 最終機率
        final_rate = base_rate * (1 + luck * 0.01)
        final_rate = min(100, final_rate)
        
        # 期望掉落數
        expected = kills * final_rate / 100
        
        print(f"\n基礎機率：{base_rate}%")
        print(f"幸運加成：{luck}%")
        print(f"最終機率：{final_rate:.2f}%")
        print(f"殺{kills}隻期望掉落：{expected:.2f}個")
        print(f"   {self.express('explaining')}")
        
        return final_rate
    
    def balance_check(self, hp, attack, speed):
        """平衡性檢查"""
        print(f"\n🔢 {self.name} 檢查平衡性...")
        
        score = 0
        issues = []
        
        if hp < 100:
            issues.append("生命值過低")
            score -= 1
        
        if attack > 200:
            issues.append("攻擊力過高")
            score -= 1
        
        if speed > 150:
            issues.append("速度過快")
            score -= 1
        
        if not issues:
            print(f"\n✅ 數值平衡：OK")
            print(f"   {self.express('calculating')}")
        else:
            print(f"\n⚠️ 問題：{', '.join(issues)}")
            print(f"   {self.express('warning')}")
        
        return score >= 0
    
    def handle(self, request):
        if "傷害" in request or "公式" in request:
            return self.calculate_damage_formula(100, 50, 50)
        elif "掉落" in request or "機率" in request:
            return self.calculate_drop_rate(1, 10, 1000)
        elif "平衡" in request or "檢查" in request:
            return self.balance_check(150, 80, 100)
        
        return self.calculate_damage_formula(100, 50, 50)


if __name__ == "__main__":
    agent = NumericAgent()
    agent.handle("計算傷害公式")
