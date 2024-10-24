# SQLInjectHunter
Automating SQL Injection Vulnerability Verification through HTTP Response Length Analysis using Python

  The primary objective of this project is to create a Python-based system that could simulate SQL Injection attacks by sending multiple malicious payloads to the target web application and then analyzing the response length that the server returns. In which the system will automatically detect the difference in response lengths, indicating any potential vulnerability, and then report the outcome to the user.

  In this project, the file [sql.txt] serves as the base dataset for SQL injection payloads used by the Python-based system.

  The file [sqlTest.py] contains the main code for simulating SQL Injection attacks. The system utilizes the [requests] module, which allows for sending HTTP requests and receiving response objects containing the server’s data. Additionally, the [argparse] module is employed to create command-line interfaces for user input.

  Three key variables are initialized in [sqlTest.py]: 
    1. [vpn] – representing the VPN of the target web application, 
    2. [cookie] – representing the cookie associated with the target web application, and 
    3. [security] – representing the security level of the target web application. 

  Another variable, [url], is created to store the target web’s URL using the value of [vpn].

  The Python-based system prompts the user for these three variables, which are necessary for the simulation. First, the VPN of the target web is entered, followed by the cookie (which must be entered from the first character up to the one immediately preceding the semicolon (;)). Lastly, the user inputs the security level of the target (low, medium, high, or impossible). The system will then processes this data to simulate the SQL Injection attack on the target web application.

  
