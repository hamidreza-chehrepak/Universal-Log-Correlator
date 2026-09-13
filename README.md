\# Universal-Log-Correlator



A Python-based Mini-SIEM and Security Log Correlation Engine designed for Security Operations Center (SOC) environments.



\## Features



\- Log parsing and normalization

\- Security event modeling with Pydantic

\- Event correlation by source IP and username

\- Brute-force attack detection

\- Security alert generation

\- Threat severity classification

\- Automated testing with pytest



\## Detection Example



The system detects multiple failed login attempts from the same source IP and username.



Example:



```text

Source IP: 192.168.1.50

Username: admin

Failed Attempts: 4

Severity: HIGH

