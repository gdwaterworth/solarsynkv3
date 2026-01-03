import logging
import json
import requests
from datetime import datetime

class ConsoleColor:    
    OKBLUE = "\033[34m"
    OKCYAN = "\033[36m"
    OKGREEN = "\033[32m"        
    MAGENTA = "\033[35m"
    WARNING = "\033[33m"
    FAIL = "\033[31m"
    ENDC = "\033[0m"
    BOLD = "\033[1m" 

# Load settings from JSON file
try:
    with open('/data/options.json') as options_file:
        json_settings = json.load(options_file)
        api_server = json_settings['API_Server']
except Exception as e:
    logging.error(f"Failed to load settings: {e}")
    print(ConsoleColor.FAIL + "Error loading settings.json. Ensure the file exists and is valid JSON." + ConsoleColor.ENDC)
    exit()
    
def GetInverterInfo(Token,Serial):    
    global api_server         
    # Inverter URL
    inverter_url = f"https://{api_server}/api/v1/inverter/{Serial}"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":
            print("Inverter fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json);   
            return parsed_inverter_json['data'] if 'data' in parsed_inverter_json else None
        else:
            print("Inverter fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)

def GetInverterSettingsData(Token,Serial):    
    global api_server    
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" https://{api_server}/api/v1/inverter/$inverter_serial/realtime/input
    #inverter_url = f"https://{api_server}/api/v1/inverter/{Serial}/realtime/input"
    inverter_url = f"https://{api_server}/api/v1/common/setting/{Serial}/read"
    
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "Settings data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json);
            return parsed_inverter_json['data'] if 'data' in parsed_inverter_json else None
        else:
            print("Settings data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)  

def GetPvData(Token,Serial):    
    global api_server    
    # Inverter URL
    #curl -s -k -X GET -H "Content-Type: application/json" -H "authorization: Bearer $ServerAPIBearerToken" https://{api_server}/api/v1/inverter/$inverter_serial/realtime/input
    inverter_url = f"https://{api_server}/api/v1/inverter/{Serial}/realtime/input"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "PV data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json);
            return parsed_inverter_json['data'] if 'data' in parsed_inverter_json else None
        else:
            print("PV data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)        

def GetGridData(Token,Serial):    
    global api_server   
    inverter_url = f"https://{api_server}/api/v1/inverter/grid/{Serial}/realtime?sn={Serial}"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success": 
            print(ConsoleColor.BOLD + "Grid data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json)
            return parsed_inverter_json['data'] if 'data' in parsed_inverter_json else None
        else:
            print("Grid data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)                

def GetBatteryData(Token,Serial):  
    global api_server  
    inverter_url = f"https://{api_server}/api/v1/inverter/battery/{Serial}/realtime?sn={Serial}&lan=en"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success": 
            print(ConsoleColor.BOLD + "Battery data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json)
            return parsed_inverter_json['data'] if 'data' in parsed_inverter_json else None
        else:
            print("Battery data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)         
        
def GetLoadData(Token,Serial): 
    global api_server    
    inverter_url = f"https://{api_server}/api/v1/inverter/load/{Serial}/realtime?sn={Serial}"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "Load data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json)
            return parsed_inverter_json['data'] if 'data' in parsed_inverter_json else None
        else:
            print("Load data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)          
        
def GetOutputData(Token,Serial):
    global api_server   
    inverter_url = f"https://{api_server}/api/v1/inverter/{Serial}/realtime/output"
    # Headers (Fixed Bearer token format)
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Token}"
    }

    try:
        # Corrected to use GET request
        response = requests.get(inverter_url, headers=headers, timeout=10)
        response.raise_for_status()

        parsed_inverter_json = response.json()

        if parsed_inverter_json.get('msg') == "Success":           
            print(ConsoleColor.BOLD + "Output data fetch response: " + ConsoleColor.OKGREEN + parsed_inverter_json['msg'] + ConsoleColor.ENDC)
            #print(parsed_inverter_json)
            return parsed_inverter_json['data'] if 'data' in parsed_inverter_json else None           
        else:
            print("Output data fetch response: " + ConsoleColor.FAIL + parsed_inverter_json['msg'] + ConsoleColor.ENDC)

    except requests.exceptions.Timeout:
        print(ConsoleColor.FAIL + "Error: Request timed out while connecting to Service Provider API." + ConsoleColor.ENDC)

    except requests.exceptions.RequestException as e:
        print(ConsoleColor.FAIL + f"Error: Failed to connect to Service Provider API. {e}" + ConsoleColor.ENDC)

    except json.JSONDecodeError:
        print(ConsoleColor.FAIL + "Error: Failed to parse Service Provider API response." + ConsoleColor.ENDC)         
       










