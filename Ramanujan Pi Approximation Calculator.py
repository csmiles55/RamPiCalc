import math
def ramanujan_pi_approximation(n_terms):
    factor = (2 * math.sqrt(2)) / 9801 
    series_sum = 0 

    for k in range(n_terms):
        numerator = math.factorial(4 * k) * (1103 + 26390 * k)
        denominator = (math.factorial(k) ** 4) * (396 ** (4 * k))
        series_sum += numerator / denominator 
    approximation = factor * series_sum

    return approximation

n_terms = int(input("Enter the number of terms for the approximation: "))
approximation = ramanujan_pi_approximation(n_terms)

# Print
print(f"Approximation of pi using {n_terms} terms: {1/approximation}")
