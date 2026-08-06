# SSH Terminal Chat

A simple terminal-based chat application built in Python to learn SSH, networking, multithreading, and file-based communication.

This project is designed as a learning exercise rather than a production-ready chat application. It explores how two users connected through SSH can communicate using a shared chat log, with the goal of gradually evolving into a socket-based real-time chat system.

---

## Features

* Terminal-based chat
* Runs through an SSH session
* Shared chat log
* Real-time message monitoring using a background thread
* Simple Python implementation
* Easy to understand and modify

---

## Technologies & Concepts

* Python 3
* SSH (Secure Shell)
* Terminal Programming
* Multithreading (`threading`)
* File I/O
* Networking Fundamentals
* Linux Command Line
* Docker (optional)

---

## Project Structure

```text
.
├── chat.py
├── chat.log
└── README.md
```

---

## Requirements

* Python 3.10+
* SSH Server
* Linux/macOS (or Windows with OpenSSH Server)
* Two SSH terminals connected to the same machine

---

## Start an SSH Session

From another computer:

```bash
ssh username@server-ip
```

Example:

```bash
ssh ravi@192.168.1.10
```

Or if using another port:

```bash
ssh -p 2222 username@server-ip
```

---

## Run the Chat

Navigate to the project directory:

```bash
cd SSH-Terminal-Chat
```

Run:

```bash
python3 chat.py
```

Open another SSH session and run the same command.

Both users can now exchange messages through the shared log.

---

## Learning Goals

This project explores:

* How SSH works
* Running programs remotely
* Reading and writing files
* Multithreading in Python
* Terminal input/output
* Continuous file monitoring
* Building command-line applications

---

## Future Improvements

* TCP Socket communication
* Client/Server architecture
* Multiple chat rooms
* User authentication
* Colored usernames
* Private messaging
* File sharing
* End-to-end encryption
* Message history
* Better terminal interface
* Cross-platform support

---

## Project Status

This roject is under active development as part of a networking and systems programming learning journey.
