#!/usr/bin/env python3
"""Generator statycznych stron. Uruchom z katalogu site/: python3 src/build.py"""
import html
import json
from datetime import date
from pathlib import Path

from content import SITE, SERVICES, HOURLY, BOX_NOTES, HOME_FAQ, CASES, REVIEWS, ARTICLES
from illustrations import ART

ROOT = Path(__file__).resolve().parent.parent
esc = html.escape
BUILT = []

ICONS = {
    "home": '<path d="M3 10l9-7 9 7v10a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
    "office": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1"/>',
    "route": '<circle cx="6" cy="18" r="2"/><circle cx="18" cy="6" r="2"/><path d="M8 18h7a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h7"/>',
    "sofa": '<path d="M4 11V8a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3"/><path d="M2 13a2 2 0 0 1 4 0v2h12v-2a2 2 0 0 1 4 0v5H2z"/><path d="M5 18v2M19 18v2"/>',
    "piano": '<rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 13h18M8 13v7M12 13v7M16 13v7"/>',
    "box": '<path d="M21 8l-9-5-9 5 9 5 9-5z"/><path d="M3 8v8l9 5 9-5V8M12 13v8"/>',
    "truck": '<path d="M3 7h11v9H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M22 6l-10 7L2 6"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "pin": '<path d="M12 22s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12z"/><circle cx="12" cy="10" r="2.5"/>',
    "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
    "chev": '<path d="M6 9l6 6 6-6"/>',
    "list": '<path d="M9 6h11M9 12h11M9 18h11"/><path d="M4 6l1 1 2-2M4 12l1 1 2-2M4 18l1 1 2-2"/>',
    "fridge": '<rect x="5" y="2" width="14" height="20" rx="2"/><path d="M5 9h14M9 5v2M9 12v3"/>',
    "washer": '<rect x="4" y="2" width="16" height="20" rx="2"/><circle cx="12" cy="13" r="5"/><path d="M8 6h.01M11 6h.01"/>',
    "tv": '<rect x="2" y="5" width="20" height="13" rx="2"/><path d="M8 21h8M12 18v3"/>',
    "star": '<path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
}
WA = '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.3c0-.1-.2-.2-.5-.3z"/></svg>'
VAN = '<svg viewBox="0 0 200 92" fill="none" aria-hidden="true"><path d="M6 20a6 6 0 0 1 6-6h114v58H6z" fill="#fff" stroke="currentColor" stroke-width="3"/><path d="M126 30h34l28 26v16h-62z" fill="#FF6A1A" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/><path d="M140 37h17l17 16h-34z" fill="#DCEBFA"/><path d="M6 60h182" stroke="currentColor" stroke-width="3"/><circle cx="44" cy="74" r="11" fill="#0E1B2C"/><circle cx="44" cy="74" r="4" fill="#fff"/><circle cx="160" cy="74" r="11" fill="#0E1B2C"/><circle cx="160" cy="74" r="4" fill="#fff"/></svg>'


def svg(name):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>'


TEL = "tel:" + SITE.phone.replace(" ", "")
WA_LINK = "https://wa.me/" + SITE.whatsapp


def rel(path):
    return "../" * path.count("/")


# ---------- layout ----------

def head(R, path, title, desc, schema=None):
    full = title if SITE.brand in title else f"{title} | {SITE.brand}"
    ld = f'<script type="application/ld+json">{json.dumps(schema, ensure_ascii=False)}</script>' if schema else ""
    return f'''<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{SITE.url}{path}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pl_PL">
<meta name="theme-color" content="#0E1B2C">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='32' height='32' rx='8' fill='%23FF6A1A'/%3E%3Cpath d='M6 11h12v9H6zM18 14h4l4 4v2h-8' fill='none' stroke='white' stroke-width='2.2' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Unbounded:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{R}assets/style.css">
{ld}
</head>
<body>'''


def logo(R):
    return f'<a href="{R}" class="logo"><span class="logo-mark">{svg("truck")}</span><span>{SITE.brand}</span></a>'


def header(R, active):
    dd = "".join(
        f'<a class="dd-link" href="{R}{s.slug}/"><span class="svc-ic sm">{svg(s.icon)}</span><span><b>{s.name}</b><small>{s.tagline}</small></span></a>'
        for s in SERVICES)
    links = [("cennik/", "Cennik", "cennik"), ("realizacje/", "Realizacje", "realizacje"), ("porady/", "Porady", "porady"),
             ("opinie/", "Opinie", "opinie"), ("kontakt/", "Kontakt", "kontakt")]
    nav = "".join(f'<a href="{R}{h}"{" class=\"on\"" if active == k else ""}>{t}</a>' for h, t, k in links)
    mob_svc = "".join(f'<a href="{R}{s.slug}/">{s.name}</a>' for s in SERVICES)
    mob = "".join(f'<a href="{R}{h}">{t}</a>' for h, t, _ in links)
    svc_on = " on" if active == "uslugi" else ""
    return f'''
<a class="skip" href="#main">Przejdź do treści</a>
<header id="top">
  <div class="wrap nav">
    {logo(R)}
    <nav class="menu" aria-label="Menu główne">
      <div class="dd">
        <button class="dd-btn{svc_on}" type="button" aria-expanded="false">Usługi {svg("chev")}</button>
        <div class="dd-panel">{dd}</div>
      </div>
      {nav}
    </nav>
    <div class="nav-right">
      <a class="phone" href="{TEL}"><span>{SITE.phone}</span><small>{SITE.hours}</small></a>
      <a href="{R}wycena/" class="btn btn-accent">Wycena online</a>
      <button class="burger" type="button" aria-label="Otwórz menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </div>
</header>
<div class="mobile-menu">
  <div class="mm-label">Usługi</div>{mob_svc}
  <div class="mm-label">Informacje</div>{mob}
  <a href="{R}wycena/" class="btn btn-accent">Wycena online</a>
  <a href="{TEL}" class="btn btn-ghost">Zadzwoń: {SITE.phone}</a>
</div>
<main id="main">'''


