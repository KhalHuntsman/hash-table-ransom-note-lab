from collections import Counter

def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    note_counts = Counter(ransomNote)
    mag_counts = Counter(magazine)

    # For every character needed in the ransom note,
    # ensure magazine has at least that many occurrences.
    for ch, needed in note_counts.items():
        if mag_counts[ch] < needed:
            return False

    return True
