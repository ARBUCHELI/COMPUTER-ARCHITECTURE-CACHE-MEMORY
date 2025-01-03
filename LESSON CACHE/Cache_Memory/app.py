from isa import ISA
from memory import Memory, MainMemory

class Cache(Memory):
  def __init__(self):
    # Write your code below 
    super().__init__(name="Cache", access_time=0.5)
    self.data = [
      {"tag": None, "data": ""}, 
      {"tag": None, "data": ""}, 
      {"tag": None, "data": ""}, 
      {"tag": None, "data": ""}
    ]


    

  # Returns the cache total execution time
  def get_exec_time(self):
    return self.exec_time

if __name__ == "__main__":
  cache_arch = ISA()
  # Change the code below
  cache_arch.set_memory(Cache())

  # Architecture runs the instructions
  cache_arch.read_instructions("ex3_instructions")

  # This outputs the memory data and code execution time
  exec_time = cache_arch.get_exec_time()
  if exec_time > 0:
    print(f"OUTPUT STRING: {cache_arch.output}")
    print(f"EXECUTION TIME: {exec_time:.2f} seconds")