def footer(R):
    svc = "".join(f'<li><a href="{R}{s.slug}/">{s.name}</a></li>' for s in SERVICES)
    site_js = json.dumps(dict(brand=SITE.brand, phone=SITE.phone, whatsapp=SITE.whatsapp, formEndpoint=SITE.form_endpoint), ensure_ascii=False)
    return f'''
</main>
<footer>
  <div class="wrap">
    <div class="foot">
      <div>
        {logo(R)}
        <p class="foot-desc">Przeprowadzki i transport w Warszawie i całej Polsce. Stała cena, ubezpieczenie OCP do 200 000 zł, płatność po realizacji.</p>
      </div>
      <div><h4>Usługi</h4><ul>{svc}</ul></div>
      <div><h4>Informacje</h4><ul>
        <li><a href="{R}cennik/">Cennik</a></li><li><a href="{R}realizacje/">Realizacje</a></li>
        <li><a href="{R}porady/">Porady</a></li><li><a href="{R}opinie/">Opinie</a></li><li><a href="{R}wycena/">Wycena online</a></li>
      </ul></div>
      <div><h4>Kontakt</h4><ul>
        <li><a href="{TEL}">{SITE.phone}</a></li><li><a href="mailto:{SITE.email}">{SITE.email}</a></li>
        <li>{SITE.hours}</li><li>{SITE.address}</li>
      </ul></div>
    </div>
    <div class="copy"><span>© {date.today().year} {SITE.brand}. Wszelkie prawa zastrzeżone.</span><a href="{R}polityka-prywatnosci/">Polityka prywatności</a></div>
  </div>
</footer>
<div class="fab">
  <a class="wa" href="{WA_LINK}" data-wa="Dzień dobry, chcę wycenić przeprowadzkę." target="_blank" rel="noopener" aria-label="WhatsApp">{WA}</a>
  <a class="tel" href="{TEL}" aria-label="Zadzwoń">{svg("phone")}</a>
</div>
<script>window.SITE={site_js}</script>
<script src="{R}assets/app.js" defer></script>
</body>
</html>'''


def page(path, title, desc, body, active="", schema=None, R=None):
    R = rel(path) if R is None else R
    out = head(R, path, title, desc, schema) + header(R, active) + body(R) + footer(R)
    target = ROOT / path / "index.html" if not path.endswith(".html") else ROOT / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(out, encoding="utf-8")
    if not path.endswith(".html"):
        BUILT.append(path)


# ---------- components ----------

def crumbs(R, items):
    parts = [f'<a href="{R}">Strona główna</a>'] + [f'<a href="{R}{h}">{t}</a>' if h else f'<span aria-current="page">{t}</span>' for t, h in items]
    return '<nav class="crumbs" aria-label="Okruszki">' + '<span>/</span>'.join(parts) + '</nav>'


def badges(items):
    return '<div class="badges">' + "".join(f'<span class="badge"><i>✓</i>{b}</span>' for b in items) + '</div>'


def service_options(selected=""):
    return "".join(f'<option{" selected" if s.form == selected else ""}>{s.form}</option>' for s in SERVICES)


def quick_form(title="Darmowa wycena", selected="", note="Oddzwonimy w ciągu kilku minut."):
    return f'''
<form class="quick js-quick">
  <h3>{title}</h3>
  <p>{note}</p>
  <div class="field"><label>Imię<input name="name" placeholder="Jan" autocomplete="given-name"></label></div>
  <div class="field"><label>Telefon *<input name="phone" type="tel" placeholder="+48 ___ ___ ___" required autocomplete="tel"></label></div>
  <div class="field"><label>Czego potrzebujesz?<select name="service">{service_options(selected)}</select></label></div>
  <button class="btn btn-accent" type="submit">Oddzwońcie do mnie</button>
  <div class="note">Bez zobowiązań · Wycena bezpłatna</div>
</form>'''


def quick_band(selected=""):
    return f'''
<form class="qband js-quick">
  <div class="qb-text"><h3>Darmowa wycena</h3><p>Oddzwonimy w ciągu kilku minut.</p></div>
  <label class="qb-f"><span>Imię</span><input name="name" placeholder="Jan" autocomplete="given-name"></label>
  <label class="qb-f"><span>Telefon *</span><input name="phone" type="tel" placeholder="+48 ___ ___ ___" required autocomplete="tel"></label>
  <label class="qb-f"><span>Usługa</span><select name="service">{service_options(selected)}</select></label>
  <button class="btn btn-accent" type="submit">Oddzwońcie do mnie</button>
</form>'''


def hero(R, h1, lead, badge_list, cta_primary, cta_secondary, form, crumb_html="", sub=False, below=""):
    cls = ("hero sub" if sub else "hero") + (" has-art" if below else "")
    return f'''
<section class="{cls}">
  <div class="hero-blob"></div>
  <div class="wrap hero-grid">
    <div>
      {crumb_html}
      <span class="eyebrow">{SITE.city} i okolice</span>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      {badges(badge_list)}
      <div class="hero-cta">
        <a href="{cta_primary[1]}" class="btn btn-accent">{cta_primary[0]} {svg("arrow")}</a>
        <a href="{cta_secondary[1]}" class="btn btn-ghost">{cta_secondary[0]}</a>
      </div>
      <p class="trust">{svg("clock")} Płatność dopiero po realizacji — bez zaliczek</p>
    </div>
    {form}
  </div>
  <div class="wrap">{below}</div>
</section>'''


