class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def _starts_ends_with_vowel(word: str) -> bool:
            vowels = 'aeiou'
            if ((word[0] in vowels) and (word[-1] in vowels)):
                return True
            return False

        out = []

        for query in queries:
            query_count = 0
            start_idx, end_idx = query
            
            for i in range(start_idx, end_idx + 1):
                if _starts_ends_with_vowel(words[i]):
                    query_count += 1

            out.append(query_count)

        return out

                
        