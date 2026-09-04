from dataclasses import dataclass
import subprocess

@dataclass(frozen=True)
class Connection:
    protocol:str
    local:str
    remote:str
    state:str

def snapshot()->list[Connection]:
    commands=[["ss","-tun"],["netstat","-ano"]]
    for command in commands:
        try: text=subprocess.check_output(command,text=True,stderr=subprocess.DEVNULL)
        except (OSError,subprocess.CalledProcessError): continue
        rows=[]
        for line in text.splitlines()[1:]:
            parts=line.split()
            if len(parts)>=4: rows.append(Connection(parts[0],parts[-3],parts[-2],parts[1] if parts[1] in {"ESTAB","LISTEN","TIME_WAIT"} else ""))
        return rows
    return []