def phead(R, title, lead, crumb_items, eyebrow="", extra=""):
    eb = f'<span class="eyebrow">{eyebrow}</span>' if eyebrow else ""
    return f'''
<section class="phead">
  <div class="hero-blob"></div>
  <div class="wrap">
    {crumbs(R, crumb_items)}
    {eb}
    <h1>{title}</h1>
    <p class="lead">{lead}</p>
    {extra}
  </div>
</section>'''


def sec_head(eyebrow, h2, lead=""):
    lp = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<div class="sec-head"><div><span class="eyebrow">{eyebrow}</span><h2>{h2}</h2></div>{lp}</div>'


def services_grid(R, items=None):
    items = items or SERVICES
    return '<div class="services">' + "".join(f'''
<a class="svc" href="{R}{s.slug}/"><span class="svc-ic">{svg(s.icon)}</span>
  <h3>{s.name}</h3><p>{s.short}</p><span class="more">Szczegóły i cennik →</span></a>''' for s in items) + '</div>'


def plans_html(R, plans, service_form, anchor=False):
    cards = []
    for p in plans:
        feats = "".join(f'<li{"" if ok else " class=\"no\""}>{t}</li>' for t, ok in p.feats)
        tag = '<span class="tag">Najczęściej wybierany</span>' if p.hot else ""
        pre = f'<span class="from">{p.prefix}</span>' if p.prefix else ""
        num_cls = "" if any(c.isdigit() for c in p.price) else ' class="txt"'
        btn = "btn-accent" if p.hot else "btn-ghost"
        href = f"#zamow" if anchor else f"{R}wycena/?usluga={service_form}&pakiet={p.pakiet}"
        cards.append(f'''
<div class="plan{" hot" if p.hot else ""}">
  {tag}<h3>{p.name}</h3><div class="sub">{p.sub}</div>
  <div class="price">{pre}<b{num_cls}>{p.price}</b><span>{p.unit}</span></div>
  <div class="team">{p.team}</div>
  <ul>{feats}</ul>
  <a href="{href.replace(" ", "%20")}" class="btn {btn}" data-plan="{p.pakiet}">Wybieram</a>
</div>''')
    return f'<div class="plans n{len(plans)}">' + "".join(cards) + '</div>'


def notes_box(notes, title="Dodatkowe informacje"):
    return f'<div class="box"><h3>{title}</h3><ul>' + "".join(f"<li>{n}</li>" for n in notes) + '</ul></div>'


def calculator():
    opts = "".join(f'<option value="{p.price}"{" selected" if p.hot else ""}>{p.name} — {p.price} zł/h</option>' for p in HOURLY)
    return f'''
<div class="box calc">
  <h3>Szybki kalkulator</h3>
  <div class="field"><label for="c-plan">Pakiet</label><select id="c-plan">{opts}</select></div>
  <div class="field"><label for="c-h">Czas pracy: <span class="range-val" id="c-hv">3 godz.</span></label><input id="c-h" type="range" min="1" max="10" value="3"></div>
  <div class="field"><label for="c-box">Kartony do kupienia: <span class="range-val" id="c-bv">0 szt.</span></label><input id="c-box" type="range" min="0" max="60" step="5" value="0"></div>
  <div class="out"><div><small>Szacunkowy koszt (netto)</small>Orientacyjnie</div><b id="c-out">717 zł</b></div>
</div>'''


