def humanize_bool(value: bool, true_word: str = "yes", false_word: str = "no") -> str:
    """Render a bool as a friendlier word than 'True'/'False' for CLI output."""
    return true_word if value else false_word


def pluralize(count: int, singular: str, plural: str | None = None) -> str:
    """Return the correctly-pluralized noun for a given count."""
    if count == 1:
        return f"{count} {singular}"
    return f"{count} {plural or singular + 's'}"