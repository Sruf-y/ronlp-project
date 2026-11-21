"""Preprocessing helpers for LaRoSeDa and RONEC."""

def to_binary(rating: int) -> int:
    """LaRoSeDa starRating -> binary sentiment.
    1-2 stars -> 0 (negative), 4-5 stars -> 1 (positive).
    No 3-star reviews exist in LaRoSeDa."""
    if rating <= 2: return 0
    if rating >= 4: return 1
    raise ValueError(f"Unexpected starRating: {rating}")


def combine_text(title: str, content: str, max_chars: int = 1500) -> str:
    """Concatenate title + content for LaRoSeDa, truncating for TF-IDF sanity."""
    text = f"{title.strip()} {content.strip()}"
    return text[:max_chars]
