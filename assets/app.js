(() => {
  const SITE = window.SITE || {};
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const waUrl = t => "https://wa.me/" + SITE.whatsapp + (t ? "?text=" + encodeURIComponent(t) : "");

  $$("[data-wa]").forEach(a => a.href = waUrl(a.dataset.wa));

  const header = $("header");
  addEventListener("scroll", () => header.classList.toggle("scrolled", scrollY > 10), { passive: true });

  // mobile menu
  const burger = $(".burger"), mm = $(".mobile-menu");
  burger.addEventListener("click", () => {
    const open = mm.classList.toggle("open");
    burger.setAttribute("aria-expanded", open);
    document.body.style.overflow = open ? "hidden" : "";
  });
  mm.addEventListener("click", e => {
    if (!e.target.closest("a")) return;
    mm.classList.remove("open");
    burger.setAttribute("aria-expanded", false);
    document.body.style.overflow = "";
  });

  // services dropdown (click for touch / keyboard)
  const dd = $(".dd"), ddBtn = $(".dd-btn");
  ddBtn.addEventListener("click", () => ddBtn.setAttribute("aria-expanded", dd.classList.toggle("open")));
  document.addEventListener("click", e => { if (!dd.contains(e.target)) { dd.classList.remove("open"); ddBtn.setAttribute("aria-expanded", false); } });
  document.addEventListener("keydown", e => { if (e.key === "Escape") { dd.classList.remove("open"); ddBtn.setAttribute("aria-expanded", false); } });

  async function sendLead(data) {
    if (!SITE.formEndpoint) return;
    try {
      await fetch(SITE.formEndpoint, { method: "POST", headers: { "Content-Type": "application/json", Accept: "application/json" }, body: JSON.stringify(data) });
    } catch (e) {}
  }
  const phoneOk = v => v.replace(/\D/g, "").length >= 9;
  const escapeHtml = s => s.replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));

  // calculator
  const cPlan = $("#c-plan");
  if (cPlan) {
    const cH = $("#c-h"), cB = $("#c-box");
    const calc = () => {
      const h = +cH.value, b = +cB.value;
      $("#c-hv").textContent = h + " godz.";
      $("#c-bv").textContent = b + " szt.";
      $("#c-out").textContent = Math.round(+cPlan.value * h + b * 10).toLocaleString("pl-PL") + " zł";
    };
    [cPlan, cH, cB].forEach(e => e.addEventListener("input", calc));
    calc();
  }

  // quick forms
  $$(".js-quick").forEach(f => f.addEventListener("submit", e => {
    e.preventDefault();
    const phone = f.phone.value.trim();
    if (!phoneOk(phone)) { f.phone.classList.add("invalid"); f.phone.focus(); return; }
    const msg = `Prośba o oddzwonienie\nImię: ${f.name.value || "-"}\nTelefon: ${phone}\nUsługa: ${f.service.value}\nStrona: ${document.title}`;
    sendLead({ typ: "oddzwonienie", imie: f.name.value, telefon: phone, usluga: f.service.value, strona: location.href });
    f.classList.add("done");
    f.innerHTML = `<h3>Dziękujemy!</h3><p>Oddzwonimy na numer <b style="color:#fff">${escapeHtml(phone)}</b> w ciągu kilku minut.</p>` +
      (SITE.formEndpoint ? "" : `<a class="btn btn-accent" target="_blank" rel="noopener" href="${waUrl(msg)}">Potwierdź na WhatsApp</a>`);
  }));

  // order form
  const form = $("#orderForm");
  if (!form) return;
  const steps = $$(".fstep", form), bars = $$(".stepper div", form);
  const prev = $("#prev"), next = $("#next"), err = $("#err");
  let cur = 0;
  $("#o-date").min = new Date().toISOString().slice(0, 10);

  const pick = (name, value) => {
    const r = $$(`input[name=${name}]`, form).find(i => i.value === value);
    if (r) r.checked = true;
  };
  const params = new URLSearchParams(location.search);
  if (params.get("usluga")) pick("usluga", params.get("usluga"));
  if (params.get("pakiet")) pick("pakiet", params.get("pakiet"));
  $$("[data-plan]").forEach(a => a.addEventListener("click", () => { if (a.getAttribute("href") === "#zamow") pick("pakiet", a.dataset.plan); }));

  function show(i) {
    steps.forEach((s, k) => s.classList.toggle("on", k === i));
    bars.forEach((b, k) => b.classList.toggle("on", k <= i));
    prev.hidden = !(i > 0 && i < 3);
    next.textContent = i === 2 ? "Wyślij zamówienie" : "Dalej →";
    $("#fnav").hidden = i === 3;
    err.textContent = "";
    cur = i;
  }
  function valid(i) {
    const bad = $$("[required]", steps[i]).find(el => el.type === "checkbox" ? !el.checked : !el.value.trim());
    if (bad) {
      err.textContent = bad.type === "checkbox" ? "Zaznacz zgodę, aby wysłać zamówienie." : "Uzupełnij wymagane pola (*).";
      bad.focus();
      return false;
    }
    if (i === 2 && !phoneOk(form.telefon.value)) { err.textContent = "Podaj poprawny numer telefonu."; form.telefon.focus(); return false; }
    return true;
  }
  prev.onclick = () => show(cur - 1);
  next.onclick = () => {
    if (!valid(cur)) return;
    if (cur < 2) return show(cur + 1);
    const fd = new FormData(form);
    const d = Object.fromEntries(fd);
    d.extra = fd.getAll("extra").join(", ") || "-";
    const txt =
`NOWE ZAMÓWIENIE
Usługa: ${d.usluga} (pakiet: ${d.pakiet})
Dodatkowo: ${d.extra}
Skąd: ${d.skad}, piętro ${d.pietro_skad || 0}, ${d.winda_skad}
Dokąd: ${d.dokad}, piętro ${d.pietro_dokad || 0}, ${d.winda_dokad}
Termin: ${d.data}, ${d.godzina}
Klient: ${d.imie}, ${d.telefon}${d.email ? ", " + d.email : ""}
Uwagi: ${d.uwagi || "-"}`;
    sendLead(d);
    $("#summary").textContent = txt;
    const wa = $("#sendWa");
    wa.href = waUrl(txt);
    wa.hidden = !!SITE.formEndpoint;
    show(3);
    form.scrollIntoView({ behavior: "smooth", block: "start" });
  };
})();
