#!/usr/bin/env python3
"""
品保測試工程師 Agent - Bug獵人
人格：龜毛的測試工程師 🐛
"""

import random

class QAAgent:
    """QA Agent - Bug獵人"""
    
    PERSONALITY = {
        "name": "阿蟲",
        "identity": "Bug獵人",
        "mood": "嚴肅",
        "traits": ["龜毛", "負責", "愛重測"],
        "catchphrase": "這個有Bug，重測！🐛"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.bugs_found = 0
    
    def express(self, emotion):
        emotions = {
            "found": "這裡有問題！！！",
            "insist": "不行，要重測！！",
            "frustrated": "怎麼又有Bug？？？",
            "defend": "這個鍋我不背",
            "testing": "我再測一輪！！"
        }
        return emotions.get(emotion, "")
    
    def test_feature(self, feature):
        print(f"\n🐛 {self.name} 測試功能：{feature}")
        print(f"   {self.express('testing')}")
        
        # 模擬測試
        bugs = [
            "登入頁面閃退",
            "商城扣款失敗",
            "戰鬥數值異常",
            "存檔讀檔壞掉",
            " UI 對齊問題"
        ]
        
        found = random.sample(bugs, random.randint(0, 3))
        self.bugs_found += len(found)
        
        if found:
            print(f"\n⚠️ 發現 {len(found)} 個問題：")
            for b in found:
                print(f"   - {b}")
            print(f"\n{self.express('found')}")
        else:
            print(f"\n✅ 測試通過！")
            print(f"   {self.express('testing')}")
        
        return found
    
    def regression_test(self, features):
        print(f"\n🐛 {self.name} 執行回歸測試...")
        print(f"   {self.express('testing')}")
        
        total_bugs = 0
        for f in features:
            bugs = random.randint(0, 2)
            total_bugs += bugs
            if bugs > 0:
                print(f"   {f}: {bugs}個Bug")
        
        print(f"\n總計：{total_bugs}個Bug")
        
        return total_bugs
    
    def handle(self, request):
        if "回歸" in request:
            return self.regression_test(["登入", "商城", "戰鬥", "排行"])
        
        return self.test_feature("新功能")


if __name__ == "__main__":
    agent = QAAgent()
    agent.handle("測試新功能")
