# SimpleDNS_System
Project 1:Internet Technology

0.
Name: Sai Nayan R Malladi
NetId: srm275
Name: Yeswin Chinta
NetId: ybc9

1.
The recursive client functionality works by holding keeping the connection to the servers alive in a while loop that breaks once all the PROJI-HNS.txt data has been parsed through. Therefore, each parsed line will recieve data back in a continuous stream. The TS connection stays opened till the end should it need to be opened as well, working in a similar way. ALl this logic is within the client's while loop.

2.
After removing threading, we have not seen logistical issues. Rather, once it runs it should work in accordance with the instructions. However, running on different machines on different IP addresses was confusing, as the sockets did not seem to find the host address from one partners' house to another partners' house. But that case was not clear in the instructions. I am confidant it works on ilabs and within networks (on different machines) and no doubt on the same machine as well.

3.
Dealing with running all three files at the same time was new and confusing. Lack of experience led to difficulty testing and dealing with the multi-machine aspect. Originally expanded project 0 using threading but quickly found that solution may be quite difficult to use. The logic and conceptually the project was pretty simple in scope and digestible. Found that in the coding experience non-class material issues were the hardest part of the project, particularly multi-processing. The abort connection and reconnection errors took a lot of time to debug as they were not typical errors seen from previous coding experience we had of course. Searching the errors up gave little help so those aspects took the bulk of our time.

4.
Learned a great deal about socket programming and server connections, as well as encoded data being sent between connections. As well as general python programming like digging into import documentation to understand whether its valid for use on a multi-machine connection. Socket methods and how ports work are the clearest examples of what we can take away from this project long-term.