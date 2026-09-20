#!/usr/bin/env python3
"""QR便 の法務・サポートページを生成する。

日英 2 言語ぶんを手で書き分けると必ずずれるので、1 か所から吐く。
ルートが英語、`ja/` が日本語（wake5-legal と同じ作り）。

    python build.py
"""
from __future__ import annotations

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
CONTACT = "shoya96.apps@gmail.com"
RECEIVER = "https://qrbin.pages.dev/"
UPDATED_JA = "2026年9月20日"
UPDATED_EN = "20 September 2026"

STYLE = """
  :root { color-scheme: light dark; }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Yu Gothic", sans-serif;
    line-height: 1.9;
    max-width: 42rem;
    margin: 0 auto;
    padding: 2.5rem 1.25rem 6rem;
    color: #1c1c1e;
    background: #fff;
  }
  @media (prefers-color-scheme: dark) {
    body { color: #ececec; background: #111; }
    h1, h2 { color: #fff; }
    .box, .card { background: #1c1c1e; border-color: #333; }
  }
  h1 { font-size: 1.6rem; margin-bottom: .25rem; }
  h2 { font-size: 1.15rem; margin-top: 2.5rem; }
  .updated, .lead { color: #6b6b70; font-size: .9rem; }
  .box, .card {
    display: block;
    background: #f2f5fa; border: 1px solid #dde3ec; border-radius: .75rem;
    padding: 1rem 1.25rem; margin: 1.25rem 0;
    text-decoration: none; color: inherit;
  }
  .card strong { display: block; font-size: 1.05rem; }
  .card span { color: #6b6b70; font-size: .92rem; }
  .warn { background: #fff6e9; border-color: #f0d9b5; }
  @media (prefers-color-scheme: dark) { .warn { background: #2a2015; border-color: #4a3a22; } }
  table { border-collapse: collapse; width: 100%; margin: 1rem 0; }
  th, td { border-bottom: 1px solid #e2e6ec; padding: .6rem .4rem; text-align: left; vertical-align: top; }
  th { width: 34%; font-weight: 600; }
  @media (prefers-color-scheme: dark) { th, td { border-color: #333; } }
  ul { padding-left: 1.25rem; }
  footer { margin-top: 4rem; font-size: .85rem; color: #6b6b70; }
  a { color: #4c6fb1; }
"""


def page(lang: str, title: str, body: str, home: str | None) -> str:
    # 目次ページ自身に「トップへ戻る」を出すと自分自身へのリンクになるので出さない。
    back_link = ""
    if home:
        label = "トップへ戻る" if lang == "ja" else "Back to top"
        back_link = "  <p><a href=\"" + home + "\">" + label + "</a></p>" + chr(10)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<style>{STYLE}</style>
</head>
<body>
{body}
<footer>
{back_link}  <p>QR便 — {CONTACT}</p>
</footer>
</body>
</html>
"""


# --- 英語 ---------------------------------------------------------------

EN_INDEX = f"""
<h1>QR便</h1>
<p class="lead">Move text, links and small files between your iPhone and your PC
using only a screen and a camera — no network, no account, no cable.</p>

<a class="card" href="./support.html">
  <strong>Support</strong>
  <span>How it works, FAQ, and how to reach us</span>
</a>
<a class="card" href="./privacy-policy.html">
  <strong>Privacy Policy</strong>
  <span>What we collect (nothing) and where your data lives</span>
</a>
<a class="card" href="./terms.html">
  <strong>Terms of Use</strong>
  <span>What QR便 does and does not promise</span>
</a>
<a class="card" href="./ja/">
  <strong>日本語</strong>
  <span>Japanese version</span>
</a>
"""

EN_PRIVACY = f"""
<h1>Privacy Policy</h1>
<p class="updated">QR便 &nbsp;/&nbsp; Last updated: {UPDATED_EN}</p>

