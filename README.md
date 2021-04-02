# SimpleDNS_System
Project 1:Internet Technology

0.
Name: Sai Nayan R Malladi
NetId: srm275
Name: Yeswin Chinta
NetId: ybc9

1. Briefly discuss how you implemented the LS functionality of
   tracking which TS responded to the query and timing out if neither
   TS responded.
   We set the sockets to non-blocking sockets so that the recv() call would not block any other sockets trying to push data. We used the select function which essentially creates a time out function that allows time out in case neither socket ts1 or ts2 is pushing data into the socket. 
2. Are there known issues or functions that aren't working currently in your
   attached code? If so, explain.
   There are no issues in our code, everything should work perfectly. 
3. What problems did you face developing code for this project?
We first tried use a setimeout() function but realized that the select() function was more suitable for our application, through further testing. We also did not realize we had to set different bindings to ts1 and ts2 which made our program return a "Connection reset by Peer " error. Once we realized the issue was in the bindings, we were able to set different bindings to the different sockets, allowing our program to function properly. 
4. What did you learn by working on this project?
We learned the complexity of using different top-level domain servers to communicate with one client and how using different functions like select() help us to make sure that data is not trying to be received from sockets that aren't sending data. Also, this project has overall increased our understanding of how to implement load balancing servers that connect to several servers and only return the applicable outputs. We would've originally just used recv() calls like the last project but now understand why this causes the program to hang and how we can get around it. Overall, this project was very educational and a great learning experience.
