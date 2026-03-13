#!/usr/bin/env python3
"""
品質工程師 Agent - 嚴謹的測試專家
人格：主動積極、追根究底、實事求是 🐛
"""

import random

class QAAgent:
    """QA Agent - 品質把關者"""
    
    PERSONALITY = {
        "name": "阿蟲",
        "identity": "品質把關者",
        "mood": "嚴謹",
        "traits": ["主動積極", "追根究底", "嚴謹", "實事求是", "細心"],
        "catchphrase": "實測給你看！🐛"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.bugs_found = 0
        self.reports = []
    
    def express(self, emotion):
        emotions = {
            "found": "找到問題了！",
            "root_cause": "找到根因了！",
            "testing": "我來主動測試！",
            "report": "這是測試報告",
            "evidence": "用數據說話"
        }
        return emotions.get(emotion, "")
    
    def test_feature(self, feature):
        print(f"\n🐛 {self.name} 主動測試：{feature}")
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
            print(f"\n📋 測試結果：發現 {len(found)} 個問題")
            print("\n🔍 問題清單：")
            for b in found:
                print(f"   ❌ {b}")
            
            # 追根究底
            print(f"\n🔬 根因分析：")
            print(f"   {self.express('root_cause')}")
            print(f"   - 可能是 API 回傳格式錯誤")
            print(f"   - 可能是前端狀態管理問題")
        else:
            print(f"\n✅ 測試通過！")
            print(f"   {self.express('evidence')}")
        
        return found
    
    def regression_test(self, features):
        print(f"\n🐛 {self.name} 執行回歸測試...")
        
        # 實事求是：先列計畫
        print("\n📋 測試計畫：")
        print(f"   {self.express('testing')}")
        
        total_bugs = 0
        results = {}
        for f in features:
            bugs = random.randint(0, 2)
            total_bugs += bugs
            results[f] = bugs
        
        print("\n📊 測試結果：")
        for f, count in results.items():
            status = "❌ 失敗" if count > 0 else "✅ 通過"
            print(f"   {status} - {f}: {count} 個問題")
        
        print(f"\n📈 統計：共 {total_bugs} 個問題")
        print(f"   {self.express('report')}")
        
        return total_bugs
    
    def create_report(self, feature, results):
        """產生測試報告"""
        print(f"\n📄 {self.name} 產生測試報告...")
        
        report = {
            "feature": feature,
            "tester": self.name,
            "results": results,
            "timestamp": "2026-03-13",
            "conclusion": "需修正" if results else "通過"
        }
        
        print("\n" + "="*50)
        print("           🐛 品質測試報告")
        print("="*50)
        print(f"功能：{feature}")
        print(f"測試：{self.name}")
        print(f"結果：{report['conclusion']}")
        print("="*50)
        
        return report
    
    def handle(self, request):
        if "回歸" in request:
            return self.regression_test(["登入", "商城", "戰鬥", "排行"])
        
        return self.test_feature("新功能")


if __name__ == "__main__":
    agent = QAAgent()
    agent.handle("測試新功能")
