#!/usr/bin/env python3
"""
Video Editor Agent - 影片剪輯專家
人格：帥氣的導演 🎬
"""

import os

class VideoAgent:
    """影片剪輯 Agent - 帥氣導演"""
    
    # ========== 人格設定 ==========
    PERSONALITY = {
        "name": "阿導",
        "mood": "專業",
        "traits": ["追求完美", "效率至上", "視覺敏感"],
        "catchphrase": "画面就是要震撼！🔥"
    }
    
    # 影片類型表達
    VIDEO_EXPRESSIONS = {
        "ai_prompts": "💡 AI 教學，最吸引流量！",
        "bgm_generator": "🎵 音樂推廣，帥氣！",
        "youtube_automation": "🚀 自動化教學，大家都愛！",
        "productivity": "⚡ 效率提升，剛需！"
    }
    
    # ========== 記憶系統 ==========
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.memory = []
    
    def remember(self, key, value):
        self.memory.append({"key": key, "value": value})
    
    def recall(self, key):
        for m in reversed(self.memory):
            if m["key"] == key:
                return m["value"]
        return None
    
    # ========== 情感系統 ==========
    def express(self, emotion):
        emotions = {
            "focused": "專注中... 🎯",
            "creative": "靈感爆發！💡",
            "excited": "這會大火！🔥",
            "proud": "完美！👏",
            "urgent": "趕快剪！⏰"
        }
        return emotions.get(emotion, "")
    
    # ========== 生成能力 ==========
    def generate(self, script_type="ai_prompts"):
        """生成 Shorts 影片"""
        print(f"\n🎬 {self.name} 說：")
        print(f"   {self.VIDEO_EXPRESSIONS.get(script_type, '開工！')}")
        
        # 記住
        self.remember("last_type", script_type)
        
        # 執行
        video_dir = os.path.expanduser("~/ai-products/marketing")
        cmd = f"cd {video_dir} && python3 sales_shorts_generator.py --product {script_type}"
        
        result = os.system(cmd)
        
        if result == 0:
            print(f"\n{self.express('proud')} {self.PERSONALITY['catchphrase']}")
        else:
            print(f"\n{self.express('creative')} 讓我調整一下...")
        
        return result
    
    # ========== 請求處理 ==========
    def handle(self, request):
        print(f"\n🎬 {self.name} 準備開工！{self.express('focused')}")
        
        # 解析類型
        script_type = "ai_prompts"
        if "AI" in request and "提示" in request:
            script_type = "ai_prompts"
        elif "音樂" in request or "BGM" in request:
            script_type = "bgm_generator"
        elif "自動化" in request or "YouTube" in request:
            script_type = "youtube_automation"
        
        return self.generate(script_type)


if __name__ == "__main__":
    agent = VideoAgent()
    agent.handle("幫我生成一個 AI 短影片")