<div class="box">
  <strong>QR便 collects nothing, and what you transfer never reaches a server.</strong><br>
  Data moves as animated QR codes shown on one screen and read by the other
  device's camera. There is no upload, no relay and no temporary storage —
  not even on the receiving web page.
</div>

<h2>What we collect</h2>
<p><strong>Nothing.</strong> QR便 does not:</p>
<ul>
  <li>ask you to create an account or sign in</li>
  <li>send the text, links or files you transfer anywhere</li>
  <li>use analytics, advertising or tracking SDKs</li>
  <li>read your location, contacts, calendar or health data</li>
</ul>

<h2>The camera</h2>
<p>
  The app uses the camera only to read QR codes on the other device's screen.
  Camera frames are examined on your device and are never stored or sent.
  The receiving page on your PC works the same way, inside your browser.
</p>

<h2>Photos and files</h2>
<p>
  When you pick a photo, iOS hands that single photo to the app; the app does not
  browse your library. Photos are re-encoded before sending, so information
  attached to the original (such as location) is not transferred. A file you
  receive is written to a temporary folder only so you can share or save it, and
  it is deleted when you continue or restart the app.
</p>

<h2>The receiving web page</h2>
<p>
  The page at <a href="{RECEIVER}">{RECEIVER}</a> runs entirely in your browser.
  Its Content-Security-Policy forbids the page from making any network request
  after it loads, so the data it decodes cannot leave your PC. An offline copy of
  the same page is a single HTML file you can keep on your own machine.
</p>

<h2>What is stored on your device</h2>
<p>
  Only settings: whether you have seen the tutorial, how many free transfers of
  photos and files you have used, and whether you own QR便 Pro. Deleting the app
  deletes them.
</p>

<h2>Purchases</h2>
<p>
  QR便 Pro is a one-time purchase handled by Apple. We never see your payment
  details; the app only asks Apple whether this Apple Account owns Pro.
</p>

<h2>Children</h2>
<p>QR便 is not directed at children and collects no personal data from anyone.</p>

<h2>Changes</h2>
<p>If this policy changes, the updated version will always be on this page.</p>

<h2>Contact</h2>
<p>{CONTACT}</p>
"""

EN_SUPPORT = f"""
<h1>Support</h1>
<p class="updated">QR便 &nbsp;/&nbsp; Last updated: {UPDATED_EN}</p>

<h2>How to use it</h2>
<ul>
  <li>On your PC, open <a href="{RECEIVER}">{RECEIVER}</a> in Chrome or Edge.</li>
  <li>Click “Start camera” and allow the browser to use the camera.</li>
  <li>On your iPhone or iPad, send the clipboard from the home screen, or choose
      QR便 in the share sheet, and hold the screen about 30&nbsp;cm (1&nbsp;ft) from the camera.</li>
  <li>Received text is copied on the PC automatically.</li>
</ul>

<h2>If nothing is read</h2>
<ul>
  <li>Move the phone further away — most webcams cannot focus closer than about 30&nbsp;cm.</li>
  <li>Turn the screen brightness up and avoid reflections on the glass.</li>
  <li>Hold the screen square to the camera, not at an angle.</li>
  <li>Switch the sending preset to “Stable”, which uses a coarser code.</li>
</ul>

<h2>How much can it send?</h2>
<p>
  Screen-to-camera transfer is slow by nature: a few kilobytes per second.
  Text, links and the clipboard arrive almost instantly. Files are limited to
  100&nbsp;KB, and photos are shrunk automatically to fit.
</p>

<h2>QR便 Pro</h2>
<p>
  Pro is a one-time purchase that removes the limits on text length and on how
  many photos and files you can send. If you have bought it before, use
  “Restore Purchase” on the Pro screen.
</p>

<h2>Contact</h2>
<p>{CONTACT}</p>
"""

EN_TERMS = f"""
<h1>Terms of Use</h1>
<p class="updated">QR便 &nbsp;/&nbsp; Last updated: {UPDATED_EN}</p>

