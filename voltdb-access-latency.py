#!/usr/bin/env python

#################################################################################
# VoltDB Cluster Access Latency                                                 #
# Client Interface Library:                                                     #
# https://github.com/VoltDB/voltdb-client-python/blob/master/voltdbclient.py    #
# Ugur Engin                                                                    #
#################################################################################

import os, sys
from voltdbclient import *

nano = 1000000000.0
avglatencytrigger = .01 * nano   # 10 milliseconds
maxlatencytrigger = 2 * nano     # 2 seconds

server = str(sys.argv)
if (len(sys.argv) > 1): server = sys.argv[1]
else:
   print "required a host\nexample: python voltdb-access-latency.py <voltdb-host>"
   raise SystemExit, 3

client = FastSerializer(server, 21212)
stats = VoltProcedure( client, "@Statistics",
   [ FastSerializer.VOLTTYPE_STRING,
     FastSerializer.VOLTTYPE_INTEGER ] )

# Check latency
response = stats.call([ "procedureprofile", 1 ])
avglatency = 0
maxlatency = 0
for t in response.tables:
   for row in t.tuples:
      if (avglatency < row[4]): avglatency = row[4]
      if (maxlatency < row[6]): maxlatency = row[6]

def pd():
     a='Avr=' + str(avglatency / 1000000.0)+';0;0;0' + ',' + ' ' + 'Max=' + str(maxlatency / 1000000.0)+';0;0;0'
     return a

if (avglatency > avglatencytrigger):
   print 'Warning- Average latency exceeds limit: ' + str(avglatency / 1000000.0)
   raise SystemExit, 1
elif (maxlatency > maxlatencytrigger):
   print 'Critical- Maximum latency exceeds limit: ' + str(maxlatency / 1000000.0)
   raise SystemExit, 2
else:
   print 'OK-' + ' '+ 'Avr: ' + str(avglatency / 1000000.0) + '' + 'ms' + ' ' + 'Max: ' + str(maxlatency / 1000000.0)+ ''+ 'ms' + ' |' + pd()
   raise SystemExit, 0

client.close()
