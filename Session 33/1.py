# genereaza un array de la 0 la x si afiseaza doar numerele pare
import numpy as np

if __name__ == "__main__":
    x = 100
    a = np.arange(x)
    print(a[a % 2 == 0])