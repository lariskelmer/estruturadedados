import pytest
from p4 import dijkstra

# Testes usando pytest
@pytest.mark.parametrize("graph, start, expected_result", [
    (
        {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1}},
        'A',
        {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    ),
    (
        {'A': {'B': 1, 'C': 4}, 'B': {'A': 1}, 'C': {'A': 4}, 'D': {'E': 3}, 'E': {'D': 3}},
        'A',
        {'A': 0, 'B': 1, 'C': 4, 'D': float('infinity'), 'E': float('infinity')}
    ),
    (
        {'A': {'B': 1, 'C': 4}, 'B': {'C': 2, 'D': 5}, 'C': {'D': 1}, 'D': {}},
        'A',
        {'A': 0, 'B': 1, 'C': 3, 'D': 4}
    ),
    (
        {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'D': 5}, 'C': {'D': 1}, 'D': {}},
        'A',
        {'A': 0, 'B': 1, 'C': 4, 'D': 5}
    ),
    (
        {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': -5}, 'C': {'D': 1}, 'D': {'B': -5}},
        'A',
        pytest.raises(ValueError, match="Graph contains negative cycles")
    ),
])

def test_dijkstra(graph, start, expected_result):
    if callable(expected_result):
        with expected_result:
            dijkstra(graph, start)
        print("Teste passou. Exceção levantada corretamente.")
    else:
        result = dijkstra(graph, start)
        assert result == expected_result
        print(f"Teste passou. Resultado: {result}")
