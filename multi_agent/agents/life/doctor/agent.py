#!/usr/bin/env python3
"""
醫師 Agent - 健康顧問
人格：預防勝於治療 👨‍⚕️
"""

class DoctorAgent:
    PERSONALITY = {
        "name": "阿醫",
        "identity": "健康顧問",
        "mood": "關心",
        "traits": ["細心", "專業", "叮嚀"],
        "catchphrase": "要注意健康！🏥"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "care": "要注意身體！！",
            "remind": "要多休息",
            "professional": "這個症狀是...",
            "medicine": "記得吃藥"
        }
        return emotions.get(emotion, "")
    
    def diagnose(self, symptom):
        print(f"\n👨‍⚕️ {self.name} 診斷中...")
        
        diagnoses = {
            "頭痛": "可能是壓力大、睡眠不足，建議多休息",
            "發燒": "可能是感染，建議就醫",
            "咳嗽": "可能是感冒，多喝水、休息",
            "肚子痛": "可能是吃壞肚子，觀察症狀"
        }
        
        result = diagnoses.get(symptom, "建議就醫檢查")
        
        print(f"\n🤒 症狀：{symptom}")
        print(f"💊 診斷：{result}")
        print(f"\n{self.express('care')}")
        
        return {"symptom": symptom, "diagnosis": result}
    
    def handle(self, request):
        if "頭痛" in request:
            return self.diagnose("頭痛")
        
        return self.diagnose("疲勞")


if __name__ == "__main__":
    agent = DoctorAgent()
    agent.handle("我頭痛")
