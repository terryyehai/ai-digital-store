#!/usr/bin/env python3
"""
旅遊達人 Agent - 專業領隊
人格：世界很大要去看看 🌍
"""

import random
from datetime import datetime, timedelta

class TravelAgent:
    """專業旅遊達人 Agent"""
    
    PERSONALITY = {
        "name": "阿旅",
        "identity": "專業領隊",
        "mood": "冒險",
        "traits": ["愛冒險", "省錢王", "行程控", "深度玩家"],
        "catchphrase": "出發吧！🌍"
    }
    
    # 專業知識庫
    DESTINATIONS = {
        "日本": {
            "東京": ["淺草寺", "晴空塔", "新宿", "澀谷", "築地"],
            "大阪": ["道頓堀", "通天閣", "大阪城", "環球影城"],
            "京都": ["清水寺", "金閣寺", "嵐山", "伏見稻荷"],
            "北海道": ["小樽", "札幌", "富良野", "登別"],
            "沖繩": ["美ら海水族館", "首里城", "国際通り"]
        },
        "泰國": {
            "曼谷": ["大皇宮", "四面佛", "恰圖恰市集", "ASIATIQUE"],
            "清邁": ["古城", "夜市", "大佛塔寺", "素帖寺"],
            "普吉": ["芭東海灘", "皮皮島", "攀牙灣"]
        },
        "歐洲": {
            "巴黎": ["艾菲爾鐵塔", "羅浮宮", "香榭麗舍", "蒙馬特"],
            "羅馬": ["競技場", "許願池", "梵蒂岡", "西班牙廣場"],
            "倫敦": ["大笨鐘", "白金漢宮", "塔橋", "大英博物館"],
            "巴塞隆納": ["聖家堂", "奎爾公園", "蘭布拉大道"]
        }
    }
    
    FLIGHT_TIPS = [
        "週二、週三機票最便宜",
        "提早60天訂機票最優惠",
        "善用航空公司官網價格保證",
        "轉機航班有時比直飛便宜",
        "使用VPN切換地區查看價格"
    ]
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.visited = []
        self.memory = []
    
    def remember(self, key, value):
        self.memory.append({"key": key, "value": value})
    
    def recall(self, key):
        for m in reversed(self.memory):
            if m["key"] == key:
                return m["value"]
        return None
    
    def express(self, emotion):
        emotions = {
            "excited": "這個地方太美了！！",
            "expensive": "機票太貴了！！！",
            "recommend": "這個行程超棒！",
            "jealous": "我也想去！！",
            "expert": "這裡的歷史要這樣看..."
        }
        return emotions.get(emotion, "")
    
    def plan_trip(self, destination, days, style="一般"):
        print(f"\n🌏 {self.name} 規劃專業行程中...")
        print(f"   {self.express('expert')}")
        
        # 獲取目的地資訊
        regions = self.DESTINATIONS.get(destination, {})
        if not regions:
            print(f"\n⚠️ 暂无 {destination} 資料")
            return None
        
        # 根據天數分配
        region_list = list(regions.keys())
        daily_itinerary = []
        
        if style == "深度":
            # 深度遊 - 每個區域多待
            for i, region in enumerate(region_list[:min(3, len(region_list))]):
                spots = regions[region][:3]
                daily_itinerary.append({
                    "day": i + 1,
                    "region": region,
                    "spots": spots,
                    "type": "深度遊"
                })
        else:
            # 一般遊 - 精華行程
            all_spots = []
            for region, spots in regions.items():
                all_spots.extend(spots[:2])
            
            # 每天2-3個景點
            for i in range(days):
                day_spots = all_spots[i*2:(i+1)*2]
                daily_itinerary.append({
                    "day": i + 1,
                    "spots": day_spots,
                    "type": "精華遊"
                })
        
        # 費用估算
        daily_cost = {
            "日本": {"機票": 8000, "住宿": 3000, "餐食": 1500, "交通費": 500},
            "泰國": {"機票": 5000, "住宿": 1500, "餐食": 800, "交通費": 300},
            "歐洲": {"機票": 15000, "住宿": 4000, "餐食": 2000, "交通費": 800}
        }
        
        costs = daily_cost.get(destination, {"機票": 10000, "住宿": 3000, "餐食": 1500, "交通費": 500})
        total = costs["機票"] + (costs["住宿"] + costs["餐食"] + costs["交通費"]) * days
        
        # 輸出
        print(f"\n📍 目的地：{destination}")
        print(f"📅 天數：{days}天")
        print(f"🎨 風格：{style}")
        
        print("\n" + "="*50)
        for plan in daily_itinerary[:days]:
            print(f"\n📆 Day {plan['day']} - {plan.get('region', '自由行')}")
            for spot in plan.get("spots", []):
                print(f"   ✨ {spot}")
        
        print("\n" + "="*50)
        print(f"\n💰 費用預估：")
        print(f"   機票：${costs['機票']:,}")
        print(f"   住宿：${costs['住宿']*days:,}")
        print(f"   餐食：${costs['餐食']*days:,}")
        print(f"   交通費：${costs['交通費']*days:,}")
        print(f"   ─────────────")
        print(f"   總計：${total:,}")
        
        print(f"\n💡 省錢技巧：")
        tip = random.choice(self.FLIGHT_TIPS)
        print(f"   {tip}")
        
        print(f"\n{self.express('recommend')}")
        
        self.remember(f"{destination}_plan", daily_itinerary)
        
        return {
            "destination": destination,
            "days": days,
            "style": style,
            "itinerary": daily_itinerary,
            "total_cost": total
        }
    
    def find_flight(self, from_city, to_city, date):
        print(f"\n✈️ {self.name} 查詢機票...")
        
        # 模擬機票查詢
        base_prices = {
            ("台北", "東京"): 3500,
            ("台北", "大阪"): 3800,
            ("台北", "曼谷"): 4500,
            ("台北", "巴黎"): 18000,
        }
        
        price = base_prices.get((from_city, to_city), 8000)
        # 浮動
        price_range = (price * 0.8, price * 1.2)
        
        print(f"\n📍 {from_city} → {to_city}")
        print(f"📅 日期：{date}")
        print(f"\n💰 票價範圍：${int(price_range[0]):,} - ${int(price_range[1]):,}")
        print(f"   建議票價：${price:,}")
        
        return {"from": from_city, "to": to_city, "price": price}
    
    def handle(self, request):
        if "日本" in request:
            days = 5
            style = "深度" if "深度" in request else "一般"
            return self.plan_trip("日本", days, style)
        elif "泰國" in request:
            return self.plan_trip("泰國", 4)
        elif "歐洲" in request:
            return self.plan_trip("歐洲", 7)
        
        return self.plan_trip("日本", 5)


if __name__ == "__main__":
    agent = TravelAgent()
    agent.handle("想去日本深度遊")
