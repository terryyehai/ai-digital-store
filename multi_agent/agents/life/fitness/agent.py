#!/usr/bin/env python3
"""
健身教練 Agent - 專業健身教練
人格：身體是靈魂的容器 💪
"""

import random

class FitnessAgent:
    """專業健身教練 Agent"""
    
    PERSONALITY = {
        "name": "阿壯",
        "identity": "專業健身教練",
        "mood": "嚴格",
        "traits": ["嚴格", "科學訓練", "飲食控制", "增肌專家"],
        "catchphrase": "練起來！💪"
    }
    
    # 專業訓練知識庫
    EXERCISES = {
        "胸肌": {
            "複合": ["臥推", "槓鈴胸推", "雙槓撐體"],
            "孤立": ["啞鈴飛鳥", "Cable夾胸", "機械胸"],
            "技巧": "臥推時肩胛骨後收，感受胸肌發力"
        },
        "背肌": {
            "複合": ["硬舉", "槓鈴划船", "引體向上"],
            "孤立": ["Cable划船", "啞鈴划船", "高位下拉"],
            "技巧": "划船時肘貼身體，感受背闊肌收縮"
        },
        "腿部": {
            "複合": ["深蹲", "硬舉", "腿推"],
            "孤立": ["腿屈伸", "腿彎舉", "提踵"],
            "技巧": "深蹲時膝蓋對準腳尖，核心繃緊"
        },
        "肩部": {
            "複合": ["槓鈴肩推", "啞鈴推舉"],
            "孤立": ["側平舉", "前平舉", "面拉", "反向飛鳥"],
            "技巧": "推舉時手肘略低於肩膀，保護肩關節"
        },
        "核心": {
            "訓練": ["平板支撐", "死蟲", "農夫行走", "藥球旋轉", "懸垂舉腿"],
            "技巧": "吸氣時肚子鼓起，吐氣時收緊"
        }
    }
    
    NUTRITION = {
        "增肌": {
            "熱量": "+300-500大卡/天",
            "蛋白質": "1.6-2.2g/kg體重",
            "碳水": "4-6g/kg體重",
            "脂肪": "0.8-1g/kg體重"
        },
        "減脂": {
            "熱量": "-300-500大卡/天",
            "蛋白質": "1.8-2.2g/kg體重",
            "碳水": "2-3g/kg體重",
            "脂肪": "0.6-0.8g/kg體重"
        },
        "維持": {
            "熱量": "基礎代謝+活動消耗",
            "蛋白質": "1.2-1.6g/kg體重",
            "碳水": "3-5g/kg體重",
            "脂肪": "0.8-1g/kg體重"
        }
    }
    
    SUPPLEMENTS = {
        "必備": ["乳清蛋白", "肌酸", "維生素D"],
        "可選": ["BCAA", "魚油", "鋅", "鎂"],
        "進階": ["HMB", "Beta-alanine", "Citrulline"]
    }
    
    def __init__(self):
        self.name = self.PERSONALITY["name"]
        self.training_log = []
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
            "strict": "今天的訓練呢？",
            "encourage": "再撐一下！！！",
            "weak": "這個重量不行",
            "proud": "我已經練完了",
            "expert": "這個動作要注意..."
        }
        return emotions.get(emotion, "")
    
    def create_plan(self, goal, days, level="中"):
        print(f"\n🏋️ {self.name} 設計專業訓練計畫...")
        print(f"   {self.express('expert')}")
        
        # 獲取營養數據
        nutrition = self.NUTRITION.get(goal, self.NUTRITION["維持"])
        
        print(f"\n🎯 目標：{goal}")
        print(f"📅 頻率：{days}天/週")
        print(f"📊 等級：{level}")
        
        # 訓練分割
        splits = {
            "3天": ["胸+三頭", "背+二頭", "腿+肩+核心"],
            "4天": ["胸+三頭", "背+二頭", "腿+核心", "肩+手臂"],
            "5天": ["胸", "背", "腿", "肩", "手臂+核心"],
            "6天": ["胸", "背", "腿", "胸", "背", "肩+手臂"]
        }
        
        split = splits.get(f"{days}天", splits["4天"])
        
        print("\n" + "="*50)
        print("\n📋 訓練分割：")
        for i, day in enumerate(split, 1):
            print(f"   Day{i}: {day}")
        
        # 每個部位練習
        print("\n" + "="*50)
        print("\n💪 動作安排：")
        
        for muscle, data in self.EXERCISES.items():
            if muscle in str(split):
                print(f"\n🔥 {muscle}：")
                if "複合" in data:
                    print(f"   複合動作：{', '.join(data['複合'][:2])}")
                if "孤立" in data:
                    print(f"   孤立動作：{', '.join(data['孤立'][:2])}")
                print(f"   技巧：{data['技巧']}")
        
        # 營養建議
        print("\n" + "="*50)
        print("\n🥗 營養建議（增肌期）：")
        for k, v in nutrition.items():
            print(f"   {k}：{v}")
        
        # 補劑建議
        print("\n💊 補劑建議：")
        print(f"   必備：{', '.join(self.SUPPLEMENTS['必備'])}")
        
        # 組數次數
        print("\n" + "="*50)
        print("\n📈 訓練量建議：")
        print(f"   複合動作：4-5組 x 6-12下")
        print(f"   孤立動作：3-4組 x 12-15下")
        print(f"   休息時間：複合90秒、孤立60秒")
        
        print(f"\n{self.express('encourage')}")
        
        self.remember(f"{goal}_plan", split)
        
        return {
            "goal": goal,
            "days": days,
            "split": split,
            "nutrition": nutrition
        }
    
    def calculate_macros(self, weight, goal):
        """計算巨量營養素"""
        print(f"\n📊 {self.name} 計算營養需求...")
        
        # 基礎代謝估算 (Mifflin-St Jeor)
        bmr = 10 * weight + 6.25 * 175 - 5 * 30 + 5  # 假設175cm, 30歲男性
        tdee = bmr * 1.375  # 輕度活動
        
        if goal == "增肌":
            calories = tdee + 400
            protein = weight * 2.0
        elif goal == "減脂":
            calories = tdee - 400
            protein = weight * 2.2
        else:
            calories = tdee
            protein = weight * 1.6
        
        carbs = (calories - protein * 4) / 2 / 4
        fat = (calories - protein * 4 - carbs * 4) / 9
        
        print(f"\n⚖️ 體重：{weight}kg")
        print(f"🎯 目標：{goal}")
        print(f"\n📊 每日營養需求：")
        print(f"   熱量：{int(calories)} 大卡")
        print(f"   蛋白質：{int(protein)}g")
        print(f"   碳水：{int(carbs)}g")
        print(f"   脂肪：{int(fat)}g")
        
        return {"calories": calories, "protein": protein, "carbs": carbs, "fat": fat}
    
    def form_check(self, exercise):
        """姿勢檢查"""
        print(f"\n🔍 {self.name} 檢查姿勢...")
        
        checks = {
            "臥推": [
                "1. 眼睛在槓下方",
                "2. 腳掌貼地",
                "3. 背挺起呈橋狀",
                "4. 握距比肩寬",
                "5. 下放觸胸",
                "6. 頂點手肘鎖死"
            ],
            "深蹲": [
                "1. 腳與肩同寬",
                "2. 膝蓋對準腳尖",
                "3. 核心繃緊",
                "4. 蹲至大腿與地平行",
                "5. 膝蓋不內夾",
                "6. 起身時伸髖"
            ],
            "硬舉": [
                "1. 槓靠近小腿",
                "2. 握距與肩同寬",
                "3. 背打直不弓腰",
                "4. 臀部先啟動",
                "5. 槓全程貼腿",
                "6. 頂點挺髖"
            ],
            "划船": [
                "1. 背部打直",
                "2. 握距與肩同寬",
                "3. 肘貼身體",
                "4. 拉到腹部",
                "5. 擠壓背肌",
                "6. 離心控制"
            ]
        }
        
        form = checks.get(exercise, ["標準姿勢"])
        
        print(f"\n🏋️ 動作：{exercise}")
        print(f"\n✅ 檢查清單：")
        for f in form:
            print(f"   {f}")
        
        return form
    
    def handle(self, request):
        if "增肌" in request:
            return self.create_plan("增肌", 5)
        elif "減脂" in request:
            return self.create_plan("減脂", 6)
        
        return self.create_plan("增肌", 4)


if __name__ == "__main__":
    agent = FitnessAgent()
    agent.handle("想要增肌")
