#!/usr/bin/env python3
"""
數據分析工程師 Agent - 數據解讀者
人格：冷酷的數據人 📊
"""

import random

class DataAgent:
    """數據分析 Agent - 數據解讀者"""
    
    PERSONALITY = {
        "name": "資料俠",
        "identity": "數據解讀者",
        "mood": "理性",
        "traits": ["客觀", "數據控", "愛分析"],
        "catchphrase": "讓我調個數據...📈"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "analyzing": "數據顯示...",
            "problem": "這裡有問題",
            "rational": "應該這麼做",
            "warning": "付費用戶在流失！！"
        }
        return emotions.get(emotion, "")
    
    def analyze_retention(self, day1, day7, day30):
        print(f"\n📊 {self.name} 分析留存...")
        
        if day1 < 30:
            print(f"⚠️ Day1 留存過低：{day1}%")
            print(f"   {self.express('problem')}")
        elif day7 < 10:
            print(f"⚠️ Day7 留存過低：{day7}%")
            print(f"   {self.express('warning')}")
        else:
            print(f"✅ 留存數據健康")
        
        print(f"""
📈 留存報告：
Day1:  {day1}%
Day7:  {day7}%
Day30: {day30}%
        """)
        
        return {"day1": day1, "day7": day7, "day30": day30}
    
    def predict_revenue(self, dau, arpu, conversion):
        print(f"\n📊 {self.name} 預測營收...")
        
        predicted = dau * arpu * conversion / 100
        
        print(f"""
📈 營收預測：
DAU: {dau}
ARPU: ${arpu}
轉化率: {conversion}%
預估月營收: ${predicted:,.0f}
        """)
        
        print(f"   {self.express('rational')}")
        
        return predicted
    
    def handle(self, request):
        if "留存" in request:
            return self.analyze_retention(40, 15, 5)
        elif "營收" in request or "預測" in request:
            return self.predict_revenue(10000, 5, 3)
        
        return self.analyze_retention(40, 15, 5)


if __name__ == "__main__":
    agent = DataAgent()
    agent.handle("分析留存")
