# SimpleScan

A Python-based network security scanning tool that provides multiple scanning capabilities including port scanning, network discovery, and vulnerability detection. SimpleScan offers an intuitive command-line interface for security professionals and network administrators.

## Features

- **Port Scanning**: Identify open ports on target systems
- **Network Discovery**: Detect active hosts on a network
- **Service Detection**: Identify services running on discovered ports
- **Vulnerability Scanning**: Basic vulnerability assessment capabilities
- **Multiple Scan Types**: Quick scan, full scan, and custom scan options
- **User-Friendly CLI**: Interactive command-line interface with clear menu options
- **Results Export**: Save scan results for further analysis

## Prerequisites

Before installing SimpleScan, ensure you have the following:

- Python 3.7 or higher
- pip (Python package manager)
- Administrator/root privileges (required for certain scan types)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Amina0011/SimpleScan.git
cd SimpleScan
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Verify installation:
```bash
python simplescan.py --help
```

## Usage

### Basic Usage

Launch SimpleScan with administrator privileges:

```bash
sudo python simplescan.py
```

### Scan Types

SimpleScan offers several scanning modes accessible through the interactive menu:

**1. Quick Scan**
- Scans the most common 1000 ports
- Fastest option for initial reconnaissance
```bash
Select option: 1
Enter target IP: 192.168.1.1
```

**2. Full Scan**
- Comprehensive scan of all 65535 ports
- Includes service version detection
```bash
Select option: 2
Enter target IP: 192.168.1.1
```

**3. Network Discovery**
- Identifies all active hosts on a subnet
```bash
Select option: 3
Enter network range: 192.168.1.0/24
```

**4. Vulnerability Scan**
- Performs basic vulnerability assessment on discovered services
```bash
Select option: 4
Enter target IP: 192.168.1.1
```

### Example Workflow

1. Start with network discovery to identify active hosts
2. Perform a quick scan on interesting targets
3. Run a full scan on confirmed targets for detailed information
4. Execute vulnerability scanning for security assessment

## Output and Results

Scan results are displayed in the terminal and can be exported to various formats:

- Text files for documentation
- JSON format for integration with other tools
- CSV format for spreadsheet analysis

Results include:
- Open ports and their states
- Service versions
- Potential vulnerabilities
- Host information

## Documentation Resources

### Video Tutorial

For a detailed walkthrough of SimpleScan's features and usage, watch the demonstration video:

[SimpleScan Tutorial and Demo](https://youtu.be/p45PA0CEpxs)

### Project Presentation

For a comprehensive overview of SimpleScan's architecture, design decisions, and technical implementation:

[View Project Presentation](https://www.canva.com/design/DAGThb7DUmU/IqYgDbV7YFYdbfzcupxLsg/edit?utm_content=DAGThb7DUmU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

## Security and Legal Considerations

**Important**: SimpleScan is designed for authorized security testing and network administration only.

- Only scan networks and systems you own or have explicit permission to test
- Unauthorized scanning may be illegal in your jurisdiction
- Always follow responsible disclosure practices
- Use this tool ethically and in compliance with applicable laws

## Technical Details

### Architecture

SimpleScan is built with a modular architecture:
- **Scanner Module**: Core scanning functionality
- **Parser Module**: Results processing and formatting
- **CLI Module**: User interface and interaction handling
- **Export Module**: Output generation in multiple formats

### Dependencies

Key libraries used:
- `socket`: Low-level network interface
- `scapy`: Packet manipulation and analysis
- Additional dependencies listed in `requirements.txt`

## Troubleshooting

**Permission Errors**
- Run with sudo/administrator privileges
- Check firewall settings

**Slow Scan Performance**
- Reduce thread count in configuration
- Use quick scan instead of full scan
- Check network connectivity

**Import Errors**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version compatibility

## Contributing

Contributions are welcome! If you'd like to improve SimpleScan:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Open a Pull Request

## Future Enhancements

Planned features for future releases:
- GUI interface option
- Advanced vulnerability database integration
- Custom scan profiles
- Automated report generation
- Integration with popular security frameworks

## License

This project is intended for educational and authorized security testing purposes.

## Author

Developed by Amina

## Contact

For questions, suggestions, or security concerns, please open an issue on GitHub.

---

**Disclaimer**: This tool is provided for educational and authorized security testing purposes only. The author assumes no liability for misuse or damage caused by this tool. Always obtain proper authorization before scanning any network or system.
