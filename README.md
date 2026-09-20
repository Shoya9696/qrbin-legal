# qrbin-legal

iOS アプリ **QR便** の法務・サポートページ。GitHub Pages で公開する。

```
/                     英語
/ja/                  日本語
```

| ページ | URL |
|---|---|
| サポート（ASC のサポート URL 欄に入れる） | `https://shoya9696.github.io/qrbin-legal/support.html` |
| プライバシーポリシー（ASC のプライバシー URL 欄） | `https://shoya9696.github.io/qrbin-legal/privacy-policy.html` |
| 利用規約 | `https://shoya9696.github.io/qrbin-legal/terms.html` |
| 特定商取引法に基づく表記（日本語のみ） | `https://shoya9696.github.io/qrbin-legal/ja/tokushoho.html` |

## 直しかた

**HTML を直接編集しない。** 日英でずれるので `build.py` の 1 か所から生成する。

```bash
python build.py
```

日付を変えるときは `UPDATED_JA` / `UPDATED_EN` を直す。

## 中身の方針

- **プライバシー**: QR便 は何も収集せず、**転送する内容もサーバーに送らない**（受信ページは CSP で通信そのものを禁止）。事実をそのまま書く
- **利用規約**: 画面とカメラの転送なので、**読めないことがあり得る**と最初に書く。画面の QR は周囲から見えることも書く
- **特商法**: Pro は買い切り ¥500。返金は Apple

アプリのソース・秘密情報はこのリポジトリに置かない。
