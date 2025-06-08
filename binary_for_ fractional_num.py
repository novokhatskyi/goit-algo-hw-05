import random
from rich import print
from rich.prompt import Prompt

def generate_lists():
    return [round(random.uniform(0, 1000), 1) for _ in range (20)]

def sort_by_timsort(lst):
    return sorted(lst)

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iteration = 0
    while low <= high:
        iteration += 1
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid, iteration
    return -1, iteration



if __name__ == "__main__":
    data = generate_lists()
    print(data)
    sorted_data = sort_by_timsort(data)
    print(sorted_data)

    ask = Prompt.ask("[bold blue]Чи хочеш здійснити пошук по масиву? Y/N[/bold blue]")
    if ask.lower() == "y":
        num = round(float(Prompt.ask("[bold green]Введіть число для пошуку по списку. Через крапку[/bold green]")), 1)
        index, iterations = binary_search(sorted_data, num)
        if index != -1:
            print(f"[green]Знайдено![/green] {num} на позиції {index}. Кількість ітерацій: {iterations}")
        else:
            print(f"[red]Не знайдено[/red] {num} у списку. Кількість ітерацій: {iterations}")
    else:
        print("[bold yellow]Пошук не виконано.[/bold yellown]")

