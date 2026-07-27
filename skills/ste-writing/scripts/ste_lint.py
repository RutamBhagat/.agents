import glob
import json
import os
import re
import sys

MARKETING = [
    "seamless", "seamlessly", "robust", "powerful", "cutting-edge", "effortless",
    "effortlessly", "world-class", "next-generation", "revolutionary", "blazing",
    "lightning-fast", "elegant", "delightful", "turnkey", "best-in-class",
    "state-of-the-art", "game-changing", "first-class", "battle-tested",
    "enterprise-grade", "supercharge", "unlock", "unleash", "empower", "empowers",
]
BANNED = [
    "begin", "begins", "commence", "commences", "initiate", "initiates", "originate",
    "utilize", "utilizes", "utilizing", "leverage", "leverages", "leveraging",
    "facilitate", "facilitates", "ensure", "ensures", "ensuring", "prior to",
    "subsequent to", "obtain", "obtains", "acquire", "acquires", "demonstrate",
    "demonstrates", "additionally", "furthermore", "moreover", "comprehensive",
    "comprehensively", "utilization", "aforementioned", "henceforth", "therein",
    "whilst", "amongst", "numerous", "myriad", "plethora", "in order to",
    "a variety of", "in the event that", "due to the fact that",
    "it is important to note",
]
PHRASAL = [
    "spin up", "spin down", "reach out", "dive into", "dives into", "diving into",
    "kick off", "kicks off", "roll out", "rolls out", "tear down", "ramp up",
    "circle back", "drill down", "spun up", "reaching out",
]
MODAL_HEDGE = [
    "it is important to note", "it should be noted", "it is worth noting",
    "please note that", "as mentioned", "as noted above",
]
BE = r"(?:am|is|are|was|were|be|been|being)"
IRREGULAR_PARTICIPLES = (
    r"(?:done|made|sent|read|built|kept|held|set|put|run|written|shown|given|"
    r"taken|found|got|gotten|seen|known|thrown|drawn)"
)


def strip_code(text):
    text = re.sub(r"```.*?```", " ", text, flags=re.S)
    return re.sub(r"`[^`]*`", " ", text)


def get_sentences(text):
    sentences = []
    for line in text.splitlines():
        line = re.sub(r"^\s*#{1,6}\s*", "", line.strip())
        line = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", line)
        if not line:
            continue
        parts = re.split(r"(?<=[.!?:])\s+(?=[A-Z0-9\"'\-])", line)
        sentences.extend(part.strip() for part in parts if part.strip())
    return sentences


def count_words(text):
    return len(re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-/]*", text))


def count_phrases(options):
    hits = []
    text = options["text"].lower()
    for phrase in options["phrases"]:
        pattern = rf"(?<![a-z]){re.escape(phrase)}(?![a-z])"
        hits.extend(phrase for _ in re.finditer(pattern, text))
    return len(hits), hits


def lint(text):
    raw = text
    text = strip_code(text)
    sentences = get_sentences(text)
    words = sum(count_words(sentence) for sentence in sentences) or 1
    long_sentences = [
        (count_words(sentence), sentence)
        for sentence in sentences
        if count_words(sentence) > 20
    ]
    banned_count, banned_hits = count_phrases({"text": text, "phrases": BANNED})
    marketing_count, marketing_hits = count_phrases(
        {"text": text, "phrases": MARKETING}
    )
    violations = {
        "long_sentence(>20w)": len(long_sentences),
        "semicolon": text.count(";"),
        "contraction": len(re.findall(r"\b\w+['’](?:t|re|ve|ll|d|s|m)\b", text)),
        "passive_voice": len(
            re.findall(rf"\b{BE}\s+(?:\w+ed|{IRREGULAR_PARTICIPLES})\b", text, re.I)
        ),
        "ing_main_verb": len(re.findall(rf"\b{BE}\s+\w+ing\b", text, re.I)),
        "nominalization": len(
            re.findall(
                r"\b(?:perform(?:s|ed)?|conduct(?:s|ed)?|provide(?:s|d)?|"
                r"carry out|carries out|make use of|makes use of)\b",
                text,
                re.I,
            )
        )
        + len(re.findall(r"\b\w{4,}(?:tion|ment|ance|ence)\s+of\b", text, re.I)),
        "phrasal_verb": count_phrases({"text": text, "phrases": PHRASAL})[0],
        "banned_word": banned_count,
        "marketing_adjective": marketing_count,
        "modal_hedge": count_phrases({"text": text, "phrases": MODAL_HEDGE})[0],
        "long_paragraph(>6s)": sum(
            len(get_sentences(strip_code(paragraph))) > 6
            for paragraph in re.split(r"\n\s*\n", raw)
            if paragraph.strip()
        ),
    }
    total = sum(violations.values())
    longest = max((count_words(sentence) for sentence in sentences), default=0)
    return {
        "words": words,
        "sentences": len(sentences),
        "violations": violations,
        "total": total,
        "total_per100w": round(total * 100.0 / words, 2),
        "em_dash(slop-marker)": raw.count("—") + raw.count("–"),
        "longest_sentence_words": longest,
        "sample_marketing": list(dict.fromkeys(marketing_hits))[:6],
        "sample_banned": list(dict.fromkeys(banned_hits))[:6],
    }


def main():
    if not sys.argv[1:]:
        print(json.dumps(lint(sys.stdin.read()), indent=2))
        return

    paths = []
    for path in sys.argv[1:]:
        paths.extend(sorted(glob.glob(path)) if glob.has_magic(path) else [path])

    for path in paths:
        with open(path, encoding="utf-8") as file:
            result = lint(file.read())
        print(
            f"{os.path.basename(path):32} words={result['words']:4d} "
            f"total={result['total']:3d} per100w={result['total_per100w']:6.2f} "
            f"em_dash={result['em_dash(slop-marker)']:2d}"
        )


if __name__ == "__main__":
    main()
