from rich import print
from rich.table import Table
from rich.console import Console
import timeit
from search_algorithms import kmp_search, boyer_moore_search, rabin_karp_search


with open("article.txt", "r", encoding="utf-8") as file:
    text = file.read()

pattern_1 = "Висновки"
pattern_2 = "Далі виконується цикл перебору основного рядка."

def time_for_algorithms(text, pattern, search_algorithms, number=10):
    results = []
    for name, func in search_algorithms.items():
        # Спершу викликаємо функцію для визначення, чи знайдено підрядок
        found_index = func(text, pattern)
        found = found_index != -1
        
        # Далі міряємо середній час виконання
        timer = timeit.timeit(lambda: func(text, pattern), number=number)
        avg_time = timer / number
        
        results.append({
            "Algorythm": name,
            "Pattern": pattern,
            "Found": found,
            "Avg time (sec)": avg_time
        })
    return results

def analysis_of_results(results):
    console = Console()
    table = Table(title="Порівняння алгоритмів пошуку підрядка")

    table.add_column("Algorythm", justify="left", style="cyan", no_wrap=True)
    table.add_column("Pattern", justify="left", style="yellow")
    table.add_column("Found", justify="center", style="magenta")
    table.add_column("Avg time for find (sec)", justify="right", style="green")

    for record in results:
        table.add_row(
            record["Algorythm"],
            record["Pattern"],
            str(record["Found"]),
            f"{record["Avg time (sec)"]:.4f}"
        )

    console.print(table)



search_algorithms = {
    "KMP": kmp_search,
    "Boyer-Moore": boyer_moore_search,
    "Rabin-Karp": rabin_karp_search
}

results_1 = time_for_algorithms(text, pattern_1, search_algorithms)
results_2 = time_for_algorithms(text, pattern_2, search_algorithms)

analysis_of_results(results_1)
analysis_of_results(results_2)