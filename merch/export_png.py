"""merch/*.svg を SUZURI 入稿用の透過 PNG に書き出す（Edge のヘッドレス起動を使う）。

usage: python -I merch/export_png.py
前提: merch/ を http://localhost:4178/ で配信していること（.claude/launch.json の merch-preview）
"""

import re
import subprocess
import tempfile
import time
from pathlib import Path

EDGE = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
MERCH = Path(__file__).resolve().parent
OUT = MERCH / 'suzuri'
BASE = 'http://localhost:4178'

# (ファイル名, 書き出し幅 px)。SUZURI スタンダードTシャツの推奨は 2520×2992。
# 配置・拡縮は SUZURI のエディタで行う。
TARGETS = [
    ('rinri-com_black', 3000),  # Tシャツ表面（淡色）・ステッカー
    ('rinri-com_white', 3000),  # Tシャツ表面（濃色）
    ('junshu_black', 2520),  # Tシャツ裏面（淡色）・ステッカー
    ('junshu_white', 2520),  # Tシャツ裏面（濃色）
]


def viewbox(svg_path):
    m = re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg_path.read_text(encoding='utf-8'))
    return float(m.group(1)), float(m.group(2))


def main():
    OUT.mkdir(exist_ok=True)
    page = MERCH / '_render.html'
    page.write_text(
        '<!doctype html><meta charset="utf-8"><style>html,body{margin:0;background:transparent}'
        'img{display:block;width:100vw;height:100vh}</style>'
        '<img id="i"><script>i.src=location.hash.slice(1)</script>',
        encoding='utf-8',
    )
    try:
        for name, w in TARGETS:
            vw, vh = viewbox(MERCH / f'{name}.svg')
            h = round(w * vh / vw)
            dst = OUT / f'{name}.png'
            dst.unlink(missing_ok=True)
            for _ in range(4):
                with tempfile.TemporaryDirectory() as prof:
                    subprocess.run(
                        [
                            EDGE,
                            '--headless=new',
                            '--disable-gpu',
                            '--hide-scrollbars',
                            '--force-device-scale-factor=1',
                            '--default-background-color=00000000',
                            '--virtual-time-budget=3000',
                            f'--user-data-dir={prof}',
                            f'--window-size={w},{h}',
                            f'--screenshot={dst}',
                            f'{BASE}/_render.html?{time.time_ns()}#{name}.svg',
                        ],
                        capture_output=True,
                        timeout=60,
                    )
                if dst.exists():
                    break
            print(('ok  ' if dst.exists() else 'FAIL'), dst.name, f'{w}x{h}')
    finally:
        page.unlink(missing_ok=True)


main()
