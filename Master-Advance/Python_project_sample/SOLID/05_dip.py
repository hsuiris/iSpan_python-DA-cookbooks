"""
D - Dependency Inversion Principle 相依反轉原則
===============================================
"High-level modules should not depend on low-level modules.
 Both should depend on abstractions.
 Abstractions should not depend on details. Details depend on abstractions."

口訣：「依賴抽象，不要依賴具體。」
      DIP 是把 OCP / LSP / ISP 串起來的膠水。

本檔對應 moushih.com/solid 的 SecurityService 範例：
  反例：SecurityService 內部直接 new LoginService()，與具體類別綁死。
        想換成另一種驗證方式（OAuth、LDAP、雙因素）→ 必須改 SecurityService。
  正解：SecurityService 透過 constructor injection 接收 ILoginService 介面，
        具體實作由外部組裝（IoC / DI），SecurityService 不需要知道、也不該知道。

跑：python3 05_dip.py
"""
from __future__ import annotations

from typing import Protocol


# =====================================================================
# ❌ BAD：高階模組直接 new 低階模組 → 雙向耦合
# =====================================================================
class LoginServiceBad:
    def login(self, user: str, pwd: str) -> bool:
        print(f"  [BAD][Login] 假裝查資料庫驗 {user}")
        return pwd == "1234"


class SecurityServiceBad:
    """
    違反 DIP 的訊號：
      - 在自己內部 new 具體類別
      - 想換驗證方式 → 必須打開 SecurityServiceBad 改 import / 改 new
      - 想做單元測試 → 沒辦法 mock LoginServiceBad，只能讓它真的跑起來
    """

    def __init__(self) -> None:
        self._login = LoginServiceBad()      # ← 寫死了

    def access(self, user: str, pwd: str, resource: str) -> None:
        if self._login.login(user, pwd):
            print(f"  [BAD] {user} 取得 {resource}")
        else:
            print(f"  [BAD] {user} 拒絕")


# =====================================================================
# ✅ GOOD：兩端都依賴抽象（ILoginService），具體實作由外部注入
# =====================================================================
class ILoginService(Protocol):
    """高階與低階的共同語言。"""

    def login(self, user: str, pwd: str) -> bool: ...


# 低階模組 1：傳統帳密
class PasswordLoginService:
    def login(self, user: str, pwd: str) -> bool:
        print(f"  [Pwd] 驗 {user}/{pwd}")
        return pwd == "1234"


# 低階模組 2：OAuth（不改 SecurityService 就能換）
class OAuthLoginService:
    def login(self, user: str, pwd: str) -> bool:
        print(f"  [OAuth] 把 token={pwd!r} 拿去換身分")
        return pwd.startswith("oauth_")


# 低階模組 3：測試替身（單元測試用）
class FakeLoginService:
    """測試時可以隨意決定 login 結果，不需要真的連任何系統。"""

    def __init__(self, allow: bool) -> None: self.allow = allow
    def login(self, user: str, pwd: str) -> bool: return self.allow


# 高階模組：完全不認得任何具體 class，只認 ILoginService 介面
class SecurityService:
    def __init__(self, login: ILoginService) -> None:
        self._login = login                   # ← 由外部塞進來

    def access(self, user: str, pwd: str, resource: str) -> None:
        if self._login.login(user, pwd):
            print(f"  [OK] {user} 取得 {resource}")
        else:
            print(f"  [DENY] {user} 被拒")


# =====================================================================
# Composition Root：組裝策略放在程式進入點
# =====================================================================
def build_security_service(mode: str) -> SecurityService:
    """應用程式啟動時決定要哪個實作；business code 不需要知道。"""
    impl: ILoginService
    if mode == "password":
        impl = PasswordLoginService()
    elif mode == "oauth":
        impl = OAuthLoginService()
    else:
        raise ValueError(f"unknown mode: {mode}")
    return SecurityService(impl)


def main() -> None:
    print("--- BAD：寫死 new LoginService() ---")
    SecurityServiceBad().access("Alice", "1234", "/admin")
    SecurityServiceBad().access("Bob", "wrong", "/admin")

    print("\n--- GOOD：DI 切換實作不需動 SecurityService ---")
    build_security_service("password").access("Alice", "1234", "/admin")
    build_security_service("oauth").access("Carol", "oauth_TOKEN_xyz", "/admin")
    build_security_service("oauth").access("Dave", "wrong", "/admin")

    print("\n--- 測試：注入 fake 不必動到任何真實服務 ---")
    SecurityService(FakeLoginService(allow=True)).access("Test", "*", "/test")
    SecurityService(FakeLoginService(allow=False)).access("Test", "*", "/test")

    print("""
要點：
  - 高階模組（SecurityService）不認得任何具體 class
  - 換實作只動「組裝點」（main / DI container），業務碼零修改
  - 單元測試可注入 Fake / Mock → 不必啟資料庫、不必連網路
  - 這就是「OCP / LSP / ISP 為什麼能成立」的底層機制
""")


if __name__ == "__main__":
    main()
