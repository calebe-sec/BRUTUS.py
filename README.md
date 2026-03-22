# BRUTUS.py
Ferramenta de teste ético de autenticação (HTTP/SSH/hash cracking)
# BRUTUS.py – Multi-Protocol Authentication Tester

BRUTUS.py is a **Python-based**, modular authentication testing tool developed for **authorized penetration testing**, **red team operations**, and **educational purposes** in offensive security.

It enables credential guessing (dictionary attacks, brute-force with rules) against common authentication vectors encountered in real-world security assessments.

**⚠️ LEGAL AND ETHICAL DISCLAIMER**  
This tool is **strictly for ethical and legal use only**.  
- You **must** have explicit written permission from the system owner before testing any target.  
- Unauthorized use (including against systems you do not own or have permission to test) is **illegal** and may result in criminal charges.  
- The author is **not responsible** for any misuse, damage, or legal consequences arising from the use of this tool.  
Use responsibly. Test only what you are authorized to test.

## Supported Protocols

| Protocol       | Mode                  | Description                                                                 |
|----------------|-----------------------|-----------------------------------------------------------------------------|
| **HTTP Form**  | Online brute-force   | Attacks web login forms (POST-based). Customizable success/failure detection, CSRF handling, headers, proxies. |
| **SSH**        | Online brute-force   | Targets SSH servers using Paramiko. Supports username lists, password lists, timeouts, rate limiting. |
| **Hash**       | Offline cracking     | Cracks password hashes (MD5, SHA-1, SHA-256, NTLM, bcrypt*, etc.) using wordlists or incremental brute-force. Multi-threaded. |

*Note: bcrypt and slow hashes are supported but performance-limited without GPU acceleration.

## Main Features

- Modular architecture — easy to extend for new protocols
- Threading and rate-limiting to avoid lockouts / detection
- Advanced wordlist handling (combine lists, rules, filtering)
- Proxy support (HTTP, SOCKS, Tor integration optional)
- Detailed logging (successes, failures, timestamps, attempts)
- Colorized console output (via colorama)
- Command-line friendly with argparse (or future config file support)
- Built with clean code practices for learning and contribution

## Installation

```bash
# Clone the repository
git clone https://github.com/SEU_USUARIO/BRUTUS.py.git
cd BRUTUS.py

# Install dependencies
pip install -r requirements.txt
