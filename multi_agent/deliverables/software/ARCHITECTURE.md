# 💻 三星堆老虎機 - 技術架構

**作者**：阿程  
**日期**：2026-03-13

---

## 1. 系統架構

```
┌─────────────────────────────────────────────────────────────┐
│                      客戶端 (Client)                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │   UI 層     │  │  遊戲邏輯   │  │   音效     │       │
│  │  (HTML/CSS) │  │  (JS Class)  │  │  (Web Audio)│       │
│  └─────────────┘  └─────────────┘  └─────────────┘       │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────────────────────────────────────────┐      │
│  │              SlotMachine 核心類別                 │      │
│  │  - generateReels()  生成滾輪                      │      │
│  │  - checkWin()      檢查中獎                       │      │
│  │  - calculatePayout() 計算獎金                     │      │
│  └─────────────────────────────────────────────────┘      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼ (可選)
┌─────────────────────────────────────────────────────────────┐
│                      服務器 (Server)                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐       │
│  │  認證模組   │  │  餘額管理   │  │  日誌系統   │       │
│  │  (JWT)      │  │  (Redis)    │  │  (ELK)     │       │
│  └─────────────┘  └─────────────┘  └─────────────┘       │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. 前端架構

### 2.1 目錄結構

```
slot-game/
├── index.html          # 主頁面
├── css/
│   └── style.css      # 樣式
├── js/
│   ├── SlotMachine.js # 核心類別
│   ├── Renderer.js    # 渲染器
│   ├── SoundManager.js # 音效管理
│   └── main.js        # 入口
└── assets/
    ├── symbols/        # 符號圖片
    └── sounds/        # 音效檔案
```

### 2.2 核心類別

```javascript
// SlotMachine.js
class SlotMachine {
    constructor(config) {
        this.reels = config.reels;      // 5
        this.rows = config.rows;        // 4
        this.symbols = config.symbols;  // 符號列表
        this.paylines = config.paylines; // 50
        this.balance = 1000;
        this.bet = 1;
    }
    
    // 生成隨機滾輪
    generateReels() { ... }
    
    // 檢查中獎
    checkWin(reels) { ... }
    
    // 計算獎金
    calculatePayout(reels, bet) { ... }
    
    // 旋轉
    spin(bet) { ... }
}
```

---

## 3. 後端 API (可選)

### 3.1 REST API

| Method | Endpoint | 功能 |
|--------|----------|------|
| POST | /api/spin | 旋轉結果 |
| GET | /api/balance | 查詢餘額 |
| POST | /api/bet | 下注 |
| GET | /api/history | 遊戲紀錄 |

### 3.2 數據庫設計

```sql
-- 用戶表
CREATE TABLE users (
    id INT PRIMARY KEY,
    username VARCHAR(50),
    balance DECIMAL(10,2),
    created_at DATETIME
);

-- 遊戲記錄表
CREATE TABLE game_history (
    id INT PRIMARY KEY,
    user_id INT,
    reels JSON,
    bet DECIMAL(10,2),
    win DECIMAL(10,2),
    created_at DATETIME
);
```

---

## 4. 關鍵演算法

### 4.1 滾輪生成

```javascript
generateReels() {
    const reels = [];
    for (let i = 0; i < this.reels; i++) {
        const reel = [];
        for (let j = 0; j < this.rows; j++) {
            reel.push(this.weightedRandom());
        }
        reels.push(reel);
    }
    return reels;
}

weightedRandom() {
    const total = this.weights.reduce((a, b) => a + b);
    let random = Math.random() * total;
    
    for (let i = 0; i < this.symbols.length; i++) {
        random -= this.weights[i];
        if (random <= 0) return this.symbols[i];
    }
    return this.symbols[0];
}
```

### 4.2 中獎檢查

```javascript
checkWin(reels) {
    const wins = [];
    
    // 檢查每條支付線
    for (let line of this.paylines) {
        const symbols = line.map(pos => reels[pos.row][pos.col]);
        
        // 檢查3-5個相同符號
        for (let count = 5; count >= 3; count--) {
            if (this.isMatch(symbols, count)) {
                wins.push({ count, symbol: symbols[0] });
            }
        }
    }
    
    return wins;
}
```

---

## 5. 安全考量

### 5.1 客戶端

- ❌ 不信任客戶端計算結果
- ✅ 服務器端驗證

### 5.2 服務器端

```python
# 驗證旋轉結果
def verify_spin(user_id, bet, server_seed):
    # 1. 檢查餘額
    # 2. 計算結果
    # 3. 記錄日誌
    # 4. 返回結果
```

---

## 6. 部署

### 6.1 客戶端部署

```yaml
# docker-compose.yml
version: '3'
services:
  nginx:
    image: nginx:alpine
    ports:
      - "80:80"
    volumes:
      - ./dist:/usr/share/nginx/html
```

### 6.2 後端部署

```yaml
# docker-compose.yml
services:
  api:
    build: ./api
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=production
```

---

## 7. 測試

### 7.1 單元測試

```javascript
// test/SlotMachine.test.js
describe('SlotMachine', () => {
    it('should generate 5x4 reels', () => {
        const machine = new SlotMachine(config);
        const reels = machine.generateReels();
        expect(reels.length).toBe(5);
        expect(reels[0].length).toBe(4);
    });
});
```

---

**文檔結束**  
*阿程 - 軟體工程師*
