from martypy import Marty

# Replace with your robot's IP address
ip_address = "192.168.0.107"

# Create a Marty object and connect
marty = Marty("wifi", ip_address)

# Test connection (for test)
marty.dance()