<div class="box warn">
  <strong>Transfers can fail.</strong> Reading a QR code depends on your camera,
  the lighting, the distance and the screen. QR便 verifies every transfer with a
  SHA-256 hash and shows you the result, but it cannot promise that any
  particular transfer will succeed. Do not rely on it as your only copy of
  anything important.
</div>

<h2>What QR便 is</h2>
<p>
  An app that shows data as animated QR codes so another device's camera can read
  it. It does not use a network for transfers.
</p>

<h2>Your responsibility</h2>
<ul>
  <li>You are responsible for what you transfer and for having the right to transfer it.</li>
  <li>A QR code on a screen can be seen or filmed by anyone nearby. Choose your surroundings.</li>
  <li>On a company or school computer, follow that organisation's rules.</li>
</ul>

<h2>Purchases</h2>
<p>
  QR便 Pro is a one-time purchase through Apple. Refunds are handled by Apple
  under Apple's terms.
</p>

<h2>No warranty</h2>
<p>
  QR便 is provided “as is”, without warranty of any kind. To the extent permitted
  by law, we are not liable for any loss arising from its use, including data
  that was not transferred or was transferred incorrectly.
</p>

<h2>Trademark</h2>
<p>QR Code is a registered trademark of DENSO WAVE INCORPORATED.</p>

<h2>Changes</h2>
<p>These terms may change. The version on this page is always the current one.</p>

<h2>Contact</h2>
<p>{CONTACT}</p>
"""

# --- 日本語 -------------------------------------------------------------

JA_INDEX = f"""
<h1>QR便</h1>
<p class="lead">画面とカメラだけで、iPhone と PC のあいだで文章・URL・小さなファイルを送る。
ネットワークもアカウントもケーブルも使いません。</p>

<a class="card" href="./support.html">
  <strong>サポート</strong>
  <span>使い方・よくある質問・お問い合わせ</span>
</a>
<a class="card" href="./privacy-policy.html">
  <strong>プライバシーポリシー</strong>
  <span>何も集めないこと、データの置き場所</span>
</a>
<a class="card" href="./terms.html">
  <strong>利用規約</strong>
  <span>QR便 が約束すること・しないこと</span>
</a>
<a class="card" href="./tokushoho.html">
  <strong>特定商取引法に基づく表記</strong>
  <span>販売事業者・価格・引渡し時期</span>
</a>
<a class="card" href="../">
  <strong>English</strong>
  <span>英語版</span>
</a>
"""

JA_PRIVACY = f"""
<h1>プライバシーポリシー</h1>
<p class="updated">QR便 &nbsp;/&nbsp; 最終更新: {UPDATED_JA}</p>

<div class="box">
  <strong>QR便 は何も収集しません。転送する内容もサーバーに送信されません。</strong><br>
  データは画面に出したアニメーション QR を、もう一方の端末のカメラが読み取ることで移ります。
  アップロードも中継も一時保存もありません。PC で開く受信ページでも同じです。
</div>

<h2>収集する情報</h2>
<p><strong>ありません。</strong> QR便 は次のことを行いません。</p>
<ul>
  <li>アカウントの作成やサインインを求める</li>
  <li>転送した文章・URL・ファイルをどこかへ送る</li>
  <li>解析・広告・追跡のための仕組みを入れる</li>
  <li>位置情報・連絡先・カレンダー・ヘルスケアの情報を読む</li>
</ul>

<h2>カメラ</h2>
<p>
  カメラは、もう一方の端末の画面に出ている QR を読むためだけに使います。
  映像は端末の中だけで処理し、保存も送信もしません。PC の受信ページも、
  ブラウザの中だけで同じ処理を行います。
</p>

<h2>写真とファイル</h2>
<p>
  写真を選ぶと、iOS が選んだ 1 枚だけをアプリに渡します。アプリが写真アルバムを
  見て回ることはありません。写真は送る前に作り直すため、元の写真に付いていた
  情報（位置情報など）は転送されません。受け取ったファイルは、共有・保存のために
  一時的な場所へ書き出すだけで、「続けて受け取る」を押したときと次回の起動時に消します。
