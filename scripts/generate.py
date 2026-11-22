"""Builds assets/hero.svg and assets/merged.svg from live GitHub data (falls back to data.json)."""
import json, math, os, urllib.request
from html import escape

USER = "alphasafal"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
SANS = "'Segoe UI',Inter,Helvetica,Arial,sans-serif"
PRETTY = {"microsoft": "Microsoft", "NVIDIA": "NVIDIA", "apple": "Apple", "aws-powertools": "AWS",
          "huggingface": "Hugging Face", "getsentry": "Sentry", "stanfordnlp": "Stanford NLP"}
GRAD = '<stop offset="0" stop-color="#22d3ee"/><stop offset=".5" stop-color="#a78bfa"/><stop offset="1" stop-color="#f472b6"/>'


def gh(path):
    req = urllib.request.Request("https://api.github.com/" + path,
                                 headers={"Authorization": "Bearer " + os.environ["GITHUB_TOKEN"]})
    return json.load(urllib.request.urlopen(req))


def load():
    if not os.environ.get("GITHUB_TOKEN"):
        return json.load(open("data.json"))
    items = gh(f"search/issues?per_page=100&q=is:pr+author:{USER}+is:merged+-user:{USER}")["items"]
    stars, rows = {}, []
    for i in items:
        repo = i["repository_url"].split("/repos/")[1]
        stars.setdefault(repo, gh("repos/" + repo)["stargazers_count"])
        rows.append([repo, i["number"], i["title"], stars[repo]])
    return rows


def k(n):
    return f"{n/1000:.1f}k".replace(".0k", "k") if n >= 1000 else str(n)


rows = [r for r in load() if "/awesome-" not in r[0]]  # list entries aren't code
repos = {}
for repo, num, _, st in rows:
    repos.setdefault(repo, {"stars": st, "prs": []})["prs"].append(num)
ranked = sorted(repos.items(), key=lambda x: -x[1]["stars"])
total = sum(v["stars"] for v in repos.values())
owners = list(dict.fromkeys(r.split("/")[0] for r, _ in ranked))
planets = [PRETTY[o] for o in PRETTY if o in owners][:6] or owners[:6]

# ---------- hero ----------
CX, CY, RX, RY, DUR = 945, 214, 182, 86, 26
orbit = f"M{CX-RX},{CY}a{RX},{RY} 0 1,1 {2*RX},0a{RX},{RY} 0 1,1 {-2*RX},0"
pills = []
for i, name in enumerate(planets):
    w = len(name) * 8 + 30
    b = -DUR * i / len(planets)
    sync = f'dur="{DUR}s" begin="{b:.2f}s" repeatCount="indefinite" keyTimes="0;.25;.5;.75;1"'
    pills.append(f'''<g><animateMotion path="{orbit}" dur="{DUR}s" begin="{b:.2f}s" repeatCount="indefinite"/>
<g><animateTransform attributeName="transform" type="scale" values=".9;.72;.9;1.12;.9" {sync}/>
<animate attributeName="opacity" values=".75;.35;.75;1;.75" {sync}/>
<rect x="{-w/2}" y="-14" width="{w}" height="28" rx="14" fill="#0b1020" stroke="url(#g)" stroke-width="1.2"/>
<circle cx="{-w/2+14}" cy="0" r="3.5" fill="#22d3ee"/>
<text x="{-w/2+24}" y="4.5" font-family="{SANS}" font-size="13" font-weight="600" fill="#e6edf3">{escape(name)}</text></g></g>''')


def line(y, i, prompt, out):
    d = 1.0 + i * 1.2
    return f'''<clipPath id="c{i}"><rect x="84" y="{y-17}" height="46" width="0"><animate attributeName="width" from="0" to="560" begin="{d}s" dur="1s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".4 0 .2 1"/></rect></clipPath>
<g clip-path="url(#c{i})" font-family="{MONO}" font-size="14.5"><text x="84" y="{y}"><tspan fill="#22d3ee">❯</tspan><tspan fill="#e6edf3"> {escape(prompt)}</tspan></text>
<text x="84" y="{y+22}" fill="#94a3b8">{out}</text></g>'''


