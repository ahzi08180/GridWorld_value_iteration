# GridWorld Random Policy & Evaluation

這是一個基於 Flask 的 GridWorld 網格世界視覺化工具，用於展示強化學習中的**隨機策略 (Random Policy)** 與 **策略評估 (Policy Evaluation)**。

## 功能特點
- **自定義網格**：支援 $n \times n$ 維度（5-9），可自由設定起點、終點與障礙物。
- **全自動流程**：選取完障礙物後，系統將自動生成隨機策略並進行迭代策略評估。
- **雙圖並行展示**：
  - **左圖**：展示隨機生成的行動策略（方向箭頭）。
  - **右圖**：展示計算出的狀態價值函數 $V(s)$。
- **互動式體驗**：支援即時重新生成策略，觀察價值函數的動態變化。

## 專案展示
![GridWorld Demo](https://raw.githubusercontent.com/ahzi08180/GridWorld_Random/main/demo.gif)
*(註：此處可替換為實際的專案截圖或 GIF)*

## 技術堆疊
- **Backend**: Python, Flask, NumPy
- **Frontend**: Vanilla JavaScript, CSS3 (Modern HSL palette), HTML5

## 如何在本機執行
1. **複製專案**：
   ```bash
   git clone https://github.com/ahzi08180/GridWorld_Random.git
   cd GridWorld_Random
   ```
2. **安裝依賴**：
   ```bash
   pip install -r requirements.txt
   ```
3. **啟動伺服器**：
   ```bash
   python app.py
   ```
4. **瀏覽網頁**：
   開啟瀏覽器並輸入 `http://127.0.0.1:5000`

## 數學原理
本專案使用**迭代策略評估 (Iterative Policy Evaluation)**：
$$V_{k+1}(s) = \sum_{a} \pi(a|s) \sum_{s', r} p(s', r | s, a) [r + \gamma V_k(s')]$$
其中設定如下：
- 獎勵 (Reward): 每步 $-1$
- 折扣因子 (Gamma): $0.9$
- 策略 ($\pi$): 隨機生成的確定性策略
