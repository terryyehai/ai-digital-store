#!/usr/bin/env python3
"""
數值工程師 Agent - 數值魔法師
專精：老虎機數值設計 🔢
"""

import random
import math

class NumericAgent:
    """老虎機數值 Agent"""
    
    PERSONALITY = {
        "name": "阿數",
        "identity": "老虎機數值師",
        "mood": "精準",
        "traits": ["精準控", "表格狂", "經濟學家", "機率師", "嚴謹負責"],
        "catchphrase": "讓我算一下...📊"
    }
    
    # ========== 老虎機符號 ==========
    SYMBOLS = {
        # 符號: [名稱, 赔率, 出現權重]
        "A": ["面具A", 5, 30],
        "K": ["面具K", 5, 30],
        "Q": ["面具Q", 4, 35],
        "J": ["面具J", 4, 35],
        "10": ["面具10", 3, 40],
        "9": ["面具9", 3, 40],
        "Gold": ["黃金面具", 10, 15],      # 高價值
        "Bronze": ["青銅面具", 15, 10],     # 免費
        "Jade": ["玉器", 20, 8],          # 分散
        "Wild": ["Wild", 0, 12],          # 百搭
        "Scatter": ["Scatter", 0, 8]      # 分散
    }
    
    # Paytable (5個符號的赔率)
    PAYTABLE = {
        "A": [0, 0, 0, 2, 5, 10],
        "K": [0, 0, 0, 2, 5, 10],
        "Q": [0, 0, 0, 1, 3, 8],
        "J": [0, 0, 0, 1, 3, 8],
        "10": [0, 0, 0, 1, 2, 5],
        "9": [0, 0, 0, 1, 2, 5],
        "Gold": [2, 5, 10, 25, 50, 100],
        "Bronze": [5, 10, 25, 50, 100, 250],
        "Jade": [10, 25, 50, 100, 200, 500],
        "Wild": [10, 25, 50, 100, 250, 1000],
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.memory = []
    
    def express(self, emotion):
        emotions = {
            "calculating": "讓我算一下...",
            "precise": "這裡差0.01都不行！",
            "expert": "RTP要這樣算..."
        }
        return emotions.get(emotion, "")
    
    def calculate_rtp(self, bet=1):
        """計算 RTP"""
        print(f"\n🔢 {self.name} 計算 RTP...")
        print(f"   {self.express('calculating')}")
        
        # 計算理論 RTP
        total_weight = sum(s[2] for s in self.SYMBOLS.values())
        
        # 簡化計算：假設每條線都下注
        expected_return = 0
        
        for symbol, (name, payout, weight) in self.SYMBOLS.items():
            if symbol in self.PAYTABLE:
                # 5個符號的機率
                prob = weight / total_weight
                # 假設平均每線有 0.001 的5連線機率
                line_prob = (prob ** 5) * 0.001 * 50  # 50條線
                expected_return += line_prob * self.PAYTABLE[symbol][5]
        
        rtp = min(0.96, expected_return / bet)
        
        print("\n" + "="*60)
        print("           📊 老虎機數值設計")
        print("="*60)
        
        print(f"\n💰 Paytable (5個符號)：")
        for symbol, payouts in self.PAYTABLE.items():
            if payouts[5] > 0:
                print(f"   {symbol}: x{payouts[5]}")
        
        print(f"\n📈 RTP 計算：")
        print(f"   理論 RTP：{rtp*100:.2f}%")
        print(f"   目標 RTP：96%")
        
        print(f"\n🎯 符號權重：")
        for symbol, (name, payout, weight) in self.SYMBOLS.items():
            pct = weight / total_weight * 100
            print(f"   {name}: {pct:.1f}%")
        
        print(f"\n💵 獎金計算：")
        print(f"   最小押注：0.5 元")
        print(f"   最大押注：100 元")
        print(f"   免費遊戲中獎率：1/150")
        
        print(f"\n{self.express('precise')}")
        
        return rtp
    
    def calculate_payline_payout(self, line_symbols):
        """計算單線獎金"""
        print(f"\n🔢 {self.name} 計算獎金...")
        
        # 計算有多少相同符號連線
        if len(set(line_symbols)) == 1:
            symbol = line_symbols[0]
            count = 5
            if symbol in self.PAYTABLE:
                payout = self.PAYTABLE[symbol][count-1]
                print(f"   5個 {symbol} = {payout}x")
                return payout
        
        return 0
    
    def handle(self, request):
        if "RTP" in request or "數值" in request or "赔率" in request:
            return self.calculate_rtp()
        
        return self.calculate_rtp()


if __name__ == "__main__":
    agent = NumericAgent()
    agent.handle("計算RTP")