def guarantees():
    g = [("Stała cena", "Kwota ustalona na podstawie listy rzeczy jest ostateczna. Zero dopłat na miejscu."),
         ("Płatność po realizacji", "Nie pobieramy zaliczek. Rozliczasz się, gdy wszystko stoi na miejscu."),
         ("OCP do 200 000 zł", "Twoje meble i sprzęt są ubezpieczone przez cały czas zlecenia."),
         ("Od A do Z", "Kartony, folia, narzędzia, montaż — nie musisz niczego organizować.")]
    return '<div class="guar">' + "".join(f'<div class="g"><span class="num">0{i}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(g, 1)) + '</div>'


def steps_section(with_process=True):
    process = '''
<div class="process">
  <div class="pr"><h3>Demontaż i zabezpieczenie</h3><p>Rozkręcamy meble i owijamy folią ochronną — bez rys i zabrudzeń.</p></div>
  <div class="pr"><h3>Sprzęt RTV i AGD</h3><p>Brak fabrycznych pudełek? Pakujemy w folię bąbelkową i koce transportowe.</p></div>
  <div class="pr"><h3>Delikatne przedmioty</h3><p>Szkło i porcelanę zawijamy w papier i pakujemy do kartonów.</p></div>
  <div class="pr"><h3>Ubrania</h3><p>Specjalne kartony na odzież — ubrania dojadą bez zagnieceń.</p></div>
  <div class="pr"><h3>Transport</h3><p>Pasy, wózki platformowe i auta dopasowane do ilości rzeczy.</p></div>
  <div class="pr"><h3>Rozmieszczenie</h3><p>Wnosimy, składamy i ustawiamy meble tam, gdzie chcesz.</p></div>
</div>''' if with_process else ""
    return f'''
<section class="dark">
  <div class="wrap">
    {sec_head("Jak działamy", "4 kroki do spokojnej przeprowadzki", "Wystarczy formularz online albo zdjęcia na WhatsApp — resztą zajmiemy się my.")}
    <div class="steps">
      <div class="step"><h3>Zamówienie</h3><p>Wypełnij formularz online, zadzwoń lub wyślij zdjęcia na WhatsApp.</p></div>
      <div class="step"><h3>Stała wycena</h3><p>Oddzwaniamy, ustalamy szczegóły i podajemy ostateczną cenę.</p></div>
      <div class="step"><h3>Realizacja</h3><p>Przyjeżdżamy punktualnie z planem, sprzętem i materiałami.</p></div>
      <div class="step"><h3>Gotowe</h3><p>Rzeczy bezpiecznie na miejscu. Płacisz dopiero teraz.</p></div>
    </div>
    {process}
  </div>
</section>'''


def fleet():
    vans = [("s", "Małe auto", "Do 1-pokojowego mieszkania", "Idealne do kilku mebli, zakupów z IKEA i niewielkich przeprowadzek."),
            ("m", "Średnie auto", "Mieszkania 2–3 pokojowe", "Zmieści wysokie szafy, lodówki i wyposażenie średniego mieszkania."),
            ("l", "Duże auto", "Mieszkania 3–4 pokojowe i domy", "Do dużych przeprowadzek domów, biur i sklepów — często w jednym kursie.")]
    cards = "".join(f'<div class="van"><div class="van-art {k}">{VAN}</div><h3>{t}</h3><div class="cap">{c}</div><p>{d}</p></div>' for k, t, c, d in vans)
    return f'<section class="alt"><div class="wrap">{sec_head("Nasza flota", "Auto dopasowane do ilości rzeczy", "Nie przepłacasz za zbyt duży samochód ani nie robisz kilku kursów zbyt małym.")}<div class="fleet">{cards}</div></div></section>'


def faq_section(items, alt=True, lead="Nie ma tu Twojego pytania? Zadzwoń — odpowiemy od ręki."):
    det = "".join(f'<details{" open" if i == 0 else ""}><summary>{q}</summary><p>{a}</p></details>' for i, (q, a) in enumerate(items))
    return f'''
<section class="{"alt" if alt else ""}" id="faq">
  <div class="wrap faq-grid">
    <div><span class="eyebrow">FAQ</span><h2>Najczęstsze pytania</h2><p class="lead">{lead}</p></div>
    <div>{det}</div>
  </div>
</section>'''


def cta_band(R, title="Przeprowadzka za kilka dni? Zarezerwuj termin teraz."):
    return f'''
<div class="wrap band-wrap">
  <div class="band">
    <h2>{title}</h2>
    <div class="band-btns"><a href="{R}wycena/" class="btn btn-dark">Wycena online</a><a href="{TEL}" class="btn btn-ghost">Zadzwoń</a></div>
  </div>
</div>'''


def case_cards(R, items):
    out = []
    for c in items:
        lis = "".join(f"<li>{i}</li>" for i in c["items"])
        out.append(f'''
<article class="case">
  <div class="case-top"><span class="pill">{c.pill}</span><span class="case-plan">{c.plan}</span></div>
  <h3>{c.title}</h3><div class="route">{svg("pin")} {c.route}</div>
  <ul class="checklist">{lis}</ul>
  <div class="meta"><span>👷 {c.team}</span><span>⏱ {c.time}</span></div>
</article>''')
    return '<div class="cases">' + "".join(out) + '</div>'


def post_cards(R, items):
    return '<div class="posts">' + "".join(f'''
<a class="post" href="{R}porady/{a.slug}/">
  <div class="post-cover">{svg(a.icon)}</div>
  <div class="post-body"><div class="post-meta">{a.cat} · {a.read} czytania</div><h3>{a.title}</h3><p>{a.excerpt}</p><span class="more">Czytaj →</span></div>
</a>''' for a in items) + '</div>'


def contact_list(R):
    return f'''
<div class="contact-list">
  <a class="cl" href="{TEL}"><span class="ic accent">{svg("phone")}</span><div><small>Zadzwoń · {SITE.hours}</small>{SITE.phone}</div></a>
  <a class="cl" href="{WA_LINK}" data-wa="Dzień dobry, chcę wycenić przeprowadzkę." target="_blank" rel="noopener"><span class="ic wa-bg">{WA}</span><div><small>Wyślij zdjęcia na WhatsApp</small>Wycena ze zdjęć</div></a>
  <a class="cl" href="mailto:{SITE.email}"><span class="ic ink">{svg("mail")}</span><div><small>E-mail</small>{SITE.email}</div></a>
</div>'''


def order_form():
    svc = "".join(f'<label class="choice"><input type="radio" name="usluga" value="{s.form}"{" checked" if i == 0 else ""}><span>{s.name}</span></label>' for i, s in enumerate(SERVICES))
    pk = [("Ekonomiczny", "189 zł/h · 1 osoba"), ("Standardowy", "219 zł/h · 2 osoby"), ("Kompleksowy", "239 zł/h · 2 osoby"), ("Nie wiem — doradźcie", "Dobierzemy pakiet")]
    pkh = "".join(f'<label class="choice"><input type="radio" name="pakiet" value="{v}"{" checked" if v == "Kompleksowy" else ""}><span>{v}<small>{d}</small></span></label>' for v, d in pk)
    return f'''
<form class="form-card" id="orderForm" novalidate>
  <div class="stepper"><div class="on"></div><div></div><div></div></div>
  <div class="fstep on">
    <h3>1. Co przewozimy?</h3><p class="hint">Wybierz usługę i pakiet.</p>
    <div class="choices">{svc}</div>
    <div class="choices c2">{pkh}</div>
    <div class="flabel">Dodatkowo potrzebuję</div>
    <div class="checks">
      <label class="check"><input type="checkbox" name="extra" value="Pakowanie rzeczy">Pakowanie rzeczy</label>
      <label class="check"><input type="checkbox" name="extra" value="Demontaż / montaż mebli">Demontaż / montaż</label>
      <label class="check"><input type="checkbox" name="extra" value="Kartony">Kartony</label>
      <label class="check"><input type="checkbox" name="extra" value="Faktura VAT">Faktura VAT</label>
    </div>
  </div>
  <div class="fstep">
    <h3>2. Skąd, dokąd i kiedy?</h3><p class="hint">Piętro i winda pomagają nam dokładnie wycenić.</p>
    <div class="field"><label for="o-from">Adres załadunku *</label><input id="o-from" name="skad" placeholder="ul. Marszałkowska 1, Warszawa" required></div>
    <div class="row2">
      <div class="field"><label for="o-ff">Piętro</label><input id="o-ff" name="pietro_skad" type="number" min="0" max="40" placeholder="0"></div>
      <div class="field"><label for="o-fl">Winda</label><select id="o-fl" name="winda_skad"><option>Jest winda</option><option>Brak windy</option><option>Dom / parter</option></select></div>
    </div>
    <div class="field"><label for="o-to">Adres rozładunku *</label><input id="o-to" name="dokad" placeholder="ul. Puławska 10, Piaseczno" required></div>
    <div class="row2">
      <div class="field"><label for="o-tf">Piętro</label><input id="o-tf" name="pietro_dokad" type="number" min="0" max="40" placeholder="0"></div>
      <div class="field"><label for="o-tl">Winda</label><select id="o-tl" name="winda_dokad"><option>Jest winda</option><option>Brak windy</option><option>Dom / parter</option></select></div>
    </div>
    <div class="row2">
      <div class="field"><label for="o-date">Data *</label><input id="o-date" name="data" type="date" required></div>
      <div class="field"><label for="o-time">Godzina</label><select id="o-time" name="godzina"><option>Rano (8–11)</option><option>Południe (11–14)</option><option>Popołudnie (14–19)</option><option>Elastycznie</option></select></div>
    </div>
  </div>
  <div class="fstep">
    <h3>3. Dane kontaktowe</h3><p class="hint">Oddzwonimy, aby potwierdzić termin i stałą cenę.</p>
    <div class="row2">
      <div class="field"><label for="o-name">Imię *</label><input id="o-name" name="imie" required autocomplete="name"></div>
      <div class="field"><label for="o-phone">Telefon *</label><input id="o-phone" name="telefon" type="tel" required autocomplete="tel" placeholder="+48"></div>
    </div>
    <div class="field"><label for="o-mail">E-mail</label><input id="o-mail" name="email" type="email" autocomplete="email"></div>
    <div class="field"><label for="o-note">Co przewozimy? (lista rzeczy, uwagi)</label><textarea id="o-note" name="uwagi" placeholder="np. sofa narożna, szafa 2 m, łóżko 160, pralka, ok. 20 kartonów"></textarea></div>
    <label class="check plain"><input type="checkbox" id="o-rodo" required>Zgadzam się na kontakt w sprawie wyceny i przetwarzanie danych w tym celu.</label>
  </div>
  <div class="fstep">
    <div class="success">
      <div class="big"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5L20 7"/></svg></div>
      <h3>Dziękujemy! Zamówienie przyjęte</h3>
      <p class="hint">Oddzwonimy wkrótce, aby potwierdzić termin i cenę.</p>
      <div class="summary" id="summary"></div>
      <a class="btn btn-accent" id="sendWa" target="_blank" rel="noopener" href="#">Wyślij też na WhatsApp</a>
    </div>
  </div>
  <div class="err" id="err" role="alert"></div>
  <div class="fnav" id="fnav">
    <button type="button" class="btn btn-ghost" id="prev" hidden>← Wstecz</button>
    <button type="button" class="btn btn-accent" id="next">Dalej →</button>
  </div>
</form>'''


def order_section(R, title="Zamów w 2 minuty"):
    return f'''
<section id="zamow">
  <div class="wrap order-grid">
    <div class="order-aside">
      <span class="eyebrow">Zamówienie online</span>
      <h2>{title}</h2>
      <p class="lead">Wypełnij krótki formularz — potwierdzimy termin i podamy stałą cenę. Wolisz porozmawiać? Jesteśmy pod telefonem.</p>
      {contact_list(R)}
    </div>
    {order_form()}
  </div>
</section>'''


def split_block(b, alt):
    items = "".join(f"<li>{i}</li>" for i in b["items"])
    paras = "".join(f"<p>{p}</p>" for p in b.paras)
    rev = " rev" if b.reverse else ""
    return f'''
<section class="{"alt" if alt else ""}">
  <div class="wrap split{rev}">
    <div><span class="eyebrow">{b.eyebrow}</span><h2>{b.h2}</h2>{paras}</div>
    <div class="panel"><ul class="checklist">{items}</ul></div>
  </div>
</section>'''


def chips_block(b, alt):
    chips = "".join(f"<span>{i}</span>" for i in b["items"])
    return f'<section class="{"alt" if alt else ""}"><div class="wrap">{sec_head(b.eyebrow, b.h2)}<div class="chips">{chips}</div></div></section>'


# ---------- pages ----------

BUSINESS = {
    "@context": "https://schema.org", "@type": "MovingCompany", "name": SITE.brand, "telephone": SITE.phone, "email": SITE.email,
    "url": SITE.url, "areaServed": "Warszawa i okolice", "priceRange": "189–239 zł/h",
    "address": {"@type": "PostalAddress", "addressLocality": SITE.city, "addressCountry": "PL"},
    "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"], "opens": "08:00", "closes": "19:00"}],
}


