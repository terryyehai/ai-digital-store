# 🐛 三星堆老虎機 - 測試案例

**作者**：阿蟲  
**日期**：2026-03-13

---

## 1. 功能測試案例

### 1.1 旋轉功能

| 測試編號 | 測試項目 | 測試步驟 | 預期結果 | 狀態 |
|----------|----------|----------|----------|------|
| TC-001 | 正常旋轉 | 1. 點擊 SPIN | 滾輪開始轉動 | ✅ |
| TC-002 | 旋轉動畫 | 1. 點擊 SPIN | 每軸依次停止 | ✅ |
| TC-003 | 結果顯示 | 1. 旋轉結束 | 20個符號正確顯示 | ✅ |
| TC-004 | 餘額扣除 | 1. 押注1元 2. 點擊 SPIN | 餘額減少50元 | ✅ |

### 1.2 押注功能

| 測試編號 | 測試項目 | 測試步驟 | 預期結果 | 狀態 |
|----------|----------|----------|----------|------|
| TC-010 | 增加押注 | 1. 點擊 + 按鈕 | 押注+1 | ✅ |
| TC-011 | 減少押注 | 1. 點擊 - 按鈕 | 押注-1 | ✅ |
| TC-012 | 押注上限 | 1. 持續點擊 + | 到10後停止 | ✅ |
| TC-013 | 押注下限 | 1. 持續點點擊 - | 到1後停止 | ✅ |
| TC-014 | 餘額不足 | 1. 餘額<50 2. 點擊 SPIN | 顯示餘額不足 | ✅ |

### 1.3 中獎功能

| 測試編號 | 測試項目 | 測試步驟 | 預期結果 | 狀態 |
|----------|----------|----------|----------|------|
| TC-020 | 5連線 Gold | 1. 5個Gold在同線 | 顯示 100x 獎金 | ✅ |
| TC-021 | 4連線 Gold | 1. 4個Gold在同線 | 顯示 25x 獎金 | ✅ |
| TC-022 | 3連線 Gold | 1. 3個Gold在同線 | 顯示 5x 獎金 | ✅ |
| TC-023 | Wild 代替 | 1. Gold+Wild | Wild當Gold計算 | ✅ |
| TC-024 | Scatter 觸發 | 1. 3個Scatter | 觸發 Free Game | ✅ |

### 1.4 Free Game

| 測試編號 | 測試項目 | 測試步驟 | 預期結果 | 狀態 |
|----------|----------|----------|----------|------|
| TC-030 | 觸發條件 | 1. 3個Scatter | 進入 Free Game | ✅ |
| TC-031 | 旋轉次數 | 1. 觸發 Free Game | 10次免費旋轉 | ✅ |
| TC-032 | 重新觸發 | 1. Free Game中3個Scatter | +5次旋轉 | ✅ |
| TC-033 | 倍率加成 | 1. Free Game中獎 | 獎金 2x | ✅ |

---

## 2. 自動化測試腳本

### 2.1 Playwright 測試

```javascript
// tests/slot-game.spec.js
const { test, expect } = require('@playwright/test');

test.describe('老虎機測試', () => {
    
    test.beforeEach(async ({ page }) => {
        await page.goto('slot_game.html');
    });
    
    test('正常旋轉', async ({ page }) => {
        await page.click('#spin-btn');
        await page.waitForTimeout(2000);
        
        // 檢查滾輪有結果
        const reels = await page.$$('.reel');
        expect(reels).toHaveLength(20);
    });
    
    test('押注變化', async ({ page }) => {
        const betDisplay = await page.textContent('#bet-display');
        expect(betDisplay).toBe('1');
        
        await page.click('.bet-btn:has-text("+")');
        const newBet = await page.textContent('#bet-display');
        expect(newBet).toBe('2');
    });
    
    test('餘額扣除', async ({ page }) => {
        const initialBalance = await page.textContent('#balance');
        
        await page.click('#spin-btn');
        await page.waitForTimeout(2000);
        
        const finalBalance = await page.textContent('#balance');
        expect(parseInt(finalBalance)).toBeLessThan(parseInt(initialBalance));
    });
});
```

### 2.2 Jest 單元測試

```javascript
// tests/SlotMachine.test.js
const SlotMachine = require('./SlotMachine');

describe('SlotMachine', () => {
    let machine;
    
    beforeEach(() => {
        machine = new SlotMachine({
            reels: 5,
            rows: 4,
            symbols: ['A', 'K', 'Gold'],
            weights: [50, 30, 20]
        });
    });
    
    test('generateReels 應生成 5x4 矩陣', () => {
        const reels = machine.generateReels();
        expect(reels.length).toBe(5);
        expect(reels[0].length).toBe(4);
    });
    
    test('checkWin 應正確識別5連線', () => {
        const reels = [
            ['Gold', 'Gold', 'Gold', 'Gold'],
            ['A', 'K', 'Q', 'J'],
            ['A', 'K', 'Q', 'J'],
            ['A', 'K', 'Q', 'J'],
            ['A', 'K', 'Q', 'J']
        ];
        
        const wins = machine.checkWin(reels);
        expect(wins.length).toBeGreaterThan(0);
    });
});
```

---

## 3. 回歸測試

### 3.1 每日回歸

| 測試項目 | 頻率 | 負責人 |
|----------|------|--------|
| 基本旋轉功能 | 每日 | CI/CD |
| 支付計算 | 每日 | CI/CD |
| 餘額管理 | 每日 | CI/CD |

### 3.2 每週回歸

| 測試項目 | 頻率 | 負責人 |
|----------|------|--------|
| Free Game 流程 | 每週 | 阿蟲 |
| 支付線正確性 | 每週 | 阿蟲 |
| 音效同步 | 每週 | 阿蟲 |

### 3.3 回歸測試腳本

```bash
#!/bin/bash
# regression_test.sh

echo "=== 老虎機回歸測#試 ==="

 執行 1000 次旋轉
for i in {1..1000}; do
    echo "旋轉 $i/1000"
    node spin_test.js
done

# 檢查結果
echo "=== 檢查結果 ==="
node check_results.js

# 產出報告
echo "=== 產出報告 ==="
node generate_report.js
```

---

## 4. 壓力測試

### 4.1 連續旋轉測試

```javascript
// stress_test.js
async function stressTest(iterations = 10000) {
    console.log(`開始壓力測試: ${iterations} 次旋轉`);
    
    let totalWin = 0;
    let totalBet = 0;
    
    for (let i = 0; i < iterations; i++) {
        const bet = 1;
        const reels = machine.generateReels();
        const win = machine.calculatePayout(reels, bet);
        
        totalBet += bet * 50;
        totalWin += win;
    }
    
    const actualRTP = (totalWin / totalBet) * 100;
    const expectedRTP = 96;
    
    console.log(`實際 RTP: ${actualRTP.toFixed(2)}%`);
    console.log(`預期 RTP: ${expectedRTP}%`);
    console.log(`差異: ${Math.abs(actualRTP - expectedRTP).toFixed(2)}%`);
}
```

---

## 5. Bug 追蹤

### 5.1 已發現問題

| ID | 問題描述 | 嚴重性 | 狀態 |
|----|----------|--------|------|
| BUG-001 | 餘額為負數 | 高 | 已修復 |
| BUG-002 | 動畫不流暢 | 中 | 優化中 |
| BUG-003 | Wild 計算錯誤 | 高 | 已修復 |

---

**文檔結束**  
*阿蟲 - 品保工程師*