def chip(x, val, label):
    w = len(val) * 11 + len(label) * 7.4 + 34
    return w, f'''<g transform="translate({x} 214)"><rect width="{w:.0f}" height="34" rx="17" fill="#ffffff" fill-opacity=".04" stroke="#ffffff" stroke-opacity=".1"/>
<text x="16" y="22.5" font-family="{SANS}" font-size="15"><tspan font-weight="800" fill="url(#g)">{val}</tspan><tspan fill="#94a3b8"> {label}</tspan></text></g>'''


chips, x = [], 60
for val, label in [(str(len(rows)), "PRs merged"), (str(len(repos)), "upstream repos"), (k(total) + "★", "combined")]:
    w, s = chip(x, val, label)
    chips.append(s)
    x += w + 10

hero = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 440" width="100%">
<defs>
<linearGradient id="g" x1="0" x2="1" spreadMethod="reflect">{GRAD}<animateTransform attributeName="gradientTransform" type="translate" values="-.5 0;.5 0;-.5 0" dur="10s" repeatCount="indefinite"/></linearGradient>
<linearGradient id="shine" x1="0" x2="1"><stop offset=".4" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".85"/><stop offset=".6" stop-color="#fff" stop-opacity="0"/></linearGradient>
<radialGradient id="sphere" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#c4b5fd"/><stop offset=".45" stop-color="#6d28d9"/><stop offset="1" stop-color="#0b1020"/></radialGradient>
<radialGradient id="halo"><stop offset=".3" stop-color="#a78bfa" stop-opacity=".5"/><stop offset="1" stop-color="#a78bfa" stop-opacity="0"/></radialGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="70"/></filter>
<filter id="soft" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="14"/></filter>
<pattern id="dots" width="26" height="26" patternUnits="userSpaceOnUse"><circle cx="1" cy="1" r="1" fill="#fff" fill-opacity=".07"/></pattern>
<clipPath id="card"><rect width="1200" height="440" rx="22"/></clipPath>
<clipPath id="name"><text x="56" y="150" font-family="{SANS}" font-size="84" font-weight="800" letter-spacing="-3">Safal Gupta</text></clipPath>
</defs>
<g clip-path="url(#card)">
<rect width="1200" height="440" fill="#04060c"/>
<circle cx="250" cy="60" r="190" fill="#0891b2" opacity=".35" filter="url(#blur)"><animateTransform attributeName="transform" type="translate" values="0 0;140 60;0 0" dur="16s" repeatCount="indefinite"/></circle>
<circle cx="900" cy="380" r="220" fill="#7c3aed" opacity=".38" filter="url(#blur)"><animateTransform attributeName="transform" type="translate" values="0 0;-160 -70;0 0" dur="20s" repeatCount="indefinite"/></circle>
<circle cx="1120" cy="40" r="150" fill="#db2777" opacity=".22" filter="url(#blur)"><animateTransform attributeName="transform" type="translate" values="0 0;-80 90;0 0" dur="14s" repeatCount="indefinite"/></circle>
<rect width="1200" height="440" fill="url(#dots)"/>
<rect x=".5" y=".5" width="1199" height="439" rx="22" fill="none" stroke="url(#g)" stroke-opacity=".45"/>

