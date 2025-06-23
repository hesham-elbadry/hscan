import subprocess
import os
import time

def banner():
    print(r"""
██╗  ██╗███████╗ ██████╗ █████╗ ███╗   ██╗  
██║  ██║██╔════╝██╔════╝██╔══██╗████╗  ██║
███████║█████╗  ██║     ███████║██╔██╗ ██║
██╔══██║     ██ ██║     ██╔══██║██║╚██╗██║
██║  ██║███████╗╚██████╗██║  ██║██║ ╚████║ 
╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝

        Tool: HScan
        Author: Hesham Saleh
        LinkedIn: https://www.linkedin.com/in/hesham-saleh-107861230/
        Website : https://hesham-elbadry.github.io/
    """)

def run_nmap(ip, output_dir):
    safe_ip = ip.replace('.', '_')
    output_file = os.path.join(output_dir, f"scanned-{safe_ip}.txt")
    command = [
        "nmap",
        "-sC", "-sV", "-sS", "-O", "-A", "-Pn", "-p-", "--min-rate=1000",
        "-oN", output_file,
        ip
    ]
    print(f"\n[+] Scanning {ip} ...")
    print(f"[+] Output >> {output_file}")
    print("-" * 50)
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    for line in process.stdout:
        print(line.strip())
    print("-" * 50)
    print(f"[+] Scan complete for {ip}\n")

def main():
    banner()
    ip_file = input("HScan > Set IP list path: ").strip()

    if not os.path.isfile(ip_file):
        print("[!] File not found. Please check the path and try again.")
        return

    output_dir = input("HScan > Set output folder name [default: results]: ").strip()
    if output_dir == "":
        output_dir = "results"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(ip_file, 'r') as f:
        ips = [line.strip() for line in f if line.strip()]

    print(f"\n[+] Loaded {len(ips)} IPs. Starting scan...\n")

    for ip in ips:
        run_nmap(ip, output_dir)
        time.sleep(1)  # optional delay between scans

    print(f"\n[+] All scans completed. Results saved in '{output_dir}' folder.\n")

if __name__ == "__main__":
    main()