def home(R):
    return (hero(R, "Przeprowadzka <em>bez stresu</em> i bez ukrytych kosztów",
                 "Pakujemy, demontujemy, przewozimy i ustawiamy. Cenę ustalamy przed startem — i ona się nie zmienia. Zamów online w 2 minuty.",
                 ["Stała cena", "OCP do 200 000 zł", "Płatność po realizacji", "Kompleksowo od A do Z"],
                 ("Zamów przeprowadzkę", "#zamow"), ("Zobacz cennik", f"{R}cennik/"), quick_form())
            + '''
<div class="stats"><div class="wrap stats-grid">
  <div class="stat"><b>200 000 zł</b><span>ubezpieczenia OCP</span></div>
  <div class="stat"><b>0 zł</b><span>zaliczki — płacisz po realizacji</span></div>
  <div class="stat"><b>2 min</b><span>na wycenę przez telefon</span></div>
  <div class="stat"><b>6 dni</b><span>w tygodniu, 8:00–19:00</span></div>
</div></div>'''
            + f'<section id="uslugi"><div class="wrap">{sec_head("Czym się zajmujemy", "Wszystko, czego potrzebujesz przy przeprowadzce", "Od jednej sofy po całe biuro. Własne auta, sprzęt i materiały do zabezpieczenia.")}{services_grid(R)}</div></section>'
            + f'''
<section class="alt" id="cennik">
  <div class="wrap">
    {sec_head("Cennik", "Przejrzyste stawki. Płacisz tyle, ile ustalimy.", "Rozliczenie godzinowe — idealne do mniejszych zleceń. Przy większych przeprowadzkach podajemy stałą cenę za całość.")}
    {plans_html(R, HOURLY, "Przeprowadzka mieszkania", anchor=True)}
    <div class="price-extra">{notes_box(BOX_NOTES)}{calculator()}</div>
    <p class="center-link"><a href="{R}cennik/" class="more">Pełny cennik wszystkich usług →</a></p>
  </div>
</section>'''
            + f'<section><div class="wrap">{sec_head("Dlaczego my", "Gwarancje, które daje niewiele firm")}{guarantees()}</div></section>'
            + steps_section()
            + f'<section><div class="wrap">{sec_head("Realizacje", "Tak wygląda nasza praca", "Mieszkania, domy, biura i transport specjalny — w Warszawie i całej Polsce.")}{case_cards(R, CASES[:3])}<p class="center-link"><a href="{R}realizacje/" class="more">Wszystkie realizacje →</a></p></div></section>'
            + order_section(R)
            + f'<section class="alt"><div class="wrap">{sec_head("Porady", "Poradnik przeprowadzkowy", "Praktyczne wskazówki: jak pakować, jak przewieźć AGD i jak zaplanować przeprowadzkę.")}{post_cards(R, ARTICLES[:3])}<p class="center-link"><a href="{R}porady/" class="more">Wszystkie porady →</a></p></div></section>'
            + faq_section(HOME_FAQ, alt=False)
            + cta_band(R))


