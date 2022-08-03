def days(n_days, day):
    dicc_days = {1:'monday', 2:'tuesday', 3:'wednesday', 4:'thursday', 5:'friday',
                 6:'saturday', 7:'sunday'}
    day = day.lower()
    today = 0
    for k, v in dicc_days.items():
        if day == v:
            today = k

    n_semanas = n_days // 7
    n_day = n_days % 7 
    prox_day = today+ n_days
    
    if prox_day >7:
        prox_day = 7 - n_day

    day_buscado = dicc_days.get(prox_day)

    return day_buscado.capitalize()

    
def add_time(start, duration, day=None):
    
    ls = start.split()
    #formato de hora PM or AM
    fh_start = ls[1]
    
    time_start = ls[0].split(':')
    sh = time_start[0]
    sm = time_start[1]
    if sm == '00':
        sm ='0'
    else:
        sm = sm.lstrip('0')
    
    time_dur = duration.split(':')
    dh = time_dur[0]
    dm = time_dur[1]
    if dm == '00':
        dm ='0'
    else:
        dm = dm.lstrip('0')
    
    hora_inicio = eval(sh)
    hora_dur = eval(dh) 
    minut_inicio = eval(sm)
    minut_dur = eval(dm)
    
    if fh_start == 'PM':
        hora_inicio += 12
    
    new_minut = minut_inicio + minut_dur
    new_fh = 'AM'
    n_days = 0
    
        
    if new_minut>60:
        new_minut = new_minut -60
        hora_dur +=1
    
    new_hour = hora_inicio + hora_dur
    
    if new_hour >24:
        n_days = new_hour // 24
        new_hour = new_hour - n_days*24
    if new_hour >=12:
        new_hour -= 12
        new_fh = 'PM'
        
    if day:
        prox = days(n_days, day)
        new_fh = new_fh + ', ' + prox
        
        
    if new_hour==0:
        new_hour = 12
    
    if n_days ==1:
        new_fh = new_fh + ' (next day)'
        
    elif n_days >1:
        new_fh = new_fh + ' (' + str(n_days) + ' days later)'
        
    new_minut = str(new_minut)
    if len(new_minut) ==1:
        new_minut = '0'+ new_minut

    new_time = str(new_hour) +':' + str(new_minut) + ' ' + new_fh
    
    return new_time