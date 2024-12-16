import pyvisa

def frequency_point(start_freq,stop_freq,points):
    x_values = [start_freq + i * (stop_freq - start_freq) / (points - 1) for i in range(points)]
    return x_values
def fsv3000(command):
    INSTR_IP = '192.168.1.100'
    rm = pyvisa.ResourceManager()  
    fsv = rm.open_resource(f'TCPIP0::{INSTR_IP}::INSTR')
    fsv.write_termination = '\n'
    fsv.read_termination = '\n'
    try:
        fsv.query(command)
    except Exception as e:
        print(f"Error occurred: {e}")

start_freq = fsv3000('FREQ:STAR?')
stop_freq = fsv3000('FREQ:STOP?')
data = fsv3000('TRAC:DATA? TRACE1')
# start_freq = int(input('輸入開始頻率'))
# stop_freq = int(input('輸入截止頻率'))
points = int(input('輸入點數'))
freq = frequency_point(start_freq,stop_freq,points)
