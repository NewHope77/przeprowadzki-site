"""Ilustracje SVG do sekcji hero na stronach usług (w stylu strony)."""

NAVY, NAVY2, ORANGE, ORANGE2, YELLOW, SKY, GREEN = "#0E1B2C", "#1E3350", "#FF6A1A", "#FF8A4C", "#FFB400", "#DCEBFA", "#16A36A"

VAN = (f'<path d="M6 20a6 6 0 0 1 6-6h114v58H6z" fill="#fff" stroke="{NAVY}" stroke-width="3"/>'
       f'<path d="M126 30h34l28 26v16h-62z" fill="{ORANGE}" stroke="{NAVY}" stroke-width="3" stroke-linejoin="round"/>'
       f'<path d="M140 37h17l17 16h-34z" fill="{SKY}"/><path d="M6 60h182" stroke="{NAVY}" stroke-width="3"/>'
       f'<rect x="20" y="28" width="40" height="18" rx="3" fill="{ORANGE}"/><rect x="66" y="28" width="46" height="18" rx="3" fill="{YELLOW}"/>'
       f'<circle cx="44" cy="74" r="11" fill="{NAVY}"/><circle cx="44" cy="74" r="4" fill="#fff"/>'
       f'<circle cx="160" cy="74" r="11" fill="{NAVY}"/><circle cx="160" cy="74" r="4" fill="#fff"/>')


def n(v):
    return f"{v:g}"


def box(x, y, w, h):
    return (f'<rect x="{n(x)}" y="{n(y)}" width="{n(w)}" height="{n(h)}" rx="4" fill="#F2B872"/>'
            f'<rect x="{n(x + w / 2 - 6)}" y="{n(y + 2)}" width="12" height="{n(h * .38)}" fill="#E09A4E" stroke="none"/>'
            f'<rect x="{n(x + w * .14)}" y="{n(y + h * .56)}" width="{n(w * .32)}" height="{n(h * .22)}" rx="2" fill="#fff" stroke-width="3"/>')


def plant(x, base, h=40):
    return (f'<path d="M{n(x + 4)} {n(base)}h36l6-{n(h)}H{n(x - 2)}z" fill="{ORANGE}"/>'
            f'<path d="M{n(x + 22)} {n(base - h)}c-4-30 6-50 26-58-2 26-10 44-26 58z" fill="{GREEN}"/>'
            f'<path d="M{n(x + 20)} {n(base - h)}c-12-22-30-30-46-28 8 20 24 30 46 28z" fill="{GREEN}"/>')


def scene(inner, free="", label=""):
    return f'''<svg viewBox="0 0 480 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">
<circle cx="245" cy="200" r="178" fill="#FFE9D9"/>
<circle cx="430" cy="58" r="9" fill="{YELLOW}" class="float"/>
<path d="M52 70l6 14 14 6-14 6-6 14-6-14-14-6 14-6z" fill="{ORANGE}" class="float d2"/>
<ellipse cx="240" cy="354" rx="215" ry="13" fill="{NAVY}" opacity=".08"/>
<g stroke="{NAVY}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">{inner}</g>
{free}
</svg>'''


def piano_keys():
    x0, y, w, count = 106, 211, 268, 20
    kw = w / count
    seps = "".join(f"M{n(x0 + kw * i)} {y}v18" for i in range(1, count))
    black = "".join(f'<rect x="{n(x0 + kw * (i + 1) - 4)}" y="{y}" width="8" height="11" fill="{NAVY}" stroke="none"/>'
                    for i in range(count - 1) if i % 7 in (0, 1, 3, 4, 5))
    return f'<rect x="{x0}" y="{y}" width="{w}" height="18" fill="#fff" stroke="none"/><path d="{seps}" stroke-width="1.5"/>{black}'