<g transform="translate(60 52)"><rect width="214" height="26" rx="13" fill="#22d3ee" fill-opacity=".08" stroke="#22d3ee" stroke-opacity=".35"/>
<circle cx="16" cy="13" r="4" fill="#22c55e"><animate attributeName="opacity" values="1;.25;1" dur="2s" repeatCount="indefinite"/></circle>
<text x="28" y="17.5" font-family="{MONO}" font-size="12" fill="#a5f3fc">final-year CS · VIT Vellore</text></g>
<text x="56" y="150" font-family="{SANS}" font-size="84" font-weight="800" letter-spacing="-3" fill="url(#g)" opacity=".55" filter="url(#soft)">Safal Gupta</text>
<text x="56" y="150" font-family="{SANS}" font-size="84" font-weight="800" letter-spacing="-3" fill="url(#g)">Safal Gupta</text>
<g clip-path="url(#name)"><rect y="60" width="300" height="110" fill="url(#shine)" opacity=".5"><animate attributeName="x" values="-300;700;700" keyTimes="0;.35;1" dur="6s" begin="1.5s" repeatCount="indefinite"/></rect></g>
<text x="60" y="190" font-family="{SANS}" font-size="20" fill="#cbd5e1">I find bugs in software the world runs on, and get the fix merged.</text>
{"".join(chips)}
<rect x="60" y="270" width="600" height="138" rx="14" fill="#0b1020" fill-opacity=".85" stroke="#ffffff" stroke-opacity=".1"/>
<circle cx="82" cy="290" r="5" fill="#ff5f56"/><circle cx="98" cy="290" r="5" fill="#ffbd2e"/><circle cx="114" cy="290" r="5" fill="#27c93f"/>
<text x="636" y="294" text-anchor="end" font-family="{MONO}" font-size="11" fill="#475569">zsh · ~/{USER}</text>
{line(326, 0, "cat focus.txt", "AI evals · dev tools · systems security · open source")}
{line(372, 1, "contri check <any-issue>", '<tspan fill="#4ade80">alive ✓  maintainers reply ✓  unclaimed ✓</tspan>  → ship it')}

<ellipse cx="{CX}" cy="{CY}" rx="{RX}" ry="{RY}" fill="none" stroke="url(#g)" stroke-opacity=".5" stroke-dasharray="3 7"/>
<ellipse cx="{CX}" cy="{CY}" rx="{RX+46}" ry="{RY+40}" fill="none" stroke="#ffffff" stroke-opacity=".06"/>
<circle cx="{CX}" cy="{CY}" r="120" fill="url(#halo)"><animate attributeName="r" values="105;130;105" dur="5s" repeatCount="indefinite"/></circle>
<circle cx="{CX}" cy="{CY}" r="54" fill="url(#sphere)"/>
<ellipse cx="{CX-14}" cy="{CY-22}" rx="18" ry="9" fill="#fff" opacity=".25"/>
<text x="{CX}" y="{CY+8}" text-anchor="middle" font-family="{SANS}" font-size="38" font-weight="800" fill="#fff">{len(rows)}</text>
<text x="{CX}" y="{CY+26}" text-anchor="middle" font-family="{MONO}" font-size="9" letter-spacing="2" fill="#ddd6fe">MERGED</text>
{"".join(pills)}
</g></svg>'''

# ---------- merged wall ----------
W, CW, CH, G, P, TOP, cols = 1200, 368, 112, 16, 24, 118, 3
H = TOP + math.ceil(len(ranked) / cols) * (CH + G) + 8
top_log = math.log10(max(v["stars"] for _, v in ranked) + 1)
cards = []
for i, (repo, v) in enumerate(ranked):
    x, y = P + (i % cols) * (CW + G), TOP + (i // cols) * (CH + G)
    owner, name = repo.split("/")
    bar = max(8, (CW - 44) * math.log10(v["stars"] + 1) / top_log)
    d = f"{i*.07:.2f}s"
    cards.append(f'''<g opacity="0" transform="translate({x} {y+16})">
