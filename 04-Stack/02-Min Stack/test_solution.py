import pytest
from solution import MinStack

def execute_operations(commands, args):
    """
    Helper function to execute a list of commands on the MinStack
    and return the outputs to compare against expected results.
    """
    obj = None
    results = []
    
    for cmd, arg in zip(commands, args):
        if cmd == "MinStack":
            obj = MinStack()
            results.append(None)
        elif obj is not None:
            if cmd == "push":
                obj.push(arg[0])
                results.append(None)
            elif cmd == "pop":
                obj.pop()
                results.append(None)
            elif cmd == "top":
                results.append(obj.top())
            elif cmd == "getMin":
                results.append(obj.getMin())
            
    return results

@pytest.mark.parametrize("commands, args, expected", [
    # 1. Standard LeetCode Example
    (["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], 
     [[], [1], [2], [0], [], [], [], []], 
     [None, None, None, None, 0, None, 2, 1]),

    # 2. Descending Order (Min changes every push)
    (["MinStack", "push", "push", "push", "getMin"], 
     [[], [5], [4], [3], []], 
     [None, None, None, None, 3]),

    # 3. Ascending Order (Min stays the same)
    (["MinStack", "push", "push", "push", "getMin"], 
     [[], [3], [4], [5], []], 
     [None, None, None, None, 3]),

    # 4. Duplicate Minimums
    (["MinStack", "push", "push", "push", "getMin", "pop", "getMin"], 
     [[], [2], [2], [2], [], [], []], 
     [None, None, None, None, 2, None, 2]),

    # 5. Negative Numbers
    (["MinStack", "push", "push", "getMin", "pop", "getMin"], 
     [[], [-2], [-5], [], [], []], 
     [None, None, None, -5, None, -2]),

    # 6. Large Numbers (Boundary constraints)
    (["MinStack", "push", "push", "getMin"], 
     [[], [2147483647], [-2147483648], []], 
     [None, None, None, -2147483648]),

    # 7. Single Element Stack
    (["MinStack", "push", "top", "getMin"], 
     [[], [42], [], []], 
     [None, None, 42, 42]),

    # 8. Push and Pop alternating
    (["MinStack", "push", "getMin", "pop", "push", "getMin"], 
     [[], [10], [], [], [5], []], 
     [None, None, 10, None, None, 5]),

    # 9. Multiple identical elements, popping sequentially
    (["MinStack", "push", "push", "push", "pop", "getMin", "pop", "getMin"], 
     [[], [1], [1], [1], [], [], [], []], 
     [None, None, None, None, None, 1, None, 1]),

    # 10. Heavy population of 0s
    (["MinStack", "push", "push", "push", "getMin"], 
     [[], [0], [0], [0], []], 
     [None, None, None, None, 0]),

    # 11. Bouncing Values (High, Low, High, Low)
    (["MinStack", "push", "push", "push", "push", "getMin", "pop", "getMin"], 
     [[], [100], [1], [100], [0], [], [], []], 
     [None, None, None, None, None, 0, None, 1]),

    # 12. Popping down to last element and checking min
    (["MinStack", "push", "push", "push", "pop", "pop", "getMin"], 
     [[], [7], [8], [9], [], [], []], 
     [None, None, None, None, None, None, 7]),

    # 13. Pushing after popping back to empty (Testing reset behavior)
    (["MinStack", "push", "pop", "push", "getMin"], 
     [[], [5], [], [10], []], 
     [None, None, None, None, 10]),

    # 14. Extreme value differences
    (["MinStack", "push", "push", "push", "getMin"], 
     [[], [1000000], [-1000000], [0], []], 
     [None, None, None, None, -1000000]),

    # 15. Continuous queries without state changes
    (["MinStack", "push", "push", "getMin", "top", "getMin", "top"], 
     [[], [3], [1], [], [], [], []], 
     [None, None, None, 1, 1, 1, 1]),
])
def test_min_stack(commands, args, expected):
    """
    Tests the MinStack class against 15 distinct sequences of operations,
    evaluating state changes, boundary constraints, and structural integrity.
    """
    assert execute_operations(commands, args) == expected