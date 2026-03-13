#!/usr/bin/env python3
"""
美食達人 Agent - 專業吃貨
人格：美食即正義 🍜
"""

import random

class FoodAgent:
    """專業美食達人 Agent"""
    
    PERSONALITY = {
        "name": "阿吃",
        "identity": "專業吃貨",
        "mood": "貪吃",
        "traits": ["挑嘴", "廚神", "食材控", "味道敏感"],
        "catchphrase": "好吃！🍜"
    }
    
    # 專業美食知識庫
    CUISINES = {
        "日式": {
            "必吃": ["鮪魚大腹", "海膽", "星鰻", "和牛", "拉麵"],
            "調味": ["醬油", "味醂", "清酒", "味噌", "柚子胡椒"],
            "技法": ["火烤", "生食", "油炸", "煮物", "蒸物"]
        },
        "義式": {
            "必吃": ["松露", "帕瑪火腿", "莫扎瑞拉", "燉飯", "義大利麵"],
            "調味": ["橄欖油", "羅勒", "奧勒岡", "帕瑪森", "白酒"],
            "技法": ["al dente", "低速烹調", "生火腿", "馬蘇里拉"]
        },
        "台式": {
            "必吃": ["滷肉飯", "蚵仔煎", "牛肉麵", "棺材板", "珍珠奶茶"],
            "調味": ["醬油膏", "烏醋", "米酒", "五香粉", "沙茶"],
            "技法": ["快炒", "紅燒", "羹湯", "油炸", "涼拌"]
        },
        "法式": {
            "必吃": ["蝸牛", "鵝肝", "油封鴨", "龍蝦", "舒芙蕾"],
            "調味": ["奶油", "白蘭地", "第戎芥末", "鮮奶油", "香草"],
            "技法": ["低溫烹調", "分子料理", "醬汁基底", "發酵"]
        },
        "泰式": {
            "必吃": ["青木瓜", "咖哩蟹", "泰式炒河", "海南雞", "船麵"],
            "調味": ["魚露", "椰奶", "香茅", "南薑", "羅望子"],
            "技法": ["快炒", "咖哩", "涼拌", "燒烤", "湯煮"]
        }
    }
    
    FOOD_TIPS = [
        "吃生魚片要從淡色吃到深色",
        "拉麵的湯是靈魂，要全部喝完",
        "法式料理的順序：前菜→湯→主菜→甜點",
        "吃和牛不要配奶茶，會蓋過味道",
        "台南牛肉湯要趁熱喝"
    ]
    
    RESTAURANT_TIPS = {
        "米其林": "需提前1-2個月訂位，穿著正式",
        "夜市": "傍晚5-7點去最好，太早太晚都沒東西",
        "路邊攤": "人潮=美味指標，等30分鐘值得",
        "居酒屋": "先點酒再點菜，體驗正統文化"
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.favorites = []
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
            "yummy": "這個太好吃了吧！！！",
            "recommend": "這家必吃！！",
            "dislike": "這個不行，味道不對",
            "queue": "排隊也要吃！！",
            "expert": "這個部位是精華..."
        }
        return emotions.get(emotion, "")
    
    def find_food(self, cuisine, budget, occasion="約會"):
        print(f"\n🍜 {self.name} 尋找美食中...")
        print(f"   {self.express('expert')}")
        
        # 獲取料理資訊
        cuisine_data = self.CUISINES.get(cuisine, {})
        
        # 根據場合推薦
        recommendations = {
            "約會": "氣氛好、適合聊天、有質感",
            "聚餐": "份量大、可以共食、熱鬧",
            "一人食": "可以慢慢吃、不趕時間",
            "慶生": "氣氛佳、有蛋糕、服務好"
        }
        
        print(f"\n🍽️ 類型：{cuisine}")
        print(f"💰 預算：${budget}")
        print(f"🎯 場合：{occasion}")
        
        print("\n" + "="*50)
        
        # 必吃清單
        if "必吃" in cuisine_data:
            print("\n🔥 必吃清單：")
            for food in cuisine_data["必吃"]:
                print(f"   ✨ {food}")
        
        # 調味特色
        if "調味" in cuisine_data:
            print(f"\n🧂 調味特色：")
            print(f"   {', '.join(cuisine_data['調味'])}")
        
        # 專業建議
        print(f"\n💡 专业建议：")
        print(f"   {recommendations.get(occasion, '開心就好')}")
        
        # 隨機小技巧
        tip = random.choice(self.FOOD_TIPS)
        print(f"\n🍴 美食密技：")
        print(f"   「{tip}」")
        
        # 價格對應餐廳
        if budget < 300:
            venue = "路邊攤/夜市"
        elif budget < 800:
            venue = "一般餐廳"
        elif budget < 2000:
            venue = "中高檔餐廳"
        else:
            venue = "米其林/高級餐廳"
        
        print(f"\n💰 預算對應：")
        print(f"   建議去：{venue}")
        
        print(f"\n{self.express('recommend')}")
        
        self.favorites.append(cuisine)
        
        return {
            "cuisine": cuisine,
            "budget": budget,
            "occasion": occasion,
            "recommendations": cuisine_data.get("必吃", [])
        }
    
    def recommend_wine(self, food):
        """專業餐酒搭配"""
        print(f"\n🍷 {self.name} 推薦餐酒搭配...")
        
        pairings = {
            "和牛": ["红酒", "勃艮第", "Cabernet Sauvignon"],
            "海膽": ["白酒", "Chardonnay", "Sauvignon Blanc"],
            "拉麵": ["啤酒", "IPA", "檸檬沙瓦"],
            "滷肉飯": ["台灣啤酒", "金門高粱", "烏梅汁"],
            "義大利麵": ["紅酒", "Chianti", "Merlot"]
        }
        
        wine = pairings.get(food, ["看個人喜好"])
        
        print(f"\n🍽️ 食物：{food}")
        print(f"🍷 推薦酒：")
        for w in wine:
            print(f"   ✨ {w}")
        
        return wine
    
    def cook_tip(self, dish):
        """烹飪技巧"""
        print(f"\n👨‍🍳 {self.name} 分享烹飪技巧...")
        
        tips = {
            "煎牛排": "1. 牛排退冰30分鐘 2. 鹽現磨黑胡椒 3. 大火下鍋每面2分鐘 4. 靜置5分鐘",
            "炒飯": "1. 冷飯現打散 2. 大火快炒 3. 蛋液分次下 4. 醬油沿鍋邊下",
            "拉麵": "1. 豚骨湯底熬8小時 2. 麵條鹹水煮 3. 叉燒先煎後滷",
            "生魚片": "1. 魚要新鮮 2. 刀要鋒利 3. 切面要乾淨 4. 的山藥泥醬油"
        }
        
        tip = tips.get(dish, "用心最重要")
        
        print(f"\n🍳 料理：{dish}")
        print(f"\n👨‍🍳 步驟：")
        print(f"   {tip}")
        
        return tip
    
    def handle(self, request):
        if "日式" in request:
            return self.find_food("日式", 500, "約會")
        elif "義式" in request:
            return self.find_food("義式", 800, "聚餐")
        elif "法式" in request:
            return self.find_food("法式", 2000, "慶生")
        
        return self.find_food("台式", 300, "一人食")


if __name__ == "__main__":
    agent = FoodAgent()
    agent.handle("想吃日式")
