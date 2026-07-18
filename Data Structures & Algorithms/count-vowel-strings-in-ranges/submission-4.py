class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        def _starts_ends_with_vowel(word: str) -> bool:
            vowels = 'aeiou'
            if ((word[0] in vowels) and (word[-1] in vowels)):
                return True
            return False

        out = []
        prefix_out = [0]

        for i in range(len(words)):
            if _starts_ends_with_vowel(words[i]):
                prefix_out.append(prefix_out[-1] + 1)
            else:
                prefix_out.append(prefix_out[-1])

        for query in queries:
            start, end = query
            count = prefix_out[end + 1] - prefix_out[start]
            out.append(count)

        return out


        