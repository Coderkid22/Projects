import concurrent.futures

def collatz_steps(n):
   steps = 0
   while n != 1:
       if n % 2 == 0:
           n = n // 2
       else:
           n = n * 3 + 1
       steps += 1
   return steps

if __name__ == '__main__':
   with concurrent.futures.ProcessPoolExecutor() as executor:
       for i in range(295147905179383163864, 999999999999999999999):
           future = executor.submit(collatz_steps, i)
           print(f"{i} {future.result()} steps")