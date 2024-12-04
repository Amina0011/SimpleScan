import subprocess 
import socket
import ipaddress
import pyfiglet
import psutil 
import nmap 


# Create a banner with the text "SimpleScan"
def banner():
    banner = pyfiglet.figlet_format("SimpleScan", font="slant")
    print(banner)
    
# finding local ip
def find_local_ip():
    try: 
        temp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        temp_socket.connect(("8.8.8.8", 80))
        local_ip = temp_socket.getsockname()[0]
        temp_socket.close()
        return local_ip
    except Exception as error:
        print("Error:", error)
        return None
    
# find the subnet mask for the given IP
def find_subnet_for_ip(ip):
    try:
        for interface, addrs in psutil.net_if_addrs().items():
            for addr in addrs:
                if addr.family == socket.AF_INET and addr.address == ip:
                    return addr.netmask
        return None
    except Exception as error:
        print("Error:", error)
        return None
    
# calculating IP subnet range based on local IP
def find_subnet_range(ip):
    netmask = find_subnet_for_ip(ip)
    if not netmask:
        print("Error: Could not find netmask for IP:", ip)
        return None

    cidr = sum(bin(int(octet)).count('1') for octet in netmask.split('.'))
    network_obj = ipaddress.ip_network(f"{ip}/{cidr}", strict=False)
    
    return network_obj

# printing results of scanned subnets
def ip_range(subnet):
    print(f"The IP range is {subnet.network_address} - {subnet.broadcast_address} ({len(list(subnet.hosts()))} hosts)")

# scanning all the active hosts in the subnet (2)
def scan_subnet(subnet, ports="1-65535", script=None):
    try:
        if script:
            command = f'nmap -p{ports} -sV --script {script} {subnet}'
        else:
            command = f'nmap -p{ports} -sV {subnet}'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as error:
        print(f"Error occurred: {error}")
        return None

# scanning for finding active ports (3)
def host_discovery(subnet):
    try:
        if isinstance(subnet, ipaddress.IPv4Network):
            subnet = str(subnet)

        nm = nmap.PortScanner()
        nm.scan(hosts=subnet, arguments='-sn')
        
        active_hosts = nm.all_hosts()

        if not active_hosts:
            print(f"No active hosts found in subnet {subnet}.")
        else:
            print(f"Active hosts in {subnet}:")
            for host in active_hosts:
                print(f"- {host} is up")

        return active_hosts

    except Exception as e:
        print(f"Error occurred: {e}")
        return None

# getting CIDR natation by netmask (4)
def calculating_CIDR_notation(netmask):
    try:
        octets = netmask.split('.')
        cidr = 0
        
        for octet in octets:
            binary_octet = bin(int(octet))[2:].zfill(8) 
            cidr += binary_octet.count('1') 
        
        print(f'/{cidr}')
    except Exception as e:
        print(f"Error occurred: {e}")
        return None


def single_target_scan(target, ports="1-65535", argument=None, script=None):
    try: 
        if script:
            # Adding the script argument
            command = f'nmap -p{ports} {argument if argument else ""} --script {script} {target}'
        else:
            # Running a basic Nmap scan
            command = f'nmap -p{ports} {argument if argument else ""} {target}'
            print(command)
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f'Error occurred: {e}')
        return None
    

if __name__ == "__main__":
    tool_name = ""
    
    while True:
        banner()

        local_ip = find_local_ip()

        if local_ip:
            print(f"Your local IP Address is: {local_ip}")
            subnet = find_subnet_range(local_ip)
            print(f"The calculated CIDR notation is: {subnet}")
            ip_range(subnet)
            
       
            print("\nChoose a scan target: ")
         
            print("\n1. one IP -> specific target")
            print("2. whole subnet -> all hosts(devices)")
            print("3. Host discovery -> finding active hosts (-sn)")
            print("4. Calculating CIDR notation")
            print()
            choice = input("Enter your choice (1/2/3/4): ")

            if choice == "1":
                print()
                print("You should be root to get the proper output")
                ip = str(input("Enter the IP address to perform a scan: "))
                port = str(input("Enter single or multiple ports (e.g., 22,80 or 1-65535, - (all ports)): "))
                
                print()

                print("1. SYN scan -sS")
                print("2. UDP scan -sU")
                print("3. DNS scan")
                print("4. Disable host discovery -Pn")
                print("5. Version scan -sV")
                print("6. Identifying possible vulnerabilities")
                
                print()
                choice = input("Enter your choice (1/2/3/4/5/6): ")

                if choice == "1":
                    print("\nPerforming SYN scan...")
                    scan_result = single_target_scan(target=ip, ports=port, argument="-sS")
                    print(scan_result)
                
                elif choice == "2":
                    print("\nPerforming UDP scan...")
                    scan_result = single_target_scan(target=ip, ports=port, argument="-sU")
                    print(scan_result)
                
                elif choice == "3":
                    print("\nPerforming DNS scan...")
                    scan_result = single_target_scan(ip, port, script="dns")
                    print(scan_result)
                
                elif choice == "4":
                    print("\nPerforming Ping scan...")
                    scan_result = single_target_scan(target=ip, ports=port, argument="-Pn")
                    print(scan_result)
                
                elif choice == "5":
                    print("\nPerforming Version scan...")
                    scan_result = single_target_scan(target=ip, ports=port, argument="-sV")
                    print(scan_result)
                
                elif choice == "6":
                    print("\nIdentifying possible vulnerabilities...")
                    scan_result = single_target_scan(ip, port, script="vuln")
                    print(scan_result)
                
                else:
                    print("Invalid choice! Please enter a valid option (1/2/3/4/5/6).")

                

            elif choice == "2":
                # User input about their scan choice
                print()
                print("Choose a scan option:")
                print()
                print("1. Scanning all active hosts -> all ports ( -p-)")
                print("2. Scanning all active hosts -> top 1000 ports") 
                print("3. Scan all active hosts -> all open ports -> for vulnerabilities")
                print("4. Scan all active hosts -> top 1000 ports -> for vulnerabilities")

                print()
                choice = input("Enter your choice (1/2/3/4): ")
                

                #run scan of choice 
                if choice == "1":
                    print()
                    print("Scanning process has started. all active hosts for open ports and running services. Please be patient it will take time.....")
                    scan_result = scan_subnet(subnet)
                    
                elif choice == "2":
                    print()
                    print("Scanning process has started. all active hosts' top 1000 ports to find running services. Please be patient it will take time.....")
                    scan_result = scan_subnet(subnet, ports="1-1000")
                    
                elif choice == "3":
                    print() 
                    print("Scanning process has started. all active hosts (all ports) to identify vulnerabilities. Please be patient it will take a bit more time.....")
                    scan_result = scan_subnet(subnet, script="vuln")
                
                elif choice == "4":
                    print()
                    print("Scanning process has started. active hosts (top 1000 ports) to identify vulnerabilities. Please be patient it will take a bit more time.....")
                    scan_result = scan_subnet(subnet, ports="1-1000", script="vuln")
                else:
                    print("Invalid choice.") # Error handling, print invalid choice if any other option is entered
                    scan_result = None

                if scan_result:
                    print()
                    print("Scan Results:")
                    print()
                    print(scan_result)
                else:
                    print("Scan failed or no vulnerabilities found.") # Error handling, print error message if scan was unsuccessful
            
            elif choice == "3":
                print()
                print("Scanning process started. Finding all active IP addresses. Wait a little bit....")
                scan_result = host_discovery(subnet)

            elif choice == "4":
                print()
                netmask = str(input("Enter netmask to calculate CIDR notation: eg(225.225.225.0)"))
                scan_result = calculating_CIDR_notation(netmask)


        else:
            print("Unable to retrieve local IP address.") #Error handling, print error if unable to find the local IP
        print()
        run_again = input("Do you want to run the program again? (yes/no): ") # ask the users if they wants to run the program again or exit the loop
        if run_again.lower() != 'yes':
            break