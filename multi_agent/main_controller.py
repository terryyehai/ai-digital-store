#!/usr/bin/env python3
"""
Main Controller Agent - 主要協調 Agent
"""

from bgm_agent import BGMAgent
from video_agent import VideoAgent
from youtube_agent import YouTubeAgent
from store_agent import StoreAgent

class MainController:
    """主要協調 Agent"""
    
    def __init__(self):
        self.name = "Main Controller"
        self.agents = {
            "bgm": BGMAgent(),
            "video": VideoAgent(),
            "youtube": YouTubeAgent(),
            "store": StoreAgent()
        }
        
        print("🤖 Main Controller 啟動")
        print(f"已載入 {len(self.agents)} 個 Agent:")
        for name in self.agents:
            print(f"  - {name}")
    
    def route_request(self, request):
        """路由請求到適當的 Agent"""
        
        # 音樂相關
        if any(kw in request for kw in ["音樂", "BGM", "背景音樂", "鋼琴"]):
            return self.agents["bgm"].handle_request(request)
        
        # 影片相關
        if any(kw in request for kw in ["影片", "Shorts", "短影片", "剪輯"]):
            return self.agents["video"].handle_request(request)
        
        # YouTube 相關
        if any(kw in request for kw in ["YouTube", "上傳", "頻道"]):
            return self.agents["youtube"].handle_request(request)
        
        # 商店相關
        if any(kw in request for kw in ["產品", "商品", "訂單", "商店"]):
            return self.agents["store"].handle_request(request)
        
        # 混合請求
        if "生成" in request and "音樂" in request:
            return self.agents["bgm"].handle_request(request)
        
        if "生成" in request and ("影片" in request or "短影片" in request):
            return self.agents["video"].handle_request(request)
        
        return "無法理解請求，請說明需要什麼幫助？"
    
    def run(self):
        """運行主迴圈"""
        print("\n🤖 Main Controller 就緒！")
        print("請告訴我需要什麼幫助：")
        print("  - 生成 30 秒的中國風音樂")
        print("  - 製作一個 AI 產品的短影片")
        print("  - 上傳影片到 YouTube")
        print("  - 查看產品列表")
        
        while True:
            try:
                request = input("\n> ")
                if request.lower() in ["exit", "quit", "離開"]:
                    break
                
                response = self.route_request(request)
                print(f"\n{response}")
                
            except KeyboardInterrupt:
                break
        
        print("\n再見！")


if __name__ == "__main__":
    controller = MainController()
    controller.run()
