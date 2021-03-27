def minion_game(s):
    # your code goes here
    
    v='AEIOU'
    kev=0
    st=0
    n=len(s)
    
    for i in range(n):
        if s[i] in v:
            kev = kev+(n-i)
           
        else:
            st = st+(n-i)
            
    
    if kev > st:
        print('Kevin',kev)
        
    elif kev==st:
        print('Draw')
        
    else:
        print('Stuart',st)

if __name__ == '__main__':
    s = input()
    minion_game(s)