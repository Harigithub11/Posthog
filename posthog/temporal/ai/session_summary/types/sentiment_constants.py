from typing import Literal

SENTIMENT_SIGNAL_TYPES = (
    "rage_click",
    "repeated_error",
    "backtracking",
    "long_pause",
    "abandonment",
    "dead_click",
    "confusion_loop",
    "error_cascade",
    "other",
)

SENTIMENT_OUTCOME_TYPES = ("successful", "friction", "frustrated", "blocked")

SentimentSignalType = Literal[
    "rage_click",
    "repeated_error",
    "backtracking",
    "long_pause",
    "abandonment",
    "dead_click",
    "confusion_loop",
    "error_cascade",
    "other",
]

SentimentOutcomeType = Literal["successful", "friction", "frustrated", "blocked"]
