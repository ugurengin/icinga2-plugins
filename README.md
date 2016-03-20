# VoltDB-Access-Latency-Monitoring

### Requirements
```
voltdbclient
```

### Usage
```
python voltdb-access-latency.py <voltdb-host>
```
 
### Sample Output
```
python ~/plugins/voltdb-access-latency.py <voltdb-host>
OK- Avr: 0.078648ms Max: 0.128303ms |Avr=0.078648;0;0;0, Max=0.128303;0;0;0
```

It returns avr and max latency times with perfdata which is connecting to a node of voltdb cluster.

### Compatible Monitoring
```
Icinga2
Nagios 4.x
```
### Compatible Visualization
```
Graphite 
Grafana
```
<br>
<img height="250" width="2000" src="https://www.ugurengin.com/blog/wp-content/uploads/2016/03/voltdb-access-time-1.jpg">
<br>
