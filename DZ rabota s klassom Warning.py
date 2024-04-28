import warnings

def func_warning(a, b):
    try:
        print("Перед генерацией предупреждения")
        if b < 0.01 and a < 0.01:
            warnings.warn(f'Делитель {a} близок к нулю!', UserWarning)
        print("После генерации предупреждения")
        print(a / b)
    except UserWarning as e:
        print(f"Предупреждение было перехвачено как исключение: {e}")



print("Фильтр 'error'")
warnings.simplefilter("error", UserWarning)
func_warning(0.0007, 0.001)
print("\n")

print("Фильтр 'ignore'")
warnings.simplefilter("ignore", UserWarning)
func_warning(0.003, 0.001)
print("\n")

print("Фильтр 'always'")
warnings.simplefilter("always", UserWarning)
func_warning(0.0005, 0.001)
print("\n")


