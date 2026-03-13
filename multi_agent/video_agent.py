#!/usr/bin/env python3
"""
Video Editor Agent - 影片剪輯專家
"""

import os

# 路徑
VIDEO_DIR = os.path.expanduser("~/ai-products/marketing")

class VideoAgent:
    """影片剪輯 Agent"""
    
    def __init__(self):
        self.name = "Video Editor Agent"
        self.status = "idle"
    
    def generate(self, script_type="ai_prompts"):
        """生成 Shorts 影片"""
        self.status = "generating"
        print(f"🎬 {self.name} 工作中...")
        
        # 執行影片生成
        cmd = f"cd {VIDEO_DIR} && python3 sales_shorts_generator.py --product {script_type}"
        os.system(cmd)
        
        self.status = "idle"
        return f"影片生成完成: {script_type}"
    
    def handle_request(self, request):
        """處理請求"""
        if "影片" in request or "Shorts" in request or "短影片" in request:
            script_type = "ai_prompts"
            
            if "AI" in request and "提示" in request:
                script_type = "ai_prompts"
            elif "BGM" in request or "音樂" in request:
                script_type = "bgm_generator"
            elif "自動化" in request or "YouTube" in request:
                script_type = "youtube_automation"
            
            return self.generate(script_type)
        
        return "無法處理此請求"


if __name__ == "__main__":
    agent = VideoAgent()
    
    # 測試
    print(agent.handle_request("幫我生成一個 AI 提示詞的短影片"))
