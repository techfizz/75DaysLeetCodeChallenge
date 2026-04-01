class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
          return reduce(lambda s, t: setitem(s, -1, int(action[t](s[-2], s.pop()))) or s if t in (action := {"+": add, "-": sub, "*": mul, "/": truediv}) else s+[int(t)], tokens, []).pop()