def service_page(s):
    def body(R):
        crumb = crumbs(R, [("Usługi", ""), (s.name, "")])
        out = hero(R, s.h1, s.lead, s.badges, ("Zamów online", f"{R}wycena/?usluga={s.form.replace(' ', '%20')}"),
                   ("Cennik", "#cennik"), f'<div class="hero-art">{ART[s.slug]}</div>', crumb, sub=True, below=quick_band(s.form))
        alt = True
        for b in s.blocks:
            out += split_block(b, alt) if b.type == "split" else chips_block(b, alt)
            alt = not alt
        out += f'''
<section class="{"alt" if alt else ""}" id="cennik">
  <div class="wrap">
    {sec_head("Cennik", f"{s.name} — cennik", "Ceny orientacyjne. Dokładną, stałą cenę podajemy po krótkiej rozmowie — bezpłatnie.")}
    {plans_html(R, s.plans, s.form)}
    <div class="price-extra single">{notes_box(s.notes)}</div>
  </div>
</section>'''
        out += steps_section(with_process=False)
        if s.fleet:
            out += fleet()
        out += faq_section(s.faq, alt=not s.fleet)
        others = [x for x in SERVICES if x.slug != s.slug]
        i = SERVICES.index(s)
        others = others[i:] + others[:i]
        out += f'<section><div class="wrap">{sec_head("Inne usługi", "Może przyda się też")}{services_grid(R, others[:3])}</div></section>'
        out += cta_band(R)
        return out
    page(f"{s.slug}/", s.seo_title, s.seo_desc, body, active="uslugi")


