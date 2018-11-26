#!/usr/bin/env python3
from typing import Any, List


def is_a_solution(alist: List[int], k: int, input: Any) -> Any:
    pass


def process_solution(alist: List[int], k: int, input: Any) -> Any:
    pass


def construct_candidates(
    alist: List[int], k: int, input: Any, c: Any, num_candidates: int
) -> None:
    pass


def make_move(alist: List[int], k: int, input: Any) -> Any:
    pass


def unmake_move(alist: List[int], k: int, input: Any) -> Any:
    pass


finished = False  # global var


def backtrack(alist: List[int], k: int, input: Any) -> Any:
    num_candidates = 0
    candidates = [None] * num_candidates
    if is_a_solution(alist, k, input):
        process_solution(alist, k, input)
    else:
        k = k + 1
        construct_candidates(alist, k, input, candidates, num_candidates)
        for i in range(0, num_candidates):
            alist[k] = candidates[i]  # noqa
            make_move(alist, k, input)
            backtrack(alist, k, input)
            unmake_move(alist, k, input)
            if finished:
                return
