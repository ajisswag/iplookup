import requests
from time import sleep

ip = input("Enter the IP Address: ")
print("Gathering Information.")
sleep(0.75)
print("Gathering Information..")
sleep(0.75)
print("Gathering Information...")
sleep(0.75)
print("Gathering Information.")
sleep(0.75)
print("Gathering Information..")
sleep(0.75)
print("Gathering Information...")
sleep(2)
print("Information Gathered.")
sleep(2)

def prompt():
    command = input("Enter a command: ")
    cmds(ip, command)


def cmds(ip, command):
    if command.lower() == "commands":
        commands = open('commands.txt', 'r')
        content = commands.read()
        print(content)
        commands.close()
        prompt()
    elif command.lower() == "ip":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=query")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("query:", ""))
        prompt()
    elif command.lower() == "status":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=status")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("status:", ""))
        prompt()
    elif command.lower() == "country":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=country")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("country:", "").replace("country:", ""))
        prompt()
    elif command.lower() == "countrycode":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=countryCode")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("countryCode:", ""))
        prompt()
    elif command.lower() == "region":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=region")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("region:", ""))
        prompt()
    elif command.lower() == "regionname":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=regionName")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("regionName:", ""))
        prompt()
    elif command.lower() == "city":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=city")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("city:", ""))
        prompt()
    elif command.lower() == "zip":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=zip")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("zip", ""))
        prompt()
    elif command.lower() == "lat":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=lat")
        print(str(response.text).replace("{", "").replace("}", "").replace('"', "").replace("lat:", ""))
    elif command.lower() == "lon":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=lon")
        print(str(response.text).replace("{", "").replace("}", "").replace('"', "").replace("lon:", ""))
    elif command.lower() == "isp":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=isp")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("isp:", ""))
        prompt()
    elif command.lower() == "org":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=org")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("org:", ""))
        prompt()
    elif command.lower() == "as":
        response = requests.get("http://ip-api.com/json/" + str(ip) +"?fields=as")
        print(response.text.replace('"', "").replace("{", "").replace("}", "").replace("as:", ""))
        prompt()
    elif command.lower() == "all":
        response = requests.get("http://ip-api.com/json/" + str(ip))
        print(response.text.replace(",", "\n").replace('"', "").replace("{", "").replace("}", ""))
        prompt()
    elif command.lower() == "exit":
        print("Exiting in 3 seconds.")
        sleep(3)
        exit()
    elif command.lower() == "export":
        confirm = input("This will overwrite the current results in the results.txt file, are you sure you would like to overwrite them? (Y/N): ")
        if confirm.upper() == "Y":
            print("Overwriting results.txt")
            sleep(1)
            results = open('results.txt', "w")
            response = requests.get("http://ip-api.com/json/" + str(ip))
            results.write(response.text.replace(",", "\n").replace("{", "").replace("}", "").replace('"', ""))
            print("Exported results to results.txt")
            results.close()
            prompt()
        elif confirm.upper() == "N":
            print("Cancelled.")
            prompt()
        else:
            print("Invalid Input")
            prompt()
    else:
        print("Invalid Command. Try using the 'commands' command.")
        sleep(1)
        prompt()

prompt()
