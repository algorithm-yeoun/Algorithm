def solution(video_len, pos, op_start, op_end, commands):
    video_len_num = video_len.replace(':','')
    minutes, second = pos.split(':')
    op_start_num = int(op_start.replace(':',''))
    op_end_num = op_end.replace(':','')
    
    def panel(minutes, second):
        now = int(minutes+second)
        if now<0:
            minutes, second = '00', '00'
        elif op_start_num<=now<=int(op_end_num):
            minutes, second = op_end_num[:2], op_end_num[-2:]
        elif now>int(video_len_num):
            minutes, second = video_len_num[:2], video_len_num[-2:]

        return minutes, second
        
    minutes, second = panel(minutes, second)
    
    for command in commands:
        if command =='prev':
            second = int(second)-10
            if second<0:
                if int(minutes)>0:
                    second += 60    
                    minutes = int(minutes)-1
                else:
                    minutes, second = 0, 0
        else:
            second = int(second)+10
            if second>59:
                second -= 60
                minutes = int(minutes)+1
        minutes = '0'+str(minutes) if len(str(minutes))<2 else str(minutes)
        second = '0'+str(second) if len(str(second))<2 else str(second)
        
        minutes, second = panel(minutes, second)
                
    return minutes+":"+second