<animateTransform attributeName="transform" type="translate" from="{x} {y+16}" to="{x} {y}" begin="{d}" dur=".7s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".2 .8 .2 1"/>
<animate attributeName="opacity" from="0" to="1" begin="{d}" dur=".7s" fill="freeze"/>
<rect width="{CW}" height="{CH}" rx="14" fill="#0b1020" stroke="{'url(#g)' if i < 3 else '#1e293b'}" stroke-width="{1.4 if i < 3 else 1}"/>
<g clip-path="url(#cc)"><rect width="{CW}" height="{CH}" fill="url(#shine)"><animate attributeName="x" values="-{CW};{CW};{CW}" keyTimes="0;.3;1" dur="8s" begin="{1.5+i*.18:.2f}s" repeatCount="indefinite"/></rect></g>
<circle cx="38" cy="40" r="18" fill="url(#g)" fill-opacity=".18" stroke="url(#g)"/>
<text x="38" y="46" text-anchor="middle" font-family="{SANS}" font-size="16" font-weight="800" fill="#e6edf3">{escape(owner[0].upper())}</text>
<text x="66" y="34" font-family="{MONO}" font-size="11.5" fill="#64748b">{escape(owner)}</text>
<text x="66" y="54" font-family="{SANS}" font-size="18" font-weight="700" fill="#f1f5f9">{escape(name[:24])}</text>
<text x="{CW-20}" y="34" text-anchor="end" font-family="{SANS}" font-size="14" font-weight="700" fill="#fbbf24">★ {k(v["stars"])}</text>
<rect x="22" y="72" width="{CW-44}" height="4" rx="2" fill="#1e293b"/>
<rect x="22" y="72" width="0" height="4" rx="2" fill="url(#g)"><animate attributeName="width" from="0" to="{bar:.0f}" begin="{.4+i*.07:.2f}s" dur="1.2s" fill="freeze" calcMode="spline" keyTimes="0;1" keySplines=".2 .8 .2 1"/></rect>
<text x="22" y="97" font-family="{MONO}" font-size="12"><tspan fill="#4ade80">✓ {len(v["prs"])} merged</tspan><tspan fill="#64748b">  {" ".join("#"+str(p) for p in sorted(v["prs"]))}</tspan></text>
</g>''')

n = len(ranked)
if n % cols:
    x, y = P + (n % cols) * (CW + G), TOP + (n // cols) * (CH + G)
    cards.append(f'''<g transform="translate({x} {y})"><rect width="{CW}" height="{CH}" rx="14" fill="none" stroke="#334155" stroke-dasharray="5 6"/>
<text x="{CW/2}" y="{CH/2+5}" text-anchor="middle" font-family="{MONO}" font-size="13" fill="#64748b">next PR loading<tspan>.<animate attributeName="opacity" values="0;1;1" dur="1.5s" repeatCount="indefinite"/></tspan><tspan>.<animate attributeName="opacity" values="0;0;1" dur="1.5s" repeatCount="indefinite"/></tspan></text></g>''')

merged = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="100%">
<defs><clipPath id="cc"><rect width="{CW}" height="{CH}" rx="14"/></clipPath>
<linearGradient id="g" x1="0" x2="1">{GRAD}</linearGradient>
<linearGradient id="shine" x1="0" x2="1"><stop offset=".35" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".06"/><stop offset=".65" stop-color="#fff" stop-opacity="0"/></linearGradient>
<filter id="blur" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="80"/></filter>
<clipPath id="card"><rect width="{W}" height="{H}" rx="22"/></clipPath></defs>
<g clip-path="url(#card)"><rect width="{W}" height="{H}" fill="#04060c"/>
<circle cx="1100" cy="0" r="200" fill="#7c3aed" opacity=".25" filter="url(#blur)"/>
<circle cx="80" cy="{H}" r="200" fill="#0891b2" opacity=".2" filter="url(#blur)"/></g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="22" fill="none" stroke="#ffffff" stroke-opacity=".08"/>
<text x="{P}" y="54" font-family="{SANS}" font-size="30" font-weight="800" fill="url(#g)" letter-spacing="-1">Merged upstream</text>
<text x="{P}" y="82" font-family="{MONO}" font-size="12.5" fill="#64748b">live from the GitHub API · refreshed daily · sorted by stars</text>
<text x="{W-P}" y="56" text-anchor="end" font-family="{SANS}" font-size="34" font-weight="800" fill="#f1f5f9">{k(total)}★</text>
<text x="{W-P}" y="80" text-anchor="end" font-family="{MONO}" font-size="12" fill="#64748b">{len(rows)} PRs · {len(repos)} repos</text>
{"".join(cards)}
</svg>'''

os.makedirs("assets", exist_ok=True)
open("assets/hero.svg", "w").write(hero)
open("assets/merged.svg", "w").write(merged)
print(len(rows), len(repos), total)
