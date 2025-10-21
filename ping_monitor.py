import subprocess
import datetime
import time

# Daftar IP target
targets = {
    "Gateway": "192.168.1.1",
    "DNS Google": "8.8.8.8",
    "Cloudflare": "1.1.1.1"
}

# Fungsi ping
def ping_target(name, ip):
    try:
        start = time.time()
        output = subprocess.run(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        end = time.time()
        status = "Success" if output.returncode == 0 else "Failed"
        response_time = round((end - start) * 1000, 2)
    except Exception as e:
        status = "Error"
        response_time = "-"
    return status, response_time

# Logging
def log_result(name, ip, status, response_time):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ping_log.txt", "a") as f:
        f.write(f"{timestamp} | {name} ({ip}) | {status} | {response_time} ms\n")

# Looping ping
while True:
    for name, ip in targets.items():
        status, response_time = ping_target(name, ip)
        log_result(name, ip, status, response_time)
    time.sleep(60)  # Ping setiap 60 detik
