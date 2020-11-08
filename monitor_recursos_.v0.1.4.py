# _*_ coding: utf-8 _*_

'''
Projeto iniciado em 06/09/2019
13/09/2019 - v0.1.3 - acrecido do time epoch
09/20 - v0.1.4 tentando alterar o calcul de estimativa de tempo da bateria
'''
from tkinter import *
import psutil as p
import time


# variáveis
uso_cpu = 0.0
core_cpu = 0
y1 = 60
y2 = 140
y3 = 220
y4 = 300
f1 = 40


# configuração janela
root = Tk()
root.title("Monitor")
root.geometry("600x400")


def calc_batery():
    try:
        batery = list(p.sensors_battery())
        batery[0] = str(batery[0]) + " %"
        if type(batery[1]) == type(int()):
            dia = batery[1] // 86400
            aux_d = batery[1] % 86400
            hora = aux_d // 3600
            aux_h = aux_d % 3600
            minuto = aux_h // 60
            segundo = aux_h % 60
    
            batery[1] = "{:3} - {:02}:{:02}:{:02}".format(int(dia),int(hora),
                                                          int(minuto),int(segundo))
        else:
            batery[1] = "--"
        if batery[2]:
            batery[2] = ("Adaptador AC")
        else:
            batery[2] = ("Bateria")    

        return batery                                          
            
    except TypeError as erro:
        batery= ["s/ Bateria", "--", "Adaptador AC"]

        return batery
    
        
def calc_disk():
    disk = list(p.disk_usage("C:\\"))
    for i in range(len(disk)):
        if i in (0,1,2):
            if 10**3 < disk[i] < 10**6 :
                disk[i] = str(round(i/10**3, 2))+ " KB"
            elif 10**6 < disk[i] < 10**9 :
                disk[i] = str(round(disk[i]/10**6, 2))+ " MB"
            elif 10**9 < disk[i] < 10**12 :
                disk[i] = str(round(disk[i]/10**9, 2))+ " GB"
            elif 10**12 < disk[i] < 10**15 :
                disk[i] = str(round(disk[i]/10**12, 2))+ " TB"
        elif i == 3:
            disk[i] = (str(disk[i]) + " %")
               
    return disk # memory[disk_total, disk_uso, disk_free, disk_percent}


def calc_memory():
    memory = list(p.virtual_memory())
    for i in range(len(memory)):
        if i in (0,1,3,4):
            if 10**3 < memory[i] < 10**6 :
                memory[i] = str(round(memory[i]/10**3, 2))+ " KB"
            elif 10**6 < memory[i] < 10**9 :
                memory[i] = str(round(memory[i]/10**6, 2))+ " MB"
            elif 10**9 < memory[i] < 10**12 :
                memory[i] = str(round(memory[i]/10**9, 2))+ " GB"
            elif 10**12 < memory[i] < 10**15 :
                memory[i] = str(round(memory[i]/10**12, 2))+ " TB"
        elif i == 2:
            memory[i] = (str(memory[i]) + " %")
       
    return memory  # memory[total_memory, available_memory, percent_memory, use_memory, free_memory}


def convert_time():
    boot_time = p.boot_time()
    time_now = time.time()

    boot_tempo =  time_now - boot_time 
    dia = boot_tempo // 86400
    aux_d = boot_tempo % 86400
    hora = aux_d // 3600
    aux_h = aux_d % 3600
    minuto = aux_h // 60
    segundo = aux_h % 60

    if dia <= 0:
        return "{:02}:{:02}:{:02}".\
               format(int(hora),int(minuto),int(segundo))
    else:
        return "{:3} - {:02}:{:02}:{:02}".\
               format(int(dia),int(hora),int(minuto),int(segundo))

    
def sensores():
    # sensores
    uso_cpu = p.cpu_percent(interval=None, percpu=False)
    time_display = convert_time()
    sensor_bat = calc_batery()
    freq_cpu = p.cpu_freq(percpu=False)
    data_memo = calc_memory()
    uso_disk = calc_disk()
    
    return uso_cpu , freq_cpu, data_memo, uso_disk, sensor_bat, \
           time_display


def atualiza():
    # atualizando labels
    uso_cpu,freq_cpu, data_memo, uso_disk, sensor_bat, time_display = sensores()
    display_time["text"] = time_display
    bat_percent["text"] = sensor_bat[0]
    bat_time["text"] = sensor_bat[1]
    bat_plugged["text"] = sensor_bat[2]
    uso["text"] = str(uso_cpu) + " %"
    freq["text"] = str(round(freq_cpu[0] / 1000, 2)) + " GHz" 
    total_memory["text"] = data_memo[0]
    available_memory["text"] = data_memo[1]
    percent_memory["text"] = data_memo[2]
    use_memory["text"] = data_memo[3]
    free_memory["text"] = data_memo[4]
    disk_total["text"] = uso_disk[0]
    disk_uso["text"] = uso_disk[1]
    disk_free["text"] = uso_disk[2]
    disk_percent["text"] = uso_disk[3]
    
    root.after(1000, atualiza)


# criando labels
users_lb = Label(text ="Usuário: ",font = "Arial 15").place(x= 50, y= 10)
user = Label(text= "", font = "Arial 10", bg = "white")
user.place(x= 150, y= 10)

# info time epoch
display_time_lb = Label(text= "Tempo de atividade:", font= "Arial 10").place(x= 300, y= 10)
display_time = Label(text= "00:00:00:00", font= "Arial 10", bg= "white")
display_time.place(x= 450, y= 10)

# info da(s) CPU(s)
cpus_lb = Label(text =  "CPUs:",font = "Arial 15").place(x= 50,y=y1)
uso_lb = Label(text =  "CPU:",font = "Arial 10").place(x= 50, y=y1 + f1)
uso = Label(text= "0", font = "Arial 10", bg = "white")
uso.place(x= 100, y= y1+ f1)

# info Núcleos
cores_lb = Label(text =  "Cores",font = "Arial 15").place(x= 220, y= y1)
core_lb = Label(text =  "Core:",font = "Arial 10").place(x= 220, y= y1+ f1)
core = Label(text= "0", font = "Arial 10", bg = "white")
core.place(x=270, y= y1+ f1)

# info Frequências
freqs_lb = Label(text =  "Frequências",font = "Arial 15").place(x= 350, y= y1)
freq_lb = Label(text =  "Frequência:",font = "Arial 10").place(x= 350, y= y1+ f1)
freq = Label(text = "0", font = "Arial 10", bg = "white")
freq.place(x= 450, y= y1+ f1)

# info da memoria
memory_lb = Label(text = "Memorias", font = "Arial 15").place(x= 50,
                                                                 y= y2)
total_memory_lb = Label(text = "Total:", font = "Arial 10").place(x= 50,
                                                                 y= y2+ f1)
total_memory = Label(text= "0", font = "Arial 10", bg = "white")
total_memory.place(x= 86, y= y2+ f1)
available_memory_lb = Label(text = "Disponível:", font = "Arial 10").place(
    x= 144,y=  y2+ f1)
available_memory = Label(text= "0", font = "Arial 10", bg = "white")
available_memory.place(x= 212, y= y2+ f1)
percent_memory_lb = Label(text = "Uso %:", font = "Arial 10").place(x= 472,
                                                                     y= y2+ f1)
percent_memory = Label(text= "0", font = "Arial 10", bg = "white")
percent_memory.place(x= 522, y= y2+ f1)
use_memory_lb = Label(text = "Uso:", font = "Arial 10").place(x= 283, y= y2+ f1)
use_memory = Label(text= "0", font = "Arial 10", bg = "white")
use_memory.place(x= 313, y= y2+ f1)
free_memory_lb = Label(text = "Livre:", font = "Arial 10").place(x= 372,
                                                                 y= y2+ f1)
free_memory = Label(text= "0", font = "Arial 10", bg = "white")
free_memory.place(x= 407, y= y2+ f1)
# Info do disco
disk_lb = Label(text = "Disco", font = "Arial 15").place(x= 50, y= y3)
disk_total_lb = Label(text = "Total:", font = "Arial 10").place(x= 50, y= y3+ f1)
disk_total = Label(text= "0", font = "Arial 10", bg = "white")
disk_total.place(x= 100, y= y3+ f1)
disk_uso_lb = Label(text = "Uso:", font = "Arial 10").place(x= 180,y= y3+ f1)
disk_uso = Label(text= "0", font = "Arial 10", bg = "white")
disk_uso.place(x= 230, y= y3+ f1)
disk_free_lb = Label(text = "Livre:", font = "Arial 10").place(x= 320,
                                                                 y= y3+ f1)
disk_free = Label(text= "0", font = "Arial 10", bg = "white")
disk_free.place(x= 370, y= y3+ f1)
disk_percent_lb = Label(text = "Disco:", font = "Arial 10").place(x= 450,
                                                                     y= y3+ f1)
disk_percent = Label(text= "0", font = "Arial 10", bg = "white")
disk_percent.place(x= 500, y= y3+ f1)

# info bateria
batery_lb = Label(text ="Energia: ",font = "Arial 15").place(x= 50, y= y4)
bat_percent_lb = Label(text ="Bateria: ",font = "Arial 10").place(x= 50, y= y4+ f1)
bat_percent = Label(text ="0 ",font = "Arial 10")
bat_percent.place(x= 110, y= y4+ f1)
bat_time_lb = Label(text ="Tempo: ",font = "Arial 10").place(x= 400, y= y4+ f1)
bat_time = Label(text ="0 ",font = "Arial 10")
bat_time.place(x= 450, y= y4+ f1)
bat_plugged_lb = Label(text ="Energia: ",font = "Arial 10").place(x= 190, y= y4+ f1)
bat_plugged = Label(text= "0", font = "Arial 10")
bat_plugged.place(x= 260, y= y4+ f1)

# lendo os primeiros parametros
u = p.users()

# Inserindo dados estáticos
user["text"] = u[0][0]                                                             
core["text"] = p.cpu_count(logical=True)


if __name__ == "__main__":
    atualiza()
    root.mainloop()    
