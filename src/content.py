"""Treść strony. Edytuj tutaj, potem uruchom: python3 src/build.py"""


class D(dict):
    __getattr__ = dict.get


# ===== DANE FIRMY — podmień na dane klienta =====
SITE = D(
    brand="MOVEO",
    phone="+48 000 000 000",
    whatsapp="48000000000",            # bez "+" i spacji
    email="kontakt@twojadomena.pl",
    city="Warszawa",
    address="Warszawa i okolice",
    hours="Pon–Sob, 8:00–19:00",
    map_query="Warszawa",
    google_reviews="",                 # link do opinii Google (Zostaw opinię)
    url="https://newhope77.github.io/przeprowadzki-site/",
    base="/przeprowadzki-site/",       # "/" po podpięciu własnej domeny
    form_endpoint="",                  # np. https://formspree.io/f/xxxx — puste = WhatsApp
)


def plan(name, sub, price, unit, team, feats, pakiet, hot=False, prefix=""):
    return D(name=name, sub=sub, price=price, unit=unit, team=team, hot=hot, prefix=prefix, pakiet=pakiet,
             feats=[(f[1:], False) if f.startswith("-") else (f, True) for f in feats])


HOURLY = [
    plan("Ekonomiczny", "Auto + 1 tragarz", "189", "zł / godz.", "Ekipa 1-osobowa",
         ["Transport", "Wyniesienie i wniesienie", "Bez ukrytych kosztów", "-Zabezpieczenie folią", "-Pakowanie i montaż"], "Ekonomiczny"),
    plan("Kompleksowy", "Streczowanie · Pakowanie · Montaż", "239", "zł / godz.", "Ekipa 2-osobowa",
         ["Transport, wyniesienie i wniesienie", "Zabezpieczenie mebli folią", "Zabezpieczenie delikatnych przedmiotów",
          "Pakowanie rzeczy i odzieży", "Demontaż i montaż mebli", "Ubezpieczenie mienia do 200 000 zł"], "Kompleksowy", hot=True),
    plan("Standardowy", "Bez streczowania i montażu", "219", "zł / godz.", "Ekipa 2-osobowa",
         ["Transport", "Wyniesienie i wniesienie", "Bez ukrytych kosztów", "-Zabezpieczenie folią", "-Pakowanie i montaż"], "Standardowy"),
]

BOX_NOTES = [
    "Ceny netto — przy płatności gotówką nie doliczamy VAT.",
    "Faktura VAT dla firm na życzenie (+23% VAT).",
    "Kartony 5-warstwowe (60×40×40 / 45×30×30 cm) — <b>9,99 zł / szt.</b>",
    "Wynajem kartonów do 7 dni — <b>gratis</b> w cenie przeprowadzki.",
    "Wynajem powyżej 7 dni — 20 zł za 20 szt. za każdy kolejny tydzień.",
    "Stawki nie dotyczą przedmiotów powyżej 80 kg (wycena indywidualna).",
]

FAQ_PRICE = ("Czy cena może się zmienić w dniu przeprowadzki?",
             "Nie. Przed startem ustalamy zakres usługi i listę rzeczy. Na tej podstawie podajemy ostateczną cenę — po zakończeniu nie ma żadnych dopłat.")
FAQ_INS = ("Czy moje rzeczy są ubezpieczone?",
           "Tak. Każde zlecenie jest objęte ubezpieczeniem OCP do 200 000 zł, a meble i sprzęt zabezpieczamy profesjonalnymi materiałami.")

