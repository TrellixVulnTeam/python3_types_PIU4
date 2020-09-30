# (generated with --quick)

from typing import Any

AVLTree: Any
BLACK: Any
BinarySearchTree: Any
RED: Any
RedBlackTree: Any
assume: Any
composite: Any
given: Any
inf: float
insert_delete_queries: Any
integers: Any
lists: Any
permutations: Any
sets: Any
settings: Any
test_avl_queries: Any
test_avl_tree_invariant: Any
test_bst_invariant: Any
test_bst_invariant_rotations: Any
test_rb_queries: Any
test_rb_tree_invariant: Any

def bst_invariant(t, min_key = ..., max_key = ..., parent = ...) -> Any: ...
def check_avl_properties(tree) -> Any: ...
def check_rb_tree_properties(tree, root = ...) -> Any: ...
def is_left_child(parent, child) -> bool: ...
def is_right_child(parent, child) -> bool: ...
def test_bst() -> None: ...
def test_bst_delete() -> None: ...
def test_bst_sort() -> None: ...
def test_left_rotate() -> None: ...
def test_rb_deletion() -> None: ...
def test_rb_tree() -> None: ...
def test_right_rotate() -> None: ...