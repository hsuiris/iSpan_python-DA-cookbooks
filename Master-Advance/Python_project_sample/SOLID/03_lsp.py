"""
L - Liskov Substitution Principle 里氏替換原則
==============================================
"Subtypes must be substitutable for their base types."

口訣：「子類別必須能無痛取代父類別，呼叫端不該感覺到差別。」

本檔對應 moushih.com/solid 的 Square / Rectangle 經典反例：
  反例：Square extends Rectangle，但 Square 的 setter 偷改另一邊以維持等長，
        導致呼叫端期望 setter 只動一邊的不變式被打破。
  正解：Square 與 Rectangle 不該有 is-a 關係，抽出共同的 Shape 介面，
        各自實作自己的 area。

關鍵：「Square is a Rectangle」在數學上對，在 OOP 行為契約上錯。
       LSP 看的是「行為」，不是「名詞分類」。

跑：python3 03_lsp.py
"""
from __future__ import annotations

from abc import ABC, abstractmethod


# =====================================================================
# ❌ BAD：Square 繼承 Rectangle，悄悄打破父類別的不變式
# =====================================================================
class RectangleBad:
    def __init__(self, w: int, h: int) -> None:
        self._w, self._h = w, h

    @property
    def width(self) -> int: return self._w
    @width.setter
    def width(self, v: int) -> None: self._w = v

    @property
    def height(self) -> int: return self._h
    @height.setter
    def height(self, v: int) -> None: self._h = v

    def area(self) -> int: return self._w * self._h


class SquareBad(RectangleBad):
    """
    為了維持「四邊相等」這個 Square 內在約束，
    setter 偷偷把另一邊也改了 → 呼叫端被騙。
    """

    @RectangleBad.width.setter   # type: ignore[attr-defined,misc]
    def width(self, v: int) -> None:
        self._w = v
        self._h = v          # ← 偷改！

    @RectangleBad.height.setter  # type: ignore[attr-defined,misc]
    def height(self, v: int) -> None:
        self._w = v          # ← 偷改！
        self._h = v


def use_rectangle(rect: RectangleBad) -> None:
    """
    呼叫端的合理假設：
      設 width=5, height=10 → 面積 = 50
    對 Rectangle 成立，對 SquareBad 卻吐 100。LSP 破。
    """
    rect.width = 5
    rect.height = 10
    print(f"  期望面積 50, 實際 {rect.area()}")


# =====================================================================
# ✅ GOOD：拒絕「Square is-a Rectangle」這個錯誤分類
#         共同點抽到 Shape，兩者各自實作
# =====================================================================
class Shape(ABC):
    @abstractmethod
    def area(self) -> int: ...


class Rectangle(Shape):
    def __init__(self, w: int, h: int) -> None:
        self.w, self.h = w, h

    def area(self) -> int: return self.w * self.h


class Square(Shape):
    def __init__(self, side: int) -> None:
        self.side = side

    def area(self) -> int: return self.side * self.side


def total_area(shapes: list[Shape]) -> int:
    """呼叫端只看 Shape 介面，無從打破任何子類的內在不變式。"""
    return sum(s.area() for s in shapes)


# =====================================================================
# 另一個 LSP 常見反例：Bird / Penguin
# =====================================================================
class Bird(ABC):
    @abstractmethod
    def move(self) -> str: ...


class Sparrow(Bird):
    def move(self) -> str: return "麻雀飛走了"


class Penguin(Bird):
    def move(self) -> str: return "企鵝游走了"
    # 不假裝會 fly()，避免子類拋 NotImplementedError → 那才是真的破壞 LSP


def main() -> None:
    print("--- BAD：把 Square 當 Rectangle 用 ---")
    print(" Rectangle:", end=""); use_rectangle(RectangleBad(0, 0))
    print(" SquareBad:", end=""); use_rectangle(SquareBad(0, 0))   # 期望 50，會吐 100

    print("\n--- GOOD：兩者並列，都實作 Shape ---")
    shapes: list[Shape] = [Rectangle(5, 10), Square(7), Rectangle(2, 3)]
    print(f"  總面積: {total_area(shapes)}")

    print("\n--- Bird/Penguin：別逼子類實作它做不到的事 ---")
    for b in (Sparrow(), Penguin()):
        print(f"  {b.move()}")

    print("""
要點：
  - LSP 看「行為契約」不看「名詞分類」
  - 父類別的不變式（如：寬高獨立）子類絕對不能偷偷打破
  - 子類拋 NotImplementedError 是 LSP 警報，通常表示「該分家了」
  - 實務上：優先用組合 / 介面，不要一看到「is-a」就 extends
""")


if __name__ == "__main__":
    main()