ART = {
    "przeprowadzki-prywatne": scene(label="Dom i kartony do przeprowadzki", inner=f'''
<rect x="272" y="96" width="28" height="60" fill="{NAVY}"/>
<rect x="126" y="168" width="196" height="182" fill="#fff"/>
<path d="M104 178L224 84l120 94z" fill="{ORANGE}"/>
<circle cx="224" cy="142" r="14" fill="{YELLOW}"/>
<rect x="146" y="196" width="50" height="46" rx="4" fill="{SKY}"/><path d="M171 196v46M146 219h50" stroke-width="3"/>
<rect x="252" y="196" width="50" height="46" rx="4" fill="{SKY}"/><path d="M277 196v46M252 219h50" stroke-width="3"/>
<rect x="198" y="266" width="52" height="84" rx="4" fill="{NAVY2}"/><circle cx="240" cy="310" r="4" fill="{YELLOW}" stroke="none"/>
{box(334, 284, 86, 66)}{box(348, 228, 62, 56)}{box(424, 306, 44, 44)}
{plant(54, 350)}'''),

    "przeprowadzki-biur": scene(label="Biurko z monitorem i segregatorami", inner=f'''
{plant(92, 240, 30)}
<rect x="150" y="116" width="160" height="106" rx="10" fill="{NAVY}"/>
<rect x="162" y="128" width="136" height="80" rx="4" fill="{SKY}" stroke="none"/>
<rect x="178" y="174" width="16" height="26" fill="{ORANGE}" stroke="none"/><rect x="202" y="160" width="16" height="40" fill="{YELLOW}" stroke="none"/>
<rect x="226" y="146" width="16" height="54" fill="{ORANGE}" stroke="none"/><path d="M254 190l12-12 10 6 14-18" fill="none" stroke="{GREEN}" stroke-width="3"/>
<path d="M230 222v18M208 240h44"/>
<rect x="318" y="176" width="18" height="64" rx="2" fill="{ORANGE}"/><rect x="338" y="188" width="18" height="52" rx="2" fill="{YELLOW}"/><rect x="358" y="168" width="16" height="72" rx="2" fill="{NAVY2}"/>
<rect x="76" y="240" width="310" height="16" rx="4" fill="{NAVY}"/>
<rect x="92" y="256" width="12" height="94" fill="{NAVY2}"/><rect x="360" y="256" width="12" height="94" fill="{NAVY2}"/>
<rect x="268" y="256" width="84" height="80" rx="4" fill="#fff"/><path d="M280 282h60M280 308h60" stroke-width="3"/>
<circle cx="310" cy="270" r="3" fill="{NAVY}" stroke="none"/><circle cx="310" cy="296" r="3" fill="{NAVY}" stroke="none"/><circle cx="310" cy="322" r="3" fill="{NAVY}" stroke="none"/>
{box(398, 282, 70, 68)}{box(408, 232, 52, 50)}'''),

    "przeprowadzki-miedzymiastowe": scene(label="Mapa z trasą i auto dostawcze", inner=f'''
<rect x="56" y="48" width="368" height="252" rx="24" fill="#fff"/>
<path d="M58 136c92-20 162 40 364 10" fill="none" stroke="#EEF1F5" stroke-width="14"/>
<path d="M170 50c10 94-30 164-10 248" fill="none" stroke="#EEF1F5" stroke-width="14"/>
<path d="M310 50c-10 84 40 164 30 248" fill="none" stroke="#EEF1F5" stroke-width="10"/>
<circle cx="385" cy="238" r="28" fill="#E3F3EA" stroke="none"/>
<path d="M122 222c70 4 96-96 208-92" fill="none" stroke="{ORANGE}" stroke-width="6" stroke-dasharray="2 14"/>
<g transform="translate(122 222)"><path d="M0 0c-16-20-24-32-24-44a24 24 0 0 1 48 0c0 12-8 24-24 44z" fill="{NAVY}"/><circle cy="-44" r="9" fill="#fff" stroke="none"/></g>
<g transform="translate(330 130)"><path d="M0 0c-16-20-24-32-24-44a24 24 0 0 1 48 0c0 12-8 24-24 44z" fill="{ORANGE}"/><circle cy="-44" r="9" fill="#fff" stroke="none"/></g>
<rect x="72" y="232" width="100" height="30" rx="15" fill="{NAVY}" stroke="none"/>
<text x="122" y="252" text-anchor="middle" font-size="14" font-weight="700" fill="#fff" stroke="none">Warszawa</text>
<rect x="286" y="142" width="88" height="30" rx="15" fill="{ORANGE}" stroke="none"/>
<text x="330" y="162" text-anchor="middle" font-size="14" font-weight="700" fill="#fff" stroke="none">Gdańsk</text>
<path d="M96 300h40M112 318h30M90 336h44" stroke-width="5"/>''',
                                          free=f'<g transform="translate(150 264)">{VAN}</g>'),

    "taxi-bagazowe": scene(label="Auto dostawcze z kartonami i zegarem", inner=f'''
<circle cx="380" cy="104" r="50" fill="#fff"/>
<circle cx="380" cy="104" r="38" fill="none" stroke="{YELLOW}" stroke-width="7" stroke-dasharray="180 60"/>
<path d="M380 80v24l16 10"/><circle cx="380" cy="104" r="4" fill="{NAVY}"/>
<path d="M14 262h44M30 284h34M10 306h52" stroke-width="5"/>
{box(392, 290, 72, 60)}{box(402, 242, 54, 48)}''',
                           free=f'<g transform="translate(70 218) scale(1.55)">{VAN}</g>'),

    "transport-mebli": scene(label="Sofa zabezpieczona folią i kartony", inner=f'''
<path d="M38 350v-190" stroke-width="5"/><path d="M22 350h32"/>
<path d="M14 158h48l-10-44H24z" fill="{YELLOW}"/>
<rect x="92" y="190" width="256" height="96" rx="20" fill="{ORANGE}"/>
<path d="M220 204v70" stroke="#C9500F"/>
<rect x="88" y="262" width="264" height="60" rx="14" fill="{ORANGE2}"/>
<path d="M220 268v48" stroke="#C9500F"/>
<rect x="62" y="232" width="52" height="98" rx="18" fill="{ORANGE}"/>
<rect x="326" y="232" width="52" height="98" rx="18" fill="{ORANGE}"/>
<rect x="84" y="330" width="14" height="20" rx="3" fill="{NAVY}"/><rect x="342" y="330" width="14" height="20" rx="3" fill="{NAVY}"/>
<rect x="128" y="218" width="62" height="46" rx="14" fill="{YELLOW}" transform="rotate(-8 159 241)"/>
<path d="M236 184h112q36 4 34 50v102H236z" fill="{SKY}" fill-opacity=".55" stroke="#9FC3E8" stroke-width="3"/>
<path d="M250 216l124-18M246 262l136-22M246 308l136-22" stroke="#fff" stroke-width="5" opacity=".85"/>
{box(392, 282, 76, 68)}{box(402, 228, 56, 54)}'''),

    "transport-pianin": scene(label="Pianino na wózku transportowym z pasami", inner=f'''
<rect x="120" y="96" width="240" height="214" rx="10" fill="{NAVY2}"/>
<rect x="108" y="84" width="264" height="22" rx="6" fill="{NAVY}"/>
<rect x="146" y="90" width="18" height="232" fill="{YELLOW}" stroke="none"/>
<rect x="316" y="90" width="18" height="232" fill="{YELLOW}" stroke="none"/>
<rect x="180" y="130" width="120" height="60" rx="4" fill="#fff"/>
<path d="M192 150h96M192 162h96M192 174h96" stroke-width="2"/>
<circle cx="212" cy="172" r="5" fill="{NAVY}" stroke="none"/><circle cx="240" cy="160" r="5" fill="{NAVY}" stroke="none"/><circle cx="268" cy="166" r="5" fill="{NAVY}" stroke="none"/>
<rect x="98" y="206" width="284" height="30" rx="4" fill="{NAVY}"/>
{piano_keys()}
<rect x="140" y="248" width="200" height="50" rx="6" fill="#16283F"/>
<circle cx="222" cy="304" r="5" fill="{YELLOW}" stroke="none"/><circle cx="240" cy="304" r="5" fill="{YELLOW}" stroke="none"/><circle cx="258" cy="304" r="5" fill="{YELLOW}" stroke="none"/>
<rect x="104" y="310" width="272" height="16" rx="6" fill="{ORANGE}"/>
<circle cx="138" cy="338" r="12" fill="{NAVY}"/><circle cx="138" cy="338" r="4" fill="#fff" stroke="none"/>
<circle cx="342" cy="338" r="12" fill="{NAVY}"/><circle cx="342" cy="338" r="4" fill="#fff" stroke="none"/>''',
                              free=f'''<g class="float"><circle cx="410" cy="170" r="11" fill="{ORANGE}"/><path d="M421 170v-54q14 4 22 18" fill="none" stroke="{NAVY}" stroke-width="4" stroke-linecap="round"/></g>
<g class="float d2"><circle cx="64" cy="220" r="9" fill="{YELLOW}"/><path d="M73 220v-42l20 6" fill="none" stroke="{NAVY}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/></g>'''),
}
