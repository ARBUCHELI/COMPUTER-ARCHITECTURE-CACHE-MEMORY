load_file_in_context("app.py")

if not isinstance(cache_arch.memory, Cache):
	fail_tests("Did you replace the argument in `cache_arch.set_memory()` to `Cache()`?")

pass_tests()
