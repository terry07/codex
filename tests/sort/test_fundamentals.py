import pytest
from codex.sort.basic import selection_sort, insertion_sort, bubble_sort

@pytest.mark.parametrize("sort_fn", [selection_sort, insertion_sort, bubble_sort])
def test_sorting_algorithms(sort_fn):
    items = [4, 2, 7, 1, 3]
    sort_fn(items)
    assert items == [1, 2, 3, 4, 7]

    # Already sorted
    items = [1, 2, 3]
    sort_fn(items)
    assert items == [1, 2, 3]

    # Reverse sorted
    items = [3, 2, 1]
    sort_fn(items)
    assert items == [1, 2, 3]

