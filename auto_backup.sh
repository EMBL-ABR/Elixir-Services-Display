#!/bin/bash
today=`date '+%Y_%m_%d'`;
jsonfilename="/home/ubuntu/$today.backup.json";
xmlfilename="/home/ubuntu/$today.backup.xml";
upjsonfilename="$today.backup.json";
upxmlfilename="$today.backup.xml";

echo $jsonfilename;
echo $xmlfilename;
echo $upjsonfilename;
echo $upxmlfilename;

curl -H "Accept: application/json" -X GET https://bio.tools/api/tool > $jsonfilename;
curl -H "Accept: application/xml" -X GET https://bio.tools/api/tool > $xmlfilename;
source EMBL-ABR-01-openrc.sh;

swift upload bio-tools-backups $jsonfilename --object-name $upjsonfilename;
swift upload bio-tools-backups $xmlfilename --object-name $upxmlfilename;

rm $jsonfilename;
rm $xmlfilename;
