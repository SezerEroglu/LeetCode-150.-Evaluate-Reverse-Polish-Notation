from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        heap = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                heap.append(int(heap.pop() + heap.pop()))
                continue
            if tokens[i] == "-":
                heap.append(-1 * int(int(heap.pop()) - int(heap.pop())))
                continue
            if tokens[i] == "/":
                bottom, top = heap.pop(), heap.pop()

                heap.append(int(top) / int(bottom))
                continue
            if tokens[i] == "*":
                heap.append(int(int(heap.pop()) * int(heap.pop())))
                continue
            heap.append(int(tokens[i]))

        return heap[-1]
