# Task 1 — Code Completion Analysis (200 words)

Manual implementation (manual_sort.py) is concise and efficient: it uses Python's built-in sorted() with a lambda, and performs best when the dataset is consistent (every dictionary has the same key). It has the smallest runtime overhead.

The AI-suggested implementation (copilot_sort.py) is more defensive: it uses dict.get() to handle missing keys and wraps sorting in a try/except to avoid runtime crashes on malformed data. This makes it safer in real-world datasets which may contain missing fields, but adds minimal overhead.

Efficiency: In clean data, the manual version is slightly faster. Robustness: the AI version is better because it avoids KeyError and gracefully returns a result even when data is messy. For production, the AI version is often preferred because safety and fault tolerance outweigh the tiny performance cost.

Conclusion: Use manual version for controlled tasks and prototypes; use defensive AI-suggested patterns or add guard clauses for production-grade code.
