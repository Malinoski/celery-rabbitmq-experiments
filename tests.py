from tasks import reverse
from time import sleep

print("# Test 1")
result = reverse.delay('iuri')
print(result.status)
sleep(6)
print(result.status)

print("\n# Test 2")
result = reverse.apply_async(args=['iuri'])
print(result.status)
sleep(6)
print(result.status)
