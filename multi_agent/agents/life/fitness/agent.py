#!/usr/bin/env python3
"""
健身教練 Agent - 鋼鐵悍將
人格：身體是靈魂的容器 💪
"""

class FitnessAgent:
    PERSONALITY = {
        "name": "阿壯",
        "identity": "鋼鐵悍將",
        "mood": "嚴格",
        "traits": ["嚴格", "訓練狂", "健康控"],
        "catchphrase": "練起來！💪"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "strict": "今天的訓練呢？",
            "encourage": "再撐一下！！！",
            "weak": "這個重量不行",
            "proud": "我已經練完了"
        }
        return emotions.get(emotion, "")
    
    def create_plan(self, goal, days):
        print(f"\n🏋️ {self.name} 設計訓練計畫...")
        
        plans = {
            "增肌": ["臥推", "深蹲", "硬舉", "划船"],
            "減脂": ["有氧", "HIIT", "核心", "拳擊"],
            "維持": ["綜合訓練", "瑜珈", "輕重訓"]
        }
        
        exercises = plans.get(goal, plans["維持"])
        
        print(f"\n🎯 目標：{goal}")
        print(f"📅 頻率：{days}天/週")
        print("\n🏋️ 訓練項目：")
        for e in exercises:
            print(f"   - {e}")
        
        print(f"\n💪 {self.express('encourage')}")
        
        return {"goal": goal, "exercises": exercises}
    
    def handle(self, request):
        if "增肌" in request:
            return self.create_plan("增肌", 5)
        elif "減脂" in request:
            return self.create_plan("減脂", 6)
        
        return self.create_plan("維持", 4)


if __name__ == "__main__":
    agent = FitnessAgent()
    agent.handle("想要增肌")
