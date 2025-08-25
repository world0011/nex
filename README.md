<img width="1000" height="712" alt="NexLogo_resized" src="https://github.com/user-attachments/assets/cfb4497d-41fc-40fa-8819-d9126ea79124" />

<h1 align="center">Nex</h1>

Nex is a **remote system management tool** built with Python that integrates with Discord for simple cross-platform control.  
It provides a lightweight way to manage your machines remotely, automate tasks, and monitor system activity through a familiar chat interface.  

This project is based on [Pinkcord](https://github.com/Jvr2022/pinkcord), but has been expanded with additional functionality, cross-platform improvements, and better session handling.

---

## ✨ Features

Nex offers a wide range of **system administration utilities**, including:  

- **Command execution**: Run terminal/PowerShell commands remotely.  
- **File management**: Upload, move, copy, and delete files.  
- **System monitoring**: Capture screenshots, record activity, or view active processes.  
- **Device access**: Control the webcam, audio, or clipboard when needed.  
- **Network tools**: Toggle Wi-Fi, read saved network data, and manage connections.  
- **Customization**: Change desktop wallpaper or manage startup apps.  
- **Process control**: List or terminate running tasks.  
- **Session management**: Each system is assigned a unique session ID for tracking.  

---

## 🚀 Installation (via pip)

1. Install the library:

```bash
pip install worldnex
```

2. Import it into your project:

```python
import nex
```

3. Connect it to a Discord bot:

```python
nex.start("Bot_Token")
```

---

## 📦 Installation (from source)

```bash
git clone https://github.com/world1100/Nex
cd Nex
pip install -r requirements.txt
python setup.py
```

⚠️ For most users, it is recommended to download the files directly from the [Releases page](https://github.com/world0011/Nex/releases).  

---

## 🛠 Usage

Once your bot is online, type `!h` in Discord to see all available commands.  
Each machine has a **unique session ID**, and you can also broadcast commands to all sessions at once.  

Examples:  

- `!ss <session>` → Take a screenshot.  
- `!screenrecord <session> start` → Start screen recording.  
- `!shell <session> <command>` → Run a terminal command.  
- `!processes <session>` → List running processes.  
- `!kill <session> <task>` → Stop a running process.  

---

## ⚖️ Disclaimer

Nex is intended **for educational purposes, research, and authorized system administration only**.  
Do not use this software on machines without explicit permission.  

The author assumes no responsibility for any misuse.  

---

## 🔧 Development

- Full Linux support is in progress.  
- The setup script works cross-platform, but some advanced features are currently **Windows-only**.  
- Contributions are welcome — please follow ethical and legal guidelines when submitting pull requests.  