def cennik_page():
    def body(R):
        jump = '<div class="jump">' + "".join(f'<a href="#{s.slug}">{s.name}</a>' for s in SERVICES) + '</div>'
        out = phead(R, "Cennik <em>bez ukrytych kosztów</em>", "Wszystkie stawki w jednym miejscu. Cenę za konkretne zlecenie ustalamy przed startem i gwarantujemy, że się nie zmieni.", [("Cennik", "")], extra=jump)
        out += f'<section class="alt"><div class="wrap"><div class="price-extra">{notes_box(BOX_NOTES)}{calculator()}</div></div></section>'
        for i, s in enumerate(SERVICES):
            out += f'''
<section class="{"" if i % 2 == 0 else "alt"}" id="{s.slug}">
  <div class="wrap">
    <div class="pg-head"><div><span class="eyebrow">{s.tagline}</span><h2>{s.name}</h2></div><a class="more" href="{R}{s.slug}/">Więcej o usłudze →</a></div>
    {plans_html(R, s.plans, s.form)}
    <div class="price-extra single">{notes_box(s.notes, "Warto wiedzieć")}</div>
  </div>
</section>'''
        out += faq_section(HOME_FAQ[:4], alt=len(SERVICES) % 2 == 1)
        return out + cta_band(R, "Chcesz poznać dokładną cenę? Wycenimy w 2 minuty.")
    page("cennik/", "Cennik przeprowadzek i transportu — Warszawa", "Cennik przeprowadzek w Warszawie: od 189 zł/h, transport międzymiastowy od 1,99 zł/km, pianino od 500 zł. Stała cena i płatność po realizacji.", body, active="cennik")


def realizacje_page():
    def body(R):
        out = phead(R, "Nasze <em>realizacje</em>", "Przeprowadzki mieszkań, domów i biur, transport międzymiastowy i specjalny. Zobacz, jak wygląda nasza praca.", [("Realizacje", "")])
        out += f'<section class="alt"><div class="wrap">{case_cards(R, CASES)}</div></section>'
        out += f'<section><div class="wrap">{sec_head("Dlaczego my", "Każde zlecenie z tymi samymi gwarancjami")}{guarantees()}</div></section>'
        return out + cta_band(R, "Chcesz taką przeprowadzkę? Wycenimy ją za darmo.")
    page("realizacje/", "Realizacje — przeprowadzki i transport", "Przykłady naszych realizacji: przeprowadzki mieszkań, domów i biur, transport międzymiastowy, transport pianin.", body, active="realizacje")


def opinie_page():
    def body(R):
        leave = f'<a href="{SITE.google_reviews}" class="btn btn-accent" target="_blank" rel="noopener">{svg("star")} Zostaw opinię w Google</a>' if SITE.google_reviews else f'<a href="{R}kontakt/" class="btn btn-accent">Podziel się opinią</a>'
        out = phead(R, "Opinie <em>klientów</em>", "Zależy nam na tym, żeby każdy klient polecał nas znajomym. Przeczytaj, co mówią o nas osoby, którym pomogliśmy.", [("Opinie", "")], extra=f'<div class="hero-cta">{leave}</div>')
        if REVIEWS:
            cards = "".join(f'<figure class="review"><div class="stars">★★★★★</div><blockquote>{esc(r.text)}</blockquote><figcaption><b>{esc(r.name)}</b><span>{r.source}</span></figcaption></figure>' for r in REVIEWS)
            out += f'<section class="alt"><div class="wrap"><div class="reviews">{cards}</div></div></section>'
        else:
            out += f'<section class="alt"><div class="wrap"><div class="empty">{svg("star")}<h3>Opinie klientów pojawią się tutaj wkrótce</h3><p>Korzystałeś z naszych usług? Będzie nam bardzo miło, jeśli podzielisz się swoją opinią.</p>{leave}</div></div></section>'
        out += f'<section><div class="wrap">{sec_head("Za co klienci nas cenią", "Gwarancje w każdym zleceniu")}{guarantees()}</div></section>'
        return out + cta_band(R)
    page("opinie/", "Opinie klientów", "Opinie klientów o naszych przeprowadzkach i transporcie w Warszawie.", body, active="opinie")


def porady_page():
    def body(R):
        out = phead(R, "Poradnik <em>przeprowadzkowy</em>", "Jak zaplanować przeprowadzkę, spakować kartony i bezpiecznie przewieźć AGD, RTV czy pianino. Praktyczne wskazówki od ekipy, która robi to codziennie.", [("Porady", "")])
        out += f'<section class="alt"><div class="wrap">{post_cards(R, ARTICLES)}</div></section>'
        return out + cta_band(R, "Nie chcesz robić tego sam? Zajmiemy się wszystkim.")
    page("porady/", "Porady przeprowadzkowe", "Poradnik przeprowadzkowy: jak zorganizować przeprowadzkę, pakować kartony, przewieźć lodówkę, pralkę, telewizor i pianino.", body, active="porady")


def article_page(a):
    def body(R):
        meta = f'<div class="post-meta big">{a.cat} · {a.read} czytania</div>'
        out = phead(R, a.title, a.excerpt, [("Porady", "porady/"), (a.title, "")], extra=meta)
        others = [x for x in ARTICLES if x.slug != a.slug][:3]
        out += f'''
<section class="alt">
  <div class="wrap article">
    <article class="prose">{a.body}</article>
    <aside class="aside">{quick_form("Potrzebujesz pomocy?", note="Zostaw numer — wycenimy przeprowadzkę za darmo.")}</aside>
  </div>
</section>
<section><div class="wrap">{sec_head("Czytaj dalej", "Inne porady")}{post_cards(R, others)}</div></section>'''
        return out + cta_band(R)
    schema = {"@context": "https://schema.org", "@type": "Article", "headline": a.title, "description": a.excerpt, "inLanguage": "pl-PL",
              "publisher": {"@type": "Organization", "name": SITE.brand}}
    page(f"porady/{a.slug}/", a.title, a.excerpt, body, active="porady", schema=schema)


def wycena_page():
    def body(R):
        out = phead(R, "Wycena i zamówienie <em>online</em>", "Trzy krótkie kroki. Oddzwonimy, potwierdzimy termin i podamy stałą cenę — bez zaliczek i bez zobowiązań.", [("Wycena online", "")], extra=badges(["Bezpłatnie", "Stała cena", "Płatność po realizacji"]))
        out += f'''
<section class="alt" id="zamow">
  <div class="wrap order-grid">
    <div class="order-aside">
      <h2>Wolisz inaczej?</h2>
      <p class="lead">Zadzwoń albo wyślij zdjęcia mebli na WhatsApp — wycenimy na ich podstawie.</p>
      {contact_list(R)}
    </div>
    {order_form()}
  </div>
</section>'''
        return out + faq_section(HOME_FAQ[:4], alt=False)
    page("wycena/", "Wycena online — zamów przeprowadzkę", "Zamów przeprowadzkę lub transport online w 2 minuty. Bezpłatna wycena, stała cena, płatność po realizacji.", body, active="wycena")


def kontakt_page():
    def body(R):
        out = phead(R, "Kontakt", "Zadzwoń, napisz na WhatsApp albo zostaw numer — oddzwonimy w ciągu kilku minut.", [("Kontakt", "")])
        maps = "https://www.google.com/maps?q=" + SITE.map_query.replace(" ", "+") + "&output=embed"
        out += f'''
<section class="alt">
  <div class="wrap contact-grid">
    <div>
      {contact_list(R)}
      <div class="info-card">
        <div>{svg("clock")}<span><small>Godziny pracy</small>{SITE.hours}</span></div>
        <div>{svg("pin")}<span><small>Obszar działania</small>{SITE.address}, cała Polska</span></div>
      </div>
      <iframe class="map" src="{maps}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Mapa"></iframe>
    </div>
    <div>{quick_form("Oddzwonimy do Ciebie", note="Zostaw numer telefonu — skontaktujemy się w godzinach pracy.")}</div>
  </div>
</section>'''
        return out + cta_band(R)
    page("kontakt/", "Kontakt", f"Kontakt: telefon {SITE.phone}, WhatsApp, e-mail. {SITE.hours}. Przeprowadzki i transport w Warszawie.", body, active="kontakt")


def privacy_page():
    def body(R):
        out = phead(R, "Polityka prywatności", "Informacje o przetwarzaniu danych osobowych zgodnie z RODO.", [("Polityka prywatności", "")])
        out += f'''
<section class="alt"><div class="wrap"><div class="prose narrow">
<h2>Administrator danych</h2><p>Administratorem danych osobowych jest {SITE.brand} ({SITE.address}), kontakt: <a href="mailto:{SITE.email}">{SITE.email}</a>, tel. {SITE.phone}.</p>
<h2>Jakie dane zbieramy</h2><p>Imię, numer telefonu, adres e-mail oraz informacje podane w formularzu (adresy, termin, lista rzeczy) — wyłącznie w celu przygotowania wyceny i realizacji usługi.</p>
<h2>Podstawa prawna</h2><p>Dane przetwarzamy na podstawie art. 6 ust. 1 lit. a i b RODO — Twojej zgody oraz działań zmierzających do zawarcia umowy.</p>
<h2>Jak długo przechowujemy dane</h2><p>Do czasu realizacji usługi, a następnie przez okres wymagany przepisami podatkowymi i rachunkowymi.</p>
<h2>Twoje prawa</h2><p>Masz prawo dostępu do danych, ich poprawienia, usunięcia, ograniczenia przetwarzania, przeniesienia oraz cofnięcia zgody. Możesz także złożyć skargę do Prezesa UODO.</p>
<h2>Pliki cookies</h2><p>Strona korzysta wyłącznie z technicznych plików cookies niezbędnych do działania oraz czcionek Google Fonts.</p>
</div></div></section>'''
        return out
    page("polityka-prywatnosci/", "Polityka prywatności", "Polityka prywatności i informacje RODO.", body)


def not_found():
    def body(R):
        return phead(R, "Nie ma takiej strony", "Strona mogła zostać przeniesiona. Sprawdź nasze usługi albo wróć na stronę główną.", [("404", "")],
                     extra=f'<div class="hero-cta"><a class="btn btn-accent" href="{R}">Strona główna</a><a class="btn btn-ghost" href="{R}wycena/">Wycena online</a></div>') \
            + f'<section class="alt"><div class="wrap">{services_grid(R)}</div></section>'
    page("404.html", "Nie znaleziono strony", "Nie znaleziono strony.", body, R=SITE.base)


def build():
    page("", f"{SITE.brand} — Przeprowadzki i transport w Warszawie",
         "Przeprowadzki prywatne i firmowe, transport mebli, pianin, taxi bagażowe. Stała cena, ubezpieczenie OCP do 200 000 zł, zamówienie online w 2 minuty.",
         home, schema=BUSINESS)
    for s in SERVICES:
        service_page(s)
    cennik_page(); realizacje_page(); opinie_page(); porady_page()
    for a in ARTICLES:
        article_page(a)
    wycena_page(); kontakt_page(); privacy_page(); not_found()

    today = date.today().isoformat()
    urls = "".join(f"<url><loc>{SITE.url}{p}</loc><lastmod>{today}</lastmod></url>" for p in BUILT)
    (ROOT / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>', encoding="utf-8")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE.url}sitemap.xml\n", encoding="utf-8")
    print(f"Zbudowano {len(BUILT)} stron + 404")


if __name__ == "__main__":
    build()
