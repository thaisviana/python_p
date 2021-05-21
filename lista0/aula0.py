import psutil

disco = psutil.disk_usage('.')

def format_memory(info):
    return round(info/(1024*1024*1024), 2)

print(f"Total:   {format_memory(disco.total)} GB")
print(f"Em uso:  {format_memory(disco.used)} GB")
print(f"Livre:   {format_memory(disco.free)} GB")

print("Percentual de Disco Usado:", disco.percent)

dic_interfaces = psutil.net_if_addrs()
print(dic_interfaces['wlan0'][0].address)