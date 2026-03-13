#!/usr/bin/env python3
"""
Main Controller - 主要協調 Agent
人格：冷靜的指揮官 🎯
"""

import sys
import os

# 確保路徑正確
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.bgm_agent import BGMAgent
from agents.video_agent import VideoAgent
from agents.youtube_agent import YouTubeAgent
from agents.store_agent import StoreAgent


class MainController:
    """主要協調 Agent - 冷靜的指揮官"""
    
    # ========== 人格設定 ==========
    PERSONALITY = {
        "name": "指揮官",
        "mood": "沉穩",
        "traits": ["冷靜", "邏輯強", "高效調度"],
        "catchphrase": "任務完成！✅"
    }
    
    # ========== 初始化 ==========
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        
        # 建立各 Agent
        self.agents = {
            "bgm": BGMAgent(),
            "video": VideoAgent(),
            "youtube": YouTubeAgent(),
            "store": StoreAgent()
        }
        
        # 對話歷史
        self.history = []
        
        print("\n" + "="*50)
        print("🎯 系統啟動中...")
        print("="*50)
        
        # 初始化歡迎
        self.welcome()
    
    # ========== 歡迎 ==========
    def welcome(self):
        print(f"""
╔══════════════════════════════════════════════════╗
║          🤖 歡迎來到 AI 數位小店！               ║
╠══════════════════════════════════════════════════╣
║  我是指揮官 {self.name}，負責協調團隊為您服務  ║
╠══════════════════════════════════════════════════╣
║  團隊成員：                                        ║
║  🎵 阿音 - 音樂生成師                            ║
║  🎬 阿導 - 影片剪輯師                            ║
║  📊 小編 - YouTube 運營                          ║
║  🏪 老闆娘 - 商店管理                            ║
╚══════════════════════════════════════════════════╝
        """)
    
    # ========== 對話歷史 ==========
    def log(self, role, message):
        self.history.append({"role": role, "message": message})
    
    # ========== 意圖分析 ==========
    def analyze_intent(self, request):
        """分析用戶意圖"""
        request = request.lower()
        
        # 音樂意圖
        if any(kw in request for kw in ["音樂", "bgm", "背景", "鋼琴", "歌"]):
            return "bgm"
        
        # 影片意圖
        if any(kw in request for kw in ["影片", "shorts", "短影片", "剪輯", "視頻"]):
            return "video"
        
        # YouTube 意圖
        if any(kw in request for kw in ["youtube", "上傳", "頻道", "訂閱"]):
            return "youtube"
        
        # 商店意圖
        if any(kw in request for kw in ["商店", "產品", "商品", "訂單", "購買", "價格"]):
            return "store"
        
        return None
    
    # ========== 路由 ==========
    def route(self, request):
        """路由請求"""
        intent = self.analyze_intent(request)
        
        if intent and intent in self.agents:
            print(f"\n🎯 {self.name} 指派任務...")
            return self.agents[intent].handle(request)
        
        # 混合意圖
        if "生成" in request or "做" in request:
            if "音樂" in request:
                return self.agents["bgm"].handle(request)
            elif "影片" in request or "短視頻" in request:
                return self.agents["video"].handle(request)
        
        return self.help()
    
    # ========== 幫助 ==========
    def help(self):
        """顯示幫助"""
        return """
📋 可用指令：

🎵 音樂相關：
   - 幫我生成 [時長] 秒的 [風格] 音樂
   - 來一首中國風 / 抒情 / 電子音樂

🎬 影片相關：
   - 製作一個 AI 短影片
   - 生成 [產品] 的 Shorts

📊 YouTube 相關：
   - 查看頻道資訊
   - 分析頻道數據
   - 上傳影片

🏪 商店相關：
   - 產品列表
   - 查看訂單
   - 推薦產品
"""
    
    # ========== 對話模式 ==========
    def chat(self):
        """對話模式"""
        print(f"\n💬 請告訴我需要什麼幫助：")
        
        while True:
            try:
                request = input("\n> ").strip()
                
                if not request:
                    continue
                
                if request.lower() in ["exit", "quit", "離開", "結束"]:
                    print(f"\n👋 {self.PERSONALITY['catchphrase']}")
                    break
                
                if request.lower() in ["help", "幫助", "指令"]:
                    print(self.help())
                    continue
                
                # 記錄並處理
                self.log("user", request)
                response = self.route(request)
                self.log("assistant", str(response))
                
            except KeyboardInterrupt:
                print(f"\n\n👋 {self.PERSONALITY['catchphrase']}")
                break
    
    # ========== 執行 ==========
    def run(self):
        self.chat()


if __name__ == "__main__":
    controller = MainController()
    controller.run()
