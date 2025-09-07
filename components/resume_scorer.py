class ResumeScorer:
    def score(self, text: str) -> int:
        return len(text) % 100
