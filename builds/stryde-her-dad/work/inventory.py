import json
r = json.load(open("work/lines.json"))
claims = {"L035": "held (17×) · **F3** (size of a coin) · **F4** (pressure, nothing more)", "L037": "**F4** comparative", "L038": "**F4** comparative",
          "L040": "protection ✓ · held (3 yrs, orthopaedic surgeons) · **F3** (two centimetres)", "L041": "**F5** Amazon · **F4** (stretches → doesn't work)",
          "L043": "**F4** outcome (\"you'll know in a minute\")", "L058": "**F4** (\"It's not your age\")", "L059": "held (17×)",
          "L060": "name · hidden under trousers ✓ (wear guide 6)", "L061": "held (BOGOF, 60 days) · **F5** knock-offs on Amazon"}
vn = {"L001": "VN06", "L002": "VN06", "L003": "VN07", "L004": "VN07", "L006": "VN08", "L016": "VN09", "L017": "VN09", "L025": "VN09",
      "L023": "VN10", "L032": "VN11", "L033": "VN11", "L044": "VN12", "L048": "VN13", "L049": "VN13", "L050": "VN13", "L052": "VN14",
      "L053": "VN14", "L054": "VN15", "L056": "VN15", "L057": "VN16 · VN17", "L058": "VN18", "L061": "VN18"}
out = ["| ID | Act · scene | Speaker | Line (verbatim) | Disp. | Claim | Visual note |", "|---|---|---|---|---|---|---|"]
for x in r:
    spk = x["speaker"] + (f" ({x['note']})" if x["note"] else "")
    out.append(f"| {x['id']} | {x['act']} · {x['scene']} | {spk} | {x['line']} | {x['disp']} | {claims.get(x['id'], '—')} | {vn.get(x['id'], '')} |")
open("work/inventory.md", "w").write("\n".join(out) + "\n")
print(len(r))
