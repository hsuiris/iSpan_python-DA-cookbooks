# SOLID 原則 Python 教學範例

本目錄參考 <https://moushih.com/solid/>（C# 版）的章節與情境，
以 Python 改寫成 5 支可獨立執行的教學檔案。每支檔案都遵循同一個格式：

```
1. 一句話定義
2. 反例 (BAD)  ─ 重現作者描述的痛點
3. 正解 (GOOD) ─ 套用原則後的寫法
4. main()      ─ 跑兩段對照、印出差異
```

## 為什麼學 SOLID

> "Bad programmers worry about the code. Good programmers worry about data structures."
> — Linus Torvalds

設計模式是「招式」，SOLID 是「內功」。內功不夠，招式只會擺起來像樣，
真打就破綻百出。SOLID 給你的是判斷依據：當你猶豫「這段該不該重構」，
這 5 個原則會替你回答。

## 五大原則一覽

| 縮寫 | 全名 | 一句話 | 對應檔案 |
|---|---|---|---|
| **S** | Single Responsibility | 一個類只該有一個改變的理由 | `01_srp.py` |
| **O** | Open/Closed | 對擴充開放，對修改封閉 | `02_ocp.py` |
| **L** | Liskov Substitution | 子類必須能無痛取代父類 | `03_lsp.py` |
| **I** | Interface Segregation | 多個小介面好過一個肥介面 | `04_isp.py` |
| **D** | Dependency Inversion | 依賴抽象，不要依賴具體 | `05_dip.py` |

## 五原則之間的關係

```
        ┌──────── 提高內聚 ────────┐
        │                          │
       SRP ─┐                ┌─── ISP
            │                │
            ↓                ↓
        ┌────── 用抽象解耦 ──────┐
        │                        │
       DIP ←─── 支撐 ───→ OCP ←─── 支撐 ─── LSP
```

- SRP / ISP 把「責任 / 介面」切細 → 內聚提高
- OCP / LSP 靠**正確的繼承與抽象**讓你能放心擴充
- DIP 是把上面四項串起來的膠水：高階只認介面，低階自由換

## 跑法

```bash
cd Master-Advance/Python_project_sample/SOLID

# 個別跑
python3 01_srp.py
python3 02_ocp.py
python3 03_lsp.py
python3 04_isp.py
python3 05_dip.py

# 一次跑全部
for f in 0*.py; do echo "=== $f ==="; python3 "$f"; done
```

## 學習順序建議

1. **先 SRP** —— 理解「責任」是 SOLID 的核心概念，所有其他原則都建立在它上面
2. **再 DIP** —— 學會用 `Protocol` / `ABC` 把依賴改成抽象，後面的 OCP / LSP / ISP 都會用到
3. **接 OCP** —— 看 DIP 帶來的擴充自由
4. **再 LSP** —— 經典的 Square/Rectangle 反例會讓你對「繼承」更謹慎
5. **最後 ISP** —— 體會「肥介面」是 SRP 的弟弟

## 與設計模式的關係

SOLID 解釋了「為什麼」，設計模式提供「怎麼做」。
看完本目錄後，可前往 `../desig_pattern/` 看 23 個 GoF 模式
如何把這五原則具體化。
