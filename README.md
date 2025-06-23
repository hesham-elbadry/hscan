# HScan

HScan is a terminal-based tool for scanning multiple IP addresses using Nmap.

## Install

```bash
pip install git+https://github.com/hesham-elbadry/hscan.git
(images/1.png)

## USAGE
1. **Create a file with IPs**, one per line.  
   _Example:_
   ```bash
   nano ips.txt
2. **Run the tool**
   ```bash
   hscan
3. When prompted, enter the IP list filename. (In our case: ips.txt)
4. Set the output folder name (or press Enter to use the default results folder).
5.Results will be saved as individual files, and output will look like the following format:
scanned-$IP.txt


(images/2.png)
(images/3.png)
(images/4.png)
(images/5.png)