SERVICES = [
    D(slug="przeprowadzki-prywatne", name="Przeprowadzki prywatne", icon="home", form="Przeprowadzka mieszkania",
      tagline="Mieszkania i domy",
      short="Mieszkania i domy — pakowanie, demontaż, transport i ustawienie mebli w nowym miejscu.",
      seo_title="Przeprowadzki prywatne Warszawa — mieszkania i domy",
      seo_desc="Przeprowadzki mieszkań i domów w Warszawie. Pakowanie, demontaż, transport i montaż mebli. Stała cena, OCP do 200 000 zł, płatność po realizacji.",
      h1="Przeprowadzki mieszkań i domów <em>bez stresu</em>",
      lead="Od kawalerki po dom z ogrodem. Pakujemy, demontujemy, przewozimy i ustawiamy meble — Ty tylko odbierasz klucze.",
      badges=["Stała cena", "OCP do 200 000 zł", "Płatność po realizacji", "Pakowanie i montaż"],
      blocks=[
          D(type="split", eyebrow="Zakres usługi", h2="Zajmiemy się wszystkim — od kartonów po montaż szafy",
            paras=["Każdą przeprowadzkę zaczynamy od krótkiej rozmowy: ustalamy listę rzeczy, piętra, dostęp do windy i termin. Na tej podstawie podajemy stałą cenę, która nie zmienia się w dniu realizacji.",
                   "Przyjeżdżamy autem dopasowanym do ilości rzeczy, z kartonami, folią stretch i bąbelkową, kocami transportowymi i narzędziami do demontażu."],
            items=["Pakowanie rzeczy, odzieży i kuchni", "Demontaż i montaż szaf oraz łóżek", "Zabezpieczenie mebli folią i kocami",
                   "Wyniesienie i wniesienie — także bez windy", "Transport AGD i RTV", "Ustawienie mebli w nowym mieszkaniu"]),
      ],
      plans=HOURLY, notes=BOX_NOTES, fleet=True,
      faq=[FAQ_PRICE,
           ("Ile trwa przeprowadzka mieszkania 2-pokojowego?", "Zwykle 3–5 godzin pracy ekipy — zależnie od ilości rzeczy, pięter, windy i tego, czy pakujemy za Ciebie."),
           ("Czy muszę sam spakować rzeczy?", "Nie musisz. W pakiecie Kompleksowym pakujemy rzeczy, odzież i kuchnię. Możesz też spakować się sam — kartony wypożyczymy gratis do 7 dni."),
           ("Czy pracujecie w soboty?", "Tak, od poniedziałku do soboty w godzinach 8:00–19:00. Inne godziny — do indywidualnego uzgodnienia."),
           FAQ_INS]),

    D(slug="przeprowadzki-biur", name="Przeprowadzki biur", icon="office", form="Przeprowadzka biura",
      tagline="Biura, sklepy, magazyny",
      short="Dokumenty, szafy, biurka, sprzęt IT. Sprawnie, także w sobotę — bez przestojów w pracy.",
      seo_title="Przeprowadzki biur Warszawa — firmy, sklepy, magazyny",
      seo_desc="Przeprowadzki biur i firm w Warszawie. Pakowanie dokumentów, transport mebli biurowych i sprzętu IT, praca w soboty. Faktura VAT.",
      h1="Przeprowadzki biur i firm <em>bez przestojów</em>",
      lead="Przenosimy biura, sklepy i magazyny tak, żeby Twój zespół następnego dnia pracował już w nowym miejscu.",
      badges=["Faktura VAT", "Praca w soboty", "OCP do 200 000 zł", "Oznaczanie kartonów"],
      blocks=[
          D(type="split", eyebrow="Jak pracujemy", h2="Plan, etykiety i sprawny transport",
            paras=["Przed przeprowadzką ustalamy harmonogram, liczbę stanowisk i kolejność prac. Kartony i meble oznaczamy, żeby w nowym biurze wszystko od razu trafiło na swoje miejsce.",
                   "Możemy pracować po godzinach lub w sobotę, żeby nie zakłócać pracy firmy."],
            items=["Transport biurek, krzeseł i szaf", "Pakowanie dokumentów i segregatorów", "Zabezpieczenie sprzętu IT i drukarek",
                   "Demontaż i montaż mebli biurowych", "Ciężkie szafy i sejfy (wycena indywidualna)", "Faktura VAT dla firm"]),
          D(type="chips", eyebrow="Dla kogo", h2="Obsługujemy każdy rodzaj firmy",
            items=["Biura", "Sklepy", "Magazyny", "Gabinety", "Kancelarie", "Szkoły i przedszkola", "Showroomy", "Archiwa"]),
      ],
      plans=[
          plan("Mini", "Z pomocą 1 tragarza", "149", "zł / godz.", "Ekipa 1-osobowa",
               ["Transport", "Wyniesienie i wniesienie", "-Zabezpieczenie folią", "-Demontaż mebli"], "Ekonomiczny"),
          plan("Kompleksowa", "Pakowanie · Demontaż · Montaż", "239", "zł / godz.", "Ekipa 2-osobowa i więcej",
               ["Transport, wyniesienie i wniesienie", "Pakowanie dokumentów", "Zabezpieczenie sprzętu IT", "Demontaż i montaż mebli", "Ubezpieczenie do 200 000 zł"],
               "Kompleksowy", hot=True, prefix="od"),
          plan("Ekonomiczna", "Bez pakowania i montażu", "219", "zł / godz.", "Ekipa 2-osobowa",
               ["Transport", "Wyniesienie i wniesienie", "Bez ukrytych kosztów", "-Demontaż mebli"], "Standardowy"),
      ],
      notes=["Ceny netto. Faktura VAT dla firm (+23% VAT).", "Praca po godzinach i w soboty — do uzgodnienia.",
             "Kartony 5-warstwowe — <b>9,99 zł / szt.</b>, wynajem do 7 dni gratis.", "Duże biura (20+ stanowisk) — stała cena za całość po oględzinach."],
      fleet=True,
      faq=[("Czy możecie przewieźć biuro w sobotę?", "Tak. Sobota to najczęściej wybierany termin przeprowadzek firm — w poniedziałek zespół pracuje już w nowym miejscu."),
           ("Czy wystawiacie fakturę VAT?", "Tak, wystawiamy fakturę VAT 23% dla każdej firmy."),
           ("Jak przygotować biuro do przeprowadzki?", "Wyznacz osobę kontaktową, poproś pracowników o opróżnienie biurek i odłączenie sprzętu. Resztę — kartony, oznaczenia i transport — bierzemy na siebie."),
           FAQ_PRICE, FAQ_INS]),

    D(slug="przeprowadzki-miedzymiastowe", name="Przeprowadzki międzymiastowe", icon="route", form="Przeprowadzka międzymiastowa",
      tagline="Warszawa i cała Polska",
      short="Z Warszawy w całą Polskę i z powrotem. Jeden termin, jedna ekipa, stała cena.",
      seo_title="Przeprowadzki międzymiastowe — Warszawa i cała Polska",
      seo_desc="Przeprowadzki międzymiastowe z Warszawy na terenie całej Polski. Od 1,99 zł/km, pakowanie, montaż, ubezpieczenie do 200 000 zł.",
      h1="Przeprowadzki międzymiastowe <em>w całej Polsce</em>",
      lead="Z Warszawy do Gdańska, Krakowa czy Wrocławia — i z powrotem. Jedna ekipa, jedno auto i stała cena ustalona przed wyjazdem.",
      badges=["Od 1,99 zł/km", "Cała Polska", "OCP do 200 000 zł", "Stała cena"],
      blocks=[
          D(type="split", eyebrow="Jak to wygląda", h2="Załadunek rano, rozładunek w nowym mieście",
            paras=["Przy dłuższej trasie liczy się dobre zabezpieczenie. Meble owijamy folią i kocami, mocujemy pasami, a delikatne rzeczy pakujemy do kartonów.",
                   "Cenę podajemy z góry — na podstawie listy rzeczy, pięter i kilometrów. Nie płacisz za korki ani postoje."],
            items=["Zabezpieczenie i pakowanie rzeczy", "Załadunek do jednego pojazdu", "Transport na terenie całej Polski",
                   "Rozładunek i wniesienie", "Montaż mebli i rozpakowanie", "Wywóz zbędnych rzeczy na życzenie"]),
      ],
      plans=[
          plan("Transport krajowy", "Warszawa ⇄ cała Polska", "1,99", "zł / km", "Kilometry liczone w obie strony",
               ["Transport", "Załadunek i rozładunek", "Zabezpieczenie mebli", "Ubezpieczenie do 200 000 zł", "Bez ukrytych kosztów"],
               "Kompleksowy", hot=True, prefix="od"),
          plan("Usługi dodatkowe", "Dobierasz według potrzeb", "Wycena", "indywidualna", "Ustalamy w rozmowie",
               ["Pakowanie drobnych rzeczy i odzieży", "Demontaż i montaż mebli", "Kartony i materiały", "Rozpakowanie w nowym miejscu"], "Kompleksowy"),
      ],
      notes=["Stawka za kilometr dotyczy trasy w obie strony.", "Ceny netto. Faktura VAT na życzenie (+23% VAT).",
             "Kartony 5-warstwowe — <b>9,99 zł / szt.</b>", "Transport zagraniczny — wycena indywidualna."],
      fleet=True,
      faq=[("Ile kosztuje przeprowadzka międzymiastowa?", "Cena zależy od odległości, ilości rzeczy, pięter załadunku i rozładunku oraz usług dodatkowych. Transport liczymy od 1,99 zł/km, a końcową kwotę podajemy przed wyjazdem."),
           ("Ile trwa przeprowadzka do innego miasta?", "Większość tras w Polsce realizujemy w ciągu jednego dnia: załadunek rano, rozładunek po południu lub wieczorem."),
           ("Czy muszę być na miejscu rozładunku?", "Wystarczy, że będzie tam osoba upoważniona, która wskaże, gdzie ustawić meble."),
           FAQ_INS]),

    D(slug="taxi-bagazowe", name="Taxi bagażowe", icon="box", form="Taxi bagażowe",
      tagline="Szybki przewóz rzeczy",
      short="Szybki przewóz kilku rzeczy, zakupy z IKEA, auto dostawcze z kierowcą na godziny.",
      seo_title="Taxi bagażowe Warszawa — auto dostawcze z kierowcą",
      seo_desc="Taxi bagażowe w Warszawie: transport mebli ze sklepów, AGD, kartonów i materiałów. Kierowca pomaga przy załadunku i wnoszeniu.",
      h1="Taxi bagażowe — <em>szybki przewóz</em> w Warszawie",
      lead="Nowa sofa z IKEA, kilka kartonów, pralka z ogłoszenia? Przyjedziemy autem dostawczym z kierowcą, pomożemy załadować i wnieść.",
      badges=["Nawet tego samego dnia", "Pomoc przy wnoszeniu", "Ładowność do 1,5 t", "Faktura VAT"],
      blocks=[
          D(type="chips", eyebrow="Co przewozimy", h2="Przewieziemy prawie wszystko",
            items=["Meble", "Sprzęt AGD i RTV", "Zakupy z IKEA, Castoramy, Leroy Merlin", "Materiały budowlane", "Kartony i rzeczy osobiste",
                   "Rowery i sprzęt sportowy", "Opony i felgi", "Sprzęt biurowy", "Rzeczy z OLX i Allegro Lokalnie"]),
          D(type="split", eyebrow="Auto z kierowcą", h2="Wynajem auta dostawczego z kierowcą na godziny",
            paras=["Potrzebujesz auta na kilka kursów? Wynajmij je z kierowcą na godzinę, pół dnia lub cały dzień — w Warszawie i okolicach.",
                   "Mamy pasy, koce i sprzęt do załadunku, więc przewieziemy też ładunki delikatne, jak szkło czy płyty gipsowo-kartonowe."],
            items=["Pasy i koce transportowe", "Pomoc przy załadunku i rozładunku", "Wnoszenie na piętro",
                   "Ładunki delikatne i ponadgabarytowe", "Kursy po sklepach meblowych", "Faktura VAT"]),
      ],
      plans=[
          plan("Pojedynczy transport", "Jeden mebel z wniesieniem", "350", "zł", "Ekipa 2-osobowa",
               ["Transport jednego mebla", "Wyniesienie i wniesienie", "Bez ukrytych kosztów"], "Ekonomiczny"),
          plan("Kompleksowy", "Transport · Streczowanie · Montaż", "229", "zł / godz.", "Ekipa 2-osobowa",
               ["Transport, wyniesienie i wniesienie", "Zabezpieczenie folią", "Demontaż i montaż mebli", "Ubezpieczenie do 200 000 zł"], "Kompleksowy", hot=True),
          plan("Ekonomiczny", "Bez streczowania i montażu", "199", "zł / godz.", "Ekipa 2-osobowa",
               ["Transport", "Wyniesienie i wniesienie", "-Zabezpieczenie folią", "-Montaż mebli"], "Standardowy"),
      ],
      notes=["Ceny netto. Faktura VAT na życzenie (+23% VAT).", "Transport poza Warszawę — dopłata za kilometry, podajemy z góry.",
             "Stawki nie dotyczą przedmiotów powyżej 80 kg."],
      fleet=True,
      faq=[("Ile kosztuje taxi bagażowe?", "Jeden mebel z wniesieniem w Warszawie to 350 zł. Większe zlecenia rozliczamy godzinowo — od 199 zł/h za auto z dwiema osobami."),
           ("Jak szybko przyjedziecie?", "Jeśli mamy wolne auto — nawet tego samego dnia. Najpewniej jest zarezerwować termin dzień wcześniej."),
           ("Czy kierowca pomoże wnieść rzeczy?", "Tak. W każdym pakiecie wyniesienie i wniesienie jest w cenie."),
           ("Czy jeździcie poza Warszawę?", "Tak, obsługujemy okolice Warszawy i całą Polskę. Koszt dojazdu podajemy przed zleceniem.")]),

    D(slug="transport-mebli", name="Transport mebli", icon="sofa", form="Transport mebli",
      tagline="Z wnoszeniem i montażem",
      short="Sofa ze sklepu, szafa od znajomych? Wniesiemy, zabezpieczymy folią i zmontujemy na miejscu.",
      seo_title="Transport mebli Warszawa — z wnoszeniem i montażem",
      seo_desc="Transport mebli w Warszawie: sofy, narożniki, szafy, łóżka, AGD i RTV. Wnoszenie, zabezpieczenie folią, demontaż i montaż.",
      h1="Transport mebli <em>z wnoszeniem</em>",
      lead="Sofa, narożnik, szafa, łóżko z materacem, lodówka czy pralka — przewieziemy bezpiecznie ze sklepu, od znajomych albo między mieszkaniami.",
      badges=["Wnoszenie w cenie", "Demontaż i montaż", "Folia i koce", "OCP do 200 000 zł"],
      blocks=[
          D(type="split", eyebrow="Meble", h2="Kanapy, narożniki, szafy i łóżka",
            paras=["Duże meble rozkręcamy, owijamy folią stretch i kocami, a na miejscu składamy i ustawiamy tam, gdzie chcesz.",
                   "Nie ma windy? Wąska klatka? To dla nas codzienność — mamy pasy nośne i odpowiednią ekipę."],
            items=["Sofy, narożniki i fotele", "Szafy i komody", "Łóżka z materacem", "Stoły i krzesła", "Demontaż i montaż na miejscu", "Wnoszenie bez windy"]),
          D(type="split", eyebrow="AGD i RTV", h2="Lodówki, pralki i telewizory",
            paras=["Lodówkę przewozimy w pionie, pralkę z zablokowanym bębnem, a telewizor w pozycji pionowej, zabezpieczony folią bąbelkową.",
                   "Jeśli nie masz fabrycznych pudełek — zapakujemy sprzęt w folię i koce transportowe."],
            items=["Lodówki i zamrażarki", "Pralki i zmywarki", "Telewizory i monitory", "Kuchenki i piekarniki", "Sprzęt audio"], reverse=True),
          D(type="chips", eyebrow="Ze sklepów", h2="Odbierzemy meble prosto ze sklepu",
            items=["IKEA", "Agata Meble", "Black Red White", "Jysk", "Castorama", "Leroy Merlin", "OBI", "Komisy meblowe", "OLX i Allegro Lokalnie"]),
      ],
      plans=HOURLY, notes=BOX_NOTES, fleet=True,
      faq=[("Ile kosztuje transport jednego mebla?", "Pojedynczy mebel z wniesieniem w Warszawie to 350 zł. Przy kilku meblach bardziej opłaca się stawka godzinowa."),
           ("Czy zmontujecie mebel z IKEA?", "Tak, w pakiecie Kompleksowym składamy meble na miejscu."),
           ("Jak przewozicie lodówkę?", "W pozycji pionowej, zabezpieczoną folią i pasami. Po transporcie radzimy odczekać kilka godzin przed włączeniem."),
           FAQ_INS]),

    D(slug="transport-pianin", name="Transport pianin", icon="piano", form="Transport pianina",
      tagline="Bezpiecznie i ostrożnie",
      short="Pianina i ciężkie przedmioty — pasy, wózki i doświadczona ekipa, także bez windy.",
      seo_title="Transport pianina Warszawa — bezpieczne przenoszenie",
      seo_desc="Transport i przenoszenie pianin w Warszawie. Pokrowce, pasy, wózki transportowe, doświadczona ekipa. Od 500 zł.",
      h1="Transport pianina <em>bez ryzyka</em>",
      lead="Pianino waży 200–300 kg i nie wybacza błędów. Mamy sprzęt, pasy i doświadczenie, żeby przenieść je nawet wąską klatką schodową.",
      badges=["Od 500 zł", "Pokrowce i pasy", "Wąskie klatki schodowe", "OCP do 200 000 zł"],
      blocks=[
          D(type="split", eyebrow="Zakres usługi", h2="Instrument w bezpiecznych rękach",
            paras=["Obsługujemy klientów prywatnych, szkoły muzyczne i instytucje. Pianino zabezpieczamy pokrowcami, przenosimy na pasach i wózku, a w aucie mocujemy tak, żeby nie przesunęło się ani o centymetr.",
                   "Realizujemy transport na krótkich i długich dystansach — po Warszawie i w całej Polsce."],
            items=["Zabezpieczenie pokrowcami i kocami", "Wózek transportowy i pasy nośne", "Znoszenie i wnoszenie po schodach",
                   "Mocowanie w aucie na czas jazdy", "Ustawienie w wybranym miejscu", "Terminowa realizacja"]),
          D(type="chips", eyebrow="Wycena", h2="Do wyceny potrzebujemy tylko kilku informacji",
            items=["Marka i model pianina", "Piętro załadunku i rozładunku", "Czy jest winda", "Adresy (odległość)", "Wąskie przejścia lub schody zewnętrzne"]),
      ],
      plans=[
          plan("Warszawa", "Transport w granicach miasta", "500", "zł", "Doświadczona ekipa",
               ["Transport", "Zabezpieczenie", "Wyniesienie i wniesienie", "Pomoc przy załadunku i rozładunku"], "Kompleksowy", prefix="od"),
          plan("Warszawa i okolice", "Do ok. 30 km od Warszawy", "550", "zł", "Doświadczona ekipa",
               ["Transport", "Zabezpieczenie", "Wyniesienie i wniesienie", "Ubezpieczenie do 200 000 zł"], "Kompleksowy", hot=True, prefix="od"),
      ],
      notes=["<b>+100 zł</b> za każde piętro wnoszenia lub znoszenia po schodach.", "Fortepiany i transport międzymiastowy — wycena indywidualna.",
             "Po transporcie zalecamy strojenie instrumentu (nie wykonujemy strojenia)."],
      fleet=False,
      faq=[("Czy pianino trzeba stroić po transporcie?", "Zwykle tak — zmiana temperatury i wilgotności wpływa na strój. Najlepiej odczekać 2–3 tygodnie i wtedy wezwać stroiciela."),
           ("Ile osób przenosi pianino?", "Zazwyczaj 3–4 osoby, w zależności od wagi instrumentu i liczby schodów."),
           ("Czy przewozicie fortepiany?", "Tak, po indywidualnej wycenie — fortepian wymaga częściowego demontażu i specjalnych płoz."),
           FAQ_INS]),
]

