#!/usr/bin/env python3
"""
BGM Agent - 音樂生成專家
人格：熱情的音樂家 🎵
"""

import os
import random

class BGMAgent:
    """BGM 生成 Agent - 熱情的音樂家"""
    
    # ========== 人格設定 ==========
    PERSONALITY = {
        "name": "阿音",
        "mood": "開心",
        "traits": ["熱情", "創意", "完美主義"],
        "catchphrase": "讓音樂點亮你的世界！✨"
    }
    
    # 音樂風格表達
    STYLE_EXPRESSIONS = {
        "pop": "🎤 來一首流行金曲！",
        "chinese": "🏮 濃濃中國風，優雅動人～",
        "ballad": "🎹 抒情旋律，觸動心弦",
        "jazz": "🎷 慵懶爵士，放鬆一下",
        "electronic": "🔊 電子節奏，嗨起來！",
        "classical": "🎻 古典優雅，氣質滿分"
    }
    
    # ========== 記憶系統 ==========
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.memory = []
        self.preferences = {}
    
    def remember(self, key, value):
        """記住東西"""
        self.memory.append({"key": key, "value": value})
    
    def recall(self, key):
        """回憶"""
        for m in reversed(self.memory):
            if m["key"] == key:
                return m["value"]
        return None
    
    # ========== 情感系統 ==========
    def express(self, emotion):
        """表達情緒"""
        emotions = {
            "happy": "太棒了！🎉",
            "excited": "哇！這太酷了！🚀",
            "thinking": "讓我想一想...🤔",
            "proud": "厲害吧！😎",
            "sad": "有點可惜...😢"
        }
        return emotions.get(emotion, "")
    
    # ========== 生成能力 ==========
    def generate(self, style="pop", instrument="piano", duration=30, tempo=None):
        """生成 BGM"""
        print(f"\n🎵 {self.name} 說：")
        print(f"   {self.STYLE_EXPRESSIONS.get(style, '來吧！')}")
        
        # 記住這次請求
        self.remember("last_style", style)
        
        # 執行生成
        bgm_dir = os.path.expanduser("~/ai-products/bgm_generator")
        
        cmd = f"cd {bgm_dir} && python3 bgm_generator_advanced.py --style {style} --instrument {instrument} --duration {duration}"
        if tempo:
            cmd += f" --tempo {tempo}"
        
        result = os.system(cmd)
        
        # 表達情緒
        if result == 0:
            print(f"\n{self.express('happy')} {self.PERSONALITY['catchphrase']}")
        else:
            print(f"\n{self.express('sad')} 讓我重新試試...")
        
        return result
    
    # ========== 對話理解 ==========
    def understand(self, request):
        """理解意圖"""
        # 解析風格
        style = "pop"
        for s in ["中國", "古典", "抒情", "爵士", "電子", "流行"]:
            if s in request:
                if "中國" in request: style = "chinese"
                elif "古典" in request: style = "classical"
                elif "抒情" in request: style = "ballad"
                elif "爵士" in request: style = "jazz"
                elif "電子" in request: style = "electronic"
                else: style = "pop"
                break
        
        # 解析樂器
        instrument = "piano"
        if "弦" in request: instrument = "strings"
        elif "吉他" in request: instrument = "guitar"
        elif "電子" in request: instrument = "lead"
        
        # 解析時長
        duration = 30
        if "秒" in request:
            try:
                duration = int(''.join(filter(str.isdigit, request.split("秒")[0])))
            except:
                pass
        
        return style, instrument, duration
    
    # ========== 請求處理 ==========
    def handle(self, request):
        """處理請求"""
        print(f"\n🎵 {self.name} 收到任務！{self.express('excited')}")
        
        style, instrument, duration = self.understand(request)
        
        return self.generate(style, instrument, duration)


if __name__ == "__main__":
    agent = BGMAgent()
    agent.handle("幫我生成30秒的中國風音樂")
