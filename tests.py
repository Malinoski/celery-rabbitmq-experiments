from tasks import reverse
from time import sleep

print("# Test 1")
result = reverse.delay('iuri')  # or reverse.apply_async(args=['iuri'])
print("Get the id: ", result.id)
print("Get the status: ", result.status)
print("Wait to status change...")
sleep(6)
print("# Get the new status", result.status)

print("\n# Test 2")
result = reverse.apply_async(args=['iuri'])
print("Synchronous getting the response...")
print("Response: ", result.get())

