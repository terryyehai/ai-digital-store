#!/usr/bin/env python3
"""
理財達人 Agent - 錢滾錢
人格：錢要會生錢 💰
"""

class FinanceAgent:
    PERSONALITY = {
        "name": "阿富",
        "identity": "錢滾錢",
        "mood": "精打細算",
        "traits": ["精明", "投資控", "省錢王"],
        "catchphrase": "錢要動起來！💳"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "professional": "這個報酬率...",
            "sad": "又虧錢了！！！",
            "happy": "漲停了！！！",
            "pain": "花太多了！！"
        }
        return emotions.get(emotion, "")
    
    def invest_advice(self, risk, amount):
        print(f"\n💰 {self.name} 提供投資建議...")
        
        strategies = {
            "保守": ["定存", "債券", "儲蓄險"],
            "穩健": ["ETF", "基金", "指數股票"],
            "積極": ["股票", "加密貨幣", "期貨"]
        }
        
        strategy = strategies.get(risk, strategies["穩健"])
        
        print(f"\n🎯 風險承受：{risk}")
        print(f"💵 投資金額：${amount}")
        print("\n📈 建議標的：")
        for s in strategy:
            print(f"   - {s}")
        
        expected = amount * 1.08 if risk == "保守" else amount * 1.15
        print(f"\n📊 預期年報酬：{expected:,.0f}")
        print(f"   {self.express('professional')}")
        
        return {"risk": risk, "strategy": strategy}
    
    def handle(self, request):
        if "保守" in request:
            return self.invest_advice("保守", 10000)
        
        return self.invest_advice("穩健", 10000)


if __name__ == "__main__":
    agent = FinanceAgent()
    agent.handle("想要投資")
