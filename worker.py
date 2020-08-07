from tasks import add

result = add.delay(4,51)
result.ready()
result.get(timeout=1)
#result.get(propagate=False)
#result.traceback
print(result)
print(result.backend)
