import subprocess

class Battery_Percentage:

    def __init__(self) -> None:
        pass

    def __getpercentage__():
        cmd = 'pmset -g batt | grep -Eo "\d+%" | cut -d% -f1'
        ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0]
        return int(output)

# -------- -------- -------- Testing Raw Code -------- -------- --------#

# cmd = 'pmset -g batt | grep -Eo "\d+%" | cut -d% -f1'
# ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
# output = ps.communicate()[0]
# print(str(output).split("'"))