HOME_FAQ = [
    FAQ_PRICE,
    ("Od czego zależy cena?", "Od ilości rzeczy, piętra i dostępności windy, odległości oraz zakresu usługi (pakowanie, montaż). Wycena jest zawsze bezpłatna."),
    FAQ_INS,
    ("Czy trzeba płacić zaliczkę?", "Nie. Płatność następuje dopiero po wykonaniu usługi — gotówką, przelewem lub BLIK."),
    ("Czy oferujecie kompleksową obsługę?", "Tak — od pakowania, demontażu i załadunku, przez transport, po wniesienie, montaż i ustawienie mebli."),
    ("Jak szybko możecie przyjechać?", "Przy wolnym terminie nawet tego samego dnia. Większe przeprowadzki najlepiej zamówić z kilkudniowym wyprzedzeniem."),
]

# Przykładowe zlecenia — podmień na prawdziwe realizacje klienta (najlepiej ze zdjęciami)
CASES = [
    D(title="Mieszkanie 2-pokojowe", route="Mokotów → Ursynów", pill="Przeprowadzka", team="2 osoby", time="ok. 5 h", plan="Kompleksowy",
      items=["Pakowanie kuchni i odzieży", "Demontaż szafy i łóżka", "Zabezpieczenie sofy folią", "Transport AGD", "Montaż i ustawienie mebli"]),
    D(title="Dom jednorodzinny", route="Warszawa → Piaseczno", pill="Przeprowadzka", team="4 osoby, 2 auta", time="1 dzień", plan="Kompleksowy",
      items=["Demontaż dużych szaf", "Pakowanie ok. 60 kartonów", "Transport ciężkiego wyposażenia", "Rowery i sprzęt ogrodowy", "Ustawienie w nowym domu"]),
    D(title="Biuro — 15 stanowisk", route="Wola → Służew", pill="Biuro", team="3 osoby", time="sobota", plan="Kompleksowa",
      items=["Pakowanie dokumentów", "Oznaczenie kartonów", "Transport biurek i krzeseł", "Zabezpieczenie sprzętu IT", "Montaż mebli biurowych"]),
    D(title="Mieszkanie 3-pokojowe", route="Warszawa → Gdańsk", pill="Międzymiastowa", team="3 osoby", time="1 dzień", plan="Transport krajowy",
      items=["Zabezpieczenie mebli na długą trasę", "Transport lodówki i pralki", "Mocowanie ładunku pasami", "Rozładunek i wniesienie", "Montaż łóżka"]),
    D(title="Pianino na 3. piętro", route="Żoliborz → Bielany", pill="Pianino", team="4 osoby", time="ok. 2 h", plan="Warszawa",
      items=["Pokrowiec i koce", "Znoszenie bez windy", "Wózek i pasy nośne", "Mocowanie w aucie", "Wniesienie na 3. piętro"]),
    D(title="Sofa narożna ze sklepu", route="IKEA Janki → Bemowo", pill="Taxi bagażowe", team="2 osoby", time="ok. 2 h", plan="Pojedynczy transport",
      items=["Odbiór ze sklepu", "Zabezpieczenie folią", "Wniesienie na 4. piętro", "Rozpakowanie", "Wywóz opakowań"]),
]

# Prawdziwe opinie klientów: D(name="Anna K.", text="...", source="Google")
REVIEWS = []

ARTICLES = [
    D(slug="jak-zorganizowac-przeprowadzke", icon="list", cat="Planowanie", read="6 min",
      title="Przeprowadzka krok po kroku — jak ją zorganizować?",
      excerpt="Plan na 4 tygodnie przed przeprowadzką: co zrobić najpierw, o czym nie zapomnieć i jak uniknąć stresu w dniu przeprowadzki.",
      body="""
<p>Dobrze zaplanowana przeprowadzka to połowa sukcesu. Zamiast pakować wszystko w ostatnią noc, rozłóż pracę na kilka tygodni. Oto sprawdzony harmonogram.</p>
<h2>4 tygodnie przed</h2>
<ul><li>Ustal termin i zarezerwuj firmę przeprowadzkową — w sezonie (maj–wrzesień) i na koniec miesiąca terminy szybko się kończą.</li>
<li>Zrób listę dużych mebli i sprzętów — przyda się do dokładnej wyceny.</li>
<li>Zdecyduj, czego nie zabierasz: sprzedaj, oddaj albo wyrzuć.</li></ul>
<h2>2 tygodnie przed</h2>
<ul><li>Zamów kartony, taśmę i marker.</li><li>Zacznij pakować rzeczy, których nie używasz na co dzień: książki, dekoracje, ubrania sezonowe.</li>
<li>Zgłoś zmianę adresu w banku, u pracodawcy i w usługach (internet, prąd, gaz).</li></ul>
<h2>Tydzień przed</h2>
<ul><li>Potwierdź z firmą godzinę, adresy, piętra i dostęp do windy.</li><li>Zarezerwuj miejsce parkingowe dla auta pod blokiem.</li>
<li>Zużyj zapasy z zamrażarki.</li></ul>
<div class="tip"><b>Wskazówka:</b> przygotuj „pudełko pierwszej potrzeby” — ładowarki, dokumenty, leki, papier toaletowy, czajnik i kubki. Przewieź je sam.</div>
<h2>Dzień przed</h2>
<ul><li>Rozmroź i wysusz lodówkę.</li><li>Odłącz pralkę i zabezpiecz bęben śrubami transportowymi.</li><li>Opisz kartony: zawartość i pokój docelowy.</li></ul>
<h2>W dniu przeprowadzki</h2>
<p>Bądź na miejscu, wskaż ekipie rzeczy delikatne i te, które jadą osobno. Na koniec obejdź puste mieszkanie i sprawdź szafki, piwnicę i balkon. Zanotuj stany liczników.</p>
"""),
    D(slug="jak-pakowac-kartony", icon="box", cat="Pakowanie", read="5 min",
      title="Jak pakować kartony do przeprowadzki?",
      excerpt="Ciężkie na dół, lekkie na górę, a talerze zawsze pionowo. Proste zasady, dzięki którym nic się nie stłucze.",
      body="""
<p>Źle spakowany karton to najczęstsza przyczyna zniszczonych rzeczy. Kilka prostych zasad sprawi, że wszystko dojedzie w całości.</p>
<h2>Wybierz odpowiednie kartony</h2>
<p>Używaj mocnych, wielowarstwowych kartonów. Małe pudła (45×30×30 cm) są na książki i ciężkie rzeczy, duże (60×40×40 cm) — na pościel, ubrania i lekkie przedmioty.</p>
<h2>Zasada wagi</h2>
<ul><li>Karton nie powinien ważyć więcej niż 20 kg.</li><li>Ciężkie rzeczy kładź na dno, lekkie na wierzch.</li><li>Wypełniaj wolne miejsca papierem lub ręcznikami — nic nie może się przesuwać.</li></ul>
<h2>Szkło i porcelana</h2>
<p>Każdy talerz zawiń osobno w papier i ustaw pionowo, jak płyty w szafce. Kieliszki wypełnij papierem w środku i owiń folią bąbelkową. Na karton nakle „OSTROŻNIE — SZKŁO” i strzałkę „GÓRA”.</p>
<div class="tip"><b>Wskazówka:</b> opisuj kartony z dwóch boków, nie tylko na górze — w stosie góra jest niewidoczna.</div>
<h2>Ubrania</h2>
<p>Ubrania na wieszakach najlepiej przewozić w kartonach-szafach albo w dużych workach. Rzeczy złożone możesz zostawić w szufladach komody — pod warunkiem, że nie są ciężkie.</p>
<h2>Nie chcesz pakować sam?</h2>
<p>W pakiecie Kompleksowym spakujemy wszystko za Ciebie — z własnymi kartonami i materiałami.</p>
"""),
    D(slug="jak-przewiezc-lodowke", icon="fridge", cat="AGD", read="4 min",
      title="Jak przetransportować lodówkę?",
      excerpt="Czy lodówkę można położyć? Ile czekać z włączeniem? Wyjaśniamy, jak przewieźć lodówkę bez uszkodzenia agregatu.",
      body="""
<p>Lodówka to jedno z najbardziej wrażliwych urządzeń przy przeprowadzce. Błąd przy transporcie może uszkodzić sprężarkę — a naprawa kosztuje niemal tyle, co nowa lodówka.</p>
<h2>Przygotowanie</h2>
<ul><li>Wyłącz lodówkę co najmniej 12 godzin wcześniej i rozmroź zamrażarkę.</li><li>Wyjmij półki i szuflady, spakuj je osobno.</li><li>Umyj i wysusz wnętrze, zostaw drzwi uchylone, żeby nie pojawił się zapach.</li></ul>
<h2>Transport w pionie</h2>
<p>Lodówkę przewozimy w pozycji pionowej. Położenie jej na boku może spowodować przedostanie się oleju ze sprężarki do układu chłodzenia. Drzwi zabezpieczamy taśmą, a całość folią i kocem.</p>
<div class="tip"><b>Ważne:</b> jeśli lodówka musiała być przechylona, po ustawieniu odczekaj tyle godzin, ile trwał transport w poziomie (minimum 4 godziny), zanim ją włączysz.</div>
<h2>Po przeprowadzce</h2>
<p>Ustaw lodówkę na równym podłożu, z odstępem od ściany. Po włączeniu poczekaj kilka godzin, aż osiągnie odpowiednią temperaturę, zanim włożysz jedzenie.</p>
"""),
    D(slug="jak-przewiezc-pralke", icon="washer", cat="AGD", read="4 min",
      title="Jak przewieźć pralkę, żeby jej nie uszkodzić?",
      excerpt="Śruby transportowe, woda w wężach i zabezpieczenie bębna — wszystko, o czym trzeba pamiętać przy transporcie pralki.",
      body="""
<p>Pralka jest ciężka i ma ruchomy bęben zawieszony na amortyzatorach. Bez zabezpieczenia może się uszkodzić już na pierwszej dziurze w drodze.</p>
<h2>Śruby transportowe</h2>
<p>Najważniejszy krok to zablokowanie bębna. Użyj śrub transportowych, które były dołączone do pralki (zwykle 3–4 sztuki z tyłu obudowy). Jeśli ich nie masz — zapytaj w serwisie producenta, kosztują kilkanaście złotych.</p>
<h2>Woda i węże</h2>
<ul><li>Zakręć zawór wody i odłącz wąż doprowadzający.</li><li>Opróżnij filtr pompy — zawsze zostaje w nim trochę wody.</li><li>Węże przyklej taśmą do obudowy albo spakuj osobno.</li></ul>
<div class="tip"><b>Wskazówka:</b> podstaw ręcznik i płaską miskę pod filtr — wody może być więcej, niż się spodziewasz.</div>
<h2>Transport</h2>
<p>Pralkę przewozimy w pozycji pionowej, zabezpieczoną kocem i przypiętą pasami do ściany auta. Po dojechaniu pamiętaj, aby wykręcić śruby transportowe przed pierwszym praniem.</p>
"""),
    D(slug="jak-przewiezc-telewizor", icon="tv", cat="RTV", read="3 min",
      title="Jak bezpiecznie przewieźć telewizor?",
      excerpt="Płaski ekran łatwo pęka pod naciskiem. Podpowiadamy, jak zapakować telewizor bez oryginalnego pudełka.",
      body="""
<p>Nowoczesne telewizory są cienkie i lekkie, ale matryca jest bardzo delikatna. Wystarczy mocniejszy nacisk w jednym punkcie, żeby ekran pękł.</p>
<h2>Oryginalne pudełko</h2>
<p>Najlepiej przewozić telewizor w fabrycznym kartonie ze styropianowymi wkładkami. Jeśli go nie masz — nic straconego.</p>
<h2>Pakowanie bez pudełka</h2>
<ul><li>Odkręć podstawę lub uchwyt ścienny, śruby włóż do woreczka i przyklej do obudowy.</li><li>Ekran przykryj miękkim kocem lub kartonem.</li><li>Owiń całość folią bąbelkową, a na koniec folią stretch.</li><li>Nie przyklejaj taśmy bezpośrednio do ekranu.</li></ul>
<div class="tip"><b>Zasada:</b> telewizor zawsze przewozimy pionowo, nigdy na płasko — leżący ekran może pęknąć pod własnym ciężarem.</div>
<h2>Kable</h2>
<p>Zrób zdjęcie podłączeń z tyłu telewizora, zanim wszystko odłączysz. Kable zwiń i spakuj w jednym, opisanym woreczku.</p>
"""),
    D(slug="jak-przewiezc-pianino", icon="piano", cat="Transport specjalny", read="4 min",
      title="Jak przygotować pianino do transportu?",
      excerpt="Dlaczego pianina nie warto przenosić samemu, ile osób potrzeba i kiedy nastroić instrument po przeprowadzce.",
      body="""
<p>Pianino waży zwykle 200–300 kg, a jego środek ciężkości jest wysoko. Przenoszenie bez sprzętu i doświadczenia to ryzyko dla instrumentu, klatki schodowej — i dla zdrowia.</p>
<h2>Czego potrzeba</h2>
<ul><li>3–4 osób, zależnie od wagi i schodów.</li><li>Pasów nośnych i wózka transportowego.</li><li>Pokrowca lub grubych koców.</li><li>Auta z możliwością mocowania ładunku.</li></ul>
<h2>Jak przygotować instrument</h2>
<ul><li>Zamknij i zabezpiecz klapę klawiatury.</li><li>Zdejmij z pianina nuty, lampki i dekoracje.</li><li>Zmierz szerokość drzwi i przejść w obu mieszkaniach.</li><li>Sprawdź, czy na klatce nie ma przeszkód.</li></ul>
<div class="tip"><b>Wskazówka:</b> do wyceny przygotuj markę i model pianina, piętra oraz informację o windzie — wtedy podamy dokładną cenę od razu.</div>
<h2>Po transporcie</h2>
<p>Instrument musi przyzwyczaić się do nowych warunków. Ustaw go z dala od grzejnika i okna, a stroiciela wezwij po 2–3 tygodniach.</p>
"""),
]
