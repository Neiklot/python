hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura =int(input("Event duration (minutes): "))

print(((dura//60)+hour+((mins+(dura%60))//60))%24,(mins+(dura%60))%60,sep=":")