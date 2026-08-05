"""
OCR Quality Agent
-----------------
Evaluates OCR results and assigns a quality score.
"""

import re


class OCRQualityAgent:

    def evaluate(self, text: str, confidence: float) -> float:
        """
        Returns a quality score between 0 and 1.
        """

        text = text.strip()

        if not text:
            return 0.0

        # Number of characters
        char_score = min(len(text) / 100, 1.0)

        # Number of words
        words = re.findall(r"\b[A-Za-z]+\b", text)
        word_score = min(len(words) / 20, 1.0)

        # Alphabet ratio
        letters = sum(c.isalpha() for c in text)

        alphabet_ratio = (
            letters / len(text)
            if len(text)
            else 0
        )

        # Final weighted score
        score = (
            0.4 * confidence +
            0.3 * char_score +
            0.2 * word_score +
            0.1 * alphabet_ratio
        )

        return round(score, 3)