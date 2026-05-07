# Enterprise Network Topology on GNS3

A two-phase network security project: **design** of a full enterprise network topology, followed by **insider attack simulations** to evaluate its security resilience.

![GNS3](https://img.shields.io/badge/GNS3-Network%20Emulator-00ADEF?logo=cisco&logoColor=white)
![Python](https://img.shields.io/badge/Python-Attack%20Scripts-3776AB?logo=python&logoColor=white)
![Networking](https://img.shields.io/badge/Cisco-IOS%20%2F%20Routing-1BA0D7?logo=cisco&logoColor=white)
![Security](https://img.shields.io/badge/Security-Insider%20Attacks-red)

---

## 📌 Overview

This project develops an **advanced enterprise network topology** for a corporate entity using GNS3, then stress-tests it by simulating realistic **insider attacks**. GNS3 is a network emulator that combines virtual and real devices to simulate complex networks using Cisco IOS via Dynamips.

---

## 🏗️ Phase 1 — Network Design

The topology covers all major components of a real enterprise network:

- **Campus network** — end-user workstations, VLANs, access/distribution/core switching layers
- **Data Center** — servers with redundant connectivity
- **DMZ (Demilitarised Zone)** — public-facing services isolated from the internal network
- **ISP integration** — internet connectivity with BGP/routing toward upstream providers
- **Firewall & Security Group** — perimeter protection between zones

> See [`Topology.png`](./Topology.png) for the full network diagram.

---

## 🔥 Phase 2 — Insider Attack Simulations

Unlike external penetration tests, insider attacks are conducted by individuals who already have authorised access to the network, making them potentially more damaging and harder to detect.

Three attack scenarios were simulated using Python scripts with Scapy:

### Attack Scripts

| Script | Attack Type | Description |
|--------|------------|-------------|
| `dhcpstarvation.py` | **DHCP Starvation** | Floods the DHCP server with fake MAC address requests to exhaust the IP address pool, denying new legitimate clients from getting an IP |
| `dnspoisoning.py` | **DNS Poisoning** | Intercepts and forges DNS responses to redirect victims to malicious destinations |
| `vlanhopping.py` | **VLAN Hopping** | Exploits misconfigured trunk ports to send traffic across VLANs that should be isolated |

---

## 📁 Project Structure

```
Creation-of-an-enterprise-Network-Topology-on-GNS3/
├── Attack-scripts/
│   ├── dhcpstarvation.py      # DHCP starvation attack
│   ├── dnspoisoning.py        # DNS poisoning attack
│   └── vlanhopping.py         # VLAN hopping attack
├── Configuration files/       # Cisco device configurations
├── Topology.png               # Full network diagram
└── README.md
```

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|------|---------|
| GNS3 | Network topology emulation |
| Cisco IOS (via Dynamips) | Router and switch emulation |
| Python + Scapy | Attack script development |
| VLANs, BGP, OSPF | Routing and segmentation protocols |

---

## ⚠️ Disclaimer

All attack simulations were performed in a **controlled lab environment** for **educational purposes only**. The scripts and techniques described here must not be used on any real network without explicit authorisation. Unauthorised use may be illegal.
