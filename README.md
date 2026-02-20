Pomodoro Plus

Pomodoro Plus is a terminal-based productivity timer application built in Python.  
It implements the Pomodoro Technique while extending it with customizable session settings and daily productivity tracking.

The application allows users to manage focus sessions, short and long breaks, and monitor their daily work statistics through persistent JSON-based storage.

- 25-minute focus sessions (customizable)
- Automatic short and long break cycles
- Daily statistics tracking
- Customizable session durations
- JSON-based data persistence
- Interactive terminal menu system


- Python
- time module (real-time countdown logic)
- json module (data persistence)
- datetime module (daily tracking)
- Modular function-based architecture

 Timer System
- Countdown mechanism implemented using `time.sleep()`
- Real-time minute/second formatting
- Automatic transition between work and break sessions
- Long break triggered every 4 completed Pomodoros

 Data Persistence
Two JSON files are used:

- `data.json` → Stores daily statistics
- `settings.json` → Stores customizable timer settings
