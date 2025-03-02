import random
import secrets
import time
import subprocess
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <output_directory>")
    sys.exit(1)

output_dir = sys.argv[1]

rnd_python_random_bytes = f"{output_dir}/rnd-python-random_bytes.bin"
rnd_python_random_int = f"{output_dir}/rnd-python-random_int.bin"
rnd_python_secrets = f"{output_dir}/rnd-python-secrets.bin"
rnd_openssl = f"{output_dir}/rnd-openssl.bin"

print(f'Stage 1 - Generating with random')
start_time = time.time()
print(f'Stage 1.1 - Generating with randbytes {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))}')
with open(rnd_python_random_bytes, 'wb') as f:
    for _ in range(1200000):
        f.write(random.randbytes(1024)) 
end_time = time.time()
print(f'Execution time for randbytes: {end_time - start_time:.2f} seconds')

start_time = time.time()
print(f'Stage 1.2 - Generating with randint {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))}')
with open(rnd_python_random_int, 'wb') as f:
    for _ in range(1200000000):
        num = random.randint(0, 255)
        f.write(bytes([num])) 
end_time = time.time()
print(f'Execution time for randint: {end_time - start_time:.2f} seconds')

start_time = time.time()
print(f'Stage 2 - Generating with secrets {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))}')
with open(rnd_python_secrets, 'wb') as f:
    for _ in range(1200000000):
        num = secrets.randbits(8)
        f.write(bytes([num])) 
end_time = time.time()
print(f'Execution time for secrets: {end_time - start_time:.2f} seconds')

start_time = time.time()
print(f'Stage 3 - Generating with OpenSSL {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))}')
subprocess.run(["openssl", "rand", "-out", rnd_openssl, "1200000000"], check=True)
end_time = time.time()
print(f'Execution time for OpenSSL: {end_time - start_time:.2f} seconds')