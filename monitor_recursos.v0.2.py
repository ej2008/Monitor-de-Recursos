from tkinter import *
import psutil


p = psutil
uso_cpu = 0.0
core_cpu = 0
freq_cpu = 0

class Janela:
    def __init__(self,root):
        y1 = 10
        # criando labels
        self.uso_label = Label(root, text =  "CPU               %",font = "Arial 10").place(x= 50, y= y1*3)
        self.uso_label1 = Label(text= uso_cpu, font = "Arial 10", bg = "white")
        self.uso_label1.place(x=100, y= y1*3)

        self.core_label = Label(root, text =  "Core",font = "Arial 10").place(x= 200, y= y1*3)
        self.core_label1 = Label(text= core_cpu, font = "Arial 10", bg = "white")
        self.core_label1.place(x=250, y= y1*3)

        self.freq_label = Label(root, text =  "Frequência",font = "Arial 10").place(x= 300, y= y1*3)
        self.freq_label1 = Label(text= freq_cpu, font = "Arial 10", bg = "white")
        self.freq_label1.place(x=380, y= y1*3)

        # atualizando labels
        self.uso_label1.configure(text = uso_cpu)
        self.core_label1.configure(text = core_cpu)
        self.freq_label1.configure(text = freq_cpu)


def sensores():
    # sensores
    uso_cpu = p.cpu_percent(0.5)
    core_cpu = p.cpu_count()
    freq_cpu = p.cpu_freq(percpu=False)
    freq_cpu = freq_cpu[0]
        
    return uso_cpu, core_cpu, freq_cpu

  
if __name__ == "__main__":
    root = Tk()
    root.title("Monitor")
    root.geometry("600x400")
    uso_cpu, core_cpu, freq_cpu = sensores()
    print(uso_cpu, core_cpu, freq_cpu )
    Janela(root)
    root.mainloop()
     
    


    
