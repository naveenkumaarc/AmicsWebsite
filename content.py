"""AMICS copy, adapted from the six pages of amics.in on 27 October 2026.

Keep claims and contact details factual. Product cards describe categories;
they do not imply stock availability, specific specifications or pricing.
"""

COMPANY = {
    "name": "Amics Automations",
    "email": "mail@amics.in",
    "phone": "+91 96000 33548",
    "phone_uri": "+919600033548",
    "secondary_phone": "+91 94426 67566",
    "secondary_phone_uri": "+919442667566",
    "address": "No. 48, Kamarajar Street, TMP Nagar, Padi, Chennai – 600 050.",
    "whatsapp": "https://wa.me/919600033548?text=Hello%20AMICS%2C%20I%27d%20like%20to%20discuss%20an%20automation%20requirement.",
}

SERVICES = [
    {"id": "special-purpose-machines", "title": "Special Purpose Machines", "short": "Machines built around your process.", "icon": "machine", "text": "Custom automatic and semi-automatic equipment for assembly, processing, inspection and material handling. Each system is engineered around your component, production sequence and operating requirements.", "features": ["Assembly and insertion machines", "Heat staking and pressing systems", "Conveyors, indexing and pick-and-place systems", "Custom fixtures, nests and tooling"]},
    {"id": "end-of-line-testing", "title": "End-of-Line Testing", "short": "Confidence in every finished product.", "icon": "check-square", "text": "Automated electrical and functional validation with clear pass/fail decisions and traceable results. Bring measurement, product identification and reporting into one controlled test sequence.", "features": ["Voltage, current and resistance measurement", "Digital, analogue and communication tests", "Barcode identification and test reports", "Database integration and rejection management"]},
    {"id": "plc-hmi-scada", "title": "PLC, HMI & SCADA", "short": "Control that operators can rely on.", "icon": "software", "text": "Structured control software for standalone machines, production cells and integrated lines. Clear operator interfaces, useful diagnostics and maintainable programs support everyday production.", "features": ["PLC ladder and structured-text programming", "Servo, VFD and motion control", "Alarm diagnostics and recipe management", "SCADA, remote I/O and third-party integration"]},
    {"id": "electrical-control-panels", "title": "Electrical Control Panels", "short": "Engineered, wired and ready to run.", "icon": "panel", "text": "Electrical engineering and panel manufacturing, from component selection and schematics through machine wiring, inspection and commissioning.", "features": ["Load calculations and component selection", "Electrical schematics and panel layouts", "PLC, servo, VFD and safety panels", "Cable schedules, testing and commissioning"]},
    {"id": "fixtures-jigs-tooling", "title": "Fixtures, Jigs & Tooling", "short": "Repeatability starts with good tooling.", "icon": "tool", "text": "Application-specific tooling for repeatable positioning, inspection and mistake prevention. We design around the part, operator and changeover requirements.", "features": ["Assembly and inspection fixtures", "Electrical and functional test fixtures", "Pressing and component-location tooling", "Interchangeable model-change parts"]},
    {"id": "industrial-communication", "title": "Industrial Communication", "short": "Connect your machines and your data.", "icon": "network", "text": "Reliable communication between PLCs, instruments, drives, scanners and production databases. Structured integration brings multiple devices into a coordinated system.", "features": ["Ethernet TCP/IP and Modbus TCP", "Modbus RTU, RS-232 and RS-485", "OPC UA and EtherNet/IP", "Serial device servers and remote I/O"]},
    {"id": "industrial-software", "title": "Industrial Software & Data Acquisition", "short": "Make production data useful.", "icon": "chart", "text": "Custom software for testing, monitoring, data logging and production traceability. Connect machine measurements to records that your team can use.", "features": ["LabVIEW-based machine applications", "PLC-to-PC and instrument communication", "CSV, database reporting and user access", "Barcode scanners, printers and recipe control"]},
    {"id": "retrofitting", "title": "Retrofitting & Machine Upgrades", "short": "Give existing equipment a better future.", "icon": "refresh", "text": "Modernise existing machinery to improve reliability, diagnostics, maintainability and data availability. Upgrade the controls around your production needs.", "features": ["Obsolete PLC and HMI replacement", "Panel modifications and rewiring", "Servo, VFD and safety upgrades", "Traceability, cycle-time and diagnostic improvements"]},
]

SOLUTIONS = [
    ("durability", "Two-Wheeler Durability", "machine", "Evaluate two-wheeler components and systems under demanding operating conditions with dedicated durability test setups."),
    ("motor-testing", "Motor Testing", "activity", "Measure torque, speed, efficiency and operating characteristics to assess motor performance and reliability."),
    ("electrical-testing", "Electrical Functional Testing", "bolt", "Verify electrical parameters and product operation through consistent, repeatable functional tests."),
    ("eol", "End-of-Line Functionality", "check-square", "Validate finished products against defined functionality and performance requirements before they leave production."),
    ("shock-vibration", "Shock & Vibration Testing", "activity", "Assess product strength and reliability under shock, vibration and demanding test conditions."),
    ("college-labs", "Engineering Laboratory Setups", "grid", "Equip engineering laboratories with practical testing and training systems for hands-on technical education."),
    ("engineering-services", "Engineering Services", "tool", "Develop and integrate customised testing and automation systems around your technical requirements."),
]

