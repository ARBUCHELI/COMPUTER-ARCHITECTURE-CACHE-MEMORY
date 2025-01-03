load_file_in_context("app.py")

if not isinstance(cache_arch.memory, MainMemory):
	fail_tests("Did you call `cache_arch.set_memory()` with `MainMemory()` as the argument?")

pass_tests()
