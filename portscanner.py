
'''
	DOMAIN PORT SCANNER , DEVELOPED BY MOEIN REZAIE.
'''
''' this is module!!! '''

from socket import*

def start(domain_ip):		

	#Domain = input("Enter Domain: ")

	#Domain_ip= gethostbyname(Domain)

	print("IP of this domain is :", domain_ip)

	port_list = [13,21,22,23,53,80,445,443]

	open_ports=[]

	global open_ports

	for PORT in port_list:
		
		sock= socket(AF_INET , SOCK_STREAM)
		
		sock.settimeout(1)
		
		#print("Testing :", PORT)
		
		respone = sock.connect_ex((domain_ip, PORT))
		
		if respone ==0:
		
			open_ports.append(PORT)

			
			#print(PORT,"Is open", getservbyport(PORT))
	
	print(" List of open ports : ", open_ports)	

#start()