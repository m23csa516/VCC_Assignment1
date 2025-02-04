# Virtual Machines Setup & Microservice Deployment

## 📌 Objective
This project involves setting up multiple Virtual Machines (VMs) using VirtualBox, configuring networking between them, and deploying a **Flask-based microservice application** across the VMs. The goal is to establish seamless **API-based communication** between the VMs.

---

## 🏗 Architecture Overview
- **VM1 (Data Provider):** Hosts a Flask API to provide data.
- **Host Machine (Middleware API):** Runs a Flask API that acts as a bridge between VM1 and VM2.
- **VM2 (Frontend Web Page):** Hosts a simple web page that communicates with the Host Machine API.

Each component interacts via API requests, ensuring **smooth data exchange** across VMs.

---

## ⚙️ Setup Instructions

### Install VirtualBox & Create VMs**
- Download and install **VirtualBox** from [here](https://www.virtualbox.org/).
- Create **VM1** with Ubuntu and configure:
  - **Memory:** 2GB RAM
  - **CPU:** 2 Cores
  - **Disk:** 25GB (VDI format)
  - **Network Adapter:** Bridged Adapter
- Clone **VM1** to create **VM2** with a new MAC address.
- Assign **static IP addresses** for networking.

---

### Configure Network Settings**
- Set **Bridged Adapter** to allow VM-to-VM and Host communication.
- Assign **static IPs** to each machine:

  **VM1 (Data Provider)**  
  - IP: `192.168.29.51`
  - Netmask: `255.255.255.0`
  - Gateway: `192.168.29.1`

  **VM2 (Frontend Web Page)**  
  - IP: `192.168.29.52`
  - Netmask: `255.255.255.0`
  - Gateway: `192.168.29.1`

  **Host Machine (Middleware API)**  
  - IP: `192.168.29.19`
  - Netmask: `255.255.255.0`
  - Gateway: `192.168.29.1`

- Verify connectivity:
  ```bash
  ping <VM-IP>
  
### Install Required Dependencies
sudo apt update && sudo apt install python3 python3-pip -y

pip install flask flask-cors requests



### 🚀 Execution Workflow
VM2 (Frontend) sends a request to Host Machine API.

Host Machine forwards the request to VM1.

VM1 (Data Provider) processes and returns the data.

Host Machine relays the response back to VM2.

VM2 displays the data on the web page.

This establishes successful inter-VM communication


### 🛠 Troubleshooting
If the frontend (VM2) cannot fetch data from the API:

Install Flask-CORS: pip install flask-cors

### 📚 References
VirtualBox Networking Modes – Oracle Documentation https://www.virtualbox.org/manual/ch06.html

VMware Networking Guide – VMware Docs https://docs.vmware.com/en/VMware-Workstation-Pro/index.html

Ubuntu Network Configuration (for static IP and host-only networks) https://ubuntu.com/server/docs/network-configuration

Flask Official Documentation – Building REST APIs https://flask.palletsprojects.com/en/latest/

Flask & Requests Library – API Communication https://requests.readthedocs.io/en/latest/

Flask Deployment Guide (Production Ready) – Flask Docs https://flask.palletsprojects.com/en/2.0.x/tutorial/deploy/

Flask-CORS GitHub & Docs – How to Enable CORS for Cross-Origin Requests https://flask-cors.readthedocs.io/en/latest/

Understanding CORS (Cross-Origin Resource Sharing) – MDN Web Docs https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS

### Recorded Video: https://drive.google.com/file/d/18VBMmDdkE3OicpChSruFxsd56z8eaqC1/view?usp=sharing


