#!/bin/bash
#
# check_clamav_config.sh
# This script compares the current ClamAV configuration (via clamconf)
# with a previously saved reference configuration.
#
# Reference file location: /etc/clamav/clamav_config_reference.txt
# To create an initial reference file, run:
#   sudo clamconf > /etc/clamav/clamav_config_reference.txt
#
# Optionally, you can set up email notifications by specifying your email.

# Set paths for the reference file and temporary current config file
REFERENCE="/etc/clamav/clamav_config_reference.txt"
CURRENT="/tmp/clamav_config_current.txt"

# Optional: specify your email address for notifications (requires mail utils configured)
MAILTO="your-email@example.com"  # <-- change to your email address

# Generate the current configuration output from clamconf
clamconf > "$CURRENT"

# Check if the reference configuration file exists
if [ ! -f "$REFERENCE" ]; then
    echo "Reference configuration file not found at $REFERENCE."
    echo "Creating a new reference configuration file from current settings."
    sudo cp "$CURRENT" "$REFERENCE"
    echo "Reference created. Exiting."
    rm "$CURRENT"
    exit 0
fi

# Compare the current configuration with the reference
DIFF=$(diff "$REFERENCE" "$CURRENT")

if [ -n "$DIFF" ]; then
    echo "Changes detected in ClamAV configuration:"
    echo "$DIFF"
    # Uncomment the following line to enable email notifications.
    # echo "$DIFF" | mail -s "ClamAV Configuration Change Detected" "$MAILTO"
else
    echo "No changes detected in ClamAV configuration."
fi

# Remove the temporary current configuration file
rm "$CURRENT"