PRODUCTS = [
    ("transducers", "Transducers", "sensor", "Convert physical parameters into electrical signals for accurate measurement, monitoring and testing.", "Measurement & monitoring"),
    ("can-sensors", "CAN Sensors", "network", "Combine real-time measurement with CAN communication for vehicle and industrial control applications.", "Connected sensing"),
    ("oem-sensors", "OEM Sensors", "chip", "Application-specific sensor solutions for integration into automotive and industrial equipment.", "Application integration"),
    ("vehicle-testing", "Vehicle Testing Systems", "machine", "Evaluate vehicle performance, durability and functional characteristics with dedicated test equipment.", "Automotive testing"),
    ("non-contact-sensors", "Non-contact Sensors", "sensor", "Measure position, speed, distance, temperature and other parameters without physical contact, according to the application.", "Contactless measurement"),
    ("sound-vibration", "Sound & Vibration", "activity", "Measure noise, resonance and vibration to understand dynamic product behaviour.", "Dynamic analysis"),
    ("instruments-amplifiers", "Instruments & Amplifiers", "chart", "Condition and amplify sensor signals for dependable measurement, data acquisition and testing.", "Signal conditioning"),
]

APPLICATIONS = [
    ("Automotive testing", "Instrument cluster EOL testing", "Automated test sequences, defect detection and result recording for automotive instrument clusters."),
    ("Assembly automation", "Heat staking & insert assembly", "Controlled heating, fixture-based positioning and component-presence verification for inserts in moulded parts."),
    ("Performance testing", "Alternator & motor testing", "Variable-speed control, electrical loading, measurement and automated reporting."),
    ("Process automation", "Conveyor-based processing", "Pallet transfer through interlocked stations with part tracking and controlled processing."),
    ("Industrial networking", "Multi-device communication", "Structured communication between serial and Ethernet devices, PLCs and industrial PCs."),
    ("Product traceability", "Barcode & traceability", "Product identification, process verification, result storage and label printing."),
    ("Data acquisition", "Production data logging", "Process and test data captured in CSV files or databases for production reporting."),
    ("Power testing", "Custom electrical load systems", "Controlled load switching and automated sequences for electrical and alternator testing."),
]

VALUES = [
    ("Engineering integrity", "Recommend technically sound solutions that serve the process and remain practical to maintain."),
    ("Production focus", "Evaluate every design decision against real manufacturing conditions."),
    ("Ownership", "Take responsibility from requirement study through commissioning and support."),
    ("Continuous improvement", "Refine designs, software and processes using measured performance."),
    ("Customer partnership", "Communicate constraints, risks and changes clearly, and work through them together."),
]

GALLERY = [
    ("project-06.webp", "Assembly automation line"),
    ("project-05.webp", "PLC and drive control panel"),
    ("project-08.webp", "Custom production fixture"),
    ("project-20.webp", "Conveyor-based automation system"),
    ("project-28.webp", "Multi-station production equipment"),
    ("project-14.webp", "Electrical testing equipment"),
    ("project-01.webp", "Wired test interface"),
    ("project-02.webp", "Industrial machine and operator interface"),
    ("project-03.webp", "Component testing jig"),
    ("project-04.webp", "Electrical test fixture"),
    ("project-07.webp", "Machine control panel"),
    ("project-09.webp", "Operator control enclosure"),
    ("project-10.webp", "Control enclosure wiring"),
    ("project-11.webp", "Machine control application"),
    ("project-12.webp", "Electrical control assembly"),
    ("project-13.webp", "Portable test equipment"),
    ("project-15.webp", "Test system equipment rack"),
    ("project-16.webp", "Industrial control cabinet"),
    ("project-17.webp", "Control and power equipment"),
    ("project-18.webp", "HMI operator control panel"),
    ("project-19.webp", "Motor and mechanical test setup"),
    ("project-21.webp", "Machine panel assembly"),
    ("project-22.webp", "Custom machine development"),
    ("project-23.webp", "Press and fixture assembly"),
    ("project-24.webp", "PLC and terminal wiring"),
    ("project-25.webp", "Electrical panel layout"),
    ("project-26.webp", "Terminal and relay assembly"),
    ("project-27.webp", "Portable operator interface"),
    ("project-29.webp", "AMICS workshop"),
    ("project-30.webp", "Workshop equipment"),
    ("project-31.webp", "Machine assembly in progress"),
    ("project-32.webp", "Engineering workshop"),
    ("project-33.webp", "Production equipment at the workshop"),
]
