class Solution:
    def strangePrinter(self, s: str) -> int:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        sElements = [[] for _ in range(len(alphabet))]

        for el in alphabet:
            # sElements[ord(el) - ord('a')] = [s.find(el), s.rfind(el)]
            index = 0
            while index != -1:
                index = s.find(el)
                sElements.append(index)
        
        sElements = [el for el in sElements if el[0] != -1]
        sElements = sorted(sElements, key=lambda x: (x[1] - x[0]), reverse=True)
        