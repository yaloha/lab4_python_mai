from simulation import run_simulation


def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    run_simulation(steps=500, seed=42)

if __name__ == "__main__":
    main()
