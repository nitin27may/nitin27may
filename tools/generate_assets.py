"""Generate profile README graphics: banner, stats strip, architecture (light/dark)."""
import sys, pathlib
out = pathlib.Path(sys.argv[1])
FONT = "-apple-system,BlinkMacSystemFont,'Segoe UI','Noto Sans',Helvetica,Arial,sans-serif"
TEAL, GOLD = "#0d9488", "#D4AF37"

def svg(w, h, body, title):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
            f'font-family="{FONT}" role="img" aria-label="{title}"><title>{title}</title>{body}</svg>\n')

# ---------- banner (one version: a dark brand panel reads on both themes) ----------
def banner():
    nodes = [(905, 150), (1010, 70), (1010, 150), (1010, 230), (1115, 110), (1115, 190)]
    edges = [(0, 1), (0, 2), (0, 3), (1, 4), (2, 4), (2, 5), (3, 5)]
    g = ''.join(f'<line x1="{nodes[a][0]}" y1="{nodes[a][1]}" x2="{nodes[b][0]}" y2="{nodes[b][1]}" stroke="#2dd4bf" stroke-opacity=".45" stroke-width="2"/>' for a, b in edges)
    for i, (x, y) in enumerate(nodes):
        if i == 0:
            g += f'<circle cx="{x}" cy="{y}" r="17" fill="{GOLD}"/><circle cx="{x}" cy="{y}" r="27" fill="none" stroke="{GOLD}" stroke-opacity=".35" stroke-width="2"/>'
        else:
            g += f'<circle cx="{x}" cy="{y}" r="11" fill="#0b1220" stroke="#2dd4bf" stroke-width="2.5"/>'
    grid = ''.join(f'<line x1="{x}" y1="0" x2="{x}" y2="300" stroke="#94a3b8" stroke-opacity=".06"/>' for x in range(40, 1200, 40))
    grid += ''.join(f'<line x1="0" y1="{y}" x2="1200" y2="{y}" stroke="#94a3b8" stroke-opacity=".06"/>' for y in range(20, 300, 40))
    body = f'''<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#0b1220"/><stop offset="1" stop-color="#0f2a33"/></linearGradient>
<clipPath id="r"><rect width="1200" height="300" rx="18"/></clipPath></defs>
<g clip-path="url(#r)"><rect width="1200" height="300" fill="url(#bg)"/>{grid}<rect x="0" y="0" width="8" height="300" fill="{TEAL}"/></g>
<rect x=".5" y=".5" width="1199" height="299" rx="18" fill="none" stroke="#334155"/>
<text x="64" y="84" font-size="17" font-weight="700" fill="#5eead4" letter-spacing="3">NITIN SINGH  ·  SOLUTIONS ARCHITECT</text>
<text x="64" y="144" font-size="45" font-weight="800" fill="#f8fafc">Enterprise AI agent systems,</text>
<text x="64" y="198" font-size="45" font-weight="800" fill="#f8fafc">designed <tspan fill="{GOLD}">and shipped.</tspan></text>
<text x="64" y="246" font-size="21" fill="#cbd5e1">Keyless  ·  Zero trust  ·  Observable from the first commit</text>
{g}'''
    return svg(1200, 300, body, "Nitin Singh, Solutions Architect. Enterprise AI agent systems, designed and shipped. Keyless, zero trust, observable from the first commit.")

# ---------- theme palettes for transparent graphics ----------
P = {
 "light": dict(ink="#0f172a", mute="#475569", line="#94a3b8", panel="#f1f5f9", pstroke="#cbd5e1", num="#0f766e", rule="#e2e8f0"),
 "dark":  dict(ink="#f1f5f9", mute="#94a3b8", line="#64748b", panel="#161f2e", pstroke="#334155", num="#2dd4bf", rule="#263244"),
}

def stats(t):
    p = P[t]
    items = [("15+", "years building", "enterprise systems"), ("280+", "GitHub stars across", "open-source projects"),
             ("34", "chapters in the", "agent framework course"), ("90+", "articles on architecture", "and AI agents")]
    b = ""
    for i, (n, a, c) in enumerate(items):
        x = 300 * i
        if i: b += f'<line x1="{x}" y1="22" x2="{x}" y2="118" stroke="{p["rule"]}" stroke-width="2"/>'
        b += (f'<text x="{x+150}" y="62" text-anchor="middle" font-size="50" font-weight="800" fill="{p["num"]}">{n}</text>'
              f'<text x="{x+150}" y="94" text-anchor="middle" font-size="18" fill="{p["mute"]}">{a}</text>'
              f'<text x="{x+150}" y="117" text-anchor="middle" font-size="18" fill="{p["mute"]}">{c}</text>')
    return svg(1200, 140, b, "15+ years building enterprise systems. 280+ GitHub stars across open-source projects. A 34-chapter agent framework course. 90+ articles on architecture and AI agents.")

