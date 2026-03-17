"""
Prime Number – Quick Notes

✔ To check a single number, use √n method
→ Check divisibility from 2 to √n
→ Time complexity: O(√n)
→ Best for one number

✔ To find all primes up to n, use Sieve
→ Mark multiples in bulk
→ Time complexity: O(n log log n)
→ Avoids repeated checks

Sieve useful,

Problem starts when finding primes up to 50.

Using normal method:

For 29 → check 2,3,4,5
For 30 → check 2,3,4,5
For 31 → check 2,3,4,5
For 32 → check 2,3,4,5

See the repetition?
We keep checking divisibility by 2 again and again for every number.


"""

def sieve(n):
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, n + 1, i):
                prime[j] = False
    
    primes = [i for i in range(n + 1) if prime[i]]
    return primes


print(sieve(50))



# Method 2
import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def find_primes(n):
    primes = []
    
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    
    return primes


print(find_primes(50))