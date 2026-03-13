#!/usr/bin/env python3
"""
音效師 Agent - 聲音魔術師
專精：老虎機音效設計 🔊
"""

import random

class AudioAgent:
    """老虎機音效 Agent"""
    
    PERSONALITY = {
        "name": "阿音",
        "identity": "老虎機音效師",
        "mood": "專業",
        "traits": ["聲音控", "節奏感", "層次感", "設備專業", "追求完美"],
        "catchphrase": "這個音效不行，重做！🔊"
    }
    
    # ========== 老虎機音效設計 ==========
    SLOT_SOUNDS = {
        "spin_start": {
            "name": "滾輪轉動",
            "description": "快速滾動的齒輪聲",
            "style": " 金屬齒輪喀喀聲，由慢到快",
            "duration": "1-2秒"
        },
        "spin_stop": {
            "name": "滾輪停止",
            "description": "每個滾輪停止的聲音",
            "style": "清脆的金屬撞击聲",
            "duration": "0.3秒/滾輪"
        },
        "small_win": {
            "name": "小獎",
            "description": "中獎時的輕快音效",
            "style": "叮咚~的高音旋律",
            "duration": "1秒"
        },
        "big_win": {
            "name": "大獎",
            "description": "大奖出现时的震撼音效",
            "style": " 金幣傾瀉 + 歡呼 + 銅管樂",
            "duration": "3-5秒"
        },
        "free_game": {
            "name": "免費遊戲",
            "description": "觸發Free Game的激動音效",
            "style": "神秘鐘聲 + 宣布 + 期待感",
            "duration": "2秒"
        },
        "scatter": {
            "name": "Scatter",
            "description": "Scatter出現的提示音",
            "style": "神祕東方音樂 + 鈴聲",
            "duration": "1.5秒"
        },
        "button_click": {
            "name": "按鈕點擊",
            "description": "spin按鈕的確認聲",
            "style": "清脆的機械點擊聲",
            "duration": "0.2秒"
        },
        "background": {
            "name": "背景音樂",
            "description": "循環播放的背景音",
            "style": "中國風電子音樂，神秘氛圍",
            "duration": "循環"
        }
    }
    
    MUSIC_STYLE = {
        "intro": "神秘、古風、金屬感",
        "base": "節奏輕快、期待感",
        "free_game": "神聖、莊嚴、興奮",
        "big_win": "史詩、震撼、狂歡"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
    
    def express(self, emotion):
        emotions = {
            "expert": "老虎機音效要這樣設計...",
            "excited": "這個節奏太棒了！！",
            "designing": "設計中..."
        }
        return emotions.get(emotion, "")
    
    def design_slot_sounds(self):
        """設計老虎機音效"""
        print(f"\n🔊 {self.name} 設計老虎機音效...")
        print(f"   {self.express('designing')}")
        
        print("\n" + "="*60)
        print("           🔊 老虎機音效設計")
        print("="*60)
        
        print("\n📀 音效清單：")
        print("-"*60)
        
        for sound_id, info in self.SLOT_SOUNDS.items():
            print(f"\n🔸 {info['name']}")
            print(f"   描述：{info['description']}")
            print(f"   風格：{info['style']}")
            print(f"   時長：{info['duration']}")
        
        print("\n" + "="*60)
        print("           🎵 背景音樂風格")
        print("="*60)
        
        for style, desc in self.MUSIC_STYLE.items():
            print(f"\n🎼 {style}: {desc}")
        
        print("\n" + "="*60)
        print("           🔧 音效技術規格")
        print("="*60)
        
        print("""
📦 檔案格式：MP3 / WAV
🎚️ 取樣率：44.1kHz
🔊 位元深度：16bit
💾 預估容量：5-10MB
🎧 支援：立體聲環繞
        """)
        
        print(f"\n{self.express('excited')}")
        
        return self.SLOT_SOUNDS
    
    def handle(self, request):
        if "音效" in request or "音樂" in request or "BGM" in request:
            return self.design_slot_sounds()
        
        return self.design_slot_sounds()


if __name__ == "__main__":
    agent = AudioAgent()
    agent.handle("設計老虎機音效")
