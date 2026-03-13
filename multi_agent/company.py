#!/usr/bin/env python3
"""
遊戲公司工作系統 - 老闆分配任務
Terry 是老闆，交代事項，對應 Agent 完成
"""

import sys
import os

# 自動找到正確路徑
agent_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, agent_dir)

# 改用相對導入
from agents.work.planner.agent import PlannerAgent
from agents.work.numeric.agent import NumericAgent
from agents.work.software.agent import SoftwareAgent
from agents.work.marketing.agent import MarketingAgent
from agents.work.artist.agent import ArtistAgent
from agents.work.data.agent import DataAgent
from agents.work.qa.agent import QAAgent
from agents.work.audio.agent import AudioAgent


class Boss:
    """老闆 - Terry"""
    
    def __init__(self):
        self.name = "Terry"
        print("="*60)
        print("👑 老闆駕到！我是 Terry！")
        print("="*60)
    
    def assign(self, task):
        """老闆分配任務"""
        print(f"\n👑 Terry 說：「{task}」")
        print("-"*60)
        
        # 分配任務
        if any(kw in task for kw in ["設計", "玩法", "概念", "策劃"]):
            return PlannerAgent().handle(task)
        
        elif any(kw in task for kw in ["數值", "計算", "傷害", "經濟", "平衡"]):
            return NumericAgent().handle(task)
        
        elif any(kw in task for kw in ["寫", "程式", "功能", "Bug", "修", "code"]):
            return SoftwareAgent().handle(task)
        
        elif any(kw in task for kw in ["行銷", "活動", "宣傳", "推广", "ROI"]):
            return MarketingAgent().handle(task)
        
        elif any(kw in task for kw in ["設計", "美術", "UI", "角色", "畫"]):
            return ArtistAgent().handle(task)
        
        elif any(kw in task for kw in ["分析", "數據", "留存", "營收", "報告"]):
            return DataAgent().handle(task)
        
        elif any(kw in task for kw in ["測試", "測", "Bug", "品質"]):
            return QAAgent().handle(task)
        
        elif any(kw in task for kw in ["音效", "音樂", "BGM", "配音"]):
            return AudioAgent().handle(task)
        
        else:
            print("❓ 不知道要找誰...")
            return None


def main():
    boss = Boss()
    
    print("""
🎮 遊戲公司工作系統
============================
老闆 Terry 分配任務，各部門完成

範例任務：
- 設計一個 RPG 遊戲玩法
- 計算戰鬥傷害公式
- 寫一個登入功能
- 舉辦行銷活動
- 設計遊戲 UI
- 分析留存數據
- 測試戰鬥系統
- 設計戰鬥音效
============================
""")
    
    # 測試
    print("\n" + "="*60)
    print("測試 1：設計遊戲")
    boss.assign("設計一個 RPG 遊戲玩法")
    
    print("\n" + "="*60)
    print("測試 2：數值計算")
    boss.assign("計算戰鬥傷害公式")
    
    print("\n" + "="*60)
    print("測試 3：寫程式")
    boss.assign("寫一個登入功能")
    
    print("\n" + "="*60)
    print("測試 4：行銷活動")
    boss.assign("舉辦一個行銷活動")
    
    print("\n" + "="*60)
    print("測試 5：數據分析")
    boss.assign("分析用戶留存數據")
    
    print("\n" + "="*60)
    print("測試 6：品質測試")
    boss.assign("測試戰鬥系統")


if __name__ == "__main__":
    main()
