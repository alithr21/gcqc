#Documentation

This application is a web-based tool that helps to generate a quick inventory and vulnerability assessment of a Google Cloud Platform (GCP) project. The tool is developed using Flask, a lightweight web framework for Python.

#app.py

This file contains the main Flask application that serves different routes and renders corresponding HTML templates. The following routes are defined:

- / (index): Renders the homepage (index.html).
- /inventory: Runs the inventory.py script and redirects to the /inventory_report route.
- /inventory_report: Renders the inventory.html file generated by the inventory.py script.
- /vulnerabilities: Runs the vulnerability.py script and redirects to the /vulnerability_report route.
- /vulnerability_report: Renders the vulnerability.html file generated by the vulnerability.py script.
- /contact: Renders the contact page (contact.html).
- /recbucket: Renders the recommendation bucket page (recbucket.html).

#inventory.py

This script gathers information about Compute Engine instances, buckets, VPCs, and firewall rules in a GCP project. It uses the gcloud command-line tool and gsutil to retrieve data and stores the data in a CSV file (inventory.csv). Then, it generates an HTML file (inventory.html) to visualize the data.

#vulnerability.py

This script checks for public-facing buckets, instances using default service accounts, and vulnerable firewall rules in a GCP project. It uses gsutil and gcloud command-line tools to retrieve data and stores the data in a CSV file (vulnerabilities.csv). Then, it generates an HTML file (vulnerability.html) to visualize the data.

#index.html

This file contains the main HTML template for the homepage. It consists of buttons for running inventory and vulnerability checks, and links to the recommendation and contact pages. A JavaScript function showLoadingBar is used to display a loading bar while the inventory and vulnerability scripts are executed.

#Running the application

Ensure that Python 3.x and the Flask library are installed.
Ensure that the gcloud and gsutil command-line tools are installed and authenticated.
Run app.py using Python.
Open the URL displayed in the terminal (e.g., http://127.0.0.1:5000/) in your web browser.
After completing these steps, you should see the homepage of the application. Click the "INVENTORY" and "VULNERABILITIES" buttons to generate and view the respective reports.

Author Ali Taheri