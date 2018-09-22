# #!/usr/bin/env python3
#
# from typing import Any, List
#
# class Evaluator:
#     def __init__(self, args: str) -> None:  # noqa
#         self.vals: List[Any] = []
#         self.ops: List[Any] = []
#         self.args = args
#
#     def execute(self) -> int:
#         for char in self.args:
#             if char == "+":
#                 self.ops.append(char)
#             elif char == "*":
#                 self.ops.append(char)
#             elif char == ")":
#                 if self.ops.pop() == "*":
#                     self.vals.append(int(self.vals.pop()) * int(self.vals.pop())
#                 elif self.ops.pop() == "+":
#                     self.vals.append(int(self.vals.pop()) + int(self.vals.pop()))
#             else:
#                 self.vals.push(char)
#     return 1
# a = Evaluator("1+2")
# val = a->execute()
# print(val)
