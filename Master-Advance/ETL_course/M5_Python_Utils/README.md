# M5 — Python Utils

> 寫 ETL 的三個小工具 — 學會了，你的程式會變 Pythonic

## 模組內容

| 檔案 | 主題 | 為什麼重要 |
|:-----|:-----|:-----------|
| **`S5_pathlib.ipynb`** | `pathlib` 檔案路徑 | 跨平台安全、比 `os.path` 好讀 10 倍 |
| **`S6_zip_iteration.ipynb`** | `zip()` 多物件迭代 | 兩個 list 一起跑，取代 `for i in range(len(...))` |
| **`S7_type_hints.ipynb`** | Type Hints 型別提示 | IDE 自動補全、錯誤早期發現、團隊協作必備 |

---

## S5: pathlib — 物件導向的路徑操作

```python
# ❌ 舊式寫法
import os
path = os.path.join("data", "raw", "2024", "orders.csv")
if os.path.exists(path):
    basename = os.path.basename(path)
    ext = os.path.splitext(basename)[1]

# ✅ pathlib
from pathlib import Path
path = Path("data") / "raw" / "2024" / "orders.csv"
if path.exists():
    basename = path.name
    ext = path.suffix
```

## S6: zip — 同步迭代多個序列

```python
# ❌ 不 Pythonic
for i in range(len(names)):
    print(names[i], ages[i])

# ✅ Pythonic
for name, age in zip(names, ages):
    print(name, age)
```

## S7: Type Hints — 為什麼該寫？

```python
# ❌ 看不出 df 應該是什麼
def clean(df, col):
    return df[col].str.strip()

# ✅ IDE 可以幫你檢查型別、自動補全
def clean(df: pd.DataFrame, col: str) -> pd.Series:
    return df[col].str.strip()
```

**真實好處：**
- VS Code / PyCharm 可以即時抓錯
- `mypy` 可以在 CI 裡靜態檢查
- 讀別人的程式變輕鬆（一看簽名就知道要傳什麼）
