#!/usr/bin/env python3
import json
import sys

filename="PT1H.json"

iid=dict()
sip=dict()
sip400=dict()
sip500=dict()
count=0
c400=0
c500=0
with open(filename) as fp: 
	for line in fp:
		j = json.loads(line) 
		# Count total number of requests
		count += 1

		# Check how is distribution instanceId
		if j["properties"]["instanceId"] not in iid.keys():
			iid[j["properties"]["instanceId"]] = 1
		else:
			iid[j["properties"]["instanceId"]] += 1

		# Check the host server distribution
		if j["properties"]["serverRouted"] not in sip.keys():
                        sip[j["properties"]["serverRouted"]] = 1
		else:
                        sip[j["properties"]["serverRouted"]] += 1

		# Check 400 distribution between the servers
		if j["properties"]["httpStatus"] > 399 and j["properties"]["httpStatus"] < 500:
			if j["properties"]["serverRouted"] not in sip400.keys():
                        	sip400[j["properties"]["serverRouted"]] = 1
			else:
                        	sip400[j["properties"]["serverRouted"]] += 1
                # Check 500 distribution between the servers
		if j["properties"]["httpStatus"] > 499 and j["properties"]["httpStatus"] < 600:
                        if j["properties"]["serverRouted"] not in sip500.keys():
                                sip500[j["properties"]["serverRouted"]] = 1
                        else:
                                sip500[j["properties"]["serverRouted"]] += 1
		
		# Count 4xx requests
		if j["properties"]["httpStatus"] > 399 and j["properties"]["httpStatus"] < 500:
			c400 += 1
			print(str(j["properties"]["httpStatus"]) + " " + str(j["properties"]["serverStatus"]) + " " + j["properties"]["httpMethod"] + " " + j["properties"]["host"] + j["properties"]["requestUri"] + "?" + j["properties"]["requestQuery"] + " |\"" + j["properties"]["userAgent"] + "\"" + " " + str(j["properties"]["serverResponseLatency"]))
		# Count 5xx requests
		if j["properties"]["httpStatus"] > 499 and j["properties"]["httpStatus"] < 600:
			#print(str(j["properties"]["httpStatus"]) + " " + str(j["properties"]["serverStatus"]) + " " + j["properties"]["httpMethod"] + " " + j["properties"]["host"] + j["properties"]["requestUri"] + "?" + j["properties"]["requestQuery"] + " |\"" + j["properties"]["userAgent"] + "\"" + " " + str(j["properties"]["serverResponseLatency"]))
			c500 += 1
print("")

# Print results			
print("Total requests: " + str(count), file=sys.stderr)
print("Number of 4xx: " + str(c400), file=sys.stderr)
print("Number of 5xx: " + str(c500), file=sys.stderr)
print("", file=sys.stderr)
print("Instance ID Distribution", file=sys.stderr)
for key in iid:
	print(key + ": " + str(iid[key]), file=sys.stderr)
print("Lenght: " + str(len(iid)), file=sys.stderr)

print("", file=sys.stderr)
print("Server IP Distribution", file=sys.stderr)
for key in sip:
        print(key + ": " + str(sip[key]), file=sys.stderr)
print("Lenght: " + str(len(sip)), file=sys.stderr)

print("", file=sys.stderr)
print("Server IP Distribution over 4xx", file=sys.stderr)
for key in sip400:
        print(key + ": " + str(sip400[key]), file=sys.stderr)
print("Lenght: " + str(len(sip400)), file=sys.stderr)

print("", file=sys.stderr)
print("Server IP Distribution over 5xx", file=sys.stderr)
for key in sip500:
        print(key + ": " + str(sip500[key]), file=sys.stderr)
print("Lenght: " + str(len(sip500)), file=sys.stderr)