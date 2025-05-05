import re

SLANG_WORDS = {
    "yo", "bro", "lowkey", "aight", "for real", "dope", "sheesh", "bruh", "no cap", "dude", "man", "fr", "nah", "fam"
}

BAR_WORDS = {
    "beer", "ipa", "whiskey", "cocktail", "drink", "shots", "bartender", "booth", "menu", "bar", "cheers", "wings"
}


def normalize_text(text: str) -> list[str]:
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    return words


def slang_score(text: str) -> float:
    words = normalize_text(text)
    if not words:
        return 0.0
    slang_count = sum(1 for word in words if word in SLANG_WORDS)
    return slang_count / len(words)


def bar_focus_score(text: str) -> float:
    words = normalize_text(text)
    if not words:
        return 0.0
    bar_count = sum(1 for word in words if word in BAR_WORDS)
    return bar_count / len(words)


def has_slang(text: str) -> bool:
    words = normalize_text(text)
    return any(word in SLANG_WORDS for word in words)


def has_bar_reference(text: str) -> bool:
    words = normalize_text(text)
    return any(word in BAR_WORDS for word in words)


if __name__ == "__main__":
    responses = [
        "Yo bro! Whiskey sour hits diff today.",
        "That's wild, man. Haven’t seen you since uni.",
        "Aight, let's grab some wings and chill.",
        "I’m thinking of ordering a cocktail. You in?",
        "What’s good, my guy? For real, missed this vibe!",
        "This place got no soul, fam. Where the wings at?",
    ]

    print(f"{'Response':<60} | Slang | Bar")
    print("-" * 85)
    for r in responses:
        slang = slang_score(r)
        bar = bar_focus_score(r)
        print(f"{r[:55]:<60} |  {slang:.2f}  |  {bar:.2f}")