def arch(t):
    p = P[t]
    def box(x, y, w, h, fill, stroke, l1, l2=None, fs=20):
        s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
        cy = y + h / 2
        if l2:
            s += f'<text x="{x+w/2}" y="{cy-4}" text-anchor="middle" font-size="{fs}" font-weight="700" fill="#fff">{l1}</text>'
            s += f'<text x="{x+w/2}" y="{cy+19}" text-anchor="middle" font-size="15" fill="#fff" fill-opacity=".9">{l2}</text>'
        else:
            s += f'<text x="{x+w/2}" y="{cy+7}" text-anchor="middle" font-size="{fs}" font-weight="700" fill="#fff">{l1}</text>'
        return s
    def arrow(x1, y1, x2, y2, dash=False):
        d = ' stroke-dasharray="6 6"' if dash else ''
        return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{p["line"]}" stroke-width="2.5"{d} marker-end="url(#a)"/>'
    def label(x, y, s, anchor="middle"):
        return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="15" font-weight="600" fill="{p["mute"]}">{s}</text>'
    b = f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{p["line"]}"/></marker></defs>'
    cy = 215
    # identity band
    b += f'<path d="M190 52 V36 H1010 V52" fill="none" stroke="{TEAL}" stroke-width="2" stroke-dasharray="3 5"/>'
    b += f'<rect x="405" y="22" width="390" height="28" rx="14" fill="{TEAL}"/><text x="600" y="41" text-anchor="middle" font-size="15" font-weight="700" fill="#fff">Signed-in user identity on every hop</text>'
    # user
    b += f'<rect x="20" y="{cy-24}" width="100" height="48" rx="24" fill="none" stroke="{p["line"]}" stroke-width="2"/><text x="70" y="{cy+7}" text-anchor="middle" font-size="19" font-weight="700" fill="{p["ink"]}">User</text>'
    b += arrow(120, cy, 166, cy)
    b += box(170, cy-42, 210, 84, "#1d4ed8", "#93c5fd", "Storefront", "Next.js, streaming chat")
    b += arrow(380, cy, 456, cy) + label(418, cy-12, "JWT")
    b += box(460, cy-42, 230, 84, TEAL, "#5eead4", "Orchestrator", "5 orchestration modes")
    b += arrow(690, cy, 786, cy) + label(738, cy-12, "A2A")
    # agents panel
    b += f'<rect x="790" y="62" width="220" height="306" rx="14" fill="{p["panel"]}" stroke="{p["pstroke"]}" stroke-width="2"/>'
    b += f'<text x="900" y="90" text-anchor="middle" font-size="14" font-weight="700" letter-spacing="1.5" fill="{p["mute"]}">SPECIALIST AGENTS</text>'
    for i, n in enumerate(["Product search", "Orders", "Pricing", "Reviews", "Inventory"]):
        b += box(810, 104 + i*51, 180, 41, "#1d4ed8", "#93c5fd", n, fs=17)
    b += arrow(1010, cy, 1066, cy)
    # database
    b += (f'<path d="M1070 {cy-38} v76 a52 15 0 0 0 104 0 v-76" fill="#475569" stroke="#94a3b8" stroke-width="2"/>'
          f'<ellipse cx="1122" cy="{cy-38}" rx="52" ry="15" fill="#475569" stroke="#94a3b8" stroke-width="2"/>'
          f'<text x="1122" y="{cy+6}" text-anchor="middle" font-size="16" font-weight="700" fill="#fff">PostgreSQL</text>'
          f'<text x="1122" y="{cy+26}" text-anchor="middle" font-size="14" fill="#fff" fill-opacity=".9">pgvector</text>')
    # approval + telemetry
    b += arrow(520, cy+42, 520, 316) + label(510, 294, "policy-routed", "end")
    b += box(430, 320, 180, 46, "#15803d", "#4ade80", "Human approval", fs=17)
    b += arrow(672, cy+42, 672, 316, dash=True) + label(682, 294, "traces, cost", "start")
    b += box(622, 320, 160, 46, "#475569", "#94a3b8", "OpenTelemetry", fs=17)
    return svg(1200, 390, b, "Architecture of e-commerce-agents: a user reaches a Next.js storefront, which calls an orchestrator with a JWT. The orchestrator calls five specialist agents over A2A (product search, orders, pricing, reviews, inventory), backed by PostgreSQL with pgvector. Risky actions route to human approval, and traces and cost go to OpenTelemetry. The signed-in user's identity is carried on every hop.")

(out / "banner.svg").write_text(banner())
for t in P:
    (out / f"stats-{t}.svg").write_text(stats(t))
    (out / f"architecture-{t}.svg").write_text(arch(t))
