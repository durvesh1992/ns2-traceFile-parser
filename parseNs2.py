import sys
import os

####################################################
              ##FUNCTION##
####################################################

# Parse the file 
def parse_file(results, input_file):
    print "Parsing the file "
    for line in input_file:
        if (line == "\n"):
            continue
        results.append(str(line).strip(' ').rstrip('\n'))
    return results

# Node 0
def node0_sent_bits(fileList):
    #print "Calculating Number of bits sent by Node 0"
    sum = 0
    for i in range(len(fileList)):
        if fileList[i][0] == 's' and fileList[i][2] == '_0_' and fileList[i][7] == 'tcp' :
            sum += int(fileList[i][8])
            #print fileList[i]
    return sum*8       

# Node 1
def node1_sent_bits(fileList):
    #print "Calculating Number of bits sent by Node 1"
    sum = 0
    for i in range(len(fileList)):
        if fileList[i][0] == 's' and fileList[i][2] == '_1_' and fileList[i][7] == 'tcp' :
            sum += int(fileList[i][8])
    return sum*8       
 
# Node 2
def node2_sent_bits(fileList):
    #print "Calculating Number of bits sent by Node 2"
    sum = 0
    for i in range(len(fileList)):
        if fileList[i][0] == 's' and fileList[i][2] == '_2_' and fileList[i][7] == 'tcp' :
            sum += int(fileList[i][8])
    return sum*8       


# Node 0 Recv
def node0_recv_bits(fileList):
    #print "Calculating Number of bits received by Node 0"
    recv = 0
    for i in range(len(fileList)):
        if fileList[i][0] == 'r' and fileList[i][2] == '_0_' and fileList[i][7] == 'tcp' and fileList[i][3] == 'MAC' and int(fileList[i][8]) >= 512 :
            recv += int(fileList[i][8])
            print "FileList:",fileList[i]
    return recv*8      


# Node 1 Recv
def node1_recv_bits(fileList):
    #print "Calculating Number of bits received by Node 1"
    recv = 0
    for i in range(len(fileList)):
        if fileList[i][0] == 'r' and fileList[i][2] == '_1_' and fileList[i][7] == 'tcp' and fileList[i][3] == 'MAC' and int(fileList[i][8]) >= 512 :
            if fileList[i][7] != 'tcp':
                print fileList[i][7]
            recv += int(fileList[i][8])
    return recv*8      


# Node 1 Recv from Node 0
def node1_recv_bits_node0(fileList):
    #print "Calculating Number of bits received by Node 1 from Node 0"
    recv = 0
    for i in range(len(fileList)):
        if fileList[i][0] == 'r' and fileList[i][2] == '_1_' and fileList[i][7] == 'tcp' and fileList[i][3] == 'MAC' and fileList[i][14] == '[0:0' and int(fileList[i][8]) > 512:
            recv += int(fileList[i][8])
            #print "MyFile: ",fileList[i]
    return recv*8      

# Node 1 Recv from Node 2
def node1_recv_bits_node2(fileList):
    #print "Calculating Number of bits received by Node 1 from Node 2"
    recv = 0
    for i in range(len(fileList)):
        if fileList[i][0] == 'r' and fileList[i][2] == '_1_' and fileList[i][7] == 'tcp' and fileList[i][3] == 'MAC' and fileList[i][14] == '[2:0' and int(fileList[i][8]) > 512:
            recv += int(fileList[i][8])
    return recv*8      

# Node 2 Recv
def node2_recv_bits(fileList):
    #print "Calculating Number of bits received by Node 2"
    recv = 0
    for i in range(len(fileList)):
        if fileList[i][0] == 'r' and fileList[i][2] == '_2_' and fileList[i][7] == 'tcp' and fileList[i][3] == 'MAC':
            recv += int(fileList[i][8])
    return recv*8      

# Count the total number of packets dropped
def node_drop_packets(fileList):
    #print "Calculating Dropped Packets "
    count = 0
    for i in range(len(fileList)):
        if fileList[i][0] == 'D':
            count += 1
    return count      

# Calculate the throughput
def calc_throughput(recv1):
    #print "Calculating throughput"
    throughput = int(recv1)/(5.5*1000) 
    return throughput


####################################################
              ##MAIN FUNCTION##
####################################################
 
#define some random list
results = []
fileList = []

# read and parse the file 
input_file = open("wireless-simple-mac_100.tr", "r")
results = parse_file(results, input_file)
#print "Result of file:",results[0]
#print "Length of file",len(results)

# iterate through the total results and create comma seperate list of list
for i in range(len(results)):
    fileList.append(results[i].split(' '))

#print "List obained: ",fileList[4]
#print "List obained: ",fileList[4][14]
#print "File list ka length", len(fileList)


####################################################
      ## CALL THE FUNCTIONS TO GET OUTPUT ##
####################################################
 

# calculate  total number of bits sent by the node 1
sum0 = node0_sent_bits(fileList)
sum1 = node1_sent_bits(fileList)
sum2 = node2_sent_bits(fileList)


# calculate  total number of bits Received by the users
recv0 = node0_recv_bits(fileList)
recv1 = node1_recv_bits(fileList)
recv2 = node2_recv_bits(fileList)
recv3 = node1_recv_bits_node0(fileList)
recv4 = node1_recv_bits_node2(fileList)

# count the total number of dropped packets
count = node_drop_packets(fileList)

# calculate throughput
throughput1 = calc_throughput(recv1)
throughput2 = calc_throughput(recv3)
throughput3 = calc_throughput(recv4)

####################################################
              ## DISPLAY THE OUTPUT ##
####################################################
 
print "a) Calculate the total number of bits sent by each user ?"
print "    Total number of bits SENT by NODE 0: ",sum0
print "    Total number of bits SENT by NODE 1: ",sum1
print "    Total number of bits SENT by NODE 2: ",sum2
print " "

print "b) Calculate the total number of bits received by each user ?"
print "    Total number of bits RECEIVED by NODE 0: ",recv0
print "    Total number of bits RECEIVED by NODE 1: ",recv1
print "    Total number of bits RECEIVED by NODE 2: ",recv2
print " "

print "c) Calculate the total number of packets dropped ?"
print "    Total number of DROPPED packets in the NETWORK:",count
print " "


print "d) Calculate throughput of each user ?"
print "    Total number of bits RECEIVED by NODE 1 FROM NODE 0 : ",recv3
print "    Total number of bits RECEIVED by NODE 1 FROM NODE 2 : ",recv4
print "    Throughput at node 1, TRANSMITTED BY NODE 0:"+str(throughput2)+" Kbps"
print "    Throughput at node 1, TRANSMITTED BY NODE 2:"+str(throughput3)+" Kbps"
print " "

print "e) Calculate Network throughput ?"
print "    Network Throughput:"+str(throughput1)+" Kbps"
print " "



