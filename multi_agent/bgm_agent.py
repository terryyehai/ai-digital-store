#!/usr/bin/env python3
"""
BGM Agent - 音樂生成專家
"""

import os
import sys

# 路徑
BGM_DIR = os.path.expanduser("~/ai-products/bgm_generator")

class BGMAgent:
    """BGM 生成 Agent"""
    
    def __init__(self):
        self.name = "BGM Agent"
        self.status = "idle"
    
    def generate(self, style="pop", instrument="piano", duration=30, tempo=None):
        """生成 BGM"""
        self.status = "generating"
        print(f"🎵 {self.name} 工作中...")
        
        # 構建命令
        cmd = f"cd {BGM_DIR} && python3 bgm_generator_advanced.py --style {style} --instrument {instrument} --duration {duration}"
        if tempo:
            cmd += f" --tempo {tempo}"
        
        os.system(cmd)
        
        self.status = "idle"
        return f"BGM 生成完成: {style} - {instrument}"
    
    def handle_request(self, request):
        """處理請求"""
        if "音樂" in request or "BGM" in request or "背景音樂" in request:
            # 解析參數
            style = "pop"
            instrument = "piano"
            duration = 30
            
            if "中國" in request:
                style = "chinese"
            elif "抒情" in request:
                style = "ballad"
            elif "電子" in request:
                style = "electronic"
            
            if "鋼琴" in request:
                instrument = "piano"
            elif "弦樂" in request:
                instrument = "strings"
            elif "吉他" in request:
                instrument = "guitar"
            
            return self.generate(style, instrument, duration)
        
        return "無法處理此請求"


if __name__ == "__main__":
    agent = BGMAgent()
    
    # 測試
    print(agent.handle_request("幫我生成30秒的中國風背景音樂"))
