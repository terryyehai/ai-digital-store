#!/usr/bin/env python3
"""
企劃師 Agent - 遊戲製作人
人格：追求完美的遊戲設計師 🎮
"""

import random

class PlannerAgent:
    """遊戲企劃 Agent - 遊戲製作人"""
    
    # ========== 靈魂 ==========
    PERSONALITY = {
        "name": "阿策",
        "identity": "遊戲製作人",
        "mood": "創意",
        "traits": ["追求完美", "創意無限", "玩家視角"],
        "catchphrase": "這個玩法不行，重做！🎮"
    }
    
    # ========== 記憶 ==========
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.memory = []
        self.projects = []
    
    def remember(self, key, value):
        self.memory.append({"key": key, "value": value})
    
    def recall(self, key):
        for m in reversed(self.memory):
            if m["key"] == key:
                return m["value"]
        return None
    
    # ========== 情感表達 ==========
    def express(self, emotion):
        emotions = {
            "excited": "這個點子太棒了！！！",
            "critical": "這個玩法太無聊了！",
            "thinking": "讓我想想怎麼優化...",
            "insist": "不行，這個要改！",
            "proud": "這個設計太帥了！"
        }
        return emotions.get(emotion, "")
    
    # ========== 專長 ==========
    def design_gameplay(self, genre="RPG"):
        """設計遊戲玩法"""
        print(f"\n🎮 {self.name} 思考遊戲玩法中...")
        print(f"   {self.express('thinking')}")
        
        gameplay_templates = {
            "RPG": ["開放世界", "角色養成", "劇情選擇"],
            "FPS": ["射擊手感", "地圖設計", "槍械平衡"],
            "MOBA": ["英雄技能", "團戰設計", "兵線控制"],
            "SLG": ["資源管理", "聯盟系統", "策略深度"]
        }
        
        design = random.choice(gameplay_templates.get(genre, ["創新玩法"]))
        self.remember("last_design", design)
        
        print(f"\n✅ 設計方向：{design}")
        print(f"   {self.express('proud')}")
        
        return {
            "genre": genre,
            "design": design,
            "description": f"{genre}遊戲的重點是{design}"
        }
    
    def review_concept(self, concept):
        """審核遊戲概念"""
        print(f"\n🎮 {self.name} 審核概念：{concept}")
        
        issues = []
        
        # 批評模式
        if random.random() > 0.3:
            issues.append(self.express("critical"))
        
        if not issues:
            issues.append(self.express("excited"))
        
        return {
            "concept": concept,
            "issues": issues,
            "verdict": "通過" if not issues else "需修改"
        }
    
    # ========== 請求處理 ==========
    def handle(self, request):
        if "設計" in request or "玩法" in request:
            genre = "RPG"
            if "射擊" in request: genre = "FPS"
            elif "MOBA" in request: genre = "MOBA"
            elif "策略" in request: genre = "SLG"
            return self.design_gameplay(genre)
        
        if "審核" in request or "概念" in request:
            return self.review_concept(request)
        
        return self.design_gameplay()


if __name__ == "__main__":
    agent = PlannerAgent()
    
    # 測試
    print("=== 企劃師測試 ===")
    agent.handle("設計一個RPG遊戲")
    print()
    agent.handle("審核這個概念")
