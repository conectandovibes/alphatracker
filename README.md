# AlphaTracker

AlphaTracker is a Python program that logs usage statistics for applications and provides insights into how Windows is used. It records the active application window and tracks the time each application is in use.

## Features

- Tracks active application usage on Windows.
- Logs the duration of time each application is active.
- Provides insights into application usage patterns.
- Saves usage statistics to a JSON file for later analysis.

## Requirements

- Python 3.x
- `psutil` library: For capturing system details.
- `pywin32` package: Required for capturing the active window on Windows.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/AlphaTracker.git
   cd AlphaTracker
   ```

2. Install the required dependencies:

   ```bash
   pip install psutil pywin32
   ```

## Usage

Run the program using the command:

```bash
python alphatracker.py
```

The program will start tracking active application usage and log the statistics to a file named `app_usage_stats.json`. To stop the tracking, press `Ctrl+C`.

## Insights

To view insights about application usage, the program will display a summary once stopped. The insights include the total time spent on each application.

## Note

- This program is designed for Windows systems and requires the `pywin32` package to function correctly.
- Ensure that you have the necessary permissions to install and run Python and the required packages.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.