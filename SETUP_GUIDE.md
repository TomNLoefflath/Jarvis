# 🤖 Jarvis - Complete Setup & Usage Guide

## ⚡ Quick Start (5 minutes)

### Option 1: Automatic Setup (Recommended)

#### Windows:
1. Open Command Prompt or PowerShell
2. Navigate to your jarvis folder: `cd path\to\jarvis`
3. Double-click `setup.bat` or run: `setup.bat`
4. Wait for installation to complete
5. Run Jarvis: `python main.py`

#### Mac/Linux:
1. Open Terminal
2. Navigate to jarvis folder: `cd path/to/jarvis`
3. Run: `bash setup.sh`
4. Wait for installation to complete
5. Run Jarvis: `python main.py`

### Option 2: Manual Setup

#### Step 1: Install Python
- Download from: https://www.python.org/downloads/
- **IMPORTANT**: During installation, check ✓ "Add Python to PATH"
- Verify: Open terminal/command prompt and type `python --version`

#### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Configure (Optional)
```bash
# Copy the example config
cp .env.example .env  # Mac/Linux
copy .env.example .env  # Windows

# Edit .env with your favorite text editor
# Add your API keys (OpenAI, Google, etc.)
```

#### Step 5: Run Jarvis
```bash
python main.py
```

---

## 🎮 Using Jarvis

### Interactive Mode (Recommended for Beginners)
Simply run: `python main.py`

This opens an interactive prompt where you can type commands naturally:
```
You: help
Jarvis: [Shows available commands]

You: search for python tutorials
Jarvis: [Performs search and shows results]

You: exit
Jarvis: Goodbye! Jarvis is shutting down.
```

### Command Mode
Run a single command directly:
```bash
python main.py "search for machine learning"
python main.py "generate a function that reverses a string"
python main.py "analyze data.csv"
```

### CLI Commands
```bash
python main.py --help           # Show all options
python main.py run              # Interactive mode
python main.py status           # Show Jarvis status
python main.py modules          # List loaded modules
python main.py config           # Show configuration
python main.py version          # Show version
```

---

## 📝 Example Commands

### Task Automation
```
schedule a task to clean my desk at 3pm
remind me to check emails in 30 minutes
list my tasks
```

### Web Search & Research
```
search for python debugging tips
research machine learning algorithms
find information about quantum computing
```

### Code Generation
```
generate a function that sorts a list
create a class for managing users
debug this code: [paste your code]
analyze this function
```

### Data Analysis
```
analyze data.csv
create a chart from my data
get statistics on sales data
```

### Email & Calendar
```
send email to john@example.com with message hello
schedule meeting for tomorrow at 2pm
show my calendar
```

### API Integration
```
connect to weather api
integrate slack
fetch data from api endpoint
```

---

## 🔑 Setting Up API Keys (To Enable Full Features)

### 1. OpenAI API (For Code Generation)
- Go to: https://platform.openai.com/api-keys
- Sign up if you don't have an account
- Create a new API key
- Copy it and paste into `.env` file as: `OPENAI_API_KEY=your_key_here`

### 2. Google APIs (For Search & Calendar)
- Go to: https://console.cloud.google.com/
- Create a new project
- Enable "Custom Search API" and "Google Calendar API"
- Create credentials (API key)
- Copy into `.env` file

### 3. Email Setup (For Gmail Integration)
- Go to: https://myaccount.google.com/apppasswords
- Generate an app-specific password
- Add to `.env`: `EMAIL_ADDRESS=your_email@gmail.com` and `EMAIL_PASSWORD=your_app_password`

### 4. Other APIs (Optional)
- Weather API: https://openweathermap.org/api
- News API: https://newsapi.org/
- GitHub: https://github.com/settings/tokens

---

## 🐛 Troubleshooting

### "Python not found" or "python is not recognized"
**Solution:**
1. Make sure Python is installed: https://www.python.org/downloads/
2. During installation, check ✓ "Add Python to PATH"
3. Restart your terminal/command prompt after installing Python
4. Try again

### "No module named 'openai'" or similar import error
**Solution:**
1. Make sure your virtual environment is activated
2. Windows: `venv\Scripts\activate`
3. Mac/Linux: `source venv/bin/activate`
4. Run: `pip install -r requirements.txt`

### "Permission denied" on Mac/Linux
**Solution:**
```bash
chmod +x setup.sh
bash setup.sh
```

### Features not working (search, code generation, etc.)
**Solution:**
1. These features work without API keys but with limitations
2. For full functionality, add API keys to `.env` file
3. See "Setting Up API Keys" section above

### Virtual environment not activating
**Windows:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
```

---

## 📂 Project Structure Explained

```
jarvis/
├── main.py                 # Start here! This is what you run
├── README.md              # Documentation
├── requirements.txt       # List of Python packages to install
├── .env.example          # Template for configuration (copy to .env)
├── setup.sh / setup.bat  # Automated setup scripts
│
├── config/               # Configuration files
│   └── settings.py       # Loads settings from .env
│
├── core/                 # Core functionality
│   ├── assistant.py      # Main Jarvis logic
│   ├── commands.py       # Command processing
│   └── utils.py          # Helper functions
│
└── modules/              # Feature modules
    ├── task_automation.py     # Scheduling & reminders
    ├── web_search.py          # Search & research
    ├── code_gen.py            # Code generation
    ├── data_analysis.py       # Data analysis
    ├── email_calendar.py      # Email & calendar
    └── api_integration.py     # External APIs
```

---

## 🚀 Common Tasks

### How to exit Jarvis
Type: `exit`

### How to see what I can do
Type: `help`

### How to run with a single command
```bash
python main.py "what you want to do"
```

### How to update dependencies
```bash
pip install --upgrade -r requirements.txt
```

### How to see if everything is working
```bash
python main.py status
```

---

## 💡 Tips for Success

1. **Start simple**: Try basic commands first before adding API keys
2. **Use natural language**: Jarvis understands casual English
3. **Be specific**: "search for python tutorials for beginners" is better than "search"
4. **Add API keys gradually**: Start with OpenAI for code generation
5. **Check errors**: If something doesn't work, look at the error message

---

## 🔧 Extending Jarvis

Want to add more features? Each module is self-contained:
- Task Automation: `modules/task_automation.py`
- Web Search: `modules/web_search.py`
- Code Generation: `modules/code_gen.py`
- Data Analysis: `modules/data_analysis.py`
- Email/Calendar: `modules/email_calendar.py`
- API Integration: `modules/api_integration.py`

Edit these files to customize behavior or add new commands!

---

## ❓ Still Need Help?

1. Check the error message - it usually tells you what's wrong
2. Make sure Python is installed and in your PATH
3. Make sure you're using a virtual environment
4. Make sure all dependencies are installed: `pip install -r requirements.txt`
5. Restart your terminal and try again

---

**Happy automating with Jarvis! 🎯**