</p>

<h2>PC の受信ページ</h2>
<p>
  <a href="{RECEIVER}">{RECEIVER}</a> のページは、すべてブラウザの中で動きます。
  Content-Security-Policy で、読み込んだ後の通信そのものを禁止しているため、
  復元した内容が PC の外へ出ることはありません。同じページを 1 つの HTML ファイルに
  まとめたオフライン版も用意しています。
</p>

<h2>端末に保存するもの</h2>
<p>
  設定だけです。チュートリアルを見たかどうか、写真・ファイルを無料で何回使ったか、
  QR便 Pro を持っているかどうか。アプリを削除すれば消えます。
</p>

<h2>購入について</h2>
<p>
  QR便 Pro は Apple を通じた買い切りです。お支払いの情報を当方が見ることはありません。
  アプリは「この Apple アカウントが Pro を持っているか」を Apple に尋ねるだけです。
</p>

<h2>お子さまについて</h2>
<p>QR便 は子ども向けのアプリではなく、誰からも個人情報を収集しません。</p>

<h2>変更</h2>
<p>本ポリシーは変更されることがあります。常にこのページに掲載されているものが最新版です。</p>

<h2>お問い合わせ</h2>
<p>{CONTACT}</p>
"""

JA_SUPPORT = f"""
<h1>サポート</h1>
<p class="updated">QR便 &nbsp;/&nbsp; 最終更新: {UPDATED_JA}</p>

<h2>使い方</h2>
<ul>
  <li>PC のブラウザ（Chrome / Edge）で <a href="{RECEIVER}">{RECEIVER}</a> を開きます。</li>
  <li>「カメラを起動」を押し、ブラウザの確認に「許可」を選びます。</li>
  <li>iPhone / iPad で、ホームの「クリップボードを PC へ送る」か、共有シートの「QR便」を選び、
      画面を PC のカメラから 30cm ほど離して向けます。</li>
  <li>受け取った文章は、PC で自動的にコピーされます。</li>
</ul>

<h2>読み取れないとき</h2>
<ul>
  <li>少し離してください。多くの Web カメラは 30cm より近いとピントが合いません。</li>
  <li>画面を明るくし、画面への映り込みを避けてください。</li>
  <li>斜めではなく、カメラに正面から向けてください。</li>
  <li>送信プリセットを「安定」にすると、粗い（読みやすい）QR になります。</li>
</ul>

<h2>どれくらい送れますか</h2>
<p>
  画面とカメラの転送は、もともと遅い方法です（毎秒 数 KB）。文章・URL・クリップボードは
  ほぼ一瞬で届きます。ファイルは 100KB までで、写真は自動で小さくして送ります。
</p>

<h2>QR便 Pro</h2>
<p>
  Pro は買い切りです。文章の長さの上限（無料は 400 文字）と、写真・ファイルの回数の
  制限がなくなります。以前に購入されている場合は、Pro の画面の「購入を復元」をお使いください。
</p>

<h2>お問い合わせ</h2>
<p>{CONTACT}</p>
"""

JA_TERMS = f"""
<h1>利用規約</h1>
<p class="updated">QR便 &nbsp;/&nbsp; 最終更新: {UPDATED_JA}</p>

<div class="box warn">
  <strong>転送は失敗することがあります。</strong>
  QR が読めるかどうかは、カメラ・明るさ・距離・画面によって変わります。
  QR便 は受け取った内容を SHA-256 で照合して結果をお見せしますが、
  個々の転送が必ず成功することをお約束することはできません。
  大切なものの唯一の控えとして使わないでください。
</div>

<h2>QR便 とは</h2>
<p>
  データをアニメーション QR として表示し、もう一方の端末のカメラで読み取るアプリです。
  転送にネットワークを使いません。
</p>

