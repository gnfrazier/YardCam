#Notes for YardCam


status is True if camera is in preview mode (ready to capture)  
setup puts camera into preview mode and returns True
shutdown ends preview and returns False

###Flow
initialize camera  
call to website to get sunrise, sunset and other times  

calculate which is next    
calc delay until next  
add offset from event for desired photo time  
pass tuple of offset-delay, number caps, interval

###Camera  
Resolution  
White Balance  
Color  
Brightness  

