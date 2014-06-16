d_count=int(raw_input("How many digits?"))

def findme(limit):
    print 1
    count=0
    last_sum=1
    old_sum=0
    new_sum=0
    current_sum=1
    while count <= d_count-1:
        count+=1
        new_sum=last_sum+old_sum
        old_sum=last_sum
        last_sum=new_sum
        current_sum+=new_sum
        print new_sum
        if count == d_count-1:
            break
            
findme(d_count)