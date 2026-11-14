"""技術者倫理.com グッズ用 SVG を生成する（文字はすべてアウトライン化）。

usage: python -I merch/generate.py merch
Noto Sans JP: Windows 同梱の NotoSansJP-VF.ttf (OFL)
"""

import sys
from pathlib import Path

from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.ttLib import TTFont

NOTO = 'C:/Windows/Fonts/NotoSansJP-VF.ttf'
OUT = Path(sys.argv[1])
OUT.mkdir(parents=True, exist_ok=True)

INK = {'black': '#0a0a0a', 'white': '#ffffff'}
COM_RATIO = float(__import__('os').environ.get('COM_RATIO', '0.5'))
COM_WGHT = int(__import__('os').environ.get('COM_WGHT', '700'))

_noto = TTFont(NOTO)
_gs_cache = {}


def glyphset(font, wght):
    key = (id(font), wght)
    if key not in _gs_cache:
        _gs_cache[key] = (
            font.getGlyphSet(location={'wght': wght}) if wght else font.getGlyphSet()
        )
    return _gs_cache[key]


class Text:
    """1 行のテキストをグリフ単位で配置する。"""

    def __init__(self, font, text, size, wght=None, tracking=0.0, kern=None, optical=None):
        """optical: 指定すると送り幅を無視し、字面（インク）同士の間隔をこの値(em)で揃える。"""
        self.font, self.size = font, size
        gs = self.gs = glyphset(font, wght)
        cmap = font.getBestCmap()
        upm = font['head'].unitsPerEm
        self.scale = size / upm
        self.glyphs = []  # (glyph, x_offset)
        x = 0.0
        if optical is not None:
            for ch in text:
                g = gs[cmap[ord(ch)]]
                bp = BoundsPen(gs)
                g.draw(bp)
                xmin, _, xmax, _ = bp.bounds
                # 字面の左端を x に合わせる
                self.glyphs.append((g, x - xmin * self.scale))
                x += (xmax - xmin) * self.scale + optical * size
            self.width = x - optical * size
            return
        for i, ch in enumerate(text):
            g = gs[cmap[ord(ch)]]
            self.glyphs.append((g, x))
            x += g.width * self.scale + tracking * size
            if kern:
                x += kern.get(i, 0) * size
        self.width = x - tracking * size

    def draw(self, pen, x, y):
        for g, gx in self.glyphs:
            g.draw(TransformPen(pen, (self.scale, 0, 0, -self.scale, x + gx, y)))

    def path(self, x, y):
        pen = SVGPathPen(self.gs, ntos=lambda v: f'{v:.2f}'.rstrip('0').rstrip('.'))
        self.draw(pen, x, y)
        return pen.getCommands()

    def bounds(self):
        pen = BoundsPen(self.gs)
        self.draw(pen, 0, 0)
        return pen.bounds  # (xMin, yMin, xMax, yMax) in SVG coords (y down)


def svg(w, h, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:.0f} {h:.0f}" '
        f'width="{w:.0f}" height="{h:.0f}">\n<title>{title}</title>\n{body}\n</svg>\n'
    )


def write(name, content):
    (OUT / name).write_text(content, encoding='utf-8')
    print('wrote', name)


# ---------------------------------------------------------------- 1. 技術者倫理.com
def wordmark(color):
    ink = INK[color]
    pad = 40
    # 和文は字面基準で詰め、.com は小さく軽くして主従をつける
    jp = Text(_noto, '技術者倫理', 200, wght=900, optical=0.045)
    com = Text(_noto, '.com', 200 * COM_RATIO, wght=COM_WGHT, optical=0.03)
    gap = 200 * 0.05
    total = jp.width + gap + com.width
    parts = []
    jb = jp.bounds()
    baseline = pad - jb[1]
    x0 = pad
    parts.append(f'<path fill="{ink}" d="{jp.path(x0, baseline)}"/>')
    # .com のベースラインを和文の字面の下端に揃える
    parts.append(f'<path fill="{ink}" d="{com.path(x0 + jp.width + gap, baseline + jb[3])}"/>')
    h = baseline + jb[3] + pad
    w = total + pad * 2
    write(f'rinri-com_{color}.svg', svg(w, h, '\n'.join(parts), '技術者倫理.com'))


# ---------------------------------------------------------------- 2. 技術者倫理 / 遵守（Tシャツ裏面）
def _jp(text, size, wght=900, gap=0.045):
    return Text(_noto, text, size, wght=wght, optical=gap)


def junshu_stack(color):
    """上に技術者倫理、罫線を挟んで下に大きく遵守。2 段の幅を揃える。"""
    ink = INK[color]
    pad = 40
    top = _jp('技術者倫理', 100, gap=0.12)
    W = top.width
    # 「遵守」を上段と同じ幅に合わせる
    probe = _jp('遵守', 100, gap=0.08)
    big = _jp('遵守', 100 * W / probe.width, gap=0.08)
    tb, bb = top.bounds(), big.bounds()
    rule = 8
    g1 = 34
    y_top = pad - tb[1]
    y_rule = pad + (tb[3] - tb[1]) + g1
    y_big = y_rule + rule + g1 - bb[1]
    H = y_big + bb[3] + pad
    parts = [
        f'<path fill="{ink}" d="{top.path(pad, y_top)}"/>',
        f'<rect x="{pad}" y="{y_rule:.2f}" width="{W:.2f}" height="{rule}" fill="{ink}"/>',
        f'<path fill="{ink}" d="{big.path(pad, y_big)}"/>',
    ]
    write(f'junshu_{color}.svg', svg(W + pad * 2, H, '\n'.join(parts), '技術者倫理 遵守'))


for col in INK:
    wordmark(col)
    junshu_stack(col)
