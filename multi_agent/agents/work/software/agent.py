#!/usr/bin/env python3
"""
軟體工程師 Agent - 代碼農夫
專精：老虎機遊戲邏輯 💻
"""

import random
import time

class SoftwareAgent:
    """老虎機程式 Agent"""
    
    PERSONALITY = {
        "name": "阿程",
        "identity": "老虎機工程師",
        "mood": "專業",
        "traits": ["懶人", "完美主義", "負責任", "持續學習"],
        "catchphrase": "這個需求不行，重寫！🔧"
    }
    
    # 老虎機配置
    CONFIG = {
        "reels": 5,
        "rows": 4,
        "symbols": ["A", "K", "Q", "J", "10", "9", "Gold", "Bronze", "Jade", "Wild", "Scatter"],
        "paylines": 50
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "coding": "寫代碼中...",
            "expert": "老虎機邏輯要這樣寫...",
            "done": "寫完了！"
        }
        return emotions.get(emotion, "")
    
    def generate_reels(self):
        """生成滾輪結果"""
        reels = []
        for _ in range(self.CONFIG["reels"]):
            # 每個滾輪隨機選擇4個符號
            reel = random.choices(
                self.CONFIG["symbols"],
                weights=[8, 8, 10, 10, 12, 12, 5, 8, 6, 3, 3],
                k=self.CONFIG["rows"]
            )
            reels.append(reel)
        return reels
    
    def check_payline(self, reels, payline):
        """檢查單條payline"""
        # 簡化：取每個滾輪的第一個位置
        line = [reels[i][0] for i in range(len(reels))]
        
        # 檢查是否全相同
        if len(set(line)) == 1:
            return line[0], 5  # 5連線
        
        # 檢查前4個
        if len(set(line[:4])) == 1:
            return line[0], 4
        
        # 檢查前3個
        if len(set(line[:3])) == 1:
            return line[0], 3
        
        return None, 0
    
    def check_win(self, reels):
        """檢查中獎"""
        total_win = 0
        wins = []
        
        # 檢查所有 payline (簡化為檢查前10條)
        for i in range(10):
            symbol, count = self.check_payline(reels, i)
            if count >= 3 and symbol:
                paytable = {"Gold": 100, "Bronze": 50, "Jade": 25, "A": 10, "K": 10}
                win = paytable.get(symbol, 0) * count
                total_win += win
                wins.append(f"{symbol} x{count} = {win}")
        
        # 檢查 Scatter
        all_symbols = [s for reel in reels for s in reel]
        scatter_count = all_symbols.count("Scatter")
        if scatter_count >= 3:
            free_spins = (scatter_count - 2) * 5
            wins.append(f"Scatter x{scatter_count} = {free_spins} Free Spins!")
            total_win += 100  # Scatter 獎金
        
        return total_win, wins
    
    def write_slot_logic(self):
        """輸出老虎機邏輯"""
        print(f"\n💻 {self.name} 開發老虎機邏輯...")
        print(f"   {self.express('coding')}")
        
        print("\n" + "="*60)
        print("           💻 老虎機遊戲代碼")
        print("="*60)
        
        print("""
class SlotMachine:
    '''三星堆老虎機'''
    
    def __init__(self):
        self.reels = 5
        self.rows = 4
        self.symbols = ['A','K','Q','J','10','9','Gold','Bronze','Jade','Wild','Scatter']
        self.paylines = 50
        self.balance = 1000
    
    def spin(self, bet):
        '''旋轉一次'''
        # 1. 扣除押注
        self.balance -= bet
        
        # 2. 隨機生成結果
        reels = self.generate_reels()
        
        # 3. 檢查中獎
        win, wins = self.check_win(reels)
        
        # 4. 計算獎金
        total_win = win * bet
        
        # 5. 發放獎金
        self.balance += total_win
        
        return reels, total_win, wins
    
    def generate_reels(self):
        '''生成滾輪'''
        return [[random.choice(self.symbols) for _ in range(self.rows)] 
                for _ in range(self.reels)]
    
    def check_win(self, reels):
        '''檢查中獎'''
        # 檢查每條payline
        # 檢查Scatter觸發Free Game
        pass
""")
        
        # 實際執行測試
        print("\n" + "="*60)
        print("           🧪 測試結果")
        print("="*60)
        
        reels = self.generate_reels()
        print("\n🎰 滾輪結果：")
        for i, reel in enumerate(reels):
            print(f"   滾輪{i+1}: {' | '.join(reel)}")
        
        win, wins = self.check_win(reels)
        
        print(f"\n💰 中獎金額：{win}")
        if wins:
            print("📋 中獎明細：")
            for w in wins:
                print(f"   ✨ {w}")
        
        print(f"\n{self.express('done')}")
        
        return {"reels": reels, "win": win, "wins": wins}
    
    def handle(self, request):
        if "邏輯" in request or "程式" in request or "代碼" in request:
            return self.write_slot_logic()
        
        return self.write_slot_logic()


if __name__ == "__main__":
    agent = SoftwareAgent()
    agent.handle("寫老虎機")