<h2>お客様の責任</h2>
<ul>
  <li>転送する内容と、それを転送してよい権利があることについては、お客様の責任となります。</li>
  <li>画面に出た QR は、近くにいる人から見えたり撮影されたりします。周囲にご注意ください。</li>
  <li>会社や学校の PC でお使いの場合は、その組織のルールに従ってください。</li>
</ul>

<h2>購入について</h2>
<p>
  QR便 Pro は Apple を通じた買い切りです。返金は Apple の規約に基づき、Apple へお申し出ください。
</p>

<h2>免責</h2>
<p>
  QR便 は現状のまま提供されます。法令で認められる範囲において、本アプリの利用によって
  生じた損害（転送されなかった、正しく転送されなかった場合を含みます）について、
  当方は責任を負いません。
</p>

<h2>商標</h2>
<p>QRコードは株式会社デンソーウェーブの登録商標です。</p>

<h2>変更</h2>
<p>本規約は変更されることがあります。常にこのページに掲載されているものが最新版です。</p>

<h2>お問い合わせ</h2>
<p>{CONTACT}</p>
"""

JA_TOKUSHOHO = f"""
<h1>特定商取引法に基づく表記</h1>
<p class="updated">アプリ「QR便」 &nbsp;/&nbsp; 最終更新: {UPDATED_JA}</p>

<table>
  <tr><th>販売事業者</th><td>Shoya Kurokawa（個人）</td></tr>
  <tr><th>運営統括責任者</th><td>Shoya Kurokawa</td></tr>
  <tr><th>所在地</th><td>ご請求をいただければ遅滞なく開示いたします。</td></tr>
  <tr><th>電話番号</th><td>ご請求をいただければ遅滞なく開示いたします。</td></tr>
  <tr><th>メールアドレス</th><td>{CONTACT}</td></tr>
  <tr><th>販売価格</th><td>QR便 Pro ¥500（税込）。アプリ本体は無料です。</td></tr>
  <tr><th>商品代金以外の必要料金</th><td>通信料はお客様のご負担となります（転送そのものは通信を行いません）。</td></tr>
  <tr><th>お支払い方法</th><td>Apple の App 内課金（Apple アカウントに登録された決済手段）</td></tr>
  <tr><th>お支払い時期</th><td>購入手続きの完了時</td></tr>
  <tr><th>商品の引渡時期</th><td>購入手続きの完了後、ただちにご利用いただけます。</td></tr>
  <tr><th>返品・キャンセル</th><td>デジタルコンテンツの性質上、購入後のキャンセルはお受けできません。返金は Apple の規約に基づき、Apple へお申し出ください。</td></tr>
  <tr><th>動作環境</th><td>iOS 17 以降の iPhone / iPad と、PC のブラウザ（Chrome / Edge）</td></tr>
</table>
"""

PAGES = [
    ("index.html", "en", "QR便 — Support &amp; Legal", EN_INDEX, None),
    ("privacy-policy.html", "en", "Privacy Policy | QR便", EN_PRIVACY, "./"),
    ("support.html", "en", "Support | QR便", EN_SUPPORT, "./"),
    ("terms.html", "en", "Terms of Use | QR便", EN_TERMS, "./"),
    ("ja/index.html", "ja", "QR便 — サポート・法務", JA_INDEX, None),
    ("ja/privacy-policy.html", "ja", "プライバシーポリシー｜QR便", JA_PRIVACY, "./"),
    ("ja/support.html", "ja", "サポート｜QR便", JA_SUPPORT, "./"),
    ("ja/terms.html", "ja", "利用規約｜QR便", JA_TERMS, "./"),
    ("ja/tokushoho.html", "ja", "特定商取引法に基づく表記｜QR便", JA_TOKUSHOHO, "./"),
]


def main() -> None:
    for name, lang, title, body, home in PAGES:
        path = ROOT / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(page(lang, title, body, home), encoding="utf-8")
        print(f"{name:<28} {len(path.read_bytes()):>6} bytes")


if __name__ == "__main__":
    main()
