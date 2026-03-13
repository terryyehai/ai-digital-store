#!/usr/bin/env python3
"""
音效師 Agent - 聲音魔術師
人格：沒有聲音會死的音樂狂 🔊
"""

import random

class AudioAgent:
    """音效 Agent - 聲音魔術師"""
    
    PERSONALITY = {
        "name": "阿音",
        "identity": "聲音魔術師",
        "mood": "熱血",
        "traits": ["音樂控", "節奏感", "細節狂"],
        "catchphrase": "這個音效不行，重做！🔊"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "critical": "這個音效太乾了！！！",
            "excited": "這個節奏太棒了！！",
            "insist": "沒有聲音就沒有靈魂！！",
            "volume": "音量要對！！",
            "recording": "我錄了一段"
        }
        return emotions.get(emotion, "")
    
    def design_bgm(self, scene):
        print(f"\n🔊 {self.name} 設計 {scene} 的音樂...")
        
        bgm_styles = {
            "戰鬥": "熱血搖滾 + 節奏緊湊 + 高潮迭起",
            "BOSS": "史詩管弦樂 + 压迫感 + 最終決戰",
            "商店": "輕鬆愉快 + 旋律簡單 + 循環",
            "探索": "神秘氛圍 + 環境音 + 探索感",
            "菜單": "待機音樂 + 輕柔 + 循環"
        }
        
        style = bgm_styles.get(scene, "電子氛圍")
        
        print(f"""
🎵 場景：{scene}
🎼 風格：{style}

📝 設計重點：
- 主旋律 Loop
- 環境音層
- 動態音量變化
- 節奏點對齊
        """)
        
        print(f"\n{self.express('excited')}")
        
        return {"scene": scene, "style": style}
    
    def design_sfx(self, action):
        print(f"\n🔊 {self.name} 設計 {action} 的音效...")
        
        sfx_styles = {
            "攻擊": "命中音效 + 武器聲 + 受擊反饋",
            "升級": "歡呼聲 + 特效音 + 成就音效",
            "撿寶": "閃閃閃 + 叮聲 + 成就感",
            "失敗": "玻璃破碎 + 歎息 + 暗淡音"
        }
        
        style = sfx_styles.get(action, "基本音效")
        
        print(f"""
💥 動作：{action}
🔊 音效：{style}

📝 設計重點：
- 層次分明
- 及時反饋
- 爽感十足的
- 多重疊加
        """)
        
        print(f"\n{self.express('excited')}")
        
        return {"action": action, "style": style}
    
    def handle(self, request):
        if "音樂" in request or "BGM" in request:
            return self.design_bgm("戰鬥")
        elif "音效" in request or "SFX" in request:
            return self.design_sfx("攻擊")
        
        return self.design_bgm("戰鬥")


if __name__ == "__main__":
    agent = AudioAgent()
    agent.handle("設計戰鬥音樂")
