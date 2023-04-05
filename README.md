# GCQC
# Google Cloud Quick Check - Inventory and Vulnerability Identifier  
Pentesting and Inventory of Google Cloud Deployment

This application has been created as a research project for Douglas College, BC Canada.

GCQC is a web application that admins and pen testers can run in their Google cloud deployments to quickly get an overview of their main assets and then use the vulnerability detector function to identify any miss configuration in those assets and check if proper security measures has been taken to safe guard the cloud assets.
on top of inventory and vulnerability, you have a recommendation page that would instruct you on how to fix or solve the identified vulnerabilities.

# Main Functions:
- Inventory: overview of 1- Compute Engine Instances (name, zone, status) 2- Storage Buckets 3- VPCs 4- Firewall Rules.
- Vulnerability: 1- Public Facing Buckets 2- Instances that use default service account credentials 3- Vulnerable firewall rules.
- Recommendation: Reasoning, Step-by-Step guide to mitigate the risk, type of attack you might be facing.

# Getting Started - Setup

1-	Download the code from https://github.com/alithr21/gcqc.git (easier to get the zipped file).

2-	Sign into the organization google cloud environment as admin.

3-	Open the shell.

4-  Authorize your shell (run any command ex: gsutil).

5-	Press the “Open Editor “button to go to the editor.

6-	Drag and drop the app folder to your file system.

7-	Click on the app.py and press the green Play icon to run it.

8-	Click the newly created browser link in your cloud shell.

** Important note: Only an admin with full privilege can run the program completely with all the functions. Make sure you authorize your shell environment before running the application.

*Ensure that Python 3.x and the Flask library are installed.

Contact me regarding any issues or bugs.
malitrix@yahoo.com

Programmer: Ali Taher

Instructor: Prof. Stephen Chiong



