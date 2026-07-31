#!/usr/bin/env python3
"""Generate a matched FAQ block — visible HTML + FAQPage JSON-LD from ONE source.

The recurring gotcha on this site: Google drops the FAQ rich result unless the
FAQPage JSON-LD text EXACTLY matches the visible FAQ text (after tag-strip +
entity-decode). Hand-editing the two separately drifts. This tool emits both from a
single list of Q&A pairs, so they can't disagree — paste each block into the page,
then confirm with `python3 tools/qa_check.py`.

Usage:
  python3 tools/faq_gen.py faqs.json          # a JSON array of {"q":..., "a":...}
  echo '[{"q":"...","a":"..."}]' | python3 tools/faq_gen.py -

Rules baked in (match the house style + mgsf-core claim rules):
  - Visible uses &amp; / &lt; / &gt; ; JSON-LD uses raw & (so both decode equal).
  - Answers should already be claim-safe (no fabricated numbers, no guaranteed
    savings, no mold-elimination) — this tool formats, it does not invent.

Dependency-free. Output is two blocks: the <div class="faq"> visible section and the
<script type="application/ld+json"> FAQPage block.
"""
import json
import sys


def esc_html(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    src = sys.argv[1]
    raw = sys.stdin.read() if src == "-" else open(src, encoding="utf-8").read()
    try:
        pairs = json.loads(raw)
    except Exception as e:
        print("ERROR: input must be JSON array of {q,a}: %s" % e, file=sys.stderr)
        return 2
    pairs = [p for p in pairs if p.get("q") and p.get("a")]
    if not pairs:
        print("ERROR: no valid {q,a} pairs", file=sys.stderr)
        return 2

    # visible block
    vis = ['  <div class="sec-head center"><span class="eyebrow">Questions</span><h2>FAQ</h2></div>',
           '  <div class="faq">']
    for p in pairs:
        vis.append('    <details><summary>%s</summary><p>%s</p></details>'
                   % (esc_html(p["q"].strip()), esc_html(p["a"].strip())))
    vis.append('  </div>')

    # JSON-LD block (raw & — decodes equal to the &amp; visible)
    entities = [{
        "@type": "Question",
        "name": p["q"].strip(),
        "acceptedAnswer": {"@type": "Answer", "text": p["a"].strip()},
    } for p in pairs]
    ld = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": entities}
    ld_str = json.dumps(ld, ensure_ascii=False, indent=2)

    print("<!-- ===== paste into the page body (inside a <section>) ===== -->")
    print("\n".join(vis))
    print("\n<!-- ===== paste into <head> ===== -->")
    print('<script type="application/ld+json">')
    print(ld_str)
    print("</script>")
    print("\n# %d Q&A pairs. After pasting, run: python3 tools/qa_check.py" % len(pairs), file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
