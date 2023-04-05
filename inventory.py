import os
import sys
import csv
import subprocess




def main():    
    # List Compute Engine instances
    compute_instances = subprocess.check_output(['gcloud', 'compute', 'instances', 'list', '--format', 'csv(name,zone,status)'])
    compute_instances = compute_instances.decode().split('\n')

    # List buckets
    buckets = subprocess.check_output(['gsutil', 'ls'])
    buckets = buckets.decode().split('\n')

    # List VPCs
    vpcs = subprocess.check_output(['gcloud', 'compute', 'networks', 'list', '--format', 'csv(name)'])
    vpcs = vpcs.decode().split('\n')

    # List firewall rules
    firewall_rules = subprocess.check_output(['gcloud', 'compute', 'firewall-rules', 'list', '--format', 'csv(name,allowed)'])
    firewall_rules = firewall_rules.decode().split('\n')
    # Write the CSV file
    csv_file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'csv', 'inventory.csv')

    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Compute Engine instances'])
        writer.writerow(['Name', 'Zone', 'Status'])
        for instance in csv.reader(compute_instances):
            if instance:
                writer.writerow(instance)
        writer.writerow([''])
        writer.writerow(['Buckets'])
        writer.writerow(['Name'])
        for bucket in buckets:
            if bucket:
                writer.writerow([bucket])
        writer.writerow([''])
        writer.writerow(['VPCs'])
        writer.writerow(['Name'])
        for vpc in csv.reader(vpcs):
            if vpc:
                writer.writerow(vpc)
        writer.writerow([''])
        writer.writerow(['Firewall rules'])
        writer.writerow(['Name', 'Allowed'])
        for rule in csv.reader(firewall_rules):
            if rule:
                writer.writerow(rule)

    # Generate the HTML file
    html_file_path = os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])), 'templates', 'inventory.html')    
    with open(html_file_path, 'w') as htmlfile:
        # Write the HTML header
        htmlfile.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Inventory</title>\n')
        htmlfile.write('<link rel="stylesheet" href="static/styles.css">\n')
        htmlfile.write('<style>\n')
        htmlfile.write('table, th, td { border: 1px solid black; border-collapse: collapse; padding: 5px; }\n')
        htmlfile.write('th { background-color: #dddddd; }\n')
        htmlfile.write('</style>\n')
        htmlfile.write('</head>\n<body>\n')

        # Write the Compute Engine instances table
        htmlfile.write('<h1>Compute Engine instances</h1>\n')
        htmlfile.write('<table>\n<tr><th>Name</th><th>Zone</th><th>Status</th></tr>\n')
        for instance in csv.reader(compute_instances):
            if instance:
                htmlfile.write('<tr><td>{}</td><td>{}</td><td>{}</td></tr>\n'.format(*instance))
        htmlfile.write('</table>\n')

        # Write the Buckets table
        htmlfile.write('<h1>Buckets</h1>\n')
        htmlfile.write('<ul>\n')
        for bucket in buckets:
            if bucket:
                htmlfile.write('<li>{}</li>\n'.format(bucket))
        htmlfile.write('</ul>\n')

        # Write the VPCs table
        htmlfile.write('<h1>VPCs</h1>\n')
        htmlfile.write('<table>\n<tr><th>Name</th></tr>\n')
        for vpc in csv.reader(vpcs):
            if vpc:
                htmlfile.write('<tr><td>{}</td></tr>\n'.format(*vpc))
        htmlfile.write('</table>\n')

        # Write the Firewall rules table
        htmlfile.write('<h1>Firewall rules</h1>\n')
        htmlfile.write('<table>\n<tr><th>Name</th><th>Allowed</th></tr>\n')
        for rule in csv.reader(firewall_rules):
            if rule:
                htmlfile.write('<tr><td>{}</td><td>{}</td></tr>\n'.format(*rule))
        htmlfile.write('</table>\n')

        # Write the HTML footer
        htmlfile.write('</body>\n</html>\n')


if __name__ == '__main__':